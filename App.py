import streamlit as st
from datetime import date
import json
import os

st.title("Don't Forget Me")
st.image("fridge.png", width=350)
DATA_FILE = os.path.join(os.path.dirname(__file__), "foods.json")
if "foods" not in st.session_state:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            saved_foods = json.load(file)

        st.session_state.foods = [
            {
                "name": food["name"],
                "expiry": date.fromisoformat(food["expiry"])
            }
            for food in saved_foods
        ]
    else:
        st.session_state.foods = []


def save_foods():
    saved_foods = []

    for food in st.session_state.foods:
        saved_foods.append({
            "name": food["name"],
            "expiry": food["expiry"].isoformat()
        })

    with open(DATA_FILE, "w") as file:
        json.dump(saved_foods, file, indent=4)
st.info("How to Use: Enter a food name, select the expiry date, and click Add Food.")

st.write("Food lists: milk, egg, apple, banana, bread, leftover, fish.")
food_name = st.text_input("Food name")
expiry_date = st.date_input("Expiry date")

today = date.today()
days_left = (expiry_date - today).days
if st.button("Add Food"):
    st.session_state.foods.append({
        "name": food_name,
        "expiry": expiry_date
    })
    save_foods()
st.subheader("My Food List")

for i, food in enumerate(st.session_state.foods):
    remaining = (food["expiry"] - date.today()).days

    images = {
        "milk": "milk.png",
        "egg": "egg.png",
        "apple": "apple.png",
        "banana": "banana.png",
        "leftover":"leftover.png",
        "fish":"fish.png",
        "bread":"bread.png"
    }

    name = food["name"].strip().lower()

    if remaining < 0:
        status = "🔴 Expired"
    elif remaining == 0:
        status = "🟠 Expires Today"
    elif remaining <= 3:
        status = "🟡 Expiring Soon"
    else:
        status = "🟢 Still Fresh"

    st.divider()

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if name in images:
            st.image(images[name], width=90)

    with col2:
        st.subheader(food["name"])
        st.write(status)
        st.write("Days left:", remaining)

    with col3:
        if st.button("Delete", key=i):
            st.session_state.foods.pop(i)
            save_foods()
            st.rerun()
