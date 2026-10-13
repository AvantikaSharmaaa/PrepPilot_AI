# PrepPilot AI — Interview Preparation App

A beginner-friendly Streamlit app for practicing technical interviews, HR questions, coding questions, and project explanations.

## Features
- Dashboard with practice metrics and checklist
- Question bank: HR, Python, AI/ML, SQL, Software Development
- Sample answers and transparent keyword-based practice scoring
- One-question-at-a-time mock interview mode
- Beginner coding prompts, hints, and sample solutions
- Project speaking-notes builder with TXT download
- Dark-themed UI
- No paid API key required

## Requirements
- Python 3.10–3.13 recommended
- Internet connection for the first installation only

## Run in VS Code / Windows CMD or PowerShell

Open a terminal in this folder and run:

```bash
py -m venv .venv
```

Activate the environment:

**CMD**
```bat
.venv\Scripts\activate
```

**PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

The app opens in your browser. If it does not, open the local URL shown in the terminal (usually `http://localhost:8501`).

## GitHub upload commands

Create an empty repository on GitHub, then run these commands from this project folder:

```bash
git init
git add app.py requirements.txt README.md .gitignore
git commit -m "Add PrepPilot AI interview preparation app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own repository URL. If a remote already exists, use `git remote set-url origin YOUR-REPOSITORY-URL`.

## Deploy on Streamlit Community Cloud
1. Push the files to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create an app and select your repository.
4. Set the main file path to `app.py`.
5. Deploy.

## Important notes
- This version is an offline-friendly practice tool; it does not use a real AI model.
- The answer score is a basic keyword/length indicator, not a reliable assessment of interview readiness.
- The coding editor does not execute code. Copy a solution into a local `.py` file to run and test it.
- Answers are stored in Streamlit session state during the current session; they are not saved permanently to a database.
