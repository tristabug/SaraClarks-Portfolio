from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
toEmail = 'sara.clark88@gmail.com'
senderEmail = 'mailtrap@demomailtrap.com'

app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = '2ef3caebce81870cfbe1ef48fa749868'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail=Mail(app)

# ROUTES
# home page
@app.route('/')
def home():
    return render_template("home.html", projects=projects, icons=project_icons)

# resume page
@app.route('/resume')
def resume():
    return render_template("resume.html", skills=skills)

# contact page 
@app.route('/contact', methods=["POST", "GET"])
def contact():
    sender_name = request.form.get("email_name")
    sender_email = request.form.get("email_address")
    subject = request.form.get("email_subject")
    message = request.form.get("email_message")

    if request.method == 'POST':
        message = contactFormMessage(sender_name, sender_email, message)
        send(subject, message)

    return render_template("contact.html")

# projects page
@app.route('/projects')
def projects():
    return render_template("projects.html", projects=projects, icons=project_icons)

# projects/1 page
@app.route('/project/<id>')
def project(id):
    for project in projects:
        if project['id'] == id:
            project = project['id']
            break
    return render_template("project.html", project=project)

# resume_fullview page
@app.route('/resumeFV')
def resumeFV():
    return render_template("resume_fullview.html")

# contact form email
def contactFormMessage(sender_name, sender_email, message_body):
    message = Message()
    message.html = "<h3>Contact Form Submission</h3><p><b>From: </b>" + sender_name + "</p><p><b>From Email: </b>" + sender_email + "</p><p><b>Message: </b>" + message_body + "</p>"
    return message

def send(subject_line, message):
    message.subject = subject_line
    message.recipients = [toEmail]
    message.sender = senderEmail
    mail.send(message)

skills = {
    'language' : [
        {'name': "Ruby on Rails", 'years': "3+", 'w': "30"}, 
        {'name': "Python", 'years': "3+", 'w': "30"},
        {'name': "SQL", 'years': "3+", 'w': "30"},
        {'name': "MySQL", 'years': "3+", 'w': "30"},
        {'name': "C++", 'years': "2+", 'w': "20"},
        {'name': "C#", 'years': "2+", 'w': "20"},
        {'name': "Java", 'years': "2+", 'w': "20"},
        {'name': "HTML", 'years': "7+", 'w': "70"},
        {'name': "CSS", 'years': "7+", 'w': "70"},
        {'name': "JavaScript", 'years': "7+", 'w': "70"},
        {'name': "jQuery", 'years': "7+", 'w': "70"},
        {'name': "Flask", 'years': "< 1", 'w': "6"}
    ],
    'tool' : [
        {'name': "Git & GitHub", 'years': "3+", 'w': "30"},
        {'name': "Visual Studio", 'years': "3+", 'w': "30"},
        {'name': "iTerm", 'years': "3+", 'w': "30"},
        {'name': "Docker", 'years': "2+", 'w': "20"},
        {'name': "Bootstrap", 'years': "2+", 'w': "20"},
        {'name': "Unity", 'years': "2+", 'w': "20"},
        {'name': "Atlassian Suite", 'years': "3+", 'w': "30"},
        {'name': "Microsoft Suite", 'years': "15+", 'w': "150"},
        {'name': "Adobe Suite", 'years': "15+", 'w': "150"},
        {'name': "Notion", 'years': "3+", 'w': "30"},
        {'name': "Discord", 'years': "3+", 'w': "30"},
        {'name': "Slack", 'years': "3+", 'w': "30"},
        {'name': "Canva", 'years': "3+", 'w': "30"},
        {'name': "Salesforce", 'years': "< 1", 'w': "6"},
        {'name': "FormAssembly", 'years': "< 1", 'w': "6"}
    ],
    'skill-set' : [
        {'name': "Web Design", 'years': "5+", 'w': "50"},
        {'name': "Leadership", 'years': "7+", 'w': "70"},
        {'name': "Project Management", 'years': "7+", 'w': "70"},
        {'name': "Social Media Management", 'years': "10+", 'w': "100"},
        {'name': "Organization & Planning", 'years': "15+", 'w': "150"},
        {'name': "Customer Service", 'years': "15+", 'w': "150"},
        {'name': "Test-Driven Programming", 'years': "2+", 'w': "20"}
]}

# projects
projects = [ 
        {'id': 9, 'name': "project 1", 'description': "Project1 description.", 'type': "Web App", 'specs' : ["Ruby on Rails", "CSS"], 'challenges': "These are the project1 challenges.", 'learned': "I learned a lot on this project.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb1 photo."}}}, 
        {'id': 10, 'name': "project 2", 'description': "Project2 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project2 challenges.", 'learned': "I learned too much on this project2.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb2 photo."}}},
        {'id': 11, 'name': "project 3", 'description': "Project3 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project3 challenges.", 'learned': "I learned too much on this project3.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb3 photo."}}},
        {'id': 12, 'name': "project 4", 'description': "Project4 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project4 challenges.", 'learned': "I learned too much on this project4.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb4 photo."}}},
        {'id': 13, 'name': "project 1", 'description': "Project1 description.", 'type': "Web App", 'specs' : ["Ruby on Rails", "CSS"], 'challenges': "These are the project1 challenges.", 'learned': "I learned a lot on this project.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb1 photo."}}}, 
        {'id': 14, 'name': "project 2", 'description': "Project2 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project2 challenges.", 'learned': "I learned too much on this project2.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb2 photo."}}},
        {'id': 15, 'name': "project 3", 'description': "Project3 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project3 challenges.", 'learned': "I learned too much on this project3.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb3 photo."}}},
        {'id': 16, 'name': "project 4", 'description': "Project4 description.", 'type': "Web App", 'specs' : ["Python", "Flask"], 'challenges': "These are the project4 challenges.", 'learned': "I learned too much on this project4.", 'visuals' : {'thumb': {'file': "/static/assets/miniProfilePhoto.jpg", 'desc': "Thumb4 photo."}}}
]

# projects - placeholder icons
# software dev process (plan - dev - code - test - release)
project_icons = { 
        1 : {'name': "Planning", 'description': "In the process of planning, which includes determining requirements, data needs, security, and creating wireframes.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/planningIcon.jpg", 'desc': "Icon of the planning phase of development."}}}, 
        2 : {'name': "Developing", 'description': "Currently in development.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/inDevIcon.jpg", 'desc': "Icon of the development phase."}}},
        3 : {'name': "Coding", 'description': "Currently coding this project.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/codingIcon.jpg", 'desc': "Icon of the coding phase."}}},
        4 : {'name': "Testing", 'description': "This project is currently being tested.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/testingIcon.jpg", 'desc': "Icon of the testing phase."}}},
        5 : {'name': "Releasing", 'description': "This project is about to be released!", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/releasingIcon.jpg", 'desc': "Icon of the releasing phase."}}},
        6 : {'name': "Planning", 'description': "In the process of planning, which includes determining requirements, data needs, security, and creating wireframes.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/planningIcon.jpg", 'desc': "Icon of the planning phase of development."}}},
        7 : {'name': "Developing", 'description': "Currently in development.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/inDevIcon.jpg", 'desc': "Icon of the development phase."}}},
        8 : {'name': "Coding", 'description': "Currently coding this project.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/codingIcon.jpg", 'desc': "Icon of the coding phase."}}},
        9 : {'name': "Testing", 'description': "This project is currently being tested.", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/testingIcon.jpg", 'desc': "Icon of the testing phase."}}},
        10 : {'name': "Releasing", 'description': "This project is about to be released!", 'type': "Placeholder Icon", 'specs' : [], 'challenges': "", 'learned': "", 'visuals' : {'thumb': {'file': "/static/assets/icons/releasingIcon.jpg", 'desc': "Icon of the releasing phase."}}} 
}
