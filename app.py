import streamlit as st

st.title("Smart Attendance Tracker")

st.header("Enter Your Attended Classes")

# Predefined subjects and total classes (Admin controlled)
subjects = {
    "Mathematics": 40,
    "Physics": 35,
    "Chemistry": 38,
    "Computer Science": 42
}

total_all_classes = 0
total_all_attended = 0

for subject, total_classes in subjects.items():
    st.subheader(subject)
    st.write(f"Total Classes Conducted: {total_classes}")

    attended = st.number_input(
        f"Classes Attended in {subject}",
        min_value=0,
        max_value=total_classes,
        key=subject
    )

    percentage = (attended / total_classes) * 100
    st.write(f"Attendance: {percentage:.2f}%")

    total_all_classes += total_classes
    total_all_attended += attended

# Aggregate Attendance
if st.button("Calculate Overall Attendance"):
    overall_percentage = (total_all_attended / total_all_classes) * 100
    st.header(f"Overall Attendance: {overall_percentage:.2f}%")

    if overall_percentage < 75:
        st.error("Warning: Overall Attendance Below 75%!")
    else:
        st.success("Good Overall Attendance!")