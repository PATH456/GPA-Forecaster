# Backend Agent Guide

Use this when working on the Django + Django REST Framework backend.

## Backend Purpose

The backend stores academic data and owns the calculation logic for GPA forecasting.

## Target Stack

- Django
- Django REST Framework
- PostgreSQL for production
- SQLite acceptable only for early local development
- No user accounts or login in the MVP

## Core Models

```text
AcademicTerm
  term_name
  season
  year

Course
  term
  course_name
  course_code
  credit_hours

GradeComponent
  course
  name
  weight_percent
  item_count
  points_per_item

GradeItem
  component
  name
  points_earned
  points_possible
  is_graded
```

## API Shape

Expected MVP endpoints:

```text
GET    /api/terms/
POST   /api/terms/
GET    /api/terms/:id/
DELETE /api/terms/:id/
GET    /api/terms/:id/courses/
POST   /api/terms/:id/courses/
GET    /api/courses/:id/
DELETE /api/courses/:id/
GET    /api/courses/:id/components/
POST   /api/courses/:id/components/
GET    /api/components/:id/items/
PATCH  /api/grade-items/:id/
GET    /api/dashboard/summary/
```

## Calculation Ownership

Backend services should calculate:

- course best possible grade
- course progress
- term best possible GPA
- overall best possible GPA
- UVic letter grade
- UVic 9.0 GPA value

The frontend may do temporary optimistic previews, but Django should be the source of truth.

## UVic Grading Standard

```text
90-100 -> A+  -> 9
85-89  -> A   -> 8
80-84  -> A-  -> 7
77-79  -> B+  -> 6
73-76  -> B   -> 5
70-72  -> B-  -> 4
65-69  -> C+  -> 3
60-64  -> C   -> 2
50-59  -> D   -> 1
0-49   -> E/F -> 0
```

## MVP Constraints

- Do not build authentication yet.
- Do not add AI syllabus parsing.
- Keep business logic in service/helper functions rather than duplicating formulas inside views.
- Validate component weights and grade item scores before saving.
- Make API responses convenient for the frontend pages described in the UI documentation.
