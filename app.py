from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('job_recommendation.db')

@app.route('/recommend', methods=['POST'])
def recommend_jobs():
    user_profile = request.json

    # Validate input
    if not user_profile:
        return jsonify({"error": "No user profile provided"}), 400
    if 'skills' not in user_profile or not isinstance(user_profile['skills'], list):
        return jsonify({"error": "Skills must be a list"}), 400
    if 'preferences' not in user_profile or 'locations' not in user_profile['preferences']:
        return jsonify({"error": "Preferences must include locations"}), 400

    user_skills = set(user_profile['skills'])
    user_experience = user_profile['experience_level']
    user_locations = user_profile['preferences']['locations']
    user_job_type = user_profile['preferences']['job_type']

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": "Database error: " + str(e)}), 500
    finally:
        if conn:
            conn.close()

    recommendations = []
    for job in jobs:
        job_id, job_title, company, required_skills, location, job_type, experience_level = job
        required_skills_set = set(json.loads(required_skills))

        if (user_experience == experience_level and 
            job_type == user_job_type and 
            location in user_locations and 
            user_skills.intersection(required_skills_set)):
            
            recommendations.append({
                "job_title": job_title,
                "company": company,
                "location": location,
                "job_type": job_type,
                "required_skills": json.loads(required_skills),
                "experience_level": experience_level
            })

    return jsonify(recommendations)

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

