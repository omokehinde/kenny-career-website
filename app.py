from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def home():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)

@app.route("/job/<id>")
def show_job(id):
  JOB = load_job_from_db(id)
  if not JOB:
    return 'Note found', 494
  return render_template('jobpage.html', job=JOB)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  data = request.form
  add_application_to_db(id, data)
  return render_template('applicationSubmitted.html', 
                        application=data)

@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)

@app.route("/api/job/<id>")
def show_job_api(id):
  job = load_job_from_db(id)
  return jsonify(job)

if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)