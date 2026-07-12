# Project Context

GPA Forecaster is a focused MVP for students who want to forecast the best grades they can still achieve.

## MVP Workflow

```text
Add academic term
  -> Add course inside that term
  -> Add grade components inside that course
  -> Add individual grade items inside each component
  -> Check best possible course grade
  -> Check best possible term GPA
  -> Check best possible overall GPA
```

## Tech Stack

- Frontend: Next.js + React
- Frontend language: JavaScript
- Styling: Tailwind CSS, CSS modules, or one consistent CSS system
- Icons: Lucide React
- Backend: Django + Django REST Framework
- Database: PostgreSQL for production
- Local database: PostgreSQL preferred, SQLite acceptable for early experiments

## Source Of Truth

Read these before making product or UI changes:

```text
README.md
frontend/design-principals/UI-DOCUMENTATION.md
frontend/Roadmap/Todo
```

The demo screenshots in `frontend/design-principals/demo-screenshot/` are the visual reference for the MVP.

## MVP Boundaries

In scope:

- Dashboard
- Add Term modal
- Term detail page
- Add Course modal
- Course detail page
- Add Grade Component modal
- Individual grade item entry
- Best possible course grade
- Best possible term GPA
- Best possible overall GPA
- Desktop and mobile responsive website

Out of scope for MVP:

- User accounts and login
- AI syllabus parsing
- Custom forecast scenarios
- Target GPA calculator
- Charts
- PDF export
- Dark mode
- Native mobile app

## Important Product Notes

- MVP data should be usable without accounts or login.
- UVic's 9.0 grading standard is the source of truth for letter grades and GPA values.
- A 4.0 scale option is still unresolved because UVic's official scale is 9.0-based.
- Add Course should keep the user on the term page and show the new course card.
- The app navigates to a course page only when the user clicks a course card.
