import sqlite3

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
    (1, "Software Engineer", "Tech Solutions Inc.", "JavaScript, React, Node.js", "San Francisco", "Full-Time", "Intermediate"),
    (2, "Data Scientist", "Data Analytics Corp.", "Python, Data Analysis,Machine Learning", "Remote", "Full-Time", "Intermediate"),
    (3, "Frontend Developer", "Creative Designs LLC", "HTML, CSS, JavaScript, Vue.js", "New York", "Part-Time", "Junior"),
    (4, "Backend Developer", "Web Services Co.", "Python, Django, REST APIs", "Chicago", "Full-Time", "Senior"),
    (5, "Machine Learning Engineer", "AI Innovations", "Python, Machine Learning, TensorFlow", "Boston", "Full-Time", "Intermediate"),
    (6, "DevOps Engineer", "Cloud Networks", "AWS, Docker, Kubernetes", "Seattle", "Full-Time", "Senior"),
    (7, "Full Stack Developer", "Startup Hub", "JavaScript, Node.js, Angular, MongoDB", "Austin", "Full-Time", "Intermediate"),
    (8, "Data Analyst", "Finance Analytics", "SQL, Python, Tableau", "New York", "Full-Time", "Junior"),
    (9, "Quality Assurance Engineer", "Reliable Software", "Selenium, Java, Testing", "San Francisco", "Contract", "Intermediate"),
    (10, "Systems Administrator", "Enterprise Solutions", "Linux, Networking, Shell Scripting", "Remote", "Full-Time", "Senior")
]

# Insert the mock data into the database
cursor.executemany('''
INSERT INTO job_postings (job_id, job_title, company, required_skills, location, job_type, experience_level)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', job_postings)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete and job postings inserted.")

