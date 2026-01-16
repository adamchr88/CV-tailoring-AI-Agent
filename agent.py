from parser import read_file
from templates import generate_summary, generate_bullets, generate_cover_letter

def compute_score(cv, job):
    job_words = set(job.lower().split())
    cv_words = set(cv.lower().split())
    match = job_words & cv_words
    score = len(match) / len(job_words) * 100
    return round(score, 1)

def run_agent(cv_path, job_path):
    cv_text = read_file(cv_path)
    job_text = read_file(job_path)

    print("\n📊 Match Score:")
    print(f"{compute_score(cv_text, job_text)}% overlap")

    print("\n🧠 Tailored Summary:")
    print(generate_summary(cv_text, job_text))

    print("\n📌 Relevant Bullet Points:")
    bullets = generate_bullets(cv_text, job_text)
    for bullet in bullets:
        print(f"- {bullet}")

    print("\n✉️ Draft Cover Letter:")
    print(generate_cover_letter(cv_text, job_text))
