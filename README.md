# MobilePlace.ng — Sales Record App

> A web-based sales record management system for **MobilePlace.ng**, a gadgets & accessories store in Lagos, Nigeria.

---

## Features

- **Staff Authentication** — Login, signup, and role-based access (CEO, Manager, Unit Head, Secretary, Sales Staff)
- **Sales Records** — Add, edit, and manage sales entries with full details (invoice, customer, IMEI, price, account, status)
- **Period Filtering** — Filter records by year and month, or view all-time data
- **Revenue Stats** — Live dashboard showing total records, sold, pending, and revenue with month-on-month comparison
- **Undo / Redo** — Step back or forward through changes (up to 50 steps)
- **Recycle Bin** — Password-gated soft delete; restore or permanently remove records
- **CSV Export** — Download records for the selected period as a CSV file
- **Search & Filter** — Search by name, invoice, IMEI, goods, and filter by status
- **PWA Ready** — Installable on mobile and desktop via service worker + manifest

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python / Flask |
| Storage | JSON files (`sales_data.json`, `users_data.json`, `bin_data.json`) |
| Hosting | Render (free tier) |

---

## Project Structure

```
Mobileplace-record-app/
├── app.py                  # Flask backend & API routes
├── sales_data.json         # Sales records storage
├── users_data.json         # Staff accounts storage
├── bin_data.json           # Soft-deleted records (recycle bin)
├── templates/
│   └── index.html          # Full frontend (single-page app)
└── static/
    ├── manifest.json       # PWA manifest
    └── sw.js               # Service worker
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/login` | Staff login |
| POST | `/api/signup` | Create new staff account |
| POST | `/api/logout` | Sign out |
| GET | `/api/records` | Fetch all records |
| POST | `/api/records` | Add a new record |
| PUT | `/api/records/<id>` | Update a record |
| DELETE | `/api/records/<id>` | Move record to bin |
| PUT | `/api/records/bulk` | Bulk update (used by undo/redo) |
| GET | `/api/bin` | Fetch bin contents |
| PUT | `/api/bin` | Save bin contents |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/emmyblisschuks/Mobileplace-record-app.git
cd Mobileplace-record-app

# Install dependencies
pip install flask

# Run the app
python app.py
```

Then open your browser and go to: `http://localhost:5000`

---

## Deployment

This app is deployed on **Render** (free tier).

> ⚠️ **Note:** Render's free tier has an ephemeral filesystem. Data stored in JSON files may be lost when the server spins down after inactivity. A persistent database (e.g. Supabase or PostgreSQL) is recommended for production use.

---

## Staff Roles

| Role | Description |
|------|-------------|
| CEO | Full access |
| Manager | Full access |
| Unit Head | Full access |
| Secretary | Full access |
| Sales Staff | Full access |

---

## Screenshots

> *Coming soon*

---

## Built By

**EmmyTech** · Lagos, Nigeria  
© 2025 MobilePlace.ng · All rights reserved
