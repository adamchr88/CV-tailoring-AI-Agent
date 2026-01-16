from ollama import Client

client = Client(host='http://localhost:11434')

def ask_ollama(prompt):
    response = client.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

def generate_summary(cv, job):
    prompt = f"Summarize why this person is a good fit:\n\nCV:\n{cv}\n\nJob:\n{job}"
    return ask_ollama(prompt)

def generate_bullets(cv, job):
    prompt = f"List 3 bullet points from the CV that match the job:\n\nCV:\n{cv}\n\nJob:\n{job}"
    text = ask_ollama(prompt)
    return [line.strip("- ").strip() for line in text.splitlines() if line.strip()]

def generate_cover_letter(cv, job):
    prompt = f"Write a short cover letter based on the CV and job:\n\nCV:\n{cv}\n\nJob:\n{job}"
    return ask_ollama(prompt)
