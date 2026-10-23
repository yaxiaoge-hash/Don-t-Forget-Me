# Import the libraries needed for the app

import streamlit as st # Creates the web interface, including input boxes, buttons and food lists
from datetime import date # Works with dates, such as getting today's date and calculating expiry dates
import json # Reads food records from foods.json and saves updated records to the file
import os # Checks whether files exist and helps find the correct file path

# Display the app title and fridge image
st.title("Don't Forget Me")
st.image("fridge.png", width=350)

# Set the path to the file used to store food records
DATA_FILE = os.path.join(os.path.dirname(__file__), "foods.json")

# Check whether the food list has been created in the current session
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

# Define a function to save the current food list to a JSON file
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
        
# Show users how to use the app
st.info("How to Use: Enter a food name, select the expiry date, and click Add Food.")

# Show examples of supported food names
st.write("Food lists: milk, egg, apple, banana, bread, leftover, fish.")

# Let users enter a food name and choose an expiry date
food_name = st.text_input("Food name")
expiry_date = st.date_input("Expiry date")

# Get today's date
today = date.today()

# Calculate the days left until the selected expiry date
days_left = (expiry_date - today).days

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
    
# Check the remaining days and set the food status
    if remaining < 0:
        status = "🔴 Expired"
    elif remaining == 0:
        status = "🟠 Expires Today"
    elif remaining <= 3:
        status = "🟡 Expiring Soon"
    else:
        status = "🟢 Still Fresh"
        
# Add a divider between food items
    st.divider()
    
# Create three columns for the image, details and delete button
    col1, col2, col3 = st.columns([1, 3, 1])
    
# Show the food image in the first column
    with col1:
        if name in images:
            st.image(images[name], width=90)
            
# Show the food name, status and remaining days in the second column
    with col2:
        st.subheader(food["name"])
        st.write(status)
        st.write("Days left:", remaining)
        
# Show a delete button in the third column
    with col3:
        if st.button("Delete", key=i):
            
            # Remove the selected food from the list
            st.session_state.foods.pop(i)
            
            # Save the updated list
            save_foods()
            
             # Refresh the app to show the updated list
            st.rerun()
