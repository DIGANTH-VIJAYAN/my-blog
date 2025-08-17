# Upgraded Blog (Flask)

Simple Flask app.

## Run locally
1. Create a venv and activate:
   - Windows PowerShell:
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
2. Install deps:
   pip install -r requirements.txt

3. Create a `.env` file (not committed) and set:
   MY_GMAIL=your@gmail.com
   MY_PASSWORD=your_app_password
   TO_GMAIL=recipient@gmail.com

4. Start:
   python main.py
   App runs on http://127.0.0.1:5000

## Deploy
- Uses `gunicorn` with Procfile: `web: gunicorn main:app`
- Add environment variables in the hosting dashboard (Render/Railway/etc.).
