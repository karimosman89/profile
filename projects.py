import os
import streamlit as st
from PIL import Image

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Project Data
projects = [
    {
        "title": "NLP with Transformers",
        "description": "Advanced text classification models using BERT for sentiment analysis and topic classification.",
        "link": "https://github.com/karimosman89/NLP-with-Transformers",
        "image": os.path.join(current_dir, "images", "background5.jpg"),
    },
    {
        "title": "Time Series Forecasting",
        "description": "Robust forecasting models employing LSTM, ARIMA, and Prophet for stock prices.",
        "link": "https://github.com/karimosman89/time-series",
        "image": os.path.join(current_dir, "images", "background9.jpg"),
    },
    {
        "title": "End-to-End ML Pipeline on AWS",
        "description": "Scalable ML pipeline for customer churn prediction using AWS and CI/CD.",
        "link": "https://github.com/karimosman89/ML-Pipeline-AWS",
        "image": os.path.join(current_dir, "images", "background10.jpg"),
    },
    {
        "title": "Real-Time Data Pipeline",
        "description": "High-performance ETL pipeline for streaming log data using Apache Kafka and Spark.",
        "link": "https://github.com/karimosman89/Data-Pipeline",
        "image": os.path.join(current_dir, "images", "background15.jpg"),
    },
]

# Header
st.title("🏆 Notable Projects")
st.write("Explore projects demonstrating skills in Machine Learning, AI, and Data Engineering.")

# CSS for Grid Layout, Card Style, and Hover Animation
st.markdown("""
   <style>
    /* Basic styling for the body */
    body {
        font-family: Arial, sans-serif;
    }

    /* Grid container for cards */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        padding: 20px;
        max-width: 1000px;
        margin: 0 auto;
    }

    /* Card styling */
    .project-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        overflow: hidden;
        text-align: center;
        padding: 15px;
    }
    .project-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    /* Card image */
    .project-image {
        width: 100%;
        height: 100px;
        object-fit: cover;
        border-radius: 10px 10px 0 0;
    }

    /* Title styling */
    .project-title {
        font-weight: bold;
        font-size: 1.2em;
        color: #333;
        margin-top: 10px;
    }

    /* Description styling */
    .project-description {
        color: #555;
        font-size: 1em;
        margin: 10px 0;
    }

    /* Link styling */
    .project-link {
        color: #ffffff;
        background-color: #007bff;
        padding: 8px 12px;
        border-radius: 5px;
        text-decoration: none;
        font-size: 0.9em;
        transition: background-color 0.3s;
        display: inline-block;
        margin-top: 10px;
    }
    .project-link:hover {
        background-color: #0056b3;
    }
   </style>
""", unsafe_allow_html=True)

# Display each project as a card within a grid
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

for project in projects:
    # Start each project card container
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)

    # Load and display the project image, resizing if necessary
    if os.path.exists(project["image"]):
        image = Image.open(project["image"])
        image.thumbnail((300, 300))  # Resize image to fit within card
        st.image(image, use_column_width=True, caption=project["title"])

    # Add project title, description, and link with styles applied
    st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
    st.markdown(f"<a href='{project['link']}' class='project-link' target='_blank'>View Project</a>", unsafe_allow_html=True)

    # Close each project card container
    st.markdown("</div>", unsafe_allow_html=True)

# Close the grid container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #666;'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
