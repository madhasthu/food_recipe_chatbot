import streamlit as st
from chatbot import get_recipe_with_details, get_recipe_image

st.set_page_config(page_title="🍽️ Recipe Chatbot", layout="wide")
st.title("👨‍🍳 Food Recipe Chatbot")
st.markdown("Welcome! Ask me for any recipe, and I'll help you cook something delicious!")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Inputs
with st.form("recipe_form"):
    recipe_name = st.text_input("🍽️ What would you like to cook today?")
    experience = st.selectbox("👩‍🍳 Your cooking experience level:", ["Beginner", "Intermediate", "Advanced"])
    servings = st.number_input("🍛 How many servings?", min_value=1, max_value=20, step=1, value=2)
    dietary = st.text_input("🌱 Dietary preferences (e.g., vegetarian, vegan, gluten-free):", "")
    equipment = st.text_input("🍳 Available equipment (e.g., oven, grill, skillet):", "")
    generate_button = st.form_submit_button("Get Recipe")

# Generate Recipe
if generate_button and recipe_name:
    with st.spinner("🍳 Generating your personalized recipe..."):
        recipe_text = get_recipe_with_details(recipe_name, experience, servings, dietary, equipment)
        st.session_state.chat_history.append((recipe_name, recipe_text))

        st.markdown("### 📜 Recipe Instructions")
        st.markdown(recipe_text)

    # Generate image
    with st.spinner("🖼️ Looking for a recipe image..."):
        image_url = get_recipe_image(recipe_name)

        # If a valid URL is returned (basic check), display the image
        if image_url and image_url.startswith("http"):
            st.markdown("### 📷 Here's how it might look:")
            try:
                st.image(image_url, caption=recipe_name, use_container_width=True)
            except:
                pass  # Silently fail if image can't be shown
        else:
            pass  # Don't show anything if the image isn't usable

# Chat history
if st.session_state.chat_history:
    st.markdown("## 🧾 Chat History")
    for user_query, response in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {user_query}")
        st.markdown(f"**ChefBot:** {response}")
