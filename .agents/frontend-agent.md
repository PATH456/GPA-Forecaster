# Frontend Agent Guide

Use this when working on the Next.js + React frontend.

## Primary References

- `frontend/design-principals/UI-DOCUMENTATION.md`
- `frontend/design-principals/demo-screenshot/`
- `README.md`

## Routes

Target MVP routes:

```text
/                    Dashboard
/terms/[termId]      Term detail page
/courses/[courseId]  Course detail page
```

## UI Priorities

- Match the screenshots before adding new visual ideas.
- Keep the layout clean, light, and SaaS-like.
- Use white cards, light gray page background, indigo primary buttons, green best-possible values, and quiet gray supporting text.
- Build reusable components for cards, buttons, inputs, selects, modals, stat cards, and empty states.
- Use icon + text buttons where the design shows icons.
- Use Lucide React icons.
- Make the MVP responsive for desktop and mobile.

## Required MVP Behavior

- Dashboard shows best possible overall GPA, total credits, and academic terms.
- Add Term modal creates a term and returns to the dashboard.
- Term page shows best possible term GPA, total credits, and course cards.
- Add Course modal creates a course, closes, and stays on the term page.
- Course page opens only when a user clicks a course card.
- Course page shows best possible course grade, course progress, and grading breakdown.
- Add Grade Component modal creates grade components and individual grade items.
- Users can enter scores for individual grade items, such as `Homework 1`, `Homework 2`, and `Homework 3`.

## Avoid During MVP

- Do not add login UI.
- Do not add AI upload flows.
- Do not add charts unless requested later.
- Do not invent a landing page; the first screen should be the usable dashboard.
- Do not redesign away from the Figma/demo screenshot direction.

## Data Contract Expectations

The frontend should treat Django REST Framework as the API source. Calculation values may come from backend responses so the UI stays consistent across pages.
