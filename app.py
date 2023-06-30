import zipfile
from flask import Flask, render_template, send_file, request, make_response
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
        config = request.form.to_dict()
        print(config)
        file_names = [file.filename for file in request.files if file and allowed_file(file.filename)]
        for file_name in file_names:
            file = request.files[file_name]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            config[file_name] = file_name

    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    summary = request.form['summary']
    degree = request.form['degree']
    major = request.form['major']
    university = request.form['university']
    school_start = request.form['school-start']
    school_end = request.form['school-end']
    school_misc = request.form['school-misc']
    skill1 = request.form['skill1']
    skill1_prof = request.form['skill1-prof']
    skill2 = request.form['skill2']
    skill2_prof = request.form['skill2-prof']
    skill3 = request.form['skill3']
    skill3_prof = request.form['skill3-prof']
    skill4 = request.form['skill4']
    skill4_prof = request.form['skill4-prof']
    skill5 = request.form['skill5']
    skill5_prof = request.form['skill5-prof']
    skill6 = request.form['skill6']
    skill6_prof = request.form['skill6-prof']
    title1 = request.form['title1']
    name_location1 = request.form['name-location1']
    work_start1 = request.form['work-start1']
    work_end1 = request.form['work-end1']
    work_description1 = request.form['work-description1']
    title2 = request.form['title2']
    name_location2 = request.form['name-location2']
    work_start2 = request.form['work-start2']
    work_end2 = request.form['work-end2']
    work_description2 = request.form['work-description2']
    title3 = request.form['title3']
    name_location3 = request.form['name-location3']
    work_start3 = request.form['work-start3']
    work_end3 = request.form['work-end3']
    work_description3 = request.form['work-description3']
    project1_name = request.form['project1-name']
    project1_description = request.form['project1-description']
    project2_name = request.form['project2-name']
    project2_description = request.form['project2-description']
    project3_name = request.form['project3-name']
    project3_description = request.form['project3-description']
    award1 = request.form['award1']
    award1_year = request.form['award1-year']
    award2 = request.form['award2']
    award2_year = request.form['award2-year']
    award3 = request.form['award3']
    award3_year = request.form['award3-year']
    award4 = request.form['award4']
    award4_year = request.form['award4-year']
    award5 = request.form['award5']
    award5_year = request.form['award5-year']
    
    headshot=request.files['headshot']
    resume=request.files['resume']
    project1_picture1=request.files['project1-picture1']
    project1_picture2=request.files['project1-picture2']
    project2_picture1=request.files['project2-picture1']
    project2_picture2=request.files['project2-picture2']
    project3_picture1=request.files['project3-picture1']
    project3_picture2=request.files['project3-picture2']


    # Generate the HTML content for the portfolio
    rendered_content = render_template('portfolio-template.html',
                                   name=name,
                                   number=number,
                                   email=email,
                                   headshot=headshot,
                                   resume=resume,
                                   summary=summary,
                                   degree=degree,
                                   major=major,
                                   university=university,
                                   school_start=school_start,
                                   school_end=school_end,
                                   school_misc=school_misc,
                                   skill1=skill1,
                                   skill1_prof=skill1_prof,
                                   skill2=skill2,
                                   skill2_prof=skill2_prof,
                                   skill3=skill3,
                                   skill3_prof=skill3_prof,
                                   skill4=skill4,
                                   skill4_prof=skill4_prof,
                                   skill5=skill5,
                                   skill5_prof=skill5_prof,
                                   skill6=skill6,
                                   skill6_prof=skill6_prof,
                                   title1=title1,
                                   name_location1=name_location1,
                                   work_start1=work_start1,
                                   work_end1=work_end1,
                                   work_description1=work_description1,
                                   title2=title2,
                                   name_location2=name_location2,
                                   work_start2=work_start2,
                                   work_end2=work_end2,
                                   work_description2=work_description2,
                                   title3=title3,
                                   name_location3=name_location3,
                                   work_start3=work_start3,
                                   work_end3=work_end3,
                                   work_description3=work_description3,
                                   project1_name=project1_name,
                                   project1_description=project1_description,
                                   project1_picture1=project1_picture1,
                                   project1_picture2=project1_picture2,
                                   project2_name=project2_name,
                                   project2_description=project2_description,
                                   project2_picture1=project2_picture1,
                                   project2_picture2=project2_picture2,
                                   project3_name=project3_name,
                                   project3_description=project3_description,
                                   project3_picture1=project3_picture1,
                                   project3_picture2=project3_picture2,
                                   award1=award1,
                                   award1_year=award1_year,
                                   award2=award2,
                                   award2_year=award2_year,
                                   award3=award3,
                                   award3_year=award3_year,
                                   award4=award4,
                                   award4_year=award4_year,
                                   award5=award5,
                                   award5_year=award5_year)
    # Serve the rendered content as a response
    response = make_response(rendered_content)
    response.headers['Content-Type'] = 'text/html'

    return response

if __name__ == '__main__':
    app.run(debug=True)
