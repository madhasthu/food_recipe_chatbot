import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Recipe generation with user details
def get_recipe_with_details(recipe_name, experience, servings, dietary, equipment):
    prompt = f"""
You are a professional chef bot. Give a complete, detailed recipe for: {recipe_name}

User Details:
- Cooking experience: {experience}
- Number of servings: {servings}
- Dietary preferences: {dietary}
- Equipment available: {equipment}

Return:
- A shopping list (ingredients with quantities)
- Step-by-step instructions
- Cooking tips
- Adjustments for dietary preference if possible
- Cooking time and preparation time

Use markdown formatting for headings and sections.
"""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

# Optional: If using image generation
def get_recipe_image(recipe_name):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Generate a realistic image of the dish: {recipe_name}."
    response = model.generate_content(prompt)
    return response.text.strip()  # This may depend on actual response structure (e.g., URL or base64)

def get_recipe_response(user_input):
    prompt = f"You are a helpful cooking assistant. User asked: {user_input}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
