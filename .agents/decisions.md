# Project Decisions

This file records settled product and architecture decisions so teammates do not need to rediscover them.

## Settled Decisions

- Frontend stack is Next.js + React.
- Backend stack is Django + Django REST Framework.
- PostgreSQL is the production database direction.
- MVP should work as a responsive website on desktop and mobile.
- MVP does not include accounts or login.
- Users should be able to test the main flow immediately without signing up.
- MVP focuses on the workflow: term -> course -> grade components -> individual grade items -> best possible GPA.
- Add Course stays on the term page after submission.
- A new course appears as a course card on the term page.
- Users navigate to a course page only by clicking a course card.
- Grade entry should support individual items inside each grade component.
- Example: `Homework` can contain `Homework 1`, `Homework 2`, and `Homework 3`.
- UVic's 9.0 grading standard is the source of truth.
- The UI should match the demo screenshots before new design ideas are added.

## Open Decisions

- If the MVP keeps a `4.0 Scale` option, define the app-specific conversion from UVic's 9.0 scale to 4.0.
- Decide whether old static prototype files should remain as references after the Next.js implementation begins.

## Not MVP

- User accounts
- Login/register
- AI syllabus parsing
- Custom forecast scenarios
- Target GPA calculator
- Charts
- PDF export
- Dark mode
- Native mobile app
