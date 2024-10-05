# Job Recommendation Service

## Overview
This job recommendation service helps users find suitable job postings by 
matching their profiles with available job requirements. The service 
evaluates user skills, experience levels, and preferences to deliver 
personalized job suggestions.

## Technologies Used
- **Python**: Programming language used for backend development.
- **Flask**: A lightweight web framework for building RESTful APIs.
- **SQLite**: A self-contained, serverless database engine used for data 
storage.

## Features
- User profile management: Store user information, skills, and 
preferences.
- Job posting management: Store job details and requirements.
- Recommendation engine: Match user profiles with relevant job postings.
- Easy-to-use API for clients to interact with the service.

## Setup Instructions

### Prerequisites
- Ensure you have Python 3 and SQLite installed on your machine.

### Steps to Set Up
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yusrakhan12/job_recommendation.git
   cd https://github.com/yusrakhan12/job_recommendation.git


2.Install Dependencies: Make sure you have Python and pip installed, then 
run:
--pip install Flask


3.Set Up the Database: Ensure your SQLite database is created and 
populated with job postings. You may need to run a setup script if provided.
Add the Database Setup Code: Copy and paste the following code into 
setup_database.py:
###import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('jobs.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for job postings
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_postings (
    job_id INTEGER PRIMARY KEY,
    job_title TEXT NOT NULL,
    company TEXT NOT NULL,
    required_skills TEXT NOT NULL,
    location TEXT NOT NULL,
    job_type TEXT NOT NULL,
    experience_level TEXT NOT NULL
)
''')

# Insert mock job postings
job_postings = [
    (1, "Software Engineer", "Tech Solutions Inc.", "JavaScript, React, 
Node.js", "San Francisco", "Full-Time", "Intermediate"),
    (2, "Data Scientist", "Data Analytics Corp.", "Python, Data Analysis, 
Machine Learning", "Remote", "Full-Time", "Intermediate"),
    (3, "Frontend Developer", "Creative Designs LLC", "HTML, CSS, 
JavaScript, Vue.js", "New York", "Part-Time", "Junior"),
    (4, "Backend Developer", "Web Services Co.", "Python, Django, REST 
APIs", "Chicago", "Full-Time", "Senior"),
    (5, "Machine Learning Engineer", "AI Innovations", "Python, Machine 
Learning, TensorFlow", "Boston", "Full-Time", "Intermediate"),
    (6, "DevOps Engineer", "Cloud Networks", "AWS, Docker, Kubernetes", 
"Seattle", "Full-Time", "Senior"),
    (7, "Full Stack Developer", "Startup Hub", "JavaScript, Node.js, 
Angular, MongoDB", "Austin", "Full-Time", "Intermediate"),
    (8, "Data Analyst", "Finance Analytics", "SQL, Python, Tableau", "New 
York", "Full-Time", "Junior"),
    (9, "Quality Assurance Engineer", "Reliable Software", "Selenium, 
Java, Testing", "San Francisco", "Contract", "Intermediate"),
    (10, "Systems Administrator", "Enterprise Solutions", "Linux, 
Networking, Shell Scripting", "Remote", "Full-Time", "Senior")
]

# Insert the mock data into the database
cursor.executemany('''
INSERT INTO job_postings (job_id, job_title, company, required_skills, 
location, job_type, experience_level)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', job_postings)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete and job postings inserted.")
####
Run the Database Setup Script


4.Run the Application: Start the Flask server:
--python app.py


5.Access the API: The API will be available at 
http://127.0.0.1:5000/recommend

Tested the API using cURL
###curl -X POST http://127.0.0.1:5000/recommend \
-H "Content-Type: application/json" \
-d '{
    "skills": ["JavaScript"],
    "experience_level": "Intermediate",
    "preferences": {
        "locations": ["San Francisco"],
        "job_type": "Full-Time"
    }
}'
####
7.got the output as ----
[
  {
    "company": "Tech Solutions Inc.",
    "experience_level": "Intermediate",
    "job_title": "Software Engineer",
    "job_type": "Full-Time",
    "location": "San Francisco",
    "required_skills": [
      "JavaScript",
      "React",
      "Node.js"
    ]
  }
]
----
