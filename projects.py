import os
import streamlit as st

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

# Styling for 3D effect and hover animations
st.markdown("""
   <style>
    /* Container for project cards */
    .project-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }

    /* Project card styling */
    .project-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        margin: 20px;
        width: 300px;
        transform-style: preserve-3d;
        transition: transform 0.5s, box-shadow 0.5s;
        cursor: pointer;
    }
    .project-card:hover {
        transform: scale(1.05) rotateX(8deg) rotateY(8deg);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
    }

    /* Image styling */
    .project-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }

    /* Project title and description styling */
    .project-title {
        color: #333333;
        font-size: 1.5em;
        font-weight: bold;
        margin: 15px;
        text-align: center;
    }
    .project-description {
        color: #555555;
        font-size: 1em;
        margin: 0 15px 15px 15px;
        text-align: center;
    }

    /* Button styling */
    .project-link {
        display: inline-block;
        text-align: center;
        color: #ffffff;
        background-color: #4CAF50;
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 5px;
        text-decoration: none;
        transition: background-color 0.3s ease-in-out;
    }
    .project-link:hover {
        background-color: #45a049;
    }
   </style>
""", unsafe_allow_html=True)

# Display Projects
st.markdown("<div class='project-container'>", unsafe_allow_html=True)
for project in projects:
    st.markdown(f"""
        <div class='project-card'>
            <img src='data:image/jpeg;base64,{st.file_uploader(project["image"])}' class='project-image' alt='{project["title"]}'>
            <div class='project-title'>{project["title"]}</div>
            <div class='project-description'>{project["description"]}</div>
            <div style='text-align: center;'>
                <a href='{project["link"]}' class='project-link' target='_blank'>View Project</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
