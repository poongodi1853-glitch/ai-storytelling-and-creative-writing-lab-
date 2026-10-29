# AI Storytelling & Creative Writing Lab
**Poongodi R - VAC Project **

A polished, responsive storytelling workspace built with Python (Flask), HTML, CSS, JavaScript, and Bootstrap.

## Features
- Responsive landing page and writing workspace
- Story generator with genre, protagonist, setting, mood, story seed, and length controls
- Copy story and save story as a `.txt` file
- Example prompt cards and live word count
- Flask backend for story generation

> Note: The included generator is a local template-based demo, not a connection to a commercial AI model. You can replace the logic in `/generate` with an AI API integration later.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## Project structure
```text
ai_storytelling_lab/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/script.js
```
