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

# CSS for 3D card hover effect
st.markdown("""
   <style>
    .project-card {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        margin: 15px;
        padding: 20px;
        width: 100%;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        transform-style: preserve-3d;
        perspective: 1000px;
    }
    .project-card:hover {
        transform: scale(1.03) rotateX(8deg) rotateY(-8deg);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
    }
    .project-title {
        color: #333333;
        font-weight: bold;
        font-size: 1.3em;
        margin-top: 10px;
    }
    .project-description {
        color: #666666;
        font-size: 0.95em;
        margin: 10px 0 20px;
    }
    .project-link {
        color: #ffffff;
        background-color: #4CAF50;
        padding: 8px 12px;
        border-radius: 5px;
        text-decoration: none;
        font-size: 0.9em;
        transition: background-color 0.3s ease;
    }
    .project-link:hover {
        background-color: #45a049;
    }
   </style>
""", unsafe_allow_html=True)

# Display Projects in a 2-column grid layout
columns_per_row = 2
for i, project in enumerate(projects):
    if i % columns_per_row == 0:
        cols = st.columns(columns_per_row)
    
    # Display each project as a card within its column
    with cols[i % columns_per_row]:
        st.markdown("<div class='project-card project-card:hover'>", unsafe_allow_html=True)
        
        # Load and display the image with fixed size
        if os.path.exists(project["image"]):
            st.image(Image.open(project["image"]), use_column_width=False, width=220)  # Set image size here
        
        st.markdown(f"<div class='project-title project-card:hover'>{project['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-description project-card:hover'>{project['description']}</div>", unsafe_allow_html=True)
        st.markdown(f"<a href='{project['link']}' class='project-link project-card:hover' target='_blank'>View Project</a>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)



# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
