# NLtomysql

# 📊 ATLIQ T-Shirts Q&A App

A fully interactive web application that allows users to ask **natural language questions** about a T-shirts database and receive meaningful answers in real-time. This project combines **Streamlit** for the frontend, **LangChain** with **Gemini-2.0-flash** for translating natural language to SQL, and **MySQL** for structured data storage. It is designed to be **scalable, portable, and serverless-ready**, and can be deployed effortlessly on **Google Cloud Run**.

---

## 🧠 Project Description

This application bridges the gap between users and raw SQL data by allowing them to interact with a MySQL database using **plain English questions**.

### ✅ Key Features:

- 🔍 **Ask natural language queries** like:  
  _"How many white Nike t-shirts are available in size XS?"_

- 🧠 **Google Gemini via LangChain** automatically converts your question into an SQL query.

- 🗂️ The SQL query is executed against a **MySQL database**.

- 🗣️ The results are converted into a **human-readable** response and displayed in a clean **Streamlit UI**.

- ☁️ Can be deployed on **Google Cloud Run** for secure, scalable, serverless hosting.

