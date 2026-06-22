# CV Tailoring AI Agent

A Python-based AI application that helps users tailor their CV for specific internship and job applications.

The app takes a CV and a job description as input, then generates tailored application content such as a stronger CV summary, improved bullet points, and a personalised cover letter.

This project was built to explore how AI can support the job application process by making CV tailoring faster, clearer, and more targeted.

---

## Features

- Tailors CV content to a specific job description
- Generates a professional CV summary
- Suggests improved CV bullet points
- Creates a tailored cover letter
- Includes a Streamlit web interface
- Supports AI-powered text generation
- Uses a modular Python structure
- Includes example files for testing and demonstration

---

## Tech Stack

- Python
- Streamlit
- OpenAI / Ollama
- File handling
- Prompt engineering
- AI agent design

---

## Project Structure

```text
CV-tailoring-AI-Agent/
│
├── examples/          # Example CVs and job descriptions
├── agent.py           # Main AI agent logic
├── file_utils.py      # File reading and processing functions
├── run.py             # Main script for running the project
├── templates.py       # Prompt templates used by the AI agent
├── web_app.py         # Streamlit web application
└── README.md          # Project documentation
```

---

## How It Works

1. The user provides their CV.
2. The user provides a job description.
3. The application processes both inputs.
4. The AI agent compares the CV against the job requirements.
5. The app generates tailored application content, including:
   - A stronger professional summary
   - Improved CV bullet points
   - A tailored cover letter

---

## Example Use Case

A computer science student applying for a software engineering internship can use this tool to tailor their CV toward a specific job description.

For example, if the job description mentions skills such as Python, teamwork, problem solving, and software development, the AI agent can help highlight the most relevant parts of the CV and rewrite sections to better match the role.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/adamchr88/CV-tailoring-AI-Agent.git
```

Move into the project folder:

```bash
cd CV-tailoring-AI-Agent
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run web_app.py
```

Alternatively, run the Python script:

```bash
python run.py
```

Windows Note

If you have more than one version of Python installed and get a module error such as No module named 'pypdf', use:

```bash
py -3.12 -m pip install -r requirements.txt
```

Then run the app with:

```bash
py -3.12 -m streamlit run web_app.py
```

---

## What I Learned

Through this project, I practised:

- Building a Python application with multiple files
- Creating a simple AI agent workflow
- Writing and structuring prompts
- Processing user input from CVs and job descriptions
- Building a web interface with Streamlit
- Designing a practical tool for real-world use
- Organising a project clearly for GitHub

---

## Future Improvements

- Add full PDF parsing support
- Add CV-to-job match scoring
- Highlight missing keywords from the job description
- Allow users to download the generated cover letter
- Improve the Streamlit user interface
- Add support for more CV formats
- Save previous application outputs
- Add better formatting for generated CV sections

---

## Skills Demonstrated

- Python programming
- AI agent development
- Prompt engineering
- Streamlit web development
- File handling
- Modular programming
- Problem solving
- User-focused software design

---

## Author

**Adam Christensen**  
Computer Science Student  

GitHub: [adamchr88](https://github.com/adamchr88)
