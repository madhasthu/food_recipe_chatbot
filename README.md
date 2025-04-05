# 🍳 Food Recipe Chatbot

An AI-powered chatbot built with **Streamlit** and **Gemini API**, designed to help you find delicious recipes, step-by-step cooking instructions, and dish images – all in one place!

---

## ✨ Features

- 🤖 Chatbot UI for natural recipe conversation
- 📸 Auto-generated image of the recipe
- 🧑‍🍳 Full cooking steps with ingredients
- 💬 Powered by Google Gemini API
- ⚡ Built using Streamlit for a responsive interface

---

## 📁 Project Structure

├── app.py # Streamlit UI 
├── chatbot.py # Gemini API logic 
├── requirements.txt # Python dependencies
├── .env # API key storage (excluded from Git) 
├── .gitignore # Git ignore rules


## 🚀 How to Run Locally

1. Clone the repo.
   
2. Create a virtual environment.
   
3. Install dependencies:
pip install -r requirements.txt

4.Add your Gemini API key to a .env file:

env
GEMINI_API_KEY=your_api_key_here

5.Run the app:
streamlit run app.py
