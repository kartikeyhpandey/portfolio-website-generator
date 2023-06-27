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
    coursework = request.form['coursework']
    club_activities = request.form['club-activities']
    experience = request.form['experience']
    
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
                                   coursework=coursework,
                                   club_activities=club_activities,
                                   experience=experience)

    
    
    # Save the generated HTML content to a file
    file_path = os.path.join('template/portfolio.html')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(rendered_content)
    
    return file_path

if __name__ == '__main__':
    app.run(debug=True)
