# 🏫 School Management System using Python, Pandas & Streamlit

> A complete data-driven School Management & Analytics platform built with **Python**, **Pandas**, and **Streamlit** — track student journeys, academics, attendance, and fees through a single 

## 📖 Project Overview

The **School Management System** is designed to digitize and analyze the complete academic lifecycle of a school — from admission to pass-out. Unlike a simple record-keeping tool, this project focuses on **data analytics and visualization**, allowing school administrators to make informed decisions based on real, interconnected student data.

The system tracks every student's **complete journey** across academic sessions — admissions, promotions, roll numbers, marks, attendance, and fee payments — and presents this information through a **modern, interactive Streamlit dashboard**.

> ⚠️ **Note:** This project uses only data analytics techniques (Pandas, NumPy, visualization). **No Machine Learning is involved.**

---

## 🎯 Objectives

- 📌 Digitize student records across multiple academic sessions and classes.
- 📌 Maintain a permanent, traceable **Student_ID** for every learner's entire school journey.
- 📌 Analyze academic performance, attendance patterns, and fee collection trends.
- 📌 Provide administrators with a **single-glance dashboard** for school-wide and class-wise insights.
- 📌 Enable instant **individual student search** to retrieve a complete academic and financial profile.
- 📌 Demonstrate practical use of **Pandas** for real-world relational data analysis (without a database).

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧑‍🎓 **Student Lifecycle Tracking** | Follows each student from admission through promotion, transfer, dropout, or pass-out |
| 🔍 **Instant Student Search** | Search any `Student_ID` to view their full academic history |
| 📊 **Interactive Analytics** | School-wide, class-wise, and subject-wise performance breakdowns |
| 🗓️ **Attendance Insights** | Identify most punctual, best-attendance, and at-risk students |
| 💰 **Fee Management Analysis** | Track paid, pending, and total fee collections |
| 📈 **Visual Dashboards** | Rich charts powered by Matplotlib & Plotly |
| 📥 **Downloadable Reports** | Export filtered data and analytics as CSV/Excel |
| 🧩 **Fully Interconnected Data** | All CSV files linked via `Student_ID` for relational analysis |


## 🗂️ Dataset Description

The system is powered by **five interconnected CSV files**, all linked using a common `Student_ID` field, enabling full relational analysis without a database engine.


### 1️⃣ `students.csv` — Master Student Profile
Stores the **permanent** identity and personal details of every student.

| Column | Description |
|---|---|
| `Student_ID` | Unique, permanent student identifier |
| `Full_Name`, `Father_Name`, `Mother_Name` | Personal & parental details |
| `Gender`, `Date_of_Birth`, `Age` | Demographic information |
| `Original_Admission_Date` | Date the student first joined the school (never changes) |
| `First_Class` | The class the student was originally admitted into |
| `Parent_Phone`, `Parent_Email`, `Address` | Contact information |
| `Blood_Group` | Medical reference |
| `Current_Class`, `Current_Status` | Most recent class & status (Active / Drop Out / Transfer / Pass Out) |

### 2️⃣ `student_history.csv` — Academic Journey Log
The **core file** of the system — records every class a student has ever attended, session by session.

| Column | Description |
|---|---|
| `History_ID` | Unique record identifier |
| `Student_ID` | Links back to `students.csv` |
| `Academic_Session`, `Class`, `Roll_No` | Session-specific class placement |
| `Previous_Class`, `Promotion_Status` | Tracks promotion path (New Admission / Promoted) |
| `Class_Start_Date`, `Class_End_Date` | Duration in that class |
| `Status`, `Status_Date`, `Exit_Reason` | Active / Drop Out / Transfer / Pass Out details |

### 3️⃣ `marks.csv` — Academic Performance Records
Session-wise subject marks and computed results for every student.

| Column | Description |
|---|---|
| `Marks_ID`, `Student_ID`, `Academic_Session`, `Class` | Record identifiers |
| `English`, `Urdu`, `Mathematics`, `Science`, `Computer`, `Islamiat` | Subject-wise marks |
| `Total_Marks`, `Obtained_Marks`, `Percentage` | Computed academic performance |
| `Grade`, `Position`, `Result`, `Remarks` | Final evaluation for the session |

### 4️⃣ `attendance.csv` — Attendance Records
Session-wise attendance statistics per student.

| Column | Description |
|---|---|
| `Attendance_ID`, `Student_ID`, `Academic_Session`, `Class` | Record identifiers |
| `Working_Days`, `Present_Days`, `Absent_Days`, `Leave_Days` | Attendance breakdown |
| `Late_Days` | Punctuality tracking |
| `Attendance_Percentage` | Computed attendance rate |

### 5️⃣ `fees.csv` — Fee & Payment Records
Session-wise fee structure and payment status per student.

| Column | Description |
|---|---|
| `Fee_ID`, `Student_ID`, `Academic_Session`, `Class` | Record identifiers |
| `Registration_Fee`, `Admission_Fee` | Charged only for new admissions |
| `Monthly_Fee`, `Other_Fee`, `Total_Fee` | Fee components |
| `Paid_Amount`, `Remaining_Amount` | Payment tracking |
| `Payment_Status`, `Payment_Date` | Paid / Pending status |

---

## 📊 Data Analysis Modules

| Module | Description |
|---|---|
| 🏫 **School Overview Analysis** | Total students, boys/girls ratio, active/dropout/transfer/pass-out counts |
| 🧑‍🎓 **Student Analysis** | Individual profile lookup, journey mapping, roll number history |
| 📚 **Academic Performance Analysis** | Class toppers, subject-wise toppers, pass/fail ratios, grade distribution |
| 🗓️ **Attendance Analysis** | Best & lowest attendance, most punctual students, class-wise trends |
| 💰 **Fee Analysis** | Total billed, collected, and pending fees, defaulter identification |
| 🔗 **School Data Integration & Advanced Analysis** | Cross-file analytics combining academics, attendance, and fees for holistic insights |

---

## 🖥️ Streamlit Dashboard Features
## 🖥️ Streamlit Dashboard Features

The application provides a centralized school management dashboard with three main navigation sections, allowing administrators to access student records, academic information, financial details, and reports through a single interface.

### 1. 🧑‍🎓 Student Details and Academics
- View student details, including student ID, name, class, gender, and admission information.
- Search for students and retrieve their individual profiles.
- View academic history across academic sessions.
- Analyze subject-wise marks, total marks, percentages, grades, and results.
- Visualize class-wise academic performance and subject comparisons.
- Identify class toppers and student performance trends.
- Review student promotion history and current status.

### 2. 💰 Fees and Payments
- View total fees billed, total fees collected, and outstanding balances.
- Analyze paid and pending fee amounts.
- Display fee collection summaries and payment status.
- Compare fee collection across classes and academic sessions.
- Identify students with outstanding fee balances.
- Visualize fee collection and pending dues using charts.

### 3. 📊 Reports and Exports
- Generate school-wide and class-wise analytical summaries.
- Review academic performance and attendance summaries where supported by the existing data.
- Compare student statistics across academic sessions.
- Filter records by available class, session, gender, or student status.
- Export filtered student, academic, and fee records to CSV or Excel.
- Provide downloadable reports for administrative review.

### 📈 Dashboard Visualizations
- Display key statistics using metric cards.
- Use bar charts for class-wise student counts, academic performance, and fee collection.
- Use readable class labels such as 1st, 2nd, 3rd, and 10th on relevant charts.
- Present clear report summaries with readable text and sufficient contrast.
- Ensure chart labels, legends, navigation buttons, and section headings remain visible.

### 🛠️ Technology Stack
- **Dashboard:** Streamlit
- **Programming language:** Python
- **Data analysis:** Pandas and NumPy
- **Visualization:** Plotly and Matplotlib
- **Data storage:** CSV files
- **Report export:** CSV and Excel using Pandas and OpenPyXL

**Project scope:** The system focuses on student record management, academic and financial analysis, interactive visualizations, and report generation. Machine learning predictions, authentication, and database integration are potential future enhancements rather than existing features.


---

## 📁 Folder Structure

```

School-Management-System/
│
├── app.py                        # Main Streamlit application entry point
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
│
|
├── students.csv
├── student_history.csv
├── marks.csv
├── attendance.csv
└── fees.csv
│
---

## 📦 Requirements

```
pandas
numpy
streamlit
matplotlib
plotly
openpyxl
```

---

## ▶️ How to Run the Project

Once dependencies are installed, launch the dashboard with:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application will open automatically in your default browser at:

```
http://localhost:8501
```

## 🚀 Future Improvements

- 🔐 Add role-based authentication (Admin / Teacher / Parent login)
- ☁️ Migrate data storage to a proper database (PostgreSQL / MongoDB)
- 📱 Build a mobile-friendly / responsive UI
- 🔔 Add automated fee-due and attendance-alert notifications
- 🧾 Generate printable PDF report cards and fee receipts
- 🌐 Deploy the dashboard publicly (Streamlit Cloud / Render / AWS)
- 🤖 future integration of predictive analytics (performance forecasting ML model)

---


## 🏁 Conclusion

The School Management System shows how Pandas and Streamlit can turn school data into useful reports and interactive dashboards. It helps manage student records, attendance, marks, and fees in a simple and organized way. This project also demonstrates practical skills in data analysis, data visualization, and dashboard development, making it a good project for learning and real-world school management.
