from sqlalchemy import create_engine, text

url = "mysql+pymysql://hyq5lpsc14cytkcu3spd:pscale_pw_cFouzNqFjNHuFOqwNF8RNeH4CFa6S9gXQ4IYUTNMAHb@us-east.connect.psdb.cloud/kennycareer?charset=utf8mb4"

engine = create_engine( 
  url, connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  jobs = []
  for row in result.all():
    jobs.append(dict(row._mapping ))
    
  return jobs