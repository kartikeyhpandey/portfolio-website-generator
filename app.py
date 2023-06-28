from flask import Flask, render_template, request
import os

app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')

@app.route('/generate', methods=['POST'])
def generate(): 
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    degree = request.form['degree']
    major = request.form['major']
    university = request.form['university']
    school_start = request.form['school-start']
    school_end = request.form['school-end']
    title1 = request.form['title1']
    location1 = request.form['location1']
    work_start1 = request.form['work-start1']
    work_end1 = request.form['work-end1']
    work_description1 = request.form['work-description1']
    title2 = request.form['title2']
    location2 = request.form['location2']
    work_start2 = request.form['work-start2']
    work_end2 = request.form['work-end2']
    work_description2 = request.form['work-description2']
    title3 = request.form['title3']
    location3 = request.form['location3']
    work_start3 = request.form['work-start3']
    work_end3 = request.form['work-end3']
    work_description3 = request.form['work-description3']
    
    # Generate the HTML content for the portfolio
    rendered_content = render_template('portfolio-template.html', 
                                   name=name,
                                   number=number,
                                   email=email,                                   
                                   degree=degree,
                                   major=major,
                                   university=university,
                                   school_start=school_start,
                                   school_end=school_end,
                                   title1=title1,
                                   location1=location1,
                                   work_start1=work_start1,
                                   work_end1=work_end1,
                                   work_description1=work_description1,
                                   title2=title2,
                                   location2=location2,
                                   work_start2=work_start2,
                                   work_end2=work_end2,
                                   work_description2=work_description2,
                                   title3=title3,
                                   location3=location3,
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
