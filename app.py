# 🏫 School Management System — app.py

import io
import re
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


# PAGE CONFIGURATION

st.set_page_config(
    page_title="School Management System",
    page_icon="🏫",
    layout="wide",
)


# THEME — ORIGINAL SAGE GREEN PALETTE RETAINED
st.markdown(
    """
    <style>
    :root {
        --ink: #34483C;
        --muted: #52675A;
        --line: #DCE6DE;
        --canvas: #F7F8F4;
        --navy: #34483C;
        --teal: #789483;
        --purple: #A8BBAE;
        --white: #FFFFFF;
    }

    /* Page spacing: prevents the top of the dashboard being cut off */
    .stApp {
        background-color: #F7F8F4;
        color: #34483C;
    }

    .main .block-container {
        padding-top: 1.8rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1500px;
        overflow: visible !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
        height: 2.5rem;
    }

    [data-testid="stAppViewContainer"] {
        overflow: visible;
    }

    /* General text contrast */
    h1, h2, h3, h4, h5, h6,
    p, label, li, span, div {
        color: inherit;
    }

    h1, h2, h3, h4 {
        color: #34483C !important;
        font-weight: 700 !important;
    }

    p, label, li {
        color: #34483C;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #34483C;
    }

    .subtitle {
        color: #52675A !important;
        font-size: 0.95rem;
        margin-top: -0.45rem;
        margin-bottom: 1.1rem;
    }

    /* Main dashboard header */
    .hero {
        background: linear-gradient(115deg, #34483C 0%, #627D6D 58%, #789483 100%);
        padding: 1.6rem 1.8rem;
        border-radius: 16px;
        margin: 0 0 1.2rem 0;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(52, 72, 60, 0.10);
        overflow: visible;
    }

    .hero h1 {
        color: #FFFFFF !important;
        font-size: 1.8rem !important;
        line-height: 1.3 !important;
        margin: 0 0 0.4rem 0 !important;
        padding: 0 !important;
    }

    .hero p {
        color: #F5F8F5 !important;
        margin: 0 !important;
        font-size: 0.95rem;
    }

    /* Navigation: readable dark labels */
    div[role="radiogroup"] {
        gap: 0.5rem;
        margin-top: 0.2rem;
        margin-bottom: 1rem;
    }

    div[role="radiogroup"] label {
        background: #FFFFFF;
        border: 1px solid #DCE6DE;
        border-radius: 10px;
        padding: 0.65rem 1rem;
        color: #34483C !important;
        font-weight: 700 !important;
    }

    div[role="radiogroup"] label p,
    div[role="radiogroup"] label span {
        color: #34483C !important;
        font-weight: 700 !important;
    }

    div[role="radiogroup"] label:has(input:checked) {
        background: #34483C !important;
        border-color: #34483C !important;
        color: #FFFFFF !important;
    }

    div[role="radiogroup"] label:has(input:checked) p,
    div[role="radiogroup"] label:has(input:checked) span {
        color: #FFFFFF !important;
    }

    /* KPI cards */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #DCE6DE;
        border-radius: 13px;
        padding: 1rem 1.1rem;
        min-height: 105px;
        box-shadow: 0 2px 7px rgba(52, 72, 60, 0.04);
    }

    .metric-label {
        color: #52675A !important;
        font-size: 0.84rem;
        font-weight: 600;
        margin-bottom: 0.35rem;
    }

    .metric-value {
        color: #34483C !important;
        font-size: 1.65rem;
        font-weight: 750;
        line-height: 1.25;
        overflow-wrap: anywhere;
    }

    .metric-note {
        color: #52675A !important;
        font-size: 0.78rem;
        margin-top: 0.3rem;
    }

    /* Section cards */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #DCE6DE;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 0.8rem;
    }

    /* Input controls */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="textarea"] > div {
        background-color: #FFFFFF !important;
        border-color: #B8C9BC !important;
    }

    input, textarea {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    }

    div[data-baseweb="select"] * {
        color: #34483C !important;
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        background: #34483C;
        color: #FFFFFF !important;
        border: 1px solid #34483C;
        border-radius: 9px;
        font-weight: 650;
    }

    .stButton > button p,
    .stDownloadButton > button p {
        color: #FFFFFF !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #627D6D;
        border-color: #627D6D;
        color: #FFFFFF !important;
    }

    /* Dataframes and tables */
    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        border: 1px solid #DCE6DE;
        border-radius: 8px;
    }

    /* Tabs and expanders */
    button[data-baseweb="tab"] {
        color: #34483C !important;
        font-weight: 650 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #34483C !important;
    }

    [data-testid="stExpander"] {
        background: #FFFFFF;
        border: 1px solid #DCE6DE;
        border-radius: 10px;
    }

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p {
        color: #34483C !important;
        font-weight: 650 !important;
    }

    /* Report summary */
    .report-summary {
        background: #E8F1EC;
        border: 1px solid #C8D9CD;
        border-left: 5px solid #627D6D;
        border-radius: 10px;
        padding: 1rem 1.1rem;
        color: #34483C !important;
        margin: 0.5rem 0 1rem 0;
    }

    .report-summary h4 {
        color: #34483C !important;
        margin: 0 0 0.4rem 0;
    }

    .report-summary p,
    .report-summary li {
        color: #34483C !important;
        line-height: 1.55;
    }

    .small-muted {
        color: #52675A !important;
        font-size: 0.85rem;
    }

    hr {
        border-color: #DCE6DE;
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1.2rem !important;
        }

        .hero {
            padding: 1.2rem;
        }

        .hero h1 {
            font-size: 1.45rem !important;
        }

        div[role="radiogroup"] label {
            padding: 0.45rem 0.55rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# DATA FILES
# Keep these CSV files in the same folder as app.py

DATA_DIR = Path(__file__).parent

FILES = {
    "students": DATA_DIR / "students.csv",
    "history": DATA_DIR / "student_history.csv",
    "marks": DATA_DIR / "marks.csv",
    "attendance": DATA_DIR / "attendance.csv",
    "fees": DATA_DIR / "fees.csv",
}



# HELPER FUNCTIONS

def clean_columns(df):
    """Normalize column names without changing their meaning."""
    df = df.copy()
    df.columns = [
        re.sub(r"\s+", "_", str(col).strip())
        for col in df.columns
    ]
    return df


def load_csv(path):
    """Load one CSV safely."""
    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
        return clean_columns(df)
    except Exception as exc:
        st.warning(f"Could not read {path.name}: {exc}")
        return pd.DataFrame()


def money(value):
    """Format a number as Indian rupees."""
    try:
        if pd.isna(value):
            value = 0
        return f"₹{float(value):,.2f}"
    except (TypeError, ValueError):
        return "₹0.00"


def numeric_series(df, column):
    """Return a numeric series; use zeros if the column is absent."""
    if column not in df.columns:
        return pd.Series(0.0, index=df.index)
    return pd.to_numeric(df[column], errors="coerce").fillna(0)


def first_existing_column(df, candidates):
    """Return the first matching column from a list of possible names."""
    lower_map = {str(col).lower(): col for col in df.columns}

    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]

    return None


def ordinal_class(value):
    """Convert class numbers into labels such as 1st, 2nd, 3rd, 4th."""
    if pd.isna(value):
        return "Not specified"

    text = str(value).strip()

    # Keep meaningful text such as Nursery, LKG, UKG, or Class 1.
    match = re.search(r"\d+", text)

    if not match:
        return text

    number = int(match.group())

    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")

    return f"{number}{suffix}"


def normalize_key_values(df, columns):
    """Normalize common join keys to reduce mismatched CSV joins."""
    df = df.copy()

    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip()

    return df


def merge_source(base, source, source_name):
    """
    Merge a source dataframe into the base dataframe.
    Prefer Student_ID and other shared academic keys where available.
    """
    if source.empty or base.empty:
        return base

    key_candidates = [
        "Student_ID",
        "Academic_Session",
        "Class",
    ]

    keys = [
        col for col in key_candidates
        if col in base.columns and col in source.columns
    ]

    if not keys:
        return base

    left = base.copy()
    right = source.copy()

    left = normalize_key_values(left, keys)
    right = normalize_key_values(right, keys)

    # Avoid a many-to-many explosion when a source has exact duplicate rows.
    right = right.drop_duplicates()

    # Keep overlapping non-key columns without overwriting the base columns.
    overlap = [
        col for col in right.columns
        if col in left.columns and col not in keys
    ]

    if overlap:
        right = right.rename(
            columns={col: f"{col}_{source_name}" for col in overlap}
        )

    try:
        return left.merge(right, on=keys, how="left")
    except Exception:
        return base


def get_display_name(row):
    """Find a usable student name across common dataset formats."""
    for col in ["Student_Name", "Name", "Full_Name", "Student"]:
        if col in row.index and pd.notna(row[col]):
            return str(row[col])

    return str(row.get("Student_ID", "Unknown student"))


def display_metric(label, value, note=""):
    """Render a consistent metric card with readable text."""
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_table(df, height=350):
    """Show a dataframe with a friendly empty state."""
    if df.empty:
        st.info("No records are available for this selection.")
        return

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=height,
    )


def csv_bytes(df):
    """Convert a dataframe to downloadable CSV bytes."""
    return df.to_csv(index=False).encode("utf-8-sig")


def excel_bytes(sheets):
    """Create a multi-sheet Excel workbook in memory."""
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet_name, frame in sheets.items():
            safe_name = sheet_name[:31]
            frame.to_excel(
                writer,
                sheet_name=safe_name,
                index=False,
            )

    output.seek(0)
    return output.getvalue()


# LOAD DATA

@st.cache_data(show_spinner=False)
def load_all_data():
    return {
        name: load_csv(path)
        for name, path in FILES.items()
    }


data = load_all_data()

students = data["students"].copy()
history = data["history"].copy()
marks = data["marks"].copy()
attendance = data["attendance"].copy()
fees = data["fees"].copy()


# DATA VALIDATION AND COMBINED DATA

if students.empty:
    st.markdown(
        """
        <div class="hero">
            <h1>🏫 School Management System</h1>
            <p>Student records, academics, attendance, fees and reports</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.error(
        "The students.csv file could not be found or contains no data."
    )
    st.info(
        "Place students.csv, student_history.csv, marks.csv, "
        "attendance.csv and fees.csv in the same folder as app.py."
    )
    st.stop()


# Ensure the main student table has a student ID field.
student_id_col = first_existing_column(
    students,
    ["Student_ID", "StudentID", "Student_Id", "Admission_ID"],
)

if student_id_col and student_id_col != "Student_ID":
    students = students.rename(
        columns={student_id_col: "Student_ID"}
    )

if "Student_ID" not in students.columns:
    st.error(
        "A Student_ID column is required in students.csv. "
        "Please check the column name in your file."
    )
    st.stop()


# Normalize common join keys across all dataframes.
key_columns = ["Student_ID", "Academic_Session", "Class"]

students = normalize_key_values(students, key_columns)
history = normalize_key_values(history, key_columns)
marks = normalize_key_values(marks, key_columns)
attendance = normalize_key_values(attendance, key_columns)
fees = normalize_key_values(fees, key_columns)

# Remove duplicate master student IDs when the same student appears more than once.
students = students.drop_duplicates(
    subset=["Student_ID"],
    keep="first",
).reset_index(drop=True)

# Create a combined view, using the student master as the base.
combined = students.copy()
combined = merge_source(combined, history, "history")
combined = merge_source(combined, marks, "marks")
combined = merge_source(combined, attendance, "attendance")
combined = merge_source(combined, fees, "fees")

# Create useful fallback columns.
if "Student_Name" not in combined.columns:
    possible_name = first_existing_column(
        combined,
        ["Name", "Full_Name", "Student"],
    )
    if possible_name:
        combined["Student_Name"] = combined[possible_name]
    else:
        combined["Student_Name"] = combined["Student_ID"]

# Identify common fields used by the dashboard.
class_col = first_existing_column(
    combined,
    ["Class", "Grade", "Standard", "Class_Name"],
)

session_col = first_existing_column(
    combined,
    ["Academic_Session", "Session", "Academic_Year", "Year"],
)

total_fee_col = first_existing_column(
    combined,
    [
        "Total_Fee",
        "Total_Fees",
        "Fee_Amount",
        "Total_Amount",
        "Fees",
    ],
)

paid_fee_col = first_existing_column(
    combined,
    [
        "Paid_Amount",
        "Amount_Paid",
        "Fee_Paid",
        "Paid_Fees",
        "Total_Paid",
    ],
)

remaining_fee_col = first_existing_column(
    combined,
    [
        "Remaining_Fee",
        "Fee_Due",
        "Outstanding",
        "Balance",
        "Pending_Fees",
    ],
)

attendance_col = first_existing_column(
    combined,
    [
        "Attendance_Percentage",
        "Attendance_Percent",
        "Attendance_Rate",
        "Attendance",
    ],
)

percentage_col = first_existing_column(
    combined,
    [
        "Percentage",
        "Total_Percentage",
        "Overall_Percentage",
        "Average_Percentage",
    ],
)

grade_col = first_existing_column(
    combined,
    ["Grade", "Final_Grade", "Overall_Grade"],
)

result_col = first_existing_column(
    combined,
    ["Result", "Final_Result", "Status"],
)

# Add a readable class label to the combined table.
if class_col:
    combined["Class_Label"] = combined[class_col].apply(ordinal_class)
else:
    combined["Class_Label"] = "Not specified"


# HEADER

st.markdown(
    """
    <div class="hero">
        <h1>🏫 School Management System</h1>
        <p>
            Manage student profiles, academic performance, fees,
            attendance and school reports in one place.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# NAVIGATION — ONLY THREE SCREENS

page = st.radio(
    "Main navigation",
    [
        "Student Details & Academics",
        "Fees & Payments",
        "Reports & Exports",
    ],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown("---")


# SCREEN 1 — STUDENT DETAILS AND ACADEMICS

if page == "Student Details & Academics":

    st.title("Student Details & Academics")
    st.markdown(
        '<p class="subtitle">Search for a student and view their profile, '
        'academic information, marks and attendance.</p>',
        unsafe_allow_html=True,
    )

    # Search by student ID or name.
    search = st.text_input(
        "Search student",
        placeholder="Enter student name, student ID or roll number...",
        key="student_search",
    )

    filtered_students = combined.copy()

    if search.strip():
        search_text = search.strip().lower()

        search_columns = [
            col for col in [
                "Student_ID",
                "Student_Name",
                "Name",
                "Roll_Number",
                "Roll_No",
                "Admission_Number",
            ]
            if col in filtered_students.columns
        ]

        if search_columns:
            mask = pd.Series(
                False,
                index=filtered_students.index,
            )

            for col in search_columns:
                mask |= (
                    filtered_students[col]
                    .astype(str)
                    .str.lower()
                    .str.contains(search_text, na=False)
                )

            filtered_students = filtered_students[mask]

    # Optional class filter.
    if class_col:
        available_classes = sorted(
            combined[class_col]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if available_classes:
            selected_class = st.selectbox(
                "Filter by class",
                ["All Classes"] + [
                    ordinal_class(value)
                    for value in available_classes
                ],
                key="student_class_filter",
            )

            if selected_class != "All Classes":
                filtered_students = filtered_students[
                    filtered_students["Class_Label"] == selected_class
                ]

    if filtered_students.empty:
        st.warning("No students match your search or filter.")
    else:
        # Build labels for the student selector.
        student_options = {}

        for idx, row in filtered_students.iterrows():
            name = get_display_name(row)
            sid = row.get("Student_ID", "N/A")
            class_name = row.get("Class_Label", "Not specified")

            label = f"{name} | ID: {sid} | Class: {class_name}"
            student_options[label] = idx

        selected_label = st.selectbox(
            "Select student",
            list(student_options.keys()),
            key="selected_student",
        )

        selected_index = student_options[selected_label]
        student = filtered_students.loc[selected_index]

        st.markdown("### Student overview")

        # Academic percentage and attendance values.
        percentage_value = (
            pd.to_numeric(
                pd.Series([student.get(percentage_col)]),
                errors="coerce",
            ).iloc[0]
            if percentage_col
            else np.nan
        )

        attendance_value = (
            pd.to_numeric(
                pd.Series([student.get(attendance_col)]),
                errors="coerce",
            ).iloc[0]
            if attendance_col
            else np.nan
        )

        grade_value = (
            str(student.get(grade_col))
            if grade_col and pd.notna(student.get(grade_col))
            else "N/A"
        )

        result_value = (
            str(student.get(result_col))
            if result_col and pd.notna(student.get(result_col))
            else "N/A"
        )

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            display_metric(
                "Student ID",
                str(student.get("Student_ID", "N/A")),
                "Student record",
            )

        with m2:
            display_metric(
                "Class",
                str(student.get("Class_Label", "N/A")),
                "Current class",
            )

        with m3:
            display_metric(
                "Academic Percentage",
                f"{percentage_value:.1f}%"
                if pd.notna(percentage_value)
                else "N/A",
                "Available academic record",
            )

        with m4:
            display_metric(
                "Attendance",
                f"{attendance_value:.1f}%"
                if pd.notna(attendance_value)
                else "N/A",
                "Available attendance record",
            )

        st.markdown("### Complete student information")

        # Display every available student field.
        profile_exclude = {
            "Class_Label",
        }

        profile_fields = [
            col for col in students.columns
            if col not in profile_exclude
        ]

        profile_data = []

        for col in profile_fields:
            value = student.get(col, None)

            if pd.notna(value):
                profile_data.append(
                    {
                        "Field": col.replace("_", " "),
                        "Details": str(value),
                    }
                )

        if profile_data:
            profile_df = pd.DataFrame(profile_data)
            left, right = st.columns(2)

            midpoint = (len(profile_df) + 1) // 2

            with left:
                show_table(profile_df.iloc[:midpoint], height=300)

            with right:
                show_table(profile_df.iloc[midpoint:], height=300)

        # Academic, attendance and fee information in separate tabs.
        academic_tab, attendance_tab, fee_tab, full_tab = st.tabs(
            [
                "📚 Academics",
                "📅 Attendance",
                "💳 Fees",
                "📋 All Available Data",
            ]
        )

        with academic_tab:
            st.markdown("#### Academic performance")
            st.caption(
                "All available marks and academic fields for this student."
            )

            academic_columns = [
                col for col in combined.columns
                if any(
                    word in col.lower()
                    for word in [
                        "mark",
                        "score",
                        "subject",
                        "percentage",
                        "grade",
                        "result",
                        "exam",
                        "test",
                        "rank",
                        "academic",
                        "session",
                    ]
                )
            ]

            if academic_columns:
                academic_record = student[academic_columns].to_frame(
                    name="Value"
                ).reset_index()

                academic_record.columns = ["Academic Field", "Value"]

                show_table(academic_record, height=350)
            else:
                st.info(
                    "No recognizable academic columns were found. "
                    "Check the column names in marks.csv and student_history.csv."
                )

            if percentage_col and pd.notna(percentage_value):
                if percentage_value >= 90:
                    st.success("Excellent academic performance.")
                elif percentage_value >= 75:
                    st.info("Good academic performance.")
                elif percentage_value >= 50:
                    st.info("There is room to improve academic performance.")
                else:
                    st.warning("This student may need additional academic support.")

            if grade_value != "N/A" or result_value != "N/A":
                c1, c2 = st.columns(2)

                with c1:
                    display_metric("Grade", grade_value)

                with c2:
                    display_metric("Result", result_value)

        with attendance_tab:
            st.markdown("#### Attendance record")

            attendance_columns = [
                col for col in combined.columns
                if any(
                    word in col.lower()
                    for word in [
                        "attendance",
                        "present",
                        "absent",
                        "leave",
                        "working_day",
                        "date",
                    ]
                )
            ]

            if attendance_columns:
                attendance_record = student[
                    attendance_columns
                ].to_frame(name="Value").reset_index()

                attendance_record.columns = [
                    "Attendance Field",
                    "Value",
                ]

                show_table(attendance_record, height=300)
            else:
                st.info(
                    "No attendance fields were found in the combined dataset."
                )

        with fee_tab:
            st.markdown("#### Student fee details")

            fee_columns = [
                col for col in combined.columns
                if any(
                    word in col.lower()
                    for word in [
                        "fee",
                        "paid",
                        "payment",
                        "amount",
                        "balance",
                        "due",
                        "transaction",
                    ]
                )
            ]

            if fee_columns:
                fee_record = student[fee_columns].to_frame(
                    name="Value"
                ).reset_index()

                fee_record.columns = ["Fee Field", "Value"]
                show_table(fee_record, height=300)
            else:
                st.info("No fee fields were found for this student.")

        with full_tab:
            st.markdown("#### All merged data")
            show_table(
                student.to_frame(name="Value").reset_index().rename(
                    columns={
                        "index": "Field",
                        "Value": "Details",
                    }
                ),
                height=400,
            )

        st.download_button(
            "⬇️ Download Student Record",
            data=csv_bytes(student.to_frame().T),
            file_name=f"student_{student.get('Student_ID', 'record')}.csv",
            mime="text/csv",
            key="download_student",
        )


# SCREEN 2 — FEES AND PAYMENTS

elif page == "Fees & Payments":

    st.title("Fees & Payments")
    st.markdown(
        '<p class="subtitle">Review fee collection, payments, outstanding '
        'balances and collection by class.</p>',
        unsafe_allow_html=True,
    )

    fee_df = combined.copy()

    # Determine available fee columns.
    if total_fee_col:
        fee_df["Dashboard_Total_Fee"] = numeric_series(
            fee_df,
            total_fee_col,
        )
    else:
        fee_df["Dashboard_Total_Fee"] = 0.0

    if paid_fee_col:
        fee_df["Dashboard_Paid_Fee"] = numeric_series(
            fee_df,
            paid_fee_col,
        )
    else:
        fee_df["Dashboard_Paid_Fee"] = 0.0

    if remaining_fee_col:
        fee_df["Dashboard_Remaining_Fee"] = numeric_series(
            fee_df,
            remaining_fee_col,
        )
    else:
        fee_df["Dashboard_Remaining_Fee"] = (
            fee_df["Dashboard_Total_Fee"]
            - fee_df["Dashboard_Paid_Fee"]
        ).clip(lower=0)

    # Apply class filter if available.
    if class_col:
        class_labels = sorted(
            fee_df["Class_Label"].dropna().astype(str).unique().tolist()
        )

        selected_fee_class = st.selectbox(
            "Filter fees by class",
            ["All Classes"] + class_labels,
            key="fees_class_filter",
        )

        if selected_fee_class != "All Classes":
            fee_df = fee_df[
                fee_df["Class_Label"] == selected_fee_class
            ]

    total_fee = fee_df["Dashboard_Total_Fee"].sum()
    total_paid = fee_df["Dashboard_Paid_Fee"].sum()
    total_due = fee_df["Dashboard_Remaining_Fee"].sum()

    collection_rate = (
        (total_paid / total_fee) * 100
        if total_fee > 0
        else 0
    )

    st.markdown("### Collection summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        display_metric(
            "Total Fees",
            money(total_fee),
            "Fees recorded for selection",
        )

    with c2:
        display_metric(
            "Fees Collected",
            money(total_paid),
            "Payments received",
        )

    with c3:
        display_metric(
            "Outstanding Fees",
            money(total_due),
            "Remaining amount",
        )

    with c4:
        display_metric(
            "Collection Rate",
            f"{collection_rate:.1f}%",
            "Collected ÷ total fees",
        )

    st.markdown("---")
    st.markdown("### Fee collection by class")

    # Aggregate by class so charts use 1st, 2nd, 3rd, etc.
    if "Class_Label" in fee_df.columns and not fee_df.empty:
        chart_df = (
            fee_df.groupby("Class_Label", dropna=False)[
                [
                    "Dashboard_Total_Fee",
                    "Dashboard_Paid_Fee",
                    "Dashboard_Remaining_Fee",
                ]
            ]
            .sum()
            .reset_index()
        )

        # Order numeric classes correctly rather than alphabetically.
        def class_sort_key(value):
            match = re.search(r"\d+", str(value))
            return (
                0,
                int(match.group()),
            ) if match else (1, str(value).lower())

        chart_df = chart_df.sort_values(
            "Class_Label",
            key=lambda series: series.map(class_sort_key),
        )

        chart_tab1, chart_tab2 = st.tabs(
            ["Collection", "Outstanding Fees"]
        )

        with chart_tab1:
            st.markdown("#### Collected vs total fees")
            collection_chart = chart_df[
                [
                    "Class_Label",
                    "Dashboard_Total_Fee",
                    "Dashboard_Paid_Fee",
                ]
            ].rename(
                columns={
                    "Class_Label": "Class",
                    "Dashboard_Total_Fee": "Total Fees",
                    "Dashboard_Paid_Fee": "Fees Collected",
                }
            ).set_index("Class")

            st.bar_chart(
                collection_chart,
                use_container_width=True,
            )

        with chart_tab2:
            st.markdown("#### Remaining fees by class")

            outstanding_chart = chart_df[
                [
                    "Class_Label",
                    "Dashboard_Remaining_Fee",
                ]
            ].rename(
                columns={
                    "Class_Label": "Class",
                    "Dashboard_Remaining_Fee": "Outstanding Fees",
                }
            ).set_index("Class")

            st.bar_chart(
                outstanding_chart,
                use_container_width=True,
            )

    else:
        st.info(
            "Class-wise charts require a Class column and fee records."
        )

    st.markdown("### Student payment details")

    fee_search = st.text_input(
        "Search fee records",
        placeholder="Search by student name or ID...",
        key="fee_search",
    )

    if fee_search.strip():
        term = fee_search.strip().lower()

        mask = (
            fee_df["Student_ID"].astype(str).str.lower().str.contains(
                term,
                na=False,
            )
            |
            fee_df["Student_Name"].astype(str).str.lower().str.contains(
                term,
                na=False,
            )
        )

        fee_df = fee_df[mask]

    fee_table_columns = [
        col for col in [
            "Student_ID",
            "Student_Name",
            class_col,
            "Dashboard_Total_Fee",
            "Dashboard_Paid_Fee",
            "Dashboard_Remaining_Fee",
        ]
        if col and col in fee_df.columns
    ]

    fee_table = fee_df[fee_table_columns].copy()

    fee_table = fee_table.rename(
        columns={
            "Dashboard_Total_Fee": "Total Fees",
            "Dashboard_Paid_Fee": "Fees Paid",
            "Dashboard_Remaining_Fee": "Outstanding Fees",
        }
    )

    if "Class_Label" in fee_df.columns and class_col:
        fee_table["Class"] = fee_df["Class_Label"].values
        if class_col in fee_table.columns:
            fee_table = fee_table.drop(columns=[class_col])

    show_table(fee_table, height=400)

    st.download_button(
        "⬇️ Download Fee Report",
        data=csv_bytes(fee_table),
        file_name="fee_collection_report.csv",
        mime="text/csv",
        key="download_fees",
    )

    if not total_fee_col or not paid_fee_col:
        st.warning(
            "Some fee columns were not detected. Check your fees.csv "
            "column names. The dashboard supports common names such as "
            "Total_Fee, Paid_Amount and Remaining_Fee."
        )


# SCREEN 3 — REPORTS AND EXPORTS

elif page == "Reports & Exports":

    st.title("Reports & Exports")
    st.markdown(
        '<p class="subtitle">Review school-wide summaries and download '
        'filtered student, academic, attendance and fee data.</p>',
        unsafe_allow_html=True,
    )

    report_df = combined.copy()

    # Report filters.
    filter1, filter2 = st.columns(2)

    with filter1:
        if class_col:
            report_classes = sorted(
                report_df["Class_Label"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            report_class = st.selectbox(
                "Class",
                ["All Classes"] + report_classes,
                key="report_class",
            )
        else:
            report_class = "All Classes"

    with filter2:
        if session_col:
            sessions = sorted(
                report_df[session_col]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            report_session = st.selectbox(
                "Academic session",
                ["All Sessions"] + sessions,
                key="report_session",
            )
        else:
            report_session = "All Sessions"

    if report_class != "All Classes":
        report_df = report_df[
            report_df["Class_Label"] == report_class
        ]

    if (
        session_col
        and report_session != "All Sessions"
    ):
        report_df = report_df[
            report_df[session_col].astype(str) == report_session
        ]

    # Calculate report summary metrics.
    student_count = (
        report_df["Student_ID"].nunique()
        if "Student_ID" in report_df.columns
        else len(report_df)
    )

    average_percentage = (
        pd.to_numeric(
            report_df[percentage_col],
            errors="coerce",
        ).mean()
        if percentage_col
        else np.nan
    )

    average_attendance = (
        pd.to_numeric(
            report_df[attendance_col],
            errors="coerce",
        ).mean()
        if attendance_col
        else np.nan
    )

    report_total_fee = (
        numeric_series(report_df, total_fee_col).sum()
        if total_fee_col
        else 0
    )

    report_paid_fee = (
        numeric_series(report_df, paid_fee_col).sum()
        if paid_fee_col
        else 0
    )

    report_due_fee = (
        numeric_series(report_df, remaining_fee_col).sum()
        if remaining_fee_col
        else max(report_total_fee - report_paid_fee, 0)
    )

    st.markdown("### Report summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        display_metric(
            "Students",
            f"{student_count:,}",
            "Unique student records",
        )

    with c2:
        display_metric(
            "Average Percentage",
            f"{average_percentage:.1f}%"
            if pd.notna(average_percentage)
            else "N/A",
            "Available academic data",
        )

    with c3:
        display_metric(
            "Average Attendance",
            f"{average_attendance:.1f}%"
            if pd.notna(average_attendance)
            else "N/A",
            "Available attendance data",
        )

    with c4:
        display_metric(
            "Fees Outstanding",
            money(report_due_fee),
            "For the selected records",
        )

    # High-contrast summary block.
    st.markdown(
        f"""
        <div class="report-summary">
            <h4>School report overview</h4>
            <p>
                The current selection contains
                <strong>{student_count:,} students</strong>.
                Total recorded fees are
                <strong>{money(report_total_fee)}</strong>,
                of which <strong>{money(report_paid_fee)}</strong>
                have been collected. The outstanding amount is
                <strong>{money(report_due_fee)}</strong>.
            </p>
            <p>
                Average academic percentage:
                <strong>
                    {f"{average_percentage:.1f}%" if pd.notna(average_percentage) else "Not available"}
                </strong>
                &nbsp; | &nbsp;
                Average attendance:
                <strong>
                    {f"{average_attendance:.1f}%" if pd.notna(average_attendance) else "Not available"}
                </strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Class-wise academic chart.
    if class_col and percentage_col and not report_df.empty:
        st.markdown("### Academic performance by class")

        performance_df = report_df.copy()
        performance_df["_percentage_numeric"] = pd.to_numeric(
            performance_df[percentage_col],
            errors="coerce",
        )

        performance_chart = (
            performance_df.groupby("Class_Label")[
                "_percentage_numeric"
            ]
            .mean()
            .reset_index()
            .rename(
                columns={
                    "Class_Label": "Class",
                    "_percentage_numeric": "Average Percentage",
                }
            )
        )

        def class_sort_key(value):
            match = re.search(r"\d+", str(value))
            return (
                0,
                int(match.group()),
            ) if match else (1, str(value).lower())

        performance_chart = performance_chart.sort_values(
            "Class",
            key=lambda series: series.map(class_sort_key),
        )

        st.bar_chart(
            performance_chart.set_index("Class"),
            use_container_width=True,
        )

    elif not percentage_col:
        st.info(
            "Academic performance charts need a Percentage or "
            "Overall_Percentage column in your dataset."
        )

    st.markdown("---")
    st.markdown("### Data preview")

    report_table = report_df.copy()
    show_table(report_table, height=400)

    st.markdown("### Download reports")

    download1, download2 = st.columns(2)

    with download1:
        st.download_button(
            "⬇️ Export Filtered CSV",
            data=csv_bytes(report_df),
            file_name="school_report.csv",
            mime="text/csv",
            key="export_filtered_csv",
            use_container_width=True,
        )

    with download2:
        try:
            workbook = excel_bytes(
                {
                    "Student Report": report_df,
                    "Fee Summary": fee_df if "fee_df" in globals() else report_df,
                    "Attendance": attendance,
                    "Marks": marks,
                }
            )

            st.download_button(
                "⬇️ Export Excel Workbook",
                data=workbook,
                file_name="school_management_reports.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
                key="export_excel",
                use_container_width=True,
            )

        except Exception as exc:
            st.warning(
                "Excel export could not be generated. "
                "Install openpyxl using: pip install openpyxl"
            )

    st.markdown("### Individual dataset exports")

    export_cols = st.columns(4)

    export_datasets = [
        ("Students", students, "students_export.csv"),
        ("Marks", marks, "marks_export.csv"),
        ("Attendance", attendance, "attendance_export.csv"),
        ("Fees", fees, "fees_export.csv"),
    ]

    for column, (label, frame, filename) in zip(
        export_cols,
        export_datasets,
    ):
        with column:
            st.download_button(
                f"Export {label}",
                data=csv_bytes(frame),
                file_name=filename,
                mime="text/csv",
                key=f"export_{label.lower()}",
                use_container_width=True,
            )


# FOOTER

st.markdown("---")
st.markdown(
    """
    <p class="small-muted" style="text-align:center;">
        School Management System · Student Records · Academics ·
        Fees · Reports
    </p>
    """,
    unsafe_allow_html=True,
)
