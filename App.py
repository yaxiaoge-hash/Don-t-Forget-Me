# Project: Don't Forget Me — Stage 3: Streamlit Web App
# These comments identify learning resources used to understand particular techniques.
# The final app was assembled and adapted for this project.

# Reference: GeeksforGeeks, "A Beginner's Guide to Streamlit"
# https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/
# Creates the web interface, including input boxes, buttons and food lists
import streamlit as st

# Reference: GeeksforGeeks, "Python Program to Find Number of Days Between Two Given Dates"
# https://www.geeksforgeeks.org/python/python-program-to-find-number-of-days-between-two-given-dates/ 
# Works with dates, such as getting today's date and calculating expiry dates
from datetime import date

# Reference: Python documentation, "json — JSON encoder and decoder"
# https://docs.python.org/3/library/json.html
# Reads food records from foods.json and saves updated records to the file
import json

# Reference: Python documentation, "os.path"
# https://docs.python.org/3/library/os.path.html
# Checks whether files exist and helps find the correct file path
import os


# Reference: Streamlit documentation, st.image()
# https://docs.streamlit.io/develop/api-reference/media/st.image
# Display the app title and fridge image
st.title("Don't Forget Me")
st.image("fridge.png", width=350)


# Reference: Python documentation, os.path
# https://docs.python.org/3/library/os.path.html
# Build a path to foods.json in the same folder as this app.py file.
DATA_FILE = os.path.join(os.path.dirname(__file__), "foods.json")


# Reference: Python documentation, json module
# https://docs.python.org/3/library/json.html
# Load previously saved food records when the app starts
if "foods" not in st.session_state:
    
    # Check whether a saved food file already exists
    if os.path.exists(DATA_FILE):


        # Open the file and read the saved food records
        with open(DATA_FILE, "r") as file:
            saved_foods = json.load(file)
            
        # Restore the saved records to the app's food list
        # Convert each expiry date from text back into a date object
        st.session_state.foods = [
            {
                "name": food["name"],
                "expiry": date.fromisoformat(food["expiry"])
            }
            for food in saved_foods
        ]
        
    # Start with an empty list if no saved file exists
    else:
        st.session_state.foods = []

# Reference: Python documentation, json module
# https://docs.python.org/3/library/json.html
# Save changes so updated food records can be loaded next time
def save_foods():
    
    # Create a temporary list to prepare the food records for saving
    saved_foods = []
    
    # Process each food item in the current list
    for food in st.session_state.foods:
        
        # Store the food name and convert its expiry date into text
        saved_foods.append({
            "name": food["name"],
            "expiry": food["expiry"].isoformat()
        })
        
    # Open the JSON file in write mode to update the saved records
    with open(DATA_FILE, "w") as file:
        
        # Write the food records to the file in a readable format
        json.dump(saved_foods, file, indent=4)
        

# Reference: Streamlit documentation, st.info()
# https://docs.streamlit.io/develop/api-reference/status/st.info
# Reference: Streamlit documentation, st.write()
# https://docs.streamlit.io/develop/api-reference/write-magic/st.write
# Show brief instructions and examples of supported food names.
st.info("How to Use: Enter a food name, select the expiry date, and click Add Food.")
st.write("Food lists: milk, egg, apple, banana, bread, leftover, fish.")


# Reference: laxmimerit, Streamlit Tutorials, text-input example
# https://github.com/laxmimerit/streamlit-tutorials/blob/main/02_working_with_text_inputs.py
# Reference: Streamlit Input Widgets documentation
# https://docs.streamlit.io/develop/api-reference/widgets
# Create a text box and a date picker for user input.
food_name = st.text_input("Food name")
expiry_date = st.date_input("Expiry date")

# Get today's date
today = date.today()

# Calculate the days left until the selected expiry date
days_left = (expiry_date - today).days

# Reference: Streamlit documentation, st.button()
# https://docs.streamlit.io/develop/api-reference/widgets/st.button
# Add the food when the user clicks the button
if st.button("Add Food"):
    st.session_state.foods.append({
        "name": food_name,
        "expiry": expiry_date
    })
    save_foods()
    
# Display the food list heading
st.subheader("My Food List")

# Go through each food item in the saved list
for i, food in enumerate(st.session_state.foods):
    
    # Calculate the days left for this food item
    remaining = (food["expiry"] - date.today()).days

# Reference: GeeksforGeeks, "Python Dictionary"
# https://www.geeksforgeeks.org/python/python-dictionary/    
# Match each food name with its image file
    images = {
        "milk": "milk.png",
        "egg": "egg.png",
        "apple": "apple.png",
        "banana": "banana.png",
        "leftover":"leftover.png",
        "fish":"fish.png",
        "bread":"bread.png"
    }
    
# Remove extra spaces and convert the name to lowercase
    name = food["name"].strip().lower()

# Reference: GeeksforGeeks – Python Conditional Statements
# https://www.geeksforgeeks.org/python/conditional-statements-in-python/
# Check the remaining days and set the food status
    if remaining < 0:
        status = "🔴 Expired"
    elif remaining == 0:
        status = "🟠 Expires Today"
    elif remaining <= 3:
        status = "🟡 Expiring Soon"
    else:
        status = "🟢 Still Fresh"
# Reference: Streamlit documentation, st.columns()
# https://docs.streamlit.io/develop/api-reference/layout/st.columns        
# Add a divider between food items
    st.divider()
    
# Create three columns for the image, details and delete button
    col1, col2, col3 = st.columns([1, 3, 1])
    
# Reference: Streamlit documentation, st.image()
# https://docs.streamlit.io/develop/api-reference/media/st.image
# Show the food image in the first column
    with col1:
        if name in images:
            st.image(images[name], width=90)
            
# Reference: Streamlit documentation, st.write()
# https://docs.streamlit.io/develop/api-reference/write-magic/st.write
# Show the food name, status and remaining days in the second column
    with col2:
        st.subheader(food["name"])
        st.write(status)
        st.write("Days left:", remaining)

# Reference: Streamlit documentation – st.button()
# Link:https://docs.streamlit.io/develop/api-reference/widgets/st.button
# When Delete is clicked, remove the selected record, save, and refresh.
    with col3:
        if st.button("Delete", key=i):
            
            # Remove the selected food from the list
            st.session_state.foods.pop(i)
            
            # Save the updated list
            save_foods()
            
             # Refresh the app to show the updated list
            st.rerun()
