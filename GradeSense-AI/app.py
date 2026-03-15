import streamlit as st

st.title("GradeSense AI")
st.subheader("Student Performance Predictor")

st.write("Enter lifestyle factors to estimate academic performance.")

# Input sliders
study = st.slider("Study Hours per Day", 0, 12, 4)
sleep = st.slider("Sleep Hours per Day", 0, 10, 7)
attendance = st.slider("Attendance Percentage", 0, 100, 80)
social = st.slider("Social Media Hours", 0, 10, 3)

# Simple scoring formula
score = (study * 8) + (sleep * 4) + (attendance * 0.5) - (social * 3)

score = max(0, min(score, 100))

st.subheader("Predicted Academic Score")
st.metric("Estimated Score", round(score, 2))

# Risk indicator
if score >= 75:
    st.success("Low Academic Risk")
elif score >= 50:
    st.warning("Medium Academic Risk")
else:
    st.error("High Academic Risk")

st.write("This estimate is based on lifestyle inputs.")