import streamlit as st

st.set_page_config(page_title="Fitness Activity Analyzer", layout="wide")

# Simple styling
st.markdown("""
<style>
body{
background-color:#f4f6f7;
}
h1{
color:#2c3e50;
text-align:center;
}
.big{
font-size:20px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🏃 AI Fitness Activity Pattern Analyzer")

st.write("Analyze your fitness activity and get smart suggestions")

# Sidebar input
st.sidebar.header("Enter Your Fitness Data")

steps = st.sidebar.slider("Daily Steps",0,20000,5000)
calories = st.sidebar.slider("Calories Burned",0,1000,300)
workout = st.sidebar.slider("Workout Time (minutes)",0,120,30)
sleep = st.sidebar.slider("Sleep Hours",0,12,7)

st.subheader("Your Activity Data")

st.write("Steps:",steps)
st.write("Calories:",calories)
st.write("Workout Time:",workout)
st.write("Sleep:",sleep)

# Simple clustering logic
if steps < 4000 and workout < 20:
    cluster = "Low Activity ⚠"
elif steps < 9000:
    cluster = "Moderately Active 🚶"
else:
    cluster = "Highly Active 💪"

st.subheader("Fitness Cluster Result")

st.success(cluster)

# Fitness score calculation
score = (steps/20000)*40 + (calories/1000)*30 + (workout/120)*20 + (sleep/12)*10
score = round(score,2)

st.subheader("Fitness Score")

st.metric("Your Fitness Score",score)

# Suggestions
st.subheader("Fitness Suggestions")

if score < 40:
    st.error("Your activity level is low. Try walking 5000 steps daily and doing light workouts.")
elif score < 70:
    st.warning("Good progress! Increase workout intensity to improve fitness.")
else:
    st.success("Excellent fitness level! Maintain your routine.")

# Progress chart
st.subheader("Sample Weekly Activity")

steps_data = [2000,4000,6000,7000,9000,11000,12000]
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

st.line_chart({"Steps":steps_data})

# Motivation
st.subheader("Motivation")

if cluster == "Low Activity ⚠":
    st.write("Start small. Even 10 minutes of walking daily can improve health.")
elif cluster == "Moderately Active 🚶":
    st.write("You are doing well. Add strength training to improve fitness.")
else:
    st.write("Great work! Keep maintaining a healthy lifestyle.")

st.write("💡 Stay active. Stay healthy.")
