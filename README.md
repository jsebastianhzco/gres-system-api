# Environmental Certificates System – Backend API (FastAPI + PostgreSQL)

This repository contains the **backend API** for a real-world system built for **Gres del Eje**, a private environmental services company in Colombia. The system was originally developed in raw PHP and is now being **refactored using FastAPI and PostgreSQL** for modern architecture and scalability.

The **frontend (React + Vite)** lives in a separate repository and is already integrated via **Axios** for API communication.

---

## 🧩 Project Context

The backend serves a production-grade system that handles:

- Generation and management of **environmental certificates**
- **Accounts receivable** (custom invoices)
- Automated **email delivery** to clients when a certificate or invoice is issued
- **Full customer database** management and traceability

This API is part of the ongoing migration from legacy code to a modern and modular backend structure.

---

## ✅ Current Status

- 🔄 Migrated from: Legacy PHP (monolithic structure)
- ⚙️ FastAPI backend already operational and connected to frontend
- 🛢️ Database: PostgreSQL
- 📨 Email sending and PDF generation integrated in backend logic

---

## 🚀 Core Features

- Modular FastAPI architecture with `routers`, `schemas`, `models`, and `crud` layers
- **CORS configured** for seamless frontend integration
- Uses **Pydantic** for data validation and serialization
- Built-in support for:
  - Creating and listing certificates
  - Managing customers
  - Triggering invoice creation
  - Sending emails with document attachments

---

## 📂 Folder Structure
app/
├── crud/ # Business logic and DB operations
├── models/ # SQLAlchemy models
├── routers/ # API route declarations
├── schemas/ # Pydantic request and response models
├── database.py # Connection config and session management
└── main.py # Entry point, FastAPI app instance


---

## 🛠️ Tech Stack

- **FastAPI** – high-performance Python web framework
- **PostgreSQL** – relational database
- **SQLAlchemy** – ORM for DB interaction
- **Pydantic** – data parsing and validation
- **Uvicorn** – ASGI server
- **Email automation** – included for sending generated docs


