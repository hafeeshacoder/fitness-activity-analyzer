import streamlit as st

st.set_page_config(page_title="AI Gym Workout Planner", layout="wide")

# Title
st.title("🏋️ AI Gym Workout Planner & Fitness Analyzer")

st.write("Get a personalized workout and fitness analysis")

# Sidebar input
st.sidebar.header("Enter Your Details")

age = st.sidebar.slider("Age",10,60,25)
height = st.sidebar.slider("Height (cm)",140,210,170)
weight = st.sidebar.slider("Weight (kg)",40,120,70)

steps = st.sidebar.slider("Daily Steps",0,20000,5000)
workout_time = st.sidebar.slider("Workout Time (minutes)",0,120,30)

goal = st.sidebar.selectbox(
"Fitness Goal",
("Weight Loss","Muscle Gain","General Fitness")
)

# BMI Calculation
height_m = height/100
bmi = weight/(height_m*height_m)

st.subheader("📊 Body Analysis")

st.write("Your BMI:",round(bmi,2))

if bmi < 18.5:
    category="Underweight"
elif bmi < 25:
    category="Normal"
elif bmi < 30:
    category="Overweight"
else:
    category="Obese"

st.write("BMI Category:",category)

# Fitness level detection
if steps < 4000:
    fitness="Low Activity"
elif steps < 9000:
    fitness="Moderate Activity"
else:
    fitness="Highly Active"

st.subheader("🏃 Fitness Level")
st.success(fitness)

# Workout Plan
st.subheader("🏋️ Personalized Workout Plan")

if goal=="Weight Loss":

    st.write("Day 1")
    st.write("- 20 min treadmill")
    st.write("- 15 squats")
    st.write("- 15 pushups")

    st.write("Day 2")
    st.write("- 25 min cycling")
    st.write("- Jump rope")

elif goal=="Muscle Gain":

    st.write("Day 1")
    st.write("- Bench Press")
    st.write("- Dumbbell curls")
    st.write("- Pushups")

    st.write("Day 2")
    st.write("- Deadlift")
    st.write("- Squats")
    st.write("- Shoulder press")

else:

    st.write("Day 1")
    st.write("- 20 min jogging")
    st.write("- 10 pushups")
    st.write("- 20 squats")

    st.write("Day 2")
    st.write("- Cycling")
    st.write("- Plank 30 sec")

# Diet Tips
st.subheader("🥗 Diet Suggestions")

if goal=="Weight Loss":
    st.write("• Eat more vegetables")
    st.write("• Avoid sugary drinks")
    st.write("• Drink more water")

elif goal=="Muscle Gain":
    st.write("• Increase protein intake")
    st.write("• Eat eggs, chicken, nuts")
    st.write("• Maintain calorie surplus")

else:
    st.write("• Balanced diet")
    st.write("• Include fruits and vegetables")

# Fitness Score
score=(steps/20000)*50+(workout_time/120)*50
score=round(score,2)

st.subheader("⭐ Fitness Score")

st.metric("Your Score",score)

# Progress chart
st.subheader("📈 Weekly Step Progress")

data={
"Steps":[3000,5000,7000,8000,10000,12000,9000]
}

st.line_chart(data)

# Motivation
st.subheader("💡 Motivation")

if score<40:
    st.warning("Start small. Even 10 minutes of exercise helps.")
elif score<70:
    st.info("Good progress! Try increasing workout intensity.")
else:
    st.success("Excellent fitness level. Keep it up!")
