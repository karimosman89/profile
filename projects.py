import os
import streamlit as st

# Get the directory of the current script
current_dir = os.path.dirname(__file__)
def display():
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

 # Styling for better presentation
 st.markdown("""
   <style>
    .project-card {
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.3s;
    }
    .project-card:hover {
        transform: scale(1.02);
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
            st.image(project["image"], caption=project["title"], use_column_width=True)  # Display project image
        
        with col2:
            st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='project-description'>{project['description']}</div>", unsafe_allow_html=True)
            st.markdown(f"[View Project]({project['link']})", unsafe_allow_html=True)  # Link to GitHub project
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close the card

# Footer
 st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
