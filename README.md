# Library Management System – Selenium Testing Project

A common Library Management System built with **React + Vite** (frontend) and **Django REST Framework** (backend), with Selenium automation divided among five team members.

## Team ownership

| Member | Implementation | Selenium |
|---|---|---|
| Vengasree | Admin + Book Management | `selenium-tests/vengasree/` |
| Mounika | Authentication + Member Management | `selenium-tests/mounika/` |
| Gagana | Search + Book Availability | `selenium-tests/gagana/` |
| Jeevana | Book Issue + Return | `selenium-tests/jeevana/` |
| Madhupriya | Dashboard + Transactions/Reports | `selenium-tests/madhupriya/` |

Frontend ownership is also separated under `frontend/src/modules/<member>/`.

## Features

- Login and member registration
- Dashboard statistics
- Book CRUD and availability
- Member management
- Search by title, author, ISBN, or category
- Book issue and return with copy-count validation
- Transaction history and reports
- Django admin panel
- Selenium test suites for each assigned module

## 1. Start the Django backend

Windows PowerShell:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python seed.py
python manage.py runserver
```

Backend: `http://127.0.0.1:8000`

Seeded admin account:

- Username: `admin`
- Password: `Admin@123`

Django admin: `http://127.0.0.1:8000/admin/`

## 2. Start React frontend

Open a second PowerShell:

```powershell
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## 3. Selenium setup

Keep the backend and frontend running. Open a third PowerShell:

```powershell
cd selenium-tests
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```

Chrome must be installed. Selenium 4 can manage the Chrome driver automatically on supported systems.

Run one member's tests:

```powershell
pytest -v vengasree
pytest -v mounika
pytest -v gagana
pytest -v jeevana
pytest -v madhupriya
```

## 4. Git workflow

Clone/pull the common repository, create a branch for your assigned work, and push it:

```powershell
git checkout -b feature/vengasree-books
# make changes
git add .
git commit -m "Add Vengasree book management and Selenium tests"
git push -u origin feature/vengasree-books
```

Suggested branches:

- `feature/vengasree-books`
- `feature/mounika-auth-members`
- `feature/gagana-search`
- `feature/jeevana-issue-return`
- `feature/madhupriya-dashboard-reports`

Do not create five separate projects. Everyone works in this same repository.

## 5. Testing workflow for presentation

For each module:

1. Explain the requirement.
2. Show the React implementation.
3. Show the Django API used by the module.
4. Show the test cases in `test-cases/test_cases.csv`.
5. Show the Selenium code.
6. Run the Selenium test live.
7. Record PASS/FAIL in your review sheet.

## API summary

- `POST /api/auth/login/`
- `POST /api/auth/register/`
- `GET /api/auth/me/`
- `GET /api/dashboard/`
- `GET/POST/PUT/DELETE /api/books/`
- `GET/POST/PUT/DELETE /api/members/`
- `GET/POST /api/transactions/`
- `POST /api/transactions/<id>/return/`
- `GET /api/reports/`

## Notes

This is a college/testing project. The included development secret key, demo admin password, and open CORS configuration are for local development only and must be changed before production deployment.
