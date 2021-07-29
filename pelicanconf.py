#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = "Julio Melanda"
SITENAME = "Julio Cesar Eiras Melanda"
SITEURL = ""

BASEDIR = os.path.abspath(os.path.dirname(__file__))

PATH = "content"

TIMEZONE = "Europe/Copenhagen"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "images/julio.jpg": {"path": "theme/julio.jpg"},
}
THEME = os.path.join(BASEDIR, "resume")

CSS_FILE = "main-6.css"

# Profile information
NAME = "Julio Cesar Eiras Melanda"
TAGLINE = "Python Backend Developer and Data Engineer"
PIC = "julio.jpg"

# sidebar links
EMAIL = "jcemelanda@gmail.com"
PHONE = "+45 52 75 07 37"
WEBSITE = "jcemelanda.github.io"
LINKEDIN = "jcemelanda"
GITHUB = "jcemelanda"
TWITTER = "@jcemelanda"

CAREER_SUMMARY = "I'm a backend developer expert in Python, specially using Django and FastAPI. I have experience in a large amount of areas. My last work was a Data Engineer position, building a pipeline ETL with PySpark"

SKILLS = [
    {"title": "Python", "level": "100"},
    {"title": "HTML5 &amp; CSS", "level": "90"},
    {"title": "Javascript", "level": "75"},
    {"title": "Ruby", "level": "70"},
    {"title": "Java", "level": "70"},
    {"title": "C/C++", "level": "60"},
    {"title": "C#", "level": "30"},
    {"title": "sqlite3", "level": "95"},
    {"title": "PostgreSQL", "level": "85"},
    {"title": "MongoBD", "level": "75"},
    {"title": "Angular", "level": "85"},
    {"title": "React", "level": "60"},
    {"title": "Django", "level": "95"},
    {"title": "FastAPI", "level": "75"},
    {"title": "Pandas", "level": "70"},
    {"title": "PySpark", "level": "65"},
    {"title": "Docker", "level": "85"},
    {"title": "Linux", "level": "85"},
    {"title": "AWS", "level": "65"},
]

PROJECT_INTRO = "Below are a few of the projects I have developed and I am proud of."

PROJECTS = [
    {
        "title": "MathShooter",
        "tagline": "MathShooter is a simple educative arcade game intended do help children to learn and keep the basic arithmetics. Powered by Pygame",
        "link": "https://github.com/jcemelanda/MathShooter",
    },
    {
        "title": "Pygame Camera",
        "tagline": "A Python library to help Pygame developers to make the camera follow objects.",
        "link": "https://github.com/jcemelanda/pygame-camera",
    },
]

LANGUAGES = [
    {"name": "Portuguese", "description": "Native"},
    {"name": "English", "description": "Professional"},
    {"name": "Spanish", "description": "Amateur"},
    {"name": "French", "description": "Amateur"},
    {"name": "Danish", "description": "Beginner"},
]
INTERESTS = ["Gaming", "Photography", "Music", "Game Development", "Arts"]

EXPERIENCES = [
    {
        "job_title": "Data Engineer",
        "time": "Aug 2020 - Aug 2021",
        "company": "Munin Data",
        "details": [
            "Data Engineering with PySpark and Pandas",
            "Web development with Flask",
            "API development with FastAPI",
            "Fronted development using React",
        ],
    },
    {
        "job_title": "Software Engineer",
        "time": "Apr 2019 - Jul 2020",
        "company": "DTU Biosustain: Novo Nordisk Foundation Center for Biosustainability",
        "details": [
            "Fullstack Python Developer",
            "CI/CD Pipeline configuration",
            "SOftware deployment with Docker",
        ],
    },
    {
        "job_title": "Senior Software Engineer ",
        "time": "Oct 2015 - Mar 2019",
        "company": "Toptal",
        "details": [
            "Python fullstack development",
            [
                "Web development with Python and Django",
                "REST APIs with Django Rest Framework",
                "Deployment to AWS and linux servers",
                "Use and implementation of CI/CD",
            ],
            "Technologies used: PostgreSQL, MongoDB, MySQL, Python, Django, Django Rest Framewokr, AngularJS, Javascritp, Linux, NGINX, Jenkins, EBS, AWS, EC2, Requests, aiohttp, selectolax",
        ],
    },
    {
        "job_title": "Software Developer",
        "time": "Jul 2015 - Oct 2015",
        "company": "Rede Alumni",
        "details": [
            "Ruby on Rails Backend Developer",
            [
                "Features, bugfixes and improvements in Rails backend",
            ],
            "Technologies used: PostgreSQL, Ruby, Shellscript, Linux, AngularJS, javascript, Rails, Sinatra",
        ],
    },
    {
        "job_title": "Software Developer",
        "time": "May 2015 - Jul 2015",
        "company": "Qmágico",
        "details": [
            "Python Backend Developer",
            [
                "Features, bugfixes and improvements both in Python backend and AngularJS frontend",
            ],
            "Technologies used: PostgreSQL, Python, Shellscript, Linux, AngularJS, javascript, Django",
        ],
    },
    {
        "job_title": "Software Projects Coordinator and Senior Developer",
        "time": "Jan 2014 - May 2015",
        "company": "GTAC Solutions",
        "details": [
            "Software Projects Coordinator",
            "Python/Django Software Development for Startups",
            [
                "Android Mobile development with Python/Django API",
                "My main responsibilities were to assure every developer had a ticket to work on and schedule their work time to have all projects under development accordingly",
                "I also helped to organize the sprints, separate the projects in tasks and to assign tasks to the developers",
            ],
            "One of the projects I worked on as a developer and manager was a large complexity software to digitalize the files in the archives and the operations of a real state registry office. To that software we implemented a management software to manage the queues for the office booths. Also a digitalization software to get the digital versions of the files where the users were able to add metadata and also there was a module where the actual office operations could be performed digitally.",
            "As a manager I had the leadership of 8 developers divided in 6 teams for about 5 months",
            "Throughout the management position, I trained and helped about 15 developers.",
            "Under My leadership we grew the Python team from 2 to 10 developers working with about 15 projects simultaneously",
            "Technologies used: PostgreSQL, Python, Shellscript, Android, Linux, Teamcity, Jenkins, NGINX, jQuery, javascript, Django, Django Rest Framework",
        ],
    },
    {
        "job_title": "Trainee Developer",
        "time": "Dec 2012 - Jan 2014",
        "company": "Touch Health",
        "details": [
            "Java trainee web developer with use of agile (SCRUM/Kamban).",
            "Assignments: development of new features and bug fixing, help on API definition and story and code review."
            "Team AMBDEV: Collaboration in all aspects of the company’s development environment, research new technologies, deployment scripts to help in the development process, creation of new internal tools.",
            "Technologies used: Java, Selenium, PostgreSQL, Struts, Hybernate, Tomcat, Python, Shellscript",
        ],
    },
    {
        "job_title": "Developer",
        "time": "Dec 2011 - Jan 2012",
        "company": "WILCX",
        "details": [
            "Development of Mobile Android applications for Smartphones and Tablets.",
            "In order to guarantee the quality and correctness of the tablets developed by our client, I creates a test suit for the Tablets Hardware.",
            "We had a local server that I configured and managed, where we deployed the applications along with a CI and a issue tracking application.",
            "To control the team’s tasks, I worked in the creation and implementation of a task control system and time-tracking, along with an internal blog for information sharing. (Python/Django)",
            "I was the team leader, and managed some of our projects with a team of 4 developers.",
            "Technologies used: Python, Java, Linux, POstgreSQL, shellscript, Django, Andengine, AndroidSDK, NGINX,",
        ],
    },
]

EDUCATIONS = [
    {
        "degree": "Bachelor of Computer Science",
        "meta": "FEDERAL UNIVERSITY OF ITAJUBÁ (UNIFEI)",
        "highlights": "I have participated in several events of the university as a lecturer, sometimes talking about Python and others talking about Linux.",
        "time": "2007 - 2012",
    },
    {
        "degree": "Minor in Bio-inspired Computing",
        "meta": "FEDERAL UNIVERSITY OF SÃO PAULO ",
        "time": "2015",
    },
]
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
