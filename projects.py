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

# CSS for interactive and 3D card styling
st.markdown("""
   <style>
    .project-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
        margin: 20px;
        padding: 20px;
        transition: transform 0.4s, box-shadow 0.4s;
        perspective: 1000px;
        text-align: center;
    }
    .project-card:hover {
        transform: scale(1.05) rotateX(10deg) rotateY(10deg);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
    }
    .project-image {
        border-radius: 8px;
        margin-bottom: 15px;
        transition: box-shadow 0.3s ease;
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    .project-title {
        color: #333333;
        font-weight: bold;
        font-size: 1.4em;
        margin-top: 15px;
    }
    .project-description {
        color: #555555;
        font-size: 1em;
        margin: 15px 0;
    }
    .project-link {
        color: #ffffff;
        background-color: #4CAF50;
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        font-size: 1em;
        transition: background-color 0.3s;
    }
    .project-link:hover {
        background-color: #3e8e41;
    }
   </style>
""", unsafe_allow_html=True)

# Display each project as a card with animations and 3D effects
for project in projects:
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    
    # Display project image with a consistent, fixed size
    if os.path.exists(project["image"]):
        st.image(Image.open(project["image"]), use_column_width=False, width=300, caption=project["title"], output_format="JPEG")
    
    # Project information in styled card layout
    st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
    st.markdown(f"<a href='{project['link']}' class='project-link' target='_blank'>View Project</a>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)



# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
