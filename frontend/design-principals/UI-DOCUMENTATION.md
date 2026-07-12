# gpaforecast.com UI Documentation
**Version:** MVP design spec  
**Last Updated:** July 5, 2026  
**Primary References:** demo screenshots in `frontend/design-principals/demo-screenshot/`  
**MVP Goal:** Add one academic term, add one course, add grade components, then see the best possible grade for that course, the best possible GPA for that term, and the best possible overall GPA so far.

---

## Product Direction

gpaforecast.com is a focused academic planning web app. The first MVP is not a general school dashboard, transcript manager, AI syllabus parser, or advanced scenario planner. The first MVP should do one workflow very well:

```text
Dashboard
  -> Add academic term
  -> Open term
  -> Add course
  -> Open course
  -> Add grade components
  -> Check best possible course grade
  -> Check best possible term GPA
  -> Check best possible overall GPA
```

The UI should match the screenshots as closely as possible before expanding the feature set.

---

## Tech Context

### Frontend
- Next.js
- React
- JavaScript
- CSS modules, Tailwind CSS, or a consistent project CSS system
- Lucide React icons for UI icons

### Backend
- Django
- Django REST Framework
- PostgreSQL for production
- SQLite is acceptable only for early local development if needed

### MVP Form Factor
- Desktop website first
- Mobile responsive website second
- No native mobile app for MVP

---

## Visual Style

### Overall Feel
- Clean, modern SaaS-style interface
- Light gray page background
- White cards and modal surfaces
- Indigo primary actions
- Green used for best-possible grade/GPA values
- Quiet gray text for supporting information
- Spacious layout with strong alignment

### Colors From Screenshots
- Page background: very light gray, close to `#f9fafb`
- Card/modal background: `#ffffff`
- Primary indigo button/icon: close to `#6366f1`
- Success green metric: close to `#10b981`
- Primary text: dark gray/navy, close to `#111827`
- Secondary text: gray, close to `#4b5563` / `#6b7280`
- Muted icon/text: close to `#9ca3af`
- Borders: light gray, close to `#e5e7eb`
- Overlay: gray/black translucent overlay with background blur

### Typography
- Use a clean sans-serif system font stack.
- Page titles are large, bold, and dark.
- Section headings are smaller than page titles but still bold.
- Card labels are medium-weight and muted.
- Main stat values are large and bold.
- Button text is medium or semibold.

### Components
- Cards are white with subtle border/shadow and rounded corners.
- Buttons use icon + text when the screenshot shows an icon.
- Primary buttons are indigo with white text.
- Secondary buttons are white with subtle border and dark gray text.
- Modal inputs are full-width, rounded, bordered, and tall enough to feel comfortable.
- Empty states use a circular pale gray icon background.

---

## Routes

Use Next.js routes that correspond to the screenshot flows:

```text
/                  Dashboard / homepage
/terms/[termId]    Term detail page
/courses/[courseId] Course detail page
```

The screenshots show Figma preview routes, but the implemented app should use clean app routes.

---

## 1. Dashboard

Reference screenshot: `homepage.png`

### Purpose
The dashboard shows the user's overall GPA forecast and the list of academic terms.

### Layout
- Centered max-width content area.
- Top header row with app identity on the left and GPA scale controls on the right.
- Two stat cards below the header.
- Academic Terms section below the stat cards.
- Empty state appears inside a large white card when there are no terms.

### Header
Left side:
- Indigo square icon with a white graduation cap.
- App title: `GPA Calculator`
- Subtitle: `Track your academic progress and forecast your grades`

Right side:
- Settings gear icon.
- GPA scale select, shown in screenshot as `4.0 Scale`.

### Dashboard Stat Cards
Two cards in a responsive grid.

Card 1:
- Label: `Best Possible GPA`
- Value when no data: an em dash-like placeholder shown visually as a green dash
- Subtext: `4.0 scale` or `9.0 scale`
- Value color: green
- Meaning: best possible cumulative GPA across all terms from the first term to now

Card 2:
- Label: `Total Credits`
- Value when no data: `0.0`
- Subtext: `Completed & in progress`
- Value color: dark text
- Meaning: total credits across all courses included in the GPA forecast

### Academic Terms Section
Header:
- Left: `Academic Terms`
- Right: primary button `+ Add Term`

Empty state:
- Large white card.
- Centered circular icon area using a book icon.
- Title: `No terms yet`
- Description: `Get started by adding your first academic term`
- CTA: `+ Add Your First Term`

Term cards after data exists:
- Not shown in the provided screenshots.
- For MVP, term cards should be simple and consistent with the existing card style.
- Required information: term season/year, term name, best possible term GPA, course count, total credits.

### Dashboard Behavior
- `Add Term` and `Add Your First Term` open the Add New Term modal.
- Selecting a term card navigates to the term detail page.
- Changing the GPA scale updates displayed GPA values.

---

## 2. Add New Term Modal

Reference screenshot: `addTermOverlay.png`

### Purpose
Create one academic term.

### Modal Appearance
- Background page is blurred and dimmed.
- Modal is centered on the screen.
- Modal width is medium, close to 600px in the screenshot.
- Header has title on the left and an X close button on the right.
- Header and body are separated by a light divider.

### Header
- Title: `Add New Term`
- Close button: X icon

### Fields
1. `Term Name`
   - Text input
   - Placeholder: `e.g., Freshman Fall`
   - Required

2. `Season`
   - Select input
   - Default shown: `Fall`
   - Options needed for MVP: `Spring`, `Summer`, `Fall`

3. `Year`
   - Number input or select
   - Default shown: `2026`
   - Required

### Footer
- Left button: `Cancel`
- Right button: `Add Term`

### Behavior
- X closes the modal.
- Cancel closes the modal.
- Add Term creates the term.
- After creation, the app should show the new term on the dashboard.

---

## 3. Term Detail Page

Reference screenshot: `termpage.png`

### Purpose
Show one academic term, its best possible term GPA, total credits, and courses.

### Layout
- Centered max-width content area.
- Back link at the top.
- Term title and subtitle.
- Two stat cards.
- Courses section with add button.
- Empty state appears when the term has no courses.

### Back Link
- Text: `Back to Dashboard`
- Left arrow icon.
- Navigates to `/`.

### Header
- Page title example: `Fall 2026`
- Subtitle example: `Fall 2026`
- The screenshot shows both title and subtitle. If the term name is different from season/year, use the term name as the subtitle.

### Term Stat Cards
Card 1:
- Label: `Best Possible GPA`
- Value when no courses: green dash placeholder
- Subtext: `4.0 scale` or `9.0 scale`
- Meaning: best possible GPA for this term only

Card 2:
- Label: `Total Credits`
- Value when no courses: `0.0`
- Subtext: `Credit hours`
- Meaning: total credits for all courses in this term

### Courses Section
Header:
- Left: `Courses`
- Right: primary button `+ Add Course`

Empty state:
- Large white card.
- Centered circular icon area using a book icon.
- Title: `No courses yet`
- Description: `Add courses to start tracking your grades`
- CTA: `+ Add Your First Course`

Course cards after data exists:
- Not shown in the provided screenshots.
- For MVP, course cards should include course name, course code, credit hours, best possible grade, and enough information to open the course page.

### Behavior
- `Add Course` and `Add Your First Course` open the Add New Course modal.
- Selecting a course card navigates to the course detail page.

---

## 4. Add New Course Modal

Reference screenshot: `addCourseOverlay.png`

### Purpose
Create one course inside the current term.

### Modal Appearance
- Same overlay treatment as Add New Term.
- Modal is centered.
- Header and body are separated by a divider.

### Header
- Title: `Add New Course`
- Close button: X icon

### Fields
1. `Course Name`
   - Text input
   - Placeholder: `e.g., Introduction to Computer Science`
   - Required

2. `Course Code`
   - Text input
   - Placeholder: `e.g., CS 101`
   - Required

3. `Credit Hours`
   - Number input
   - Default shown: `3`
   - Helper text: `You can use decimal values like 1.5, 2.5, etc.`
   - Required

### Footer
- Left button: `Cancel`
- Right button: `Add Course`

### Behavior
- Add Course creates the course under the current term.
- After creation, the modal closes and the course appears as a new course card on the term page.
- The user stays on the term page after adding a course.
- The app navigates to the course detail page only when the user clicks a course card.

---

## 5. Course Detail Page

Reference screenshot: `coursepage.png`

### Purpose
Show one course, its best possible grade, course progress, and grading breakdown.

### Layout
- Centered max-width content area.
- Header with course name and metadata.
- Two stat cards.
- Grading Breakdown panel.
- Empty state appears when no grade components exist.

### Header
The screenshot shows:
- Title: `Calculus I`
- Metadata: `Math 100 - 1.5 credits`

For implementation:
- Use course name as the main title.
- Use course code and credits as the metadata row.

### Course Stat Cards
Card 1:
- Label: `Best Possible Grade`
- Value example: `100.0%`
- Value color: green
- Subtext example: `A - If 100% on remaining work`
- Meaning: highest possible final percentage for this course if all ungraded remaining work receives 100%

Card 2:
- Label: `Course Progress`
- Value example: `0%`
- Subtext example: `Of 0% total weight graded`
- Progress bar at bottom of card
- Meaning: how much of the total course weight has entered grades

### Grading Breakdown Section
Container:
- White card/panel with border/shadow.
- Header row with `Grading Breakdown` on the left and `+ Add Component` button on the right.
- Header and body are separated by a divider.

Empty state:
- Centered circular icon area using an upward chart/trend icon.
- Title: `No grade components yet`
- Description: `Add components like assignments, exams, and participation`
- CTA: `+ Add First Component`

Grade component table after data exists:
- Not shown in the provided screenshots.
- For MVP, it should clearly show component name, weight, graded item progress, and current component grade.
- Each component should be expandable or clickable so the user can manage its individual grade items.

### Behavior
- `Add Component` and `Add First Component` open the Add Grade Component modal.
- Updating individual grade item values recalculates the component grade, course progress, and course best possible grade.

---

## 6. Add Grade Component Modal

Reference screenshot: `gradeComponentsOverlay.png`

### Purpose
Add a grade component such as participation, homework, assignments, labs, quizzes, exams, or projects.

### Modal Appearance
- Same overlay treatment as other modals.
- Modal content is vertically scrollable when the content exceeds viewport height.
- Header is fixed at top of modal content area visually.

### Header
- Title: `Add Grade Component`
- Close button: X icon

### Quick Add Section
Label:
- `Quick add common components:`

Buttons shown in screenshot:
- `Participation`
- `Homework`
- `Assignments`
- `Labs`
- `Quizzes`
- `Midterm Exam`
- `Final Exam`
- `Project`

Behavior:
- Selecting a quick-add option should fill the component name field.
- The selected option may show a subtle highlighted state.

### Component Fields
1. `Component Name`
   - Text input
   - Placeholder: `e.g., Labs`
   - Required

2. `Weight (%)`
   - Number input
   - Default shown: `10`
   - Required
   - Represents percent of final course grade

### Individual Items Section
This section appears in a light gray nested panel.

Heading:
- `Individual Items`

Fields:
1. `How many items in total?`
   - Number input
   - Default shown: `1`

2. `Points per item`
   - Number input
   - Default shown: `100`

Preview:
- Example text: `Preview: This will create 1 item, each worth 100 points.`

Footer:
- The screenshot cuts off the bottom of the modal. The MVP should include `Cancel` and `Add Component` buttons consistent with the other modals.

### Behavior
- Add Component creates a component under the current course.
- The component can represent one item or multiple individual items.
- For MVP, the app should create the requested number of grade items under the component.
- Example: if the user creates `Homework` with `5` items and `10` points per item, the app creates `Homework 1` through `Homework 5`, each worth `10` points.
- Users should be able to enter scores for each grade item separately so the app matches real course grading.

---

## MVP Calculation Rules

### Course Best Possible Grade
For a course:

```text
graded_weight_score = sum((component_weight_percent / 100) * earned_percent for graded components)
remaining_weight = 100 - sum(component_weight for graded components)
best_possible_percent = graded_weight_score + remaining_weight
```

Example: if 20% of the course is graded at 80%, then the graded contribution is 16 percentage points. If the remaining 80% receives 100%, the best possible grade is 96%.

### Course Progress

```text
course_progress = total graded component weight / total expected course weight
```

For MVP, assume the expected total course weight is 100%.

### Term Best Possible GPA
For a term:

```text
course_grade_point = convert best_possible_course_percent to selected GPA scale
weighted_points = course_grade_point * course_credits
term_best_possible_gpa = sum(weighted_points) / sum(course_credits)
```

### Overall Best Possible GPA
Across all terms:

```text
overall_best_possible_gpa = sum(all course weighted_points) / sum(all course credits)
```

### GPA Scale
The MVP should use UVic's 9.0 grading standard as the source of truth.

| Percentage | Letter grade | UVic 9.0 value |
| --- | --- | --- |
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

The app can still include both `4.0 Scale` and `9.0 Scale` options in the UI, but UVic's official scale is 9.0. A 4.0 option would need a separate project-specific conversion rule.

---

## Responsive Requirements

### Desktop
- Match the screenshot composition first.
- Content should remain centered and not stretch too wide.
- Stat cards use two columns where shown.
- Section action buttons sit on the right side of section headers.

### Mobile
- Same website, responsive layout.
- Header content may stack.
- Stat cards should stack or use a readable single-column layout.
- Section buttons should become full width if horizontal layout feels cramped.
- Modals should fit within the viewport with scrollable content.

---

## Not In MVP

These are intentionally out of scope for the first MVP:
- User accounts and login. MVP data should be usable without creating an account.
- AI syllabus parsing
- Custom GPA scenarios
- Target GPA calculator
- Charts and trend analysis
- PDF export
- Dark mode
- Native mobile app
- Full transcript/history analytics

---

## Confirmed MVP Decisions

- After adding a course, stay on the term page and show the new course card.
- Navigate to a course page only when the user clicks a course card.
- MVP should support both 4.0 and 9.0 GPA scale options.
- MVP should not require accounts or login.
- Users should be able to test the main flow immediately: add term, add course, add grade components, and see forecast results.
- The grading table should be based on UVic's standard.
- Grade entry should support individual items inside each component, such as `Homework 1`, `Homework 2`, and `Homework 3`.

## Needs Confirmation Before Implementation

The screenshots and current product decisions still do not fully answer this detail:

1. If the MVP includes a `4.0 Scale` option, what app-specific conversion should be used from UVic's 9.0 scale to 4.0?
   - UVic's official table is 9.0-based.
   - A 4.0 table would be an additional app feature, not the UVic source-of-truth scale.
