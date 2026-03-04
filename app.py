import streamlit as st

st.title("RTU Attendance Tracker")

# RTU Subjects Semester-wise
rtu_subjects = {
    "Semester 1": ["Maths-1", "Physics", "Chemistry", "Basic Electrical", "Human Values"],
    "Semester 2": ["Civil Engineering", "Mechanical Engineering", "Maths-2", "C++", "CAEG", "Chemistry", "Human Values"],
    "Semester 3": ["Data Structures", "Digital Electronics", "Discrete Maths"],
}

# Select Semester
semester = st.selectbox("Select Your Semester", list(rtu_subjects.keys()))
subjects = rtu_subjects[semester]

st.subheader("Enter Attendance Details")

total_attended_all = 0
total_classes_all = 0

for subject in subjects:
    st.markdown(f"### {subject}")
    
    total_classes = st.number_input(
        f"Total Classes Held for {subject}",
        min_value=0,
        step=1,
        key=f"total_{subject}"
    )
    
    attended = st.number_input(
        f"Classes Attended in {subject}",
        min_value=0,
        step=1,
        key=f"attended_{subject}"
    )

    if attended > total_classes:
        st.error("Attended classes cannot be more than total classes.")
    else:
        if total_classes > 0:
            percentage = (attended / total_classes) * 100
            st.write(f"Attendance in {subject}: {percentage:.2f}%")

        total_attended_all += attended
        total_classes_all += total_classes

# Aggregate Attendance
if total_classes_all > 0:
    aggregate = (total_attended_all / total_classes_all) * 100
    st.subheader(f"Overall Attendance: {aggregate:.2f}%")

    if aggregate < 75:
        st.error("⚠ Overall attendance below 75%")
    else:
        st.success("✅ Good Attendance")