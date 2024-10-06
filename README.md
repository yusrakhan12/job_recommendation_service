##Job recommendation service
###An overview

The Job recommendation Service helps users find a number of suited job 
postings by matching profiles with available job requirements. Each job 
suggestion is tailored to the user after taking into account the user's 
skills, experience level, and preference.

###Technologies Utilized

Python: This be the programming language employed as the backbone for 
back-end development.
Flask: A lightweight web framework designed for building RESTful APIs.
SQLite: A self-contained, serverless database engine.

###Key Features

Management of the user profile: storage of user, skill, and preference 
information.
Management of job postings: storage of job details and requirements.
The recommendation engine: compares user profiles with active job 
postings.
An easy-to-use API that the clients can manipulate to convert with the 
service.

###Prerequisites

Make sure that you have installed Python 3 and SQLite on your machine.
###A guide to setup: 
1. Clone the Repository

git clone https://github.com/yusrakhan12/job_recommendation.git 
cd job_recommendation

2.Now that you have cloned the repo, let's go ahead and install the 
dependencies

pip install Flask

3.You need a database set up, with job postings inside. If a setup script 
was provided, make sure to run it.

4. verify the connection

import sqlite3

#Connect to SQLite database (or create it)

conn = sqlite3.connect('jobs.db')

#Create a cursor object

cursor = conn.cursor()
#Create a table for job postings
cursor.execute(''' CREATE TABLE IF NOT EXISTS job_postings ( job_id 
INTEGER PRIMARY KEY, job_title TEXT NOT NULL, company TEXT NOT NULL, 
required_skills TEXT NOT NULL, location TEXT NOT NULL, job_type TEXT NOT 
NULL, experience_level TEXT NOT NULL ) ''') 

Insert mock job postings

job_postings = [ (1, "Software Engineer", "Tech Solutions Inc.", 
"JavaScript, React, Node.js", "San Francisco", "Full-Time", 
"Intermediate"), (2, "Data Scientist", "Data Analytics Corp.", "Python, 
Data Analysis, Machine Learning", "Remote", "Full-Time", "Intermediate"), 
(3, "Frontend Developer", "Creative Designs LLC", "HTML, CSS, JavaScript, 
Vue.js", "New York", "Part-Time", "Junior"), (4, "Backend Developer", "Web 
Services Co.", "Python, Django, REST APIs", "Chicago", "Full-Time", 
"Senior"), (5, "Machine Learning Engineer", "AI Innovations", "Python, 
Machine Learning, TensorFlow", "Boston", "Full-Time", "Intermediate"), (6, 
"DevOps Engineer", "Cloud Networks", "AWS, Docker, Kubernetes", "Seattle", 
"Full-Time", "Senior"), (7, "Full Stack Developer", "Startup Hub", 
"JavaScript, Node.js, Angular, MongoDB", "Austin", "Full-Time", 
"Intermediate"), (8, "Data Analyst", "Finance Analytics", "SQL, Python, 
Tableau", "New York", "Full-Time", "Junior"), (9, "Quality Assurance 
Engineer", "Reliable Software", "Selenium, Java, Testing", "San 
Francisco", "Contract", "Intermediate"), (10, "Systems Administrator", 
"Enterprise Solutions", "Linux, Networking, Shell Scripting", "Remote", 
"Full-Time", "Senior") ]


5.Insert the mock data into the database

cursor.executemany(''' INSERT INTO job_postings (job_id, job_title, 
company, required_skills, location, job_type, experience_level) VALUES (?, 
?, ?, ?, ?, ?, ?) ''', job_postings)



6.Commit changes and Close Connection

conn.commit() conn.close()

print("Setup Database and Insert Job Posted")



7.Call the API It will be live at http://127.0.0.1:5000/recommend

8.Testing the API

To test the API, curl can be used.

This will give you a JSON response of the available job postings.

####Matching Logic

The recommendation algorithm connects users to job postings with the 
following criteria:

Skills Matching: Each job posting on the platform has a list of required 
skills, and this test compares a user's skills against these available 
jobs.

Experience Level: Requires matching the user's experience level with the 
job requirements.

Job Type and Location: With this filter user would enable the job postings 
based on their Job Type filters in specific Location only.
