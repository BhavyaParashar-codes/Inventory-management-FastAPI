# Inventory Management REST API

## 📌 Project Overview
A high-performance, scalable Backend API built for real-time inventory tracking and management. This project demonstrates the transition from legacy script-based management (formerly a Bakery Shop system) to a modern, RESTful web service architecture.

This project is the core deliverable of my **10-day intensive Backend Internship Sprint**.

## 🚀 Features
* **Full CRUD Lifecycle**: Efficient endpoints for Creating, Reading, Updating, and Deleting inventory items.
* **Smart Search Logic**: Implementation of case-insensitive search functionality to filter items by name.
* **Automated Documentation**: Interactive API testing and exploration interface provided via Swagger UI (OpenAPI).
* **Data Validation**: Leveraging Pydantic models for strict type checking and data integrity (e.g., price and quantity validation).

## 🛠️ Tech Stack
* **Language**: Python 3.10+
* **Framework**: FastAPI
* **Server**: Uvicorn (ASGI)
* **Testing**: Swagger UI / Postman

## 📖 How to Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/BhavyaParashar-codes/Inventory-management-FastAPI.git
2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
3. **start the server**:
   ```bash
   uvicorn main:app --reload
4.**Access the API document**:
 ```bash
http://127.0.0.1:8000/docs


