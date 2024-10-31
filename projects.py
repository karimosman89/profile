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
        "image": os.path.join(current_dir, "images", "background5.jpg"),  # Use JPG or PNG
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

# CSS for modern styling
st.markdown("""
   <style>
    body {
        background-color: #f4f4f4; /* Soft background color */
        font-family: 'Arial', sans-serif; /* Modern font */
    }
    .project-card {
        background-color: #ffffff; /* Card background color */
        border-radius: 10px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        margin: 20px auto; /* Centered margins */
        padding: 20px;
        transition: transform 0.4s, box-shadow 0.4s;
        perspective: 1000px;
        text-align: center;
        max-width: 400px; /* Max width for the cards */
    }
    .project-card:hover {
        transform: scale(1.05) rotateX(5deg) rotateY(5deg); /* Subtle 3D effect */
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    .project-image {
        border-radius: 8px;
        margin-bottom: 15px;
        width: 100%;
        height: auto; /* Responsive height */
        object-fit: cover;
    }
    .project-title {
        color: #333333; /* Dark gray for the title */
        font-weight: bold;
        font-size: 1.5em; /* Slightly larger title */
        margin-top: 15px;
    }
    .project-description {
        color: #666666; /* Medium gray for description */
        font-size: 1em;
        margin: 15px 0;
    }
    .project-link {
        color: #ffffff;
        background-color: #4CAF50; /* Green link button */
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        font-size: 1em;
        transition: background-color 0.3s;
    }
    .project-link:hover {
        background-color: #45a049; /* Darker green on hover */
    }
   </style>
""", unsafe_allow_html=True)

# Display each project as a card with animations and 3D effects
for project in projects:
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    
    # Check if the image file exists
    if os.path.exists(project["image"]):
        # Open and resize the image
        image = Image.open(project["image"])
        # Resize the image to a smaller width (e.g., 300 pixels)
        image.thumbnail((300, 300))  # Maintain aspect ratio
        st.image(image, caption=project["title"], use_column_width=True)  # Display resized image
    
    # Project information in styled card layout
    st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
    st.markdown(f"<a href='{project['link']}' class='project-link' target='_blank'>View Project</a>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p class='footer' style='text-align: center; color: #666;'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
