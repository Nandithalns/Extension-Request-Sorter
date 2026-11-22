# Extension Request Sorter – Education

## Project Overview
The Extension Request Sorter is an AI-powered Python application that analyses student assignment extension requests using the Google Gemini API.

It extracts important information, validates the extracted details, and classifies requests according to predefined academic policies.

## Features
- Reads student requests from a CSV file.
- Uses Google Gemini to extract course, requested days, reason, and summary.
- Validates extracted information using Python.
- Classifies requests into three categories:
  - `within_policy`
  - `needs_faculty_review`
  - `needs_more_info`
- Generates CSV reports and a summary report.
- Keeps final approval or rejection decisions with faculty.

## Technologies Used
- Python 3
- Google Gemini API
- CSV
- SQLite is not required.
- python-dotenv

## Project Files
- `main.py` – Main application.
- `requests.csv` – Sample student extension requests.
- `courses.csv` – Valid course codes.
- `system_prompt.txt` – Five-role system prompt.
- `.env` – API key and model configuration (not committed to Git).
- `outputs/` – Generated reports.

## Installation
Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Running the Project
Run:

```bash
python main.py
```

The application generates:
- `results.csv`
- `review_queue.csv`
- `summary.txt`

## Important Note
The application provides recommendations only. Faculty members retain responsibility for final decisions.