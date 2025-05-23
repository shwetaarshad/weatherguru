import streamlit as st
from agent.weather_agent import ask_weather_agent

st.set_page_config(page_title="WeatherGuru 🌤️", page_icon="🌤️")

st.title("🌍 WeatherGuru")
st.subheader("Ask me about the weather anywhere in the world!")

user_input = st.text_input("What's your question?", placeholder="e.g., What's the weather in Tokyo?")

if st.button("Get Weather") and user_input:
    with st.spinner("Retrieving..."):
        result = ask_weather_agent(user_input)
        st.success(result)
        st.balloons()