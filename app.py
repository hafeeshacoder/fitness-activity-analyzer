import streamlit as st
import random

st.set_page_config(page_title="AI Smart Gym Trainer", page_icon="💪", layout="wide")

# Title
st.title("💪 AI Smart Gym Trainer & Fitness Planner")
st.write("Your personal virtual gym coach")

st.sidebar.header("Enter Your Fitness Details")

age = st.sidebar.slider("Age", 15, 60, 25)
height = st.sidebar.slider("Height (cm)", 140, 210, 170)
weight = st.sidebar.slider("Weight (kg)", 40, 120, 70)

steps = st.sidebar.slider("Daily Steps", 0, 20000, 6000)
workout_time = st.sidebar.slider("Workout Time (minutes)", 0, 120, 30)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "General Fitness"]
)

experience = st.sidebar.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# BMI
st.subheader("📊 Body Analysis")

height_m = height / 100
bmi = weight / (height_m * height_m)

st.metric("Your BMI", round(bmi,2))

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

st.success(f"Body Category: {category}")

# Fitness Level
st.subheader("🏃 Activity Level")

if steps < 4000:
    level = "Low Activity"
elif steps < 9000:
    level = "Moderate Activity"
else:
    level = "Highly Active"

st.info(level)

# Workout Recommendation
st.subheader("🏋️ Recommended Exercises")

workouts = {
    "Weight Loss": ["Running", "Jump Rope", "Cycling", "Burpees"],
    "Muscle Gain": ["Bench Press", "Deadlift", "Squats", "Dumbbell Curl"],
    "General Fitness": ["Pushups", "Plank", "Jogging", "Yoga"]
}

for w in workouts[goal]:
    st.write("•", w)

# Weekly Planner
st.subheader("📅 Weekly Gym Plan")

week_plan = {
    "Monday": "Chest + Triceps",
    "Tuesday": "Back + Biceps",
    "Wednesday": "Cardio",
    "Thursday": "Leg Day",
    "Friday": "Shoulders",
    "Saturday": "Full Body",
    "Sunday": "Rest"
}

for day, plan in week_plan.items():
    st.write(day, "→", plan)

# Calories Burn Estimator
st.subheader("🔥 Calories Burn Estimator")

calories = workout_time * 8
st.metric("Estimated Calories Burned", f"{calories} kcal")

# Progress Chart
st.subheader("📈 Weekly Steps Progress")

data = {
    "Steps":[3000,5000,6500,7000,8000,10000,9000]
}

st.line_chart(data)

# Goal Tracker
st.subheader("🎯 Fitness Goal Progress")

progress = random.randint(40,90)

st.progress(progress/100)

st.write("Goal Completion:",progress,"%")

# Motivation
st.subheader("💡 Motivation")

messages = [
"Every workout counts!",
"Push yourself a little more today!",
"Consistency beats motivation!",
"Your body will thank you later!",
"Stay strong and keep going!"
]

st.success(random.choice(messages))
