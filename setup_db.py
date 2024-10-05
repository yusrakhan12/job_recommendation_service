import sqlite3

def setup_database():
    conn = sqlite3.connect('job_recommendations.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        skills TEXT,
        experience_level TEXT,
        desired_roles TEXT,
        locations TEXT,
        job_type TEXT
    )
    ''')

    # Create jobs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INTEGER PRIMARY KEY,
        job_title TEXT,
        company TEXT,
        required_skills TEXT,
        location TEXT,
        job_type TEXT,
        experience_level TEXT
    )
    ''')

    # Insert mock job postings into jobs table
    jobs = [
        (1, "Software Engineer", "Tech Solutions Inc.", 
"JavaScript,React,Node.js", "San Francisco", "Full-Time", "Intermediate"),
        (2, "Data Scientist", "Data Analytics Corp.", "Python,Data Analysis,Machine Learning", "Remote", "Full-Time", "Intermediate"),
        (3, "Frontend Developer", "Creative Designs LLC", "HTML,CSS,JavaScript,Vue.js", "New York", "Part-Time", "Junior"),
        (4, "Backend Developer", "Web Services Co.", "Python,Django,REST APIs", "Chicago", "Full-Time", "Senior"),
        (5, "Machine Learning Engineer", "AI Innovations", "Python,Machine Learning,TensorFlow", "Boston", "Full-Time", "Intermediate"),
        (6, "DevOps Engineer", "Cloud Networks", "AWS,Docker,Kubernetes", "Seattle", "Full-Time", "Senior"),
       (7, "Full Stack Developer", "Startup Hub", "JavaScript,Node.js,Angular,MongoDB", "Austin", "Full-Time", "Intermediate"),
        (8, "Data Analyst", "Finance Analytics", "SQL,Python,Tableau", "New York", "Full-Time", "Junior"),
        (9, "Quality Assurance Engineer", "Reliable Software", "Selenium,Java,Testing", "San Francisco", "Contract", "Intermediate"),
        (10, "Systems Administrator", "Enterprise Solutions", "Linux,Networking,Shell Scripting", "Remote", "Full-Time", "Senior")
    ]

    # Insert jobs into the jobs table
    cursor.executemany('INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, ?)', 
jobs)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
