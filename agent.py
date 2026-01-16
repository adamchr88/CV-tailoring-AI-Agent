from parser import read_file
from templates import generate_summary, generate_bullets, generate_cover_letter

def run_agent(cv_path, job_path):
    cv_text = read_file(cv_path)
    job_text = read_file(job_path)

    print("\n🧠 Tailored Summary:")
    print(generate_summary(cv_text, job_text))

    print("\n📌 Relevant Bullet Points:")
    print("\n".join(generate_bullets(cv_text, job_text)))

    print("\n✉️ Draft Cover Letter:")
    print(generate_cover_letter(cv_text, job_text))
