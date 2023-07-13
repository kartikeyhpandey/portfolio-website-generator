import zipfile
from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__, template_folder='template')
UPLOAD_FOLDER = os.path.join(app.root_path, 'static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')

@app.route('/download')
def download():
    zip_filename = 'website.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(app.config['UPLOAD_FOLDER']):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, app.config['UPLOAD_FOLDER'])
                zipf.write(file_path, arcname)

    # Send the zip file for download
    return send_file(zip_filename, as_attachment=True)

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        config = request.form.to_dict(flat=False)
        print(request.files.to_dict(flat=False))
        for file_field in request.files.to_dict(flat=False):
            print(file_field)
            files = request.files.to_dict(flat=False)[file_field]
            print(files)
            for file in files:
                if file and allowed_file(file.filename):
                    filename = file.filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    if file_field in config:
                        config[file_field].append(filename)
                    else:
                        config[file_field] = [filename]
    print(config)
    # Generate the HTML content for the portfolio
    rendered_content = render_template('portfolio-template.html',
                                   **config, zip=zip)
    
    # Save the generated HTML content to a file
    file_path = os.path.join('template/portfolio.html')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(rendered_content)
    
    return file_path

if __name__ == '__main__':
    app.run(debug=True)
