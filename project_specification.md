# PROJECT SPECIFICATION
## Extension Request Sorter

### 1. Project Overview
The Extension Request Sorter is an AI-powered educational application developed using Python and the Google Gemini API. It automates the initial processing and classification of student assignment extension requests.

### 2. Problem Statement
Faculty members spend time manually reading and organizing student extension requests. These requests may contain incomplete information and different explanations. This project uses AI to extract relevant details and Python to validate and classify requests according to predefined policies.

### 3. Objectives
- Automatically process student extension requests.
- Extract course codes, requested days, reasons and summaries.
- Validate extracted information using Python.
- Classify requests using predefined extension policies.
- Generate structured reports for faculty review.

### 4. Input
The application accepts two CSV files:

- `requests.csv`: Student request ID, submission date and original request.
- `courses.csv`: Valid course codes and course names.

At least 20 student requests will be provided.

### 5. AI Processing
Google Gemini extracts exactly four fields in JSON format:

- `course`: Course code or null.
- `days`: Requested extension days (1–30) or null.
- `reason`: medical, family, technical, event, workload or other.
- `summary`: A neutral summary of 15 words or fewer.

The AI must not guess missing information.

### 6. Classification Rules
- Missing course or days: `needs_more_info`
- Days 3 or fewer and reason medical, family or technical: `within_policy`
- All other requests: `needs_faculty_review`

### 7. Output
The application generates:

- `results.csv`: Classification results without original request text.
- `review_queue.csv`: Requests requiring further information or faculty review, including original request text.
- `summary.txt`: Counts grouped by recommendation, reason and course.

### 8. Technologies
Python, Google Gemini API, JSON, CSV, regular expressions, python-dotenv, Git and GitHub.

### 9. Validation and Safety
Python validates AI responses, checks course codes and explicitly stated extension days, retries invalid API responses once and uses a safe fallback when extraction fails. Sensitive information should be excluded from summaries.

### 10. Human Oversight
The system only provides recommendations. It does not approve or reject extension requests. Faculty members retain responsibility for all final decisions.

### 11. Expected Outcome
A working console-based Python application that processes student extension requests, applies predefined policies and generates reports to support faculty review.