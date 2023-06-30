import zipfile
from flask import Flask, render_template, send_file, request
import os

app=Flask(__name__,template_folder='template')

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
        static_folder = os.path.join(app.root_path, '/static')
        for root, dirs, files in os.walk(static_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = '/static/' + os.path.relpath(file_path, static_folder)
                print(arcname)
                zipf.write(file_path, arcname)

         # Add the HTML file
        zipf.write('template/portfolio.html', arcname='index.html')

    # Send the zip file for download
    return send_file(zip_filename, as_attachment=True)

    

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':  
        resume = request.files['resume']
        resume.save(os.path.join(app.root_path, 'static/' + resume.filename ))

        headshot = request.files['headshot']
        headshot.save(os.path.join(app.root_path, 'static/' + headshot.filename ))
    
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
                                   work_description3=work_description3)
    
    # Save the generated HTML content to a file
    file_path = os.path.join('template/portfolio.html')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(rendered_content)
    
    return file_path

if __name__ == '__main__':
    app.run(debug=True)
