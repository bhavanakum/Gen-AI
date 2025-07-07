# NLtomysql

# 📊 ATLIQ T-Shirts Q&A App:  https://atliq-service-747917912155.us-central1.run.app

A fully interactive web application that allows users to ask **natural language questions** about a T-shirts database and receive meaningful answers in real-time. This project combines **Streamlit** for the frontend, **LangChain** with **Google Gemini 2.0** for translating natural language to SQL, and **Google Cloud SQL (MySQL)** for structured data storage. It is designed to be **scalable, portable, and serverless-ready**, and is deployed on **Google Cloud Run**.

---

## 🧠 Project Description

This application bridges the gap between users and raw SQL data by allowing them to interact with a MySQL database using **plain English questions**.

### ✅ Key Features:

- 🔍 **Ask natural language queries** like:  
  _"How many white Nike t-shirts are available in size XS?"_

- 🧠 **Google Gemini via LangChain** automatically converts your question into an SQL query.

- 🗂️ The SQL query is executed against a **MySQL database**.

- 🗣️ The results are converted into a **human-readable** response and displayed in a clean **Streamlit UI**.

  <img width="1463" alt="Screenshot 2025-07-07 at 5 35 13 PM" src="https://github.com/user-attachments/assets/33b1f63a-b8f5-4d08-b27f-3b634e6cfcd9" />


- ☁️ **Deployed on Google Cloud Platform (Cloud Run)** for secure, scalable, and serverless hosting.  
  You can access the live app here:  
  `https://atliq-service-747917912155.us-central1.run.app`

---

## 🚀 Deployment

Screenshots demonstrating the deployment process and the live app running on Google Cloud Platform are included in the `deployment_screenshots/` folder.
<img width="1467" alt="Screenshot 2025-07-07 at 5 20 49 PM" src="https://github.com/user-attachments/assets/e5049fb0-8641-4039-9abf-f5472fba9d08" />
<img width="1470" alt="Screenshot 2025-07-07 at 5 22 55 PM" src="https://github.com/user-attachments/assets/b4bf5f11-53e6-46b4-8524-05e05fedbf86" />

