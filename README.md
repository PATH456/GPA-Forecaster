# GPA Forecaster

A full-stack GPA planning and academic forecasting web application built with **Next.js**, **React**, **TypeScript/JavaScript**, **PostgreSQL**, and **Prisma**.

GPA Forecaster helps students organize academic terms, add courses, track grade impact, and forecast different GPA outcomes based on expected grades. The goal of the project is to make academic planning easier, more visual, and more personalized than a basic GPA calculator.

---

## 🚀 Features

### 🎓 Academic Term Management

* Add, edit, and delete academic terms
* Organize courses by term, such as `Spring 2026`, `Summer 2026`, or `Fall 2026`
* View term-based GPA summaries
* Track completed credits and planned credits per term
* Separate completed, in-progress, and future academic terms

### 📚 Course Management

* Add courses manually with course code, course name, credit value, and grade information
* Store courses under specific academic terms
* Edit course details as grades change throughout the semester
* Support current grade, final grade, and expected grade fields
* Mark courses as completed, in progress, or planned

### 🧮 GPA Calculation

* Automatically recalculate GPA when grades or credits are updated
* Calculate term GPA for each academic term
* Calculate cumulative GPA across all terms
* Track total credits and weighted grade points
* Support GPA forecasting based on custom expected grades

### 🔮 GPA Forecasting

* Forecast best-case GPA scenarios
* Create custom GPA scenarios using expected grades
* Compare current GPA with projected GPA
* Test different possible outcomes before final grades are released
* Help students understand what grades they need to reach a target GPA

### 📊 Grade Impact Analysis

* Show how each course affects the overall GPA
* Highlight high-credit courses that have stronger GPA impact
* Estimate how much a course can raise or lower cumulative GPA
* Support future grade component tracking inside each course

### 👤 User Accounts

* User registration and login
* Save academic terms, courses, and GPA scenarios to each user account
* Protect user-specific academic data
* Allow users to access their GPA data from different devices

### 📄 Future AI-Powered Syllabus Parsing

* Upload a course syllabus file
* Extract grading components automatically
* Use AI to identify assignments, quizzes, midterms, projects, exams, and their weights
* Convert extracted grading information into editable structured data
* Let users review and confirm the result before saving

This feature is planned as a future improvement and is not part of the first version.

---

## 🏗️ Project Structure

```text
gpa-forecaster/
├── app/                              # Next.js App Router
│   ├── page.tsx                      # Landing page or dashboard entry
│   ├── layout.tsx                    # Root layout
│   ├── dashboard/                    # Main user dashboard
│   │   └── page.tsx
│   ├── terms/                        # Academic term pages
│   │   └── page.tsx
│   ├── courses/                      # Course management pages
│   │   └── page.tsx
│   ├── forecasts/                    # GPA forecasting pages
│   │   └── page.tsx
│   ├── auth/                         # Login/register pages
│   │   ├── login/
│   │   └── register/
│   └── api/                          # Backend API routes
│       ├── terms/
│       │   └── route.ts
│       ├── courses/
│       │   └── route.ts
│       ├── forecasts/
│       │   └── route.ts
│       └── dashboard/
│           └── summary/
│               └── route.ts
│
├── components/                       # Reusable React components
│   ├── StatCard.tsx
│   ├── TermCard.tsx
│   ├── CourseCard.tsx
│   ├── ForecastCard.tsx
│   ├── AddTermModal.tsx
│   └── AddCourseModal.tsx
│
├── lib/                              # Shared helper logic
│   ├── prisma.ts                     # Prisma client setup
│   ├── auth.ts                       # Authentication config
│   ├── gpa.ts                        # GPA calculation helpers
│   └── validations.ts                # Form/data validation schemas
│
├── prisma/                           # Database schema and migrations
│   └── schema.prisma
│
├── public/                           # Static assets
├── styles/                           # Global styles if needed
├── package.json
├── next.config.js
├── tsconfig.json
├── .env                              # Environment variables, not committed
├── .gitignore
└── README.md
```

---

## 🧰 Tech Stack

| Layer                | Technology                                |
| -------------------- | ----------------------------------------- |
| Full-Stack Framework | Next.js                                   |
| UI Library           | React                                     |
| Main Language        | TypeScript / JavaScript                   |
| Styling              | Tailwind CSS or plain CSS                 |
| Database             | PostgreSQL                                |
| ORM                  | Prisma                                    |
| Authentication       | Auth.js / NextAuth or custom auth         |
| Validation           | Zod                                       |
| Deployment           | Vercel, Railway, Render, or Supabase      |
| Future AI Feature    | OpenAI API or similar AI service          |
| Future File Parsing  | PDF parsing service or AI file extraction |

---

## ⚡ Getting Started

### Prerequisites

* Node.js 18+
* npm, pnpm, or yarn
* PostgreSQL database
* Git

---

## 1. Clone the Repository

```bash
git clone <repo-url>
cd gpa-forecaster
```

---

## 2. Install Dependencies

```bash
npm install
```

or, if using pnpm:

```bash
pnpm install
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Example environment variables:

```env
DATABASE_URL="postgresql://username:password@localhost:5432/gpa_forecaster"
NEXTAUTH_SECRET="your-secret-key"
NEXTAUTH_URL="http://localhost:3000"
```

Optional future AI feature variables:

```env
OPENAI_API_KEY="your-api-key"
```

| Variable          | Description                            |
| ----------------- | -------------------------------------- |
| `DATABASE_URL`    | PostgreSQL connection string           |
| `NEXTAUTH_SECRET` | Secret key for authentication          |
| `NEXTAUTH_URL`    | Local or production app URL            |
| `OPENAI_API_KEY`  | API key for future AI syllabus parsing |

---

## 4. Set Up the Database

Generate the Prisma client:

```bash
npx prisma generate
```

Run database migrations:

```bash
npx prisma migrate dev
```

Optional: open Prisma Studio to view and manage local database records:

```bash
npx prisma studio
```

---

## 5. Run the Development Server

```bash
npm run dev
```

Visit the app in your browser:

```text
http://localhost:3000
```

---

## 🗃️ Database Design

The app stores user-specific academic data in a relational database.

### Main Models

| Model                 | Purpose                                                                |
| --------------------- | ---------------------------------------------------------------------- |
| `User`                | Stores user account information                                        |
| `AcademicTerm`        | Represents one academic term                                           |
| `Course`              | Represents a course inside a term                                      |
| `ForecastScenario`    | Stores a custom GPA forecasting scenario                               |
| `ScenarioCourseGrade` | Stores expected grades for courses inside a scenario                   |
| `GradingComponent`    | Future model for assignments, quizzes, exams, and weighted grade items |

### Example Relationship

```text
User
└── AcademicTerm
    └── Course
        └── GradingComponent

User
└── ForecastScenario
    └── ScenarioCourseGrade
```

---

## 🔌 API Overview

The app uses Next.js API routes or server actions to handle backend logic.

Example API routes:

| Method   | Endpoint                 | Description                                 |
| -------- | ------------------------ | ------------------------------------------- |
| `POST`   | `/api/auth/register`     | Register a new user                         |
| `POST`   | `/api/auth/login`        | Log in a user                               |
| `GET`    | `/api/terms`             | Get all academic terms for the current user |
| `POST`   | `/api/terms`             | Create a new academic term                  |
| `PATCH`  | `/api/terms/:id`         | Update an academic term                     |
| `DELETE` | `/api/terms/:id`         | Delete an academic term                     |
| `GET`    | `/api/courses`           | Get all courses for the current user        |
| `POST`   | `/api/courses`           | Create a new course                         |
| `PATCH`  | `/api/courses/:id`       | Update course information                   |
| `DELETE` | `/api/courses/:id`       | Delete a course                             |
| `POST`   | `/api/forecasts`         | Create a GPA forecast scenario              |
| `GET`    | `/api/dashboard/summary` | Get GPA summary data                        |

---

## 🧮 GPA Calculation Logic

The GPA calculation is based on weighted grade points:

```text
Course weighted points = grade point × course credits
GPA = total weighted grade points / total credits
```

Example:

```text
Course A: 4.0 grade point × 3 credits = 12 weighted points
Course B: 3.0 grade point × 4 credits = 12 weighted points

Total weighted points = 24
Total credits = 7
GPA = 24 / 7 = 3.43
```

The app recalculates GPA whenever course grades, expected grades, or credit values change.

---

## 📄 Future AI Syllabus Parsing Flow

This feature is planned for a later version.

The expected workflow is:

```text
1. User uploads a syllabus file
2. App extracts text from the file
3. AI identifies grading components and weights
4. App converts the result into structured data
5. User reviews and edits the extracted components
6. User confirms and saves the components to the course
```

Example extracted result:

```json
{
  "courseName": "CSC 225",
  "gradingComponents": [
    { "name": "Assignments", "weight": 20 },
    { "name": "Quizzes", "weight": 10 },
    { "name": "Midterm", "weight": 25 },
    { "name": "Final Exam", "weight": 45 }
  ]
}
```

Important design rule:

```text
AI should suggest the grading structure, but the user should confirm it before saving.
```

---

## 🔑 Environment & Security Notes

* Never commit `.env` files to GitHub
* Keep database credentials private
* Keep authentication secrets private
* Protect all user-specific GPA data
* Validate user input before saving to the database
* Use HTTPS in production
* Do not save uploaded syllabus files permanently unless necessary
* Let users review AI-parsed syllabus data before saving

---

## 🗺️ Roadmap / TODO

### Version 1: Core Full-Stack App

* [ ] Set up Next.js project
* [ ] Design reusable React components
* [ ] Create Prisma database schema
* [ ] Add academic term CRUD
* [ ] Add course CRUD
* [ ] Add GPA calculation logic
* [ ] Add dashboard summary cards
* [ ] Save data to PostgreSQL

### Version 2: User Accounts

* [ ] Add user registration and login
* [ ] Protect dashboard routes
* [ ] Connect terms and courses to specific users
* [ ] Add account settings page

### Version 3: Forecasting System

* [ ] Add best-case GPA forecast
* [ ] Add custom expected-grade scenarios
* [ ] Add target GPA calculator
* [ ] Add course impact analysis
* [ ] Add comparison between current GPA and forecasted GPA

### Version 4: AI Syllabus Parsing

* [ ] Add syllabus upload feature
* [ ] Extract text from PDF files
* [ ] Use AI to identify grading components
* [ ] Convert parsed output into editable grading components
* [ ] Let users confirm before saving
* [ ] Add support for scanned or image-based syllabi if needed

### Version 5: Polish & Deployment

* [ ] Add form validation
* [ ] Add loading and error states
* [ ] Add responsive mobile layout
* [ ] Add unit and integration tests
* [ ] Deploy the app
* [ ] Write production setup instructions

---

## 🧪 Future Improvements

* PDF syllabus parsing
* AI-powered grade component extraction
* Assignment-level grade tracking
* GPA trend charts
* Best-case and worst-case GPA comparison
* Export GPA report as PDF
* University-specific GPA scale support
* Dark mode
* Email reminders for important academic deadlines

---

## 📝 License

This project is for personal learning, academic planning, and portfolio development.


## Author
Thanh Hải Phạm
