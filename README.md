# Don't Forget Me

## Project Overview

Don't Forget Me is a food expiry date tracking application developed using Python and Streamlit.

The purpose of this project is to help users manage food in their refrigerators, keep track of expiry dates, and reduce unnecessary food waste.

## Features

- Add food items and select their expiry dates.
- Automatically calculate the number of days remaining before food expires.
- Display different expiry status indicators.
- Show images of common food items.
- Delete food items from the list.
- Save food information using a JSON file.

## How It Works

Users enter a food name and select an expiry date. After clicking "Add Food", the application displays the food item with its expiry status.

The application uses four different indicators:

- 🟢 Still Fresh
- 🟡 Expiring Soon
- 🟠 Expires Today
- 🔴 Expired

## Technologies Used

- Python
- Streamlit
- JSON
- GitHub

## How to Run

1. Download or clone this GitHub repository.

2. Install Python on your computer.

3. Open Terminal in the project folder.

4. Install the required libraries:

pip install -r requirements.txt

5. Start the application:

python3 -m streamlit run App.py

6. The application will open in a web browser.

## Data Storage

The application uses a JSON file called foods.json to save food names and expiry dates.

When the app starts, it loads previously saved food records if the file exists. When food items are added or deleted, the updated records are saved to the file.

This allows users to keep their food records when they restart the application.

## Project Development

The project was developed in different stages, starting with basic Python programming and progressing to loops, conditional statements, and an interactive application.

The repository includes earlier Python exercises and the final application.

## Project Goal

The goal of Don't Forget Me is to demonstrate how Python programming can be used to create a practical application that addresses an everyday problem.

## Room for Improvement

The current version of Don't Forget Me focuses on basic food expiry tracking. There are several areas that could be improved in the future.

More food types: Add more food names and images to support different kinds of food.

Input validation: Check that users enter a food name before adding a new item.

Editing food records: Allow users to change a food name or expiry date after adding it.

## Acknowledgements

I used learning resources and official documentation to develop my understanding of Python and Streamlit.

LinkedIn Learning: Used to learn basic Python programming.

Streamlit Documentation: Used to understand Streamlit components and build the app interface.

GeeksforGeeks: Consulted for learning about date calculations in Python.

The final application was developed and tested as part of my Creative Coding project.
