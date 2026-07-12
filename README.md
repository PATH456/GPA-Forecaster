# gpaforecast.com

gpaforecast.com is a student-focused web app for tracking academic terms, courses, grade components, and the best possible grades still available in a term.

The MVP is intentionally focused on one core workflow: create academic terms, add courses, enter grading components, and calculate the best possible course grade, term GPA, and overall GPA.

---

## Features

### Academic Dashboard

- View best possible GPA across all terms
- View total completed/planned credits
- View all academic terms
- Create a new academic term
- Switch between supported GPA scale displays
- Open a term detail page from the dashboard

### Academic Terms

- Create terms with a name, season, and year
- View a term's best possible GPA
- View total credits inside a term
- List all courses in a term
- Add courses without leaving the term page

### Courses

- Create courses with a name, code, and credit value
- View best possible course grade
- View course progress
- Navigate from a term page into a course detail page
- Add grade components for each course

### Grade Components

- Add grading categories such as homework, quizzes, labs, midterms, finals, participation, and projects
- Store component weight, item count, and points per item
- Track individual grade items inside each component
- Use graded and ungraded work to calculate best possible outcomes

### Backend API

- Django REST Framework API foundation
- Health check endpoint at `/api/health/`
- CORS support for a separate Next.js frontend
- SQLite for local development by default
- PostgreSQL support prepared for later development or production

---

## Project Structure

```text
gpaforecast.com/
|-- backend/
|   |-- manage.py
|   |-- requirements.txt
|   |-- .env.example
|   |-- config/
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- asgi.py
|   |   `-- wsgi.py
|   `-- academics/
|       |-- models.py
|       |-- serializers.py
|       |-- views.py
|       |-- urls.py
|       |-- admin.py
|       |-- apps.py
|       |-- constants.py
|       |-- services.py
|       `-- migrations/
|           `-- __init__.py
|
|-- frontend/
|   |-- app/
|   |-- components/
|   |-- lib/
|   |-- styles/
|   |-- design-principals/
|   `-- static-prototype/
|
|-- .gitignore
`-- README.md
```

`backend/config/` contains project-level Django configuration. `backend/academics/` contains the academic domain logic. `frontend/static-prototype/` and `frontend/design-principals/` are design references while the UI is migrated into Next.js.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend Framework | Next.js |
| UI Library | React |
| Frontend Language | JavaScript |
| Backend Framework | Django |
| API | Django REST Framework |
| Local Database | SQLite |
| Production Database Target | PostgreSQL |
| Config | python-decouple |
| CORS | django-cors-headers |
| Static Files | WhiteNoise |
| Production Server | Gunicorn |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 20.9 or newer and npm
- PostgreSQL optional for later development; SQLite is used by default

### 1. Clone the repository

```bash
git clone https://github.com/PATH456/gpaforecast.com
cd gpaforecast.com
```

### 2. Create and activate the backend virtual environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install backend dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure backend environment variables

Copy the example file:

```bash
cp .env.example .env
```

Then edit `backend/.env` for your local machine.

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django signing key for local development | insecure dev key |
| `DJANGO_DEBUG` | Turns Django debug mode on/off | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts Django may serve | `localhost,127.0.0.1` |
| `DJANGO_CORS_ALLOWED_ORIGINS` | Frontend origins allowed to call the API | `http://localhost:3000,http://127.0.0.1:3000` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Trusted browser origins for CSRF checks | `http://localhost:3000,http://127.0.0.1:3000` |
| `DJANGO_USE_POSTGRES` | Use PostgreSQL instead of SQLite | `False` |
| `DJANGO_DB_NAME` | PostgreSQL database name | `gpa_forecast` |
| `DJANGO_DB_USER` | PostgreSQL username | `postgres` |
| `DJANGO_DB_PASSWORD` | PostgreSQL password | empty |
| `DJANGO_DB_HOST` | PostgreSQL host | `localhost` |
| `DJANGO_DB_PORT` | PostgreSQL port | `5432` |

### 5. Check the backend configuration

```bash
python3 manage.py check
```

### 6. Apply database migrations

```bash
python3 manage.py migrate
```

### 7. Run the backend development server

```bash
python3 manage.py runserver
```

The backend runs at `http://127.0.0.1:8000`. The health check endpoint is available at `http://127.0.0.1:8000/api/health/`.

### 8. Install frontend dependencies

Open a second terminal at the project root, then move into the frontend directory:

```bash
cd frontend
npm ci
```

`npm ci` installs the exact frontend package versions recorded in
`package-lock.json`. Use it after cloning the repository and whenever
`package.json` or `package-lock.json` changes.

The frontend uses `package.json` and `package-lock.json` for JavaScript
dependencies. The backend uses `requirements.txt` for Python dependencies.
Do not commit `node_modules/` or a Python virtual environment to Git.

### 9. Configure the frontend environment

```bash
cp .env.local.example .env.local
```

The default frontend API URL points to the Django server at
`http://127.0.0.1:8000`.

### 10. Run the frontend development server

```bash
npm run dev
```

The frontend normally runs at `http://localhost:3000`. Keep the Django server
running in the first terminal while using the frontend.

### Dependency installation summary

```bash



---

## Database

The backend uses SQLite by default so the project can run locally without a separate database server.

To use PostgreSQL, set this in `backend/.env`:

```env
DJANGO_USE_POSTGRES=True
```

Then fill in the `DJANGO_DB_*` variables for your local or hosted PostgreSQL database.

For production, PostgreSQL is recommended.

---

## API Draft

The frontend is expected to call Django REST Framework endpoints.

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/health/` | Confirm the backend is running |
| `GET` | `/api/terms/` | List academic terms |
| `POST` | `/api/terms/` | Create an academic term |
| `GET` | `/api/terms/:id/` | Get one term |
| `DELETE` | `/api/terms/:id/` | Delete one term |
| `GET` | `/api/terms/:id/courses/` | List courses for one term |
| `POST` | `/api/terms/:id/courses/` | Create a course in one term |
| `GET` | `/api/courses/:id/` | Get one course |
| `DELETE` | `/api/courses/:id/` | Delete one course |
| `GET` | `/api/courses/:id/components/` | List grade components |
| `POST` | `/api/courses/:id/components/` | Create a grade component |
| `GET` | `/api/components/:id/items/` | List grade items for one component |
| `PATCH` | `/api/grade-items/:id/` | Update one grade item's score |
| `GET` | `/api/dashboard/summary/` | Get overall GPA and credit summary |

---

## Calculation Rules

### Course Best Possible Grade

```text
graded_weight_score = sum((component_weight_percent / 100) * earned_percent for graded components)
remaining_weight = 100 - sum(component_weight for graded components)
best_possible_percent = graded_weight_score + remaining_weight
```

### Term Best Possible GPA

```text
course_grade_point = convert best_possible_course_percent to selected GPA scale
weighted_points = course_grade_point * course_credits
term_best_possible_gpa = sum(weighted_points) / sum(course_credits)
```

### Overall Best Possible GPA

```text
overall_best_possible_gpa = sum(all course weighted_points) / sum(all course credits)
```

The MVP should use UVic's grading standard as the source of truth for letter grades and 9.0 GPA values.

| Percentage | Letter Grade | UVic 9.0 Value |
|---|---|---|
| `90-100` | `A+` | `9` |
| `85-89` | `A` | `8` |
| `80-84` | `A-` | `7` |
| `77-79` | `B+` | `6` |
| `73-76` | `B` | `5` |
| `70-72` | `B-` | `4` |
| `65-69` | `C+` | `3` |
| `60-64` | `C` | `2` |
| `50-59` | `D` | `1` |
| `0-49` | `E/F` | `0` |

If the MVP keeps a 4.0 scale option, the conversion should be defined as an app-specific display conversion rather than treated as UVic's source-of-truth grading scale.

---

## Environment And Security Notes

- Never commit `backend/.env`.
- Keep `backend/.env.example` committed so teammates know which variables they need.
- Use `DJANGO_` prefixes for Django settings to avoid conflicts with system environment variables.
- Use a strong `DJANGO_SECRET_KEY` in production.
- Set `DJANGO_DEBUG=False` in production.
- Set `DJANGO_ALLOWED_HOSTS` to real production domains before deploying.
- Store production environment variables in the hosting platform's dashboard or secret manager.

---

## Roadmap / TODO

- [ ] Implement the Dashboard `Page` component in `frontend/app/page.js`.
- [ ] Implement a reusable `TermCard` component for the Dashboard.
- [ ] Run the frontend (npm run dev) and backend (python manage.py runserver ) locally, test the Dashboard, and fix any errors found.

---

## License

This project is for personal and educational use unless a different license is added later.
