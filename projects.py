import os
import streamlit as st
from PIL import Image

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Project Data
projects = [
    {
        "title": "NLP with Transformers",
        "description": "Developed advanced text classification models utilizing BERT for sentiment analysis and topic classification.",
        "link": "https://github.com/karimosman89/NLP-with-Transformers",
        "image": os.path.join(current_dir, "images", "background5.jpg"),
    },
    {
        "title": "Time Series Forecasting",
        "description": "Designed robust forecasting models employing LSTM, ARIMA, and Prophet to predict stock prices.",
        "link": "https://github.com/karimosman89/time-series",
        "image": os.path.join(current_dir, "images", "background9.jpg"),
    },
    {
        "title": "End-to-End ML Pipeline on AWS",
        "description": "Engineered a scalable ML pipeline for customer churn prediction utilizing AWS services and CI/CD methodologies.",
        "link": "https://github.com/karimosman89/ML-Pipeline-AWS",
        "image": os.path.join(current_dir, "images", "background10.jpg"),
    },
    {
        "title": "Real-Time Data Pipeline",
        "description": "Architected a high-performance ETL pipeline for processing streaming log data using Apache Kafka and Spark.",
        "link": "https://github.com/karimosman89/Data-Pipeline",
        "image": os.path.join(current_dir, "images", "background15.jpg"),
    },
]

# Header
st.title("🏆 Notable Projects")
st.write("Explore some of the projects I've worked on, demonstrating my skills in Machine Learning, AI, and Data Engineering.")

# CSS for 3D effect and hover animations
st.markdown("""
   <style>
    .project-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        margin: 20px;
        width: 300px;
        transform-style: preserve-3d;
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
        text-align: center;
    }
    .project-card:hover {
        transform: scale(1.05) rotateX(5deg) rotateY(5deg);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
    }
    .project-title {
        color: #333333;
        font-size: 1.2em;
        font-weight: bold;
        margin: 10px 0;
    }
    .project-description {
        color: #555555;
        font-size: 1em;
        margin: 0 15px 15px 15px;
    }
    .project-link {
        color: #ffffff;
        background-color: #4CAF50;
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        transition: background-color 0.3s ease;
    }
    .project-link:hover {
        background-color: #45a049;
    }
   </style>
""", unsafe_allow_html=True)

# Display Projects
for project in projects:
    with st.container():
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        
        # Load and display the image
        if os.path.exists(project["image"]):
            st.image(Image.open(project["image"]), use_column_width=True)
        else:
            st.write("Image not found.")
        
        st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
        st.markdown(f"<a href='{project['link']}' class='project-link' target='_blank'>View Project</a>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)



# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
