from flask import Flask, render_template

app = Flask(__name__)

# Portfolio Data - Edit this to change your site content
DATA = {
    "name": "RAWAD ALANI",
    "title": "Heath informatics Specialist",
    "tagline": "Architecting digital solutions for healthcare.",
    "about": "I specialize in digital health solutions and data analytics.",
    "social": {
        "github": "https://github.com/alanirawad-sketch",
        "linkedin": "https://www.linkedin.com/in/rawadtal-ani",
        "email": "mailto:alanirawad@email.com",
        "Facebook": "https://www.facebook.com/rawad.dimook",
        "Instagram": "https://www.instagram.com/rawaddimook/"
    },
    "projects": [
        {
            "id": 1,
            "name": "Neural Vision API",
            "tech": ["Python", "Flask", "OpenCV"],
            "desc": "An advanced image recognition engine with real-time processing.",
            "link": "#"
        },
        {
            "id": 2,
            "name": "Quantum Portfolio",
            "tech": ["Glassmorphism", "CSS3", "Jinja2"],
            "desc": "The very site you are looking at. Highly dynamic and responsive.",
            "link": "#"
        },
        {
            "id": 3,
            "name": "Cloud Automator",
            "tech": ["Python", "Ubuntu", "Bash"],
            "desc": "Automation suite for managing virtual server environments.",
            "link": "#"
        }
    ]
}


@app.route('/')
def index():
    # 'data' on the left is what the HTML sees
    # 'DATA' on the right is the variable name in your Python code
    return render_template('index.html', data=DATA)


if __name__ == '__main__':
    app.run(debug=True)
