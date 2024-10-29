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
        "image": os.path.join(current_dir, "images", "background5.jpg"),  # Ensure this path is correct
    },
    {
        "title": "Time Series Forecasting",
        "description": "Designed robust forecasting models employing LSTM, ARIMA, and Prophet to predict stock prices.",
        "link": "https://github.com/karimosman89/time-series",
        "image": os.path.join(current_dir, "images", "background9.jpg"),  # Ensure this path is correct
    },
    {
        "title": "End-to-End ML Pipeline on AWS",
        "description": "Engineered a scalable ML pipeline for customer churn prediction utilizing AWS services and CI/CD methodologies.",
        "link": "https://github.com/karimosman89/ML-Pipeline-AWS",
        "image": os.path.join(current_dir, "images", "background10.jpg"),  # Ensure this path is correct
    },
    {
        "title": "Real-Time Data Pipeline",
        "description": "Architected a high-performance ETL pipeline for processing streaming log data using Apache Kafka and Spark.",
        "link": "https://github.com/karimosman89/Data-Pipeline",
        "image": os.path.join(current_dir, "images", "background15.jpg"),  # Ensure this path is correct
    },
]

# Header
st.title("🏆 Notable Projects")
st.write("Explore some of the projects I've worked on, demonstrating my skills in Machine Learning, AI, and Data Engineering.")

# Styling for better presentation with 3D effect
st.markdown("""
   <style>
    .project-card {
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.3s, box-shadow 0.3s;
        perspective: 1000px; /* Create a perspective for 3D effect */
        display: inline-block; /* Make cards inline for grid layout */
        width: 300px; /* Set a fixed width for cards */
        height: 400px; /* Set a fixed height for cards */
    }
    .project-card:hover {
        transform: rotateY(10deg) rotateX(10deg) scale(1.05); /* 3D rotation and scaling */
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5); /* Add shadow for depth */
    }
    .project-image {
        width: 100%; /* Make image full width of the card */
        height: 200px; /* Fixed height for images */
        object-fit: cover; /* Cover the area, cropping if necessary */
    }
    .project-title {
        color: #1e1e1e;
        font-weight: bold;
        margin: 10px;
    }
    .project-description {
        color: #555;
        margin: 0 10px 10px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
    }
 </style>
 """, unsafe_allow_html=True)

# Projects Grid
for project in projects:
    with st.container():
        # Create a card-like layout for each project
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])  # Create two columns for layout
        
        with col1:
            # Use a try-except block to handle potential issues loading the image
            try:
                st.image(project["image"], caption=project["title"], use_column_width=True)  # Display project image
            except Exception as e:
                st.warning(f"Could not load image for project: {project['title']}. Error: {e}")  # Handle missing images
        
        with col2:
            st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
            st.markdown(f"[View Project]({project['link']})", unsafe_allow_html=True)  # Link to GitHub project
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close the card

# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
