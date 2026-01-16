import openai

# Replace with your actual OpenAI key or use an environment variable
openai.api_key = "your-api-key-here"

def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

def generate_summary(cv, job):
    prompt = f"Summarize why this person is a good fit:\n\nCV:\n{cv}\n\nJob:\n{job}"
    return ask_openai(prompt)

def generate_bullets(cv, job):
    prompt = f"List 3 bullet points from the CV that match the job:\n\nCV:\n{cv}\n\nJob:\n{job}"
    return ask_openai(prompt).splitlines()

def generate_cover_letter(cv, job):
    prompt = f"Write a short cover letter based on the CV and job:\n\nCV:\n{cv}\n\nJob:\n{job}"
    return ask_openai(prompt)
