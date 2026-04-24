# GPA Calculator - UI Documentation v1.0
**Last Updated:** April 24, 2026  
**Focus:** GPA Forecasting Tool

---

## Overview

A modern, minimal GPA calculator and grade forecasting tool for university students. The application uses a clean, SaaS-style aesthetic similar to Notion or Linear, with a card-based responsive layout and consistent indigo accent styling.

### Key Philosophy
- **Single Feature Focus:** GPA Forecasting - calculating the best possible GPA students can achieve
- **Minimal Design:** Clean, spacious layouts with ample white space
- **Consistent Styling:** Reusable components with indigo (#6366f1) as the primary accent color
- **Responsive:** Mobile-first approach that scales to desktop

---

## Design System

### Color Palette
- **Primary Accent:** `#6366f1` (Indigo) - Used for buttons, icons, key metrics
- **Background:** `#f9fafb` (Gray-50) - Page background
- **Card Background:** `#ffffff` (White)
- **Text Primary:** `#111827` (Gray-900)
- **Text Secondary:** `#6b7280` (Gray-600)
- **Text Muted:** `#9ca3af` (Gray-400)
- **Border:** `#f3f4f6` (Gray-100)
- **Success Green:** Used for "Best Possible GPA" stat cards
- **Neutral Gray:** Used for general stat cards

### Typography
- **Headers (h1):** 2xl-3xl, semibold, gray-900
- **Subheaders (h2):** lg-xl, semibold, gray-900
- **Card Titles (h3):** base, semibold, gray-900
- **Body Text:** sm-base, regular, gray-600
- **Stat Values:** lg-2xl, semibold, varies by context
- **Font Family:** System default (sans-serif)

### Component Patterns

#### Card Component
- White background
- Rounded corners (lg = 8px)
- Subtle shadow
- Padding: 1.5rem (24px)
- Hover state: Slightly elevated shadow (for clickable cards)
- Border: None (shadow defines edges)

#### Button Component
**Primary Button:**
- Background: Indigo (#6366f1)
- Text: White
- Rounded: lg
- Padding: 0.625rem 1rem
- Hover: Darker indigo
- Icon + Text layout with gap-2

**Secondary Button (if used):**
- Background: White
- Border: Gray-300
- Text: Gray-700
- Same sizing as primary

#### Stat Card Component
- Labeled value display
- Label: Small, gray-600, uppercase or title case
- Value: Large, semibold, color-coded
- Subtext: Extra small, gray-500
- Responsive grid layout
- Left-aligned content
- Color variants: blue, green, gray

#### Modal Component
- Fixed overlay: Black with 50% opacity
- Modal container: White, centered, rounded-xl
- Max width: 28rem (448px)
- Padding: 1.5rem
- Header: Title + Close button (X icon)
- Body: Form fields with labels
- Footer: Cancel (secondary) + Confirm (primary) buttons

---

## App Structure

### Navigation & Routing
The app uses React Router with the following routes:

1. **`/` - Dashboard (Homepage)**
2. **`/term/:termId` - Individual Term View**
3. **`/course/:courseId` - Course Detail View**

### Global Header Elements
Each page includes:
- **GPA Scale Selector** (Dashboard only): Dropdown to switch between 4.0 and 9.0 scale
- **Back Navigation** (Sub-pages only): Arrow + "Back to [Previous Page]" link

---

## Screen-by-Screen Documentation

---

## 1. Dashboard (Homepage) - Route: `/`

### Layout Structure
```
┌─────────────────────────────────────────────┐
│ [Indigo Icon] GPA Calculator    [Settings] │ ← Header
│ Track your academic progress and forecast   │
│                                             │
│ ┌────────────────┐ ┌────────────────┐      │ ← 2-Column Stat Cards
│ │ Best Possible  │ │ Total Credits  │      │
│ │ GPA            │ │                │      │
│ └────────────────┘ └────────────────┘      │
│                                             │
│ Academic Terms              [+ Add Term]    │ ← Section Header
│                                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐    │ ← Term Cards Grid
│ │ Fall 2025│ │ Spring   │ │ Fall 2024│    │   (3 columns on desktop,
│ │          │ │ 2025     │ │          │    │    2 on tablet,
│ │          │ │          │ │          │    │    1 on mobile)
│ └──────────┘ └──────────┘ └──────────┘    │
└─────────────────────────────────────────────┘
```

### Header Section
**Main Title Area:**
- Indigo square icon with white graduation cap (GraduationCap from lucide-react)
- Title: "GPA Calculator" - Large, semibold
- Subtitle: "Track your academic progress and forecast your grades" - Gray, regular

**Settings Section (Top Right):**
- Settings gear icon (small, gray)
- Dropdown select: "4.0 Scale" or "9.0 Scale"
- Width: 96px (w-24)
- Positioned with flexbox alignment

### Overall Stats Section
**Grid Layout:** 2 columns on all screen sizes (grid-cols-1 sm:grid-cols-2)

**Card 1: Best Possible GPA**
- Label: "Best Possible GPA"
- Value: `X.XX` (2 decimal places) or "—" if no data
- Subtext: "[4.0 or 9.0] scale"
- Color: Green accent
- **Calculation:** Best possible GPA combining all courses (completed + in-progress assuming 100% on remaining work)

**Card 2: Total Credits**
- Label: "Total Credits"
- Value: `XX.X` (1 decimal place)
- Subtext: "Completed & in progress"
- Color: Gray (neutral)
- **Calculation:** Sum of all credit hours from all courses across all terms

### Academic Terms Section

**Section Header:**
- Left: "Academic Terms" (h2, semibold)
- Right: "Add Term" button (primary, indigo)
  - Plus icon
  - Full width on mobile, auto width on desktop

**Empty State** (when no terms exist):
- Centered card with generous padding
- Icon: BookOpen (large, gray, in circular gray background)
- Title: "No terms yet" (semibold)
- Description: "Get started by adding your first academic term"
- CTA Button: "Add Your First Term" (primary button with Plus icon)

**Term Cards Grid** (when terms exist):
- Grid: 1 column (mobile) → 2 columns (tablet) → 3 columns (desktop)
- Gap: 1rem (16px) between cards
- Cards are clickable links to term detail page
- Sorted: Most recent first (by year DESC, then season DESC where Fall > Summer > Spring)

**Individual Term Card:**
```
┌─────────────────────────────────┐
│ [Calendar Icon] Fall 2025  [🗑️]│ ← Header with delete
│ Fall Semester 2025              │ ← Term name
│ ─────────────────────────────── │ ← Divider
│ Term GPA           4.00         │ ← Metrics
│ Courses              5          │
│ Credits            15.0         │
└─────────────────────────────────┘
```

**Card Elements:**
1. **Header Row:**
   - Calendar icon (gray-400, small)
   - Season + Year (semibold, truncated if too long)
   - Delete button (trash icon, hover shows gray background)

2. **Term Name:**
   - User-provided name/description
   - Gray-600, small text
   - Truncated with ellipsis if too long

3. **Divider:** Thin gray-100 line with top padding/margin

4. **Metrics (3 rows):**
   - **Term GPA:** Calculated from courses in this term
     - Label (left): "Term GPA"
     - Value (right): X.XX in indigo, large, semibold
     - Shows "—" if no courses
   - **Courses:** Count of courses
     - Label (left): "Courses"
     - Value (right): Number, gray-900, medium weight
   - **Credits:** Sum of credit hours
     - Label (left): "Credits"
     - Value (right): Number, gray-900, medium weight

**Hover State:**
- Entire card elevates slightly (shadow increases)
- Cursor becomes pointer
- Delete button shows background on hover

**Delete Interaction:**
- Click delete icon
- Browser confirm: "Delete this term and all its courses?"
- If confirmed: Term and all associated courses are removed
- Prevents event bubbling (doesn't navigate to term page)

---

## 2. Add Term Modal

**Trigger:** Click "Add Term" button from Dashboard

### Modal Structure
```
┌──────────────────────────────────┐
│ Add New Term              [X]    │ ← Modal Header
│                                  │
│ Term Name                        │ ← Form Fields
│ ┌──────────────────────────────┐│
│ │ e.g., Fall Semester 2025     ││
│ └──────────────────────────────┘│
│                                  │
│ Season          Year             │
│ ┌──────────┐   ┌──────────────┐ │
│ │ Fall ▼   │   │ 2025      ▼  │ │
│ └──────────┘   └──────────────┘ │
│                                  │
│          [Cancel]  [Add Term]    │ ← Actions
└──────────────────────────────────┘
```

### Form Fields

**1. Term Name (Text Input)**
- Label: "Term Name"
- Placeholder: "e.g., Fall Semester 2025"
- Required field
- Full width
- Standard input styling (border, rounded, padding)

**2. Season (Dropdown)**
- Label: "Season"
- Options: Spring, Summer, Fall
- Default: Fall
- Width: 50% (inline with Year)

**3. Year (Dropdown)**
- Label: "Year"
- Options: 2020 through 2030
- Default: Current year (2026)
- Width: 50% (inline with Season)

### Footer Buttons
- **Cancel:** Secondary button, closes modal without saving
- **Add Term:** Primary button (indigo), creates term and closes modal
  - Disabled if form is invalid

### Behavior
- Closes when clicking X, Cancel, or clicking outside modal (overlay)
- Creates new term with empty courses array
- After creation: Modal closes, term appears in grid
- No navigation (stays on Dashboard)

---

## 3. Term View Page - Route: `/term/:termId`

### Layout Structure
```
┌─────────────────────────────────────────────┐
│ ← Back to Dashboard                         │ ← Breadcrumb
│                                             │
│ Fall 2025                                   │ ← Page Header
│ Fall Semester 2025                          │
│                                             │
│ ┌────────────────┐ ┌────────────────┐      │ ← 2 Stat Cards
│ │ Best Possible  │ │ Total Credits  │      │
│ │ GPA            │ │                │      │
│ └────────────────┘ └────────────────┘      │
│                                             │
│ Courses                     [+ Add Course]  │ ← Section Header
│                                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐    │ ← Course Cards
│ │ MATH 101 │ │ CS 201   │ │ PHYS 150 │    │
│ └──────────┘ └──────────┘ └──────────┘    │
└─────────────────────────────────────────────┘
```

### Breadcrumb Navigation
- Arrow left icon + "Back to Dashboard"
- Gray-600 text, hover to gray-900
- Clickable link to `/`
- Positioned at top with bottom margin

### Page Header
- **Main Title:** Season + Year (e.g., "Fall 2025") - 2xl/3xl, semibold
- **Subtitle:** Term name (user-provided description) - gray-600
- Spacing: Title mb-2, subtitle after

### Stat Cards Section
**Grid Layout:** 2 columns (grid-cols-1 sm:grid-cols-2)

**Card 1: Best Possible GPA**
- Label: "Best Possible GPA"
- Value: X.XX or "—"
- Subtext: "[4.0 or 9.0] scale"
- Color: Green
- **Calculation:** Best possible GPA for THIS term only (completed courses + best possible from in-progress)

**Card 2: Total Credits**
- Label: "Total Credits"
- Value: XX.X (1 decimal)
- Subtext: "Credit hours"
- Color: Gray
- **Calculation:** Sum of credit hours for all courses in this term

### Courses Section

**Section Header:**
- Left: "Courses" (h2)
- Right: "Add Course" button (primary, with Plus icon)

**Empty State:**
- Same pattern as Dashboard empty state
- Icon: BookOpen
- Title: "No courses yet"
- Description: "Add courses to start tracking your grades"
- CTA: "Add Your First Course"

**Course Cards Grid:**
- Grid: 1 column → 2 columns → 3 columns (responsive)
- Gap: 1rem
- Cards are clickable links to course detail page

**Individual Course Card:**
```
┌─────────────────────────────────┐
│ [Book Icon] MATH 101       [🗑️]│ ← Header
│ Calculus I                      │ ← Course name
│ ─────────────────────────────── │ ← Divider
│ Current Grade      A     [✓]    │ ← Grade info
│ Percentage       95.5%          │
│ Credits           3.0           │
└─────────────────────────────────┘
```

**Card Elements:**

1. **Header Row:**
   - BookOpen icon (gray-400)
   - Course code (semibold, e.g., "MATH 101")
   - Delete button (trash icon)

2. **Course Name:**
   - Full course name (e.g., "Calculus I")
   - Gray-600, small text
   - Truncated if too long

3. **Metrics:**
   - **Grade Row:**
     - Label: "Current Grade" (or "Final Grade" if completed)
     - Value: Letter grade (A, B+, etc.) - Large, indigo, semibold
     - Check circle icon (green) if course is marked as completed
   
   - **Percentage:**
     - Label: "Percentage"
     - Value: XX.X% - gray-900
     - For in-progress: Shows current grade OR best possible if no grades entered yet
     - For completed: Shows final grade
   
   - **Credits:**
     - Label: "Credits"
     - Value: X.X - gray-900

**Card Interactions:**
- Hover: Card elevates
- Click card: Navigate to course detail page
- Click delete: Confirm dialog, then remove course

**Course Completion Status:**
- Completed courses show a green checkmark icon next to their grade
- Label changes from "Current Grade" to "Final Grade"

---

## 4. Add Course Modal

**Trigger:** Click "Add Course" from Term View page

### Modal Structure
```
┌──────────────────────────────────┐
│ Add New Course            [X]    │
│                                  │
│ Course Code                      │
│ ┌──────────────────────────────┐│
│ │ e.g., MATH 101               ││
│ └──────────────────────────────┘│
│                                  │
│ Course Name                      │
│ ┌──────────────────────────────┐│
│ │ e.g., Calculus I             ││
│ └──────────────────────────────┘│
│                                  │
│ Credit Hours                     │
│ ┌──────────────────────────────┐│
│ │ 3.0                          ││
│ └──────────────────────────────┘│
│                                  │
│          [Cancel]  [Add Course]  │
└──────────────────────────────────┘
```

### Form Fields

**1. Course Code (Text Input)**
- Label: "Course Code"
- Placeholder: "e.g., MATH 101"
- Required
- Typical format: Department + Number

**2. Course Name (Text Input)**
- Label: "Course Name"
- Placeholder: "e.g., Calculus I"
- Required
- Full course title

**3. Credit Hours (Number Input)**
- Label: "Credit Hours"
- Type: number
- Step: 0.5 (allows 1.5, 2.5, etc.)
- Min: 0.5
- Default: 3.0
- Supports decimal values for courses with non-standard credits

### Behavior
- Creates course with empty gradeComponents array
- Course starts in "in-progress" state (isCompleted: false)
- After creation: Navigates to the course detail page (`/course/:courseId`)
- This allows immediate addition of grade components

---

## 5. Course Detail Page - Route: `/course/:courseId`

### Layout Structure
```
┌─────────────────────────────────────────────────────────┐
│ ← Back to [Term Name]                                   │ ← Breadcrumb
│                                                         │
│ MATH 101                                          [✓]   │ ← Header
│ Calculus I                                        [🗑️]  │
│ Fall 2025 • 3.0 credits                                 │
│                                                         │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │ ← 4 Stat Cards
│ │ Current  │ │ Best     │ │ Completed│ │ Remaining│  │
│ │ Grade    │ │ Possible │ │ Work     │ │ Work     │  │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                         │
│ Grade Breakdown             [+ Add Grade Component]     │ ← Section Header
│                                                         │
│ ┌─────────────────────────────────────────────────┐   │ ← Grade Table
│ │ Component       Weight  Earned  Possible  Grade │   │
│ │ Homework         20%     85     100       85%   │   │
│ │ Midterm Exam     30%     —      —         —     │   │
│ │ Final Exam       50%     —      —         —     │   │
│ │ ─────────────────────────────────────────────   │   │
│ │ Total           100%                            │   │
│ └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Breadcrumb Navigation
- Arrow left icon + "Back to [Term Season Year]"
- Returns to parent term view

### Page Header

**Title Row:**
- Course code (large, semibold, e.g., "MATH 101")
- Completed indicator: Green checkmark icon in circle (if marked complete)
- Delete course button: Trash icon (far right)

**Subtitle Row:**
- Course name (gray-600, e.g., "Calculus I")

**Metadata Row:**
- Term reference: "Fall 2025" (gray-500, small)
- Bullet separator: "•"
- Credit hours: "3.0 credits" (gray-500, small)

### Action Buttons (Top Right Area)
**Mark as Completed Button** (if not completed):
- Icon: CheckCircle2
- Text: "Mark as Completed"
- Variant: Secondary or outlined
- Opens completion modal to enter final grade

**Delete Course Button:**
- Trash icon
- Hover: Gray background
- Confirmation dialog before deletion
- Returns to term view after deletion

### Stat Cards Section
**Grid Layout:** 4 columns on desktop, 2 on tablet, 1 on mobile

**Card 1: Current Grade**
- Label: "Current Grade"
- Value: 
  - Letter grade (large, indigo)
  - Percentage (smaller, gray-600)
- Subtext: "Based on completed work"
- Color: Blue
- **Calculation:** Average of completed assignments weighted by their component weights
- Shows "—" / "No grades yet" if no work is graded

**Card 2: Best Possible Grade**
- Label: "Best Possible Grade"
- Value:
  - Letter grade (large, green)
  - Percentage (smaller, gray-600)
- Subtext: "If you get 100% on remaining"
- Color: Green
- **Calculation:** Current grade + assuming 100% on all remaining work

**Card 3: Completed Work**
- Label: "Completed Work"
- Value: Percentage (e.g., "40%")
- Subtext: "X of Y components"
- Color: Gray
- **Calculation:** Percentage of grade components that have scores entered

**Card 4: Remaining Work**
- Label: "Remaining Work"
- Value: Percentage (e.g., "60%")
- Subtext: "Worth XX% of grade"
- Color: Gray
- **Calculation:** 100% - Completed Work percentage

### Grade Breakdown Section

**Section Header:**
- Left: "Grade Breakdown"
- Right: "Add Grade Component" button (primary)

**Empty State:**
- Icon: Calculator or FileText
- Title: "No grade components yet"
- Description: "Add grade components like homework, exams, and projects to track your progress"
- CTA: "Add Your First Component"

**Grade Table** (when components exist):

**Table Structure:**
```
┌─────────────────────────────────────────────────────────┐
│ Component Name    Weight   Earned   Possible   Grade    │ ← Header
├─────────────────────────────────────────────────────────┤
│ Homework           20%      85       100       85.0%    │ ← Completed row
│ Midterm Exam       30%      —        —         —        │ ← Incomplete row  
│ Final Exam         50%      —        —         —        │ ← Incomplete row
│ ─────────────────────────────────────────────────────── │ ← Divider
│ Total             100%                                  │ ← Footer
└─────────────────────────────────────────────────────────┘
```

**Table Styling:**
- White card background
- Header row: Gray-50 background, semibold text, gray-700
- Data rows: Hover state (gray-50 background)
- Borders: Subtle gray-200 between rows
- Responsive: Scrollable on mobile if needed

**Column Details:**

1. **Component Name**
   - Left-aligned
   - Semibold, gray-900
   - Shows component type/name (e.g., "Homework", "Midterm Exam")
   - Editable on click or has edit icon

2. **Weight**
   - Right-aligned
   - Shows percentage (e.g., "20%")
   - Gray-900
   - Represents portion of final grade

3. **Earned**
   - Right-aligned
   - Shows points earned (e.g., "85")
   - Shows "—" if not graded yet
   - Editable field

4. **Possible**
   - Right-aligned
   - Shows maximum points (e.g., "100")
   - Shows "—" if not graded yet
   - Editable field

5. **Grade**
   - Right-aligned
   - Calculated: (Earned / Possible) × 100
   - Shows percentage (e.g., "85.0%")
   - Shows "—" if not graded
   - Color: 
     - Green if >= 90%
     - Blue if >= 80%
     - Yellow if >= 70%
     - Red if < 70%

**Table Footer:**
- "Total" label in bold
- Shows "100%" for weight column
- Other columns empty (or could show aggregate stats)

**Row Actions:**
- Each row has hover state
- Click row or edit icon to modify
- Delete icon on hover (far right)
- Inline editing or modal for changes

---

## 6. Add Grade Component Modal

**Trigger:** Click "Add Grade Component" from Course Detail page

### Modal Structure
```
┌──────────────────────────────────┐
│ Add Grade Component       [X]    │
│                                  │
│ Component Name                   │
│ ┌──────────────────────────────┐│
│ │ e.g., Homework, Midterm      ││
│ └──────────────────────────────┘│
│                                  │
│ Weight (% of final grade)        │
│ ┌──────────────────────────────┐│
│ │ 20                           ││
│ └──────────────────────────────┘│
│                                  │
│ Points Earned (optional)         │
│ ┌──────────────────────────────┐│
│ │                              ││
│ └──────────────────────────────┘│
│                                  │
│ Points Possible (optional)       │
│ ┌──────────────────────────────┐│
│ │                              ││
│ └──────────────────────────────┘│
│                                  │
│     [Cancel]  [Add Component]    │
└──────────────────────────────────┘
```

### Form Fields

**1. Component Name (Text Input)**
- Label: "Component Name"
- Placeholder: "e.g., Homework, Midterm"
- Required
- Common examples: Homework, Quiz, Midterm Exam, Final Exam, Project, Participation

**2. Weight (Number Input)**
- Label: "Weight (% of final grade)"
- Type: number
- Min: 0
- Max: 100
- Step: 1 or 0.1
- Required
- Default: Leave empty for user to enter
- **Note:** Should validate that total weights don't exceed 100%

**3. Points Earned (Number Input)**
- Label: "Points Earned (optional)"
- Type: number
- Min: 0
- Optional - can be added later
- If left blank: Component shows as incomplete

**4. Points Possible (Number Input)**
- Label: "Points Possible (optional)"
- Type: number
- Min: 0.01
- Optional - can be added later
- If left blank: Component shows as incomplete

### Validation
- Component name is required
- Weight is required and must be 0-100
- If earned is entered, possible should also be entered (warn user)
- If possible is entered, it should be > 0

### Behavior
- Creates new grade component
- Can create "empty" components (no scores yet) for planning
- After creation: Modal closes, component appears in table
- Stay on course detail page

---

## 7. Mark Course as Completed Flow

**Trigger:** Click "Mark as Completed" button on Course Detail page

### Completion Modal
```
┌──────────────────────────────────┐
│ Mark Course as Completed  [X]    │
│                                  │
│ Enter your final grade for this  │
│ course (as a percentage):        │
│                                  │
│ Final Grade (%)                  │
│ ┌──────────────────────────────┐│
│ │ 95.5                         ││
│ └──────────────────────────────┘│
│                                  │
│ This will lock the grade and     │
│ use it for GPA calculations.     │
│                                  │
│        [Cancel]  [Confirm]       │
└──────────────────────────────────┘
```

### Form Fields

**Final Grade (Number Input)**
- Label: "Final Grade (%)"
- Type: number
- Min: 0
- Max: 100
- Step: 0.1
- Required
- Default: Could pre-fill with current/best possible grade as suggestion

### Behavior
- Sets `isCompleted: true` on course
- Stores final grade percentage
- Course card shows checkmark icon
- Grade components become locked/read-only (optional design decision)
- Label changes from "Current Grade" to "Final Grade"

---

## Data Structure Reference

### Settings Object
```javascript
{
  gpaScale: '4.0' | '9.0'  // Selected GPA scale
}
```

### Term Object
```javascript
{
  id: string,              // Unique identifier (UUID)
  name: string,            // e.g., "Fall Semester 2025"
  season: 'Spring' | 'Summer' | 'Fall',
  year: number,            // e.g., 2025
  courses: Course[]        // Array of course objects
}
```

### Course Object
```javascript
{
  id: string,              // Unique identifier (UUID)
  code: string,            // e.g., "MATH 101"
  name: string,            // e.g., "Calculus I"
  creditHours: number,     // e.g., 3.0 (supports decimals)
  termId: string,          // Parent term ID
  isCompleted: boolean,    // Completion status
  finalGrade?: number,     // Final percentage (0-100) if completed
  gradeComponents: GradeComponent[]
}
```

### GradeComponent Object
```javascript
{
  id: string,              // Unique identifier
  name: string,            // e.g., "Homework", "Midterm Exam"
  weight: number,          // Percentage of final grade (0-100)
  earnedPoints?: number,   // Points earned (optional)
  possiblePoints?: number  // Maximum points (optional)
}
```

---

## Grade Calculation Logic

### Letter Grade Conversion

**4.0 Scale:**
- A (90-100%) = 4.0
- B (80-89%) = 3.0
- C (70-79%) = 2.0
- D (60-69%) = 1.0
- F (0-59%) = 0.0

**9.0 Scale:**
- A (90-100%) = 9.0
- B (80-89%) = 7.0
- C (70-79%) = 5.0
- D (60-69%) = 3.0
- F (0-59%) = 0.0

### Current Grade Calculation
For a course with grade components:
1. Filter to components that have both earnedPoints and possiblePoints
2. For each component: `(earnedPoints / possiblePoints) × weight`
3. Sum all weighted percentages
4. Divide by total weight of completed components
5. Result: Current percentage grade

### Best Possible Grade Calculation
For a course:
1. Calculate current grade from completed components
2. Calculate remaining weight: 100 - sum(completed component weights)
3. Assume 100% on all remaining weight
4. Formula: `currentGrade + remainingWeight`
5. Result: Best possible percentage grade

### Term GPA Calculation
1. For each course in term: Convert percentage to GPA points using scale
2. Multiply course GPA by credit hours
3. Sum all (GPA × credits)
4. Divide by total credit hours
5. Result: Term GPA

### Best Possible GPA (Overall)
1. For completed courses: Use final grade
2. For in-progress courses: Use best possible grade
3. Calculate overall GPA using all courses across all terms
4. Result: Best possible cumulative GPA

---

## Responsive Behavior

### Breakpoints (Tailwind defaults)
- **Mobile:** < 640px (sm)
- **Tablet:** 640px - 1024px (sm to lg)
- **Desktop:** >= 1024px (lg)

### Layout Adaptations

**Dashboard & Term View:**
- Stat cards: 1 column (mobile) → 2 columns (all other sizes)
- Term/Course cards: 1 column → 2 columns (sm) → 3 columns (lg)
- Buttons: Full width (mobile) → auto width (desktop)
- Padding: Reduced on mobile (px-4) → normal on desktop (px-6)

**Course Detail:**
- Stat cards: 1 column → 2 columns (sm) → 4 columns (lg)
- Grade table: Horizontal scroll on mobile if needed
- Font sizes: Slightly smaller on mobile (text-2xl → text-3xl on desktop)

**Modals:**
- Full screen on mobile (optional)
- Fixed width centered on desktop (max-w-md = 28rem)

---

## Interaction Patterns

### Hover States
- **Cards:** Subtle shadow elevation, cursor pointer
- **Buttons:** Slightly darker background
- **Delete icons:** Gray background circle appears
- **Links:** Color changes from gray-600 to gray-900
- **Table rows:** Light gray background (gray-50)

### Loading States
- Not currently implemented
- Could add skeleton screens or spinners for future async operations

### Error States
- Form validation: Red border + error message below field
- Confirmation dialogs for destructive actions (delete)

### Empty States
- Centered content with icon
- Descriptive title and text
- Primary CTA button to add first item
- Used for: No terms, no courses, no grade components

---

## Accessibility Considerations

### Current Implementation
- Semantic HTML (buttons, links, forms)
- Proper label/input associations
- Keyboard navigation (buttons, links, form fields)
- Icons include text labels
- Sufficient color contrast

### Future Enhancements
- ARIA labels for icon-only buttons
- Focus indicators
- Screen reader announcements
- Keyboard shortcuts
- Form error announcements

---

## Key User Flows

### Flow 1: First-Time User Setup
1. Land on empty Dashboard
2. Click "Add Your First Term"
3. Fill in term details (name, season, year)
4. Click "Add Term" → Redirects to Dashboard with new term card
5. Click term card → Navigate to Term View
6. Click "Add Your First Course"
7. Fill in course details (code, name, credits)
8. Click "Add Course" → Navigate to Course Detail page
9. Click "Add Your First Component"
10. Fill in component details (name, weight, optional scores)
11. Click "Add Component" → Component appears in table
12. Repeat step 9-11 for all grade components
13. See Best Possible GPA update as components are added

### Flow 2: Adding Grades During Semester
1. Navigate to Course Detail page
2. Click on existing grade component row or use edit icon
3. Enter earned and possible points
4. Save changes
5. See Current Grade and Best Possible Grade update
6. See term-level and overall Best Possible GPA update

### Flow 3: Completing a Course
1. Navigate to Course Detail page
2. Click "Mark as Completed"
3. Enter final grade percentage
4. Click "Confirm"
5. Checkmark icon appears next to course name
6. Grade is locked
7. GPA calculations now use final grade instead of forecasted grade

### Flow 4: Managing Multiple Terms
1. Add multiple terms from Dashboard
2. Terms sorted automatically (most recent first)
3. Add courses to each term
4. View overall Best Possible GPA that combines all terms
5. Compare term GPAs to see progress over time

---

## Future Enhancement Ideas

These are NOT currently implemented but could be added:

### Features
- Grade distribution charts (pie chart of component weights)
- GPA trend graphs over time
- What-if scenarios ("What grade do I need on the final?")
- Import/export data (JSON, CSV)
- Print-friendly grade reports
- Dark mode
- Mobile app version

### Calculations
- Plus/minus letter grades (A+, A, A-, etc.)
- Different GPA scales (12.0, percentage-based)
- Weighted vs unweighted GPA
- Class rank calculations
- Semester vs cumulative GPA comparison

### UI/UX
- Drag-and-drop to reorder components
- Inline editing in grade table
- Bulk add/edit grade components
- Quick-add templates (standard grading schemes)
- Color-coded courses by grade
- Progress bars for completion percentage
- Notifications/reminders

---

## Version History

**v1.0 (Current) - April 24, 2026**
- Focus on GPA forecasting
- Removed completed term feature
- Simplified to 2 stat cards on Dashboard and Term View
- Clean, minimal design
- Support for 4.0 and 9.0 GPA scales
- Decimal credit hours support
- Responsive layout
- Core CRUD operations for terms, courses, and grade components

---

## Technical Stack

- **Framework:** React 18+ with TypeScript
- **Routing:** React Router v7
- **Styling:** Tailwind CSS v4
- **Icons:** Lucide React
- **State Management:** React Context API
- **Build Tool:** Vite
- **Data Persistence:** Local Storage (browser)

---

## File Structure

```
src/
├── app/
│   ├── App.tsx                          # Main app with routing
│   ├── components/
│   │   ├── Dashboard.tsx                # Homepage
│   │   ├── TermView.tsx                 # Individual term page
│   │   ├── CourseDetail.tsx             # Course detail page
│   │   ├── AddTermModal.tsx             # Add term modal
│   │   ├── AddCourseModal.tsx           # Add course modal
│   │   ├── AddGradeComponentModal.tsx   # Add grade component modal
│   │   └── ui/
│   │       ├── Button.tsx               # Reusable button
│   │       ├── Card.tsx                 # Card container
│   │       ├── StatCard.tsx             # Stat display card
│   │       └── Input.tsx                # Form inputs
│   ├── context/
│   │   └── DataContext.tsx              # Global state management
│   └── utils/
│       └── gradeCalculations.ts         # GPA calculation logic
├── styles/
│   ├── theme.css                        # Theme tokens
│   └── fonts.css                        # Font imports
└── package.json
```

---

## End of Documentation

This documentation represents the current state of the GPA Calculator UI as of v1.0. It should be used as a reference for understanding the complete user interface, user flows, and design patterns implemented in the application.
