def generate_summary(cv, job):
    if "python" in job.lower() and "python" in cv.lower():
        return "You have Python experience, which matches this role well."
    return "Based on the job description and your CV, you are a good match."

def generate_bullets(cv, job):
    bullets = []
    if "team" in job.lower():
        if "team" in cv.lower():
            bullets.append("Worked collaboratively in team environments.")
    if "api" in job.lower() and "api" in cv.lower():
        bullets.append("Developed and consumed APIs in past projects.")
    return bullets or ["No strong matches found — consider revising your CV."]

def generate_cover_letter(cv, job):
    return f"""Dear Hiring Manager,

I am excited to apply for this position. My background aligns with the key requirements you've listed, and I am confident I can contribute meaningfully to your team.

Sincerely,
Your Name
"""
