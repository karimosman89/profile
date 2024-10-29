import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import logging
import about
import projects
import skills
import contact
import resume

st.set_page_config(page_title="Karim Osman - ML Engineer Portfolio", layout="wide")

logging.basicConfig(level=logging.INFO)

@st.cache_resource
def load_lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_resource
def load_profile_photo():
    return Image.open("profile-photo.jpg")

# Load Lottie animations
data_analysis_animation = load_lottie_local('data-analyisis.json')
data_engineer_animation = load_lottie_local('data-engineer.json')
ai_engineering_animation = load_lottie_local('ai-engineering.json')
ai_animation = load_lottie_local('ai.json')
deep_learning_animation = load_lottie_local('devops.json')
dev_ops_animation = load_lottie_local('deep-learning.json')  
profile_photo = load_profile_photo()


# Streamlit app title and description

st.title("🌍 Welcome to My Portfolio!")
st.write("I’m **Karim Osman**, a passionate **Machine Learning Engineer** dedicated to solving real-world challenges through data-driven models and algorithms.")

def load_page(module_name):
    try:
        module = importlib.import_module(module_name)
        module.display()  # Assumes each module has a `display` function
    except AttributeError as e:
        st.error(f"Error loading {module_name}: {e}")
    except ImportError as e:
        st.error(f"Module {module_name} not found: {e}")


# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Skills", "Contact", "Resume"])

# Common styling          
def set_style():
    st.markdown("""
    <style>
        body {
            font-family: 'Helvetica Neue', sans-serif;
        }
        .main {
            background-color: #f5f5f5;
            padding: 2rem;
        }
        h1, h2, h4 {
            font-weight: 700;
            color: #003366;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 2.5rem;
        }
        h2 {
            color: #007ACC;
            margin-bottom: 10px;
        }
        .profile-photo {
            border-radius: 70%;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            display: block;
            width: 50px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            color: #999;
            font-size: 0.9rem;
        }
        .button {
            background-color: #007ACC;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 20px 2px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #005999;
        }
        .lottie-animation {
            max-width: 120px;
            margin: 0 auto;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()  # Apply styles

# Functions to create Plotly graphs
@st.cache_data
def plot_ml_graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines+markers', name='Model A'))
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9], mode='lines+markers', name='Model B'))
    fig.update_layout(title='Model Performance Comparison', xaxis_title='Epoch', yaxis_title='Accuracy')
    return fig

def plot_data_engineer_graph():
    fig = go.Figure(data=[go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr'], y=[10, 15, 13, 17])])
    fig.update_layout(title='Data Pipeline Throughput', xaxis_title='Month', yaxis_title='Records Processed')
    return fig

def plot_data_scientist_graph():
    fig = go.Figure(data=go.Pie(labels=['Category A', 'Category B', 'Category C'], values=[4500, 2500, 1050]))
    fig.update_layout(title='Data Distribution by Category')
    return fig

def plot_ai_engineer_graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Model A', 'Model B', 'Model C'], y=[80, 90, 70], mode='markers', marker=dict(size=[15, 20, 25]), name='AI Models'))
    fig.update_layout(title='AI Model Performance', xaxis_title='Model', yaxis_title='F1 Score')
    return fig

def plot_dl_engineer_graph():
    fig = go.Figure(data=[go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], mode='lines+markers')])
    fig.update_layout(title='Deep Learning Model Loss Over Time', xaxis_title='Epoch', yaxis_title='Loss')
    return fig

def plot_devops_graph():
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4], y=[3, 2, 5, 4], mode='lines+markers')])
    fig.update_layout(title='Deployment Frequency', xaxis_title='Week', yaxis_title='Deployments')
    return fig

# Define common business scenarios and their graphs

def get_business_scenarios():
    return {
    "Machine Learning Engineer": {
        "Customer Churn Prediction": {
            "description": "Predicting customer churn using historical data to enhance retention strategies.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Model A', 'Model B'], y=[70, 85])]).update_layout(title='Churn Prediction Accuracy', xaxis_title='Model', yaxis_title='Accuracy (%)')
        },
        "Sales Forecasting": {
            "description": "Utilizing sales data to predict future sales and optimize inventory.",
            "graph": lambda: go.Figure(data=[go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr'], y=[100, 150, 120, 180], mode='lines+markers')]).update_layout(title='Sales Forecast', xaxis_title='Month', yaxis_title='Sales ($)')
        }
    },
    "Data Engineer": {
        "ETL Pipeline Efficiency": {
            "description": "Analyzing the efficiency of ETL processes in transforming and loading data.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['ETL Job 1', 'ETL Job 2'], y=[30, 50])]).update_layout(title='ETL Job Processing Time', xaxis_title='ETL Job', yaxis_title='Time (minutes)') # type: ignore
        },
        "Data Quality Metrics": {
            "description": "Monitoring data quality metrics over time to ensure integrity and reliability.",
            "graph": lambda: go.Figure(data=[go.Scatter(x=['Week 1', 'Week 2', 'Week 3'], y=[95, 85, 90], mode='lines+markers')]).update_layout(title='Data Quality Metrics', xaxis_title='Week', yaxis_title='Quality (%)')
        }
    },
    "Data Scientist": {
        "Market Basket Analysis": {
            "description": "Analyzing customer purchase data to find associations between products.",
            "graph": lambda: go.Figure(data=[go.Pie(labels=['Product A', 'Product B', 'Product C'], values=[4500, 2500, 1050])]).update_layout(title='Market Basket Analysis')
        },
        "A/B Testing Results": {
            "description": "Evaluating the effectiveness of marketing strategies through A/B testing.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Group A', 'Group B'], y=[0.5, 0.7])]).update_layout(title='A/B Test Conversion Rate', xaxis_title='Group', yaxis_title='Conversion Rate (%)')
        }
    },
    "AI Engineer": {
        "Model Deployment Performance": {
            "description": "Assessing the performance of deployed AI models in a production environment.",
            "graph": lambda: go.Figure(data=[go.Scatter(x=['Model A', 'Model B'], y=[0.9, 0.85], mode='lines+markers')]).update_layout(title='AI Model Performance', xaxis_title='Model', yaxis_title='Performance (F1 Score)')
        },
         "User Interaction Metrics": {
            "description": "Monitoring user interactions with AI applications to improve user experience.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Week 1', 'Week 2'], y=[200, 250])]).update_layout(title='User Interaction Over Time', xaxis_title='Week', yaxis_title='Interactions')
        }
    },
    "Deep Learning Engineer": {
        "Training Time Comparison": {
            "description": "Comparing training times of various deep learning models to optimize resource usage.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Model A', 'Model B'], y=[50, 30])]).update_layout(title='Training Time Comparison', xaxis_title='Model', yaxis_title='Time (hours)')
        },
        "Validation Loss Analysis": {
            "description": "Analyzing validation loss to prevent overfitting during training.",
            "graph": lambda: go.Figure(data=[go.Scatter(x=[1, 2, 3, 4], y=[0.5, 0.3, 0.1, 0.05], mode='lines+markers')]).update_layout(title='Validation Loss Over Epochs', xaxis_title='Epoch', yaxis_title='Loss')
        }
    },
    "DevOps Engineer": {
        "Infrastructure Cost Analysis": {
            "description": "Analyzing costs associated with cloud infrastructure usage.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Month 1', 'Month 2'], y=[1000, 1200])]).update_layout(title='Infrastructure Costs Over Time', xaxis_title='Month', yaxis_title='Cost ($)')
        },
        "Deployment Success Rate": {
            "description": "Tracking the success rate of deployments to improve processes.",
            "graph": lambda: go.Figure(data=[go.Bar(x=['Successful', 'Failed'], y=[90, 10])]).update_layout(title='Deployment Success Rate', xaxis_title='Status', yaxis_title='Percentage (%)')
        }
    }
}
business_scenarios = get_business_scenarios()
# Render pages based on the selection
if page == "Home":
    # Content for Home
    logging.info("Displaying Home Page")
    st.markdown("<h2>Explore My Expertise</h2>", unsafe_allow_html=True)

    # Create columns for animations
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    animations = [
        (data_analysis_animation, "Machine Learning Engineer"),
        (data_engineer_animation, "Data Engineer"),
        (ai_engineering_animation, "Data Scientist"),
        (ai_animation, "AI Engineer"),
        (deep_learning_animation, "Deep Learning Engineer"),
        (dev_ops_animation, "DevOps Engineer")
    ]

    for col, (animation, title) in zip([col1, col2, col3, col4, col5, col6], animations):
        with col:
            st_lottie(animation, height=80, width=80,key=title)
            st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)

    # Profile Photo Section
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    image = Image.open("profile-photo.jpg")
    # Display the profile photo with custom styling
    st.image(image, caption=' Karim Osman', use_column_width=False,width=100)
    st.write("""
        As a Machine Learning Engineer, I specialize in building intelligent systems that help businesses make better decisions. 
        My expertise spans various domains including machine learning, AI engineering, and data science. I’m driven by my passion for turning data into actionable insights.
    """)
    
    

    # Role Examples Section
    st.markdown("<h2>Role Examples</h2>", unsafe_allow_html=True)

    role_descriptions = {
        "Machine Learning Engineer": (
            "As a **Machine Learning Engineer**, I specialize in developing predictive models that address complex business challenges. "
            "My expertise lies in analyzing vast datasets to extract meaningful insights, which inform strategic decision-making. "
            "I leverage a variety of machine learning algorithms, including supervised and unsupervised learning techniques, to build robust models that not only predict outcomes but also adapt over time. "
            "My proficiency in tools like TensorFlow and Scikit-learn enables me to implement solutions that enhance efficiency and drive innovation."
        ),
        "Data Engineer": (
            "In the role of a **Data Engineer**, I design and build comprehensive data pipelines that facilitate the ingestion and transformation of data from diverse sources. "
            "My approach involves optimizing data flow and ensuring data integrity to support analytics and machine learning initiatives. "
            "By utilizing technologies such as Apache Kafka, Spark, and various database systems (SQL and NoSQL), I ensure that data is accessible, reliable, and structured, enabling teams to derive actionable insights and make data-driven decisions."
        ),
        "Data Scientist": (
            "As a **Data Scientist**, I apply statistical analysis and machine learning techniques to transform raw data into strategic insights. "
            "I utilize data visualization tools like Tableau and Matplotlib to present findings in an easily digestible format for stakeholders. "
            "My experience includes conducting exploratory data analysis, feature engineering, and model evaluation, ensuring that the insights provided are both actionable and aligned with business objectives. "
            "My goal is to turn complex data sets into stories that drive impactful decisions."
        ),
        "AI Engineer": (
            "In my capacity as an **AI Engineer**, I develop and deploy AI models and algorithms that enable machines to perform tasks intelligently. "
            "I work with deep learning frameworks such as Keras and PyTorch to build systems that mimic human cognitive functions, including natural language processing and computer vision. "
            "My projects focus on creating scalable solutions that enhance user experiences and streamline operations, positioning businesses at the forefront of technological advancements."
        ),
        "Deep Learning Engineer": (
            "As a **Deep Learning Engineer**, my focus is on harnessing the power of advanced neural networks to tackle complex problems. "
            "I specialize in designing architectures that improve model accuracy and efficiency, particularly in applications involving image recognition, speech processing, and reinforcement learning. "
            "My work involves rigorous experimentation and tuning to achieve optimal results, ensuring that the models I develop are both effective and scalable for real-world applications."
        ),
        "DevOps Engineer": (
            "As a **DevOps Engineer**, I bridge the gap between development and operations by implementing practices that streamline application deployment and management. "
            "My expertise includes managing infrastructure as code (IaC) with tools like Docker and Kubernetes, which enhance scalability and reliability. "
            "I advocate for continuous integration and delivery (CI/CD) practices to ensure rapid and safe software releases, enabling teams to respond quickly to changing business needs."
        ),
    }

    for role, description in role_descriptions.items():
        st.markdown(f"<h4>{role}</h4>", unsafe_allow_html=True)
        st.write(description)
        
        # Display business scenarios for each role
        if role in business_scenarios:
            for scenario, details in business_scenarios[role].items():
                st.markdown(f"### {scenario}")
                st.write(details["description"])
                st.plotly_chart(details["graph"]())

        st.markdown("---")  # Add a horizontal line for separation

    # Footer
    
    st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)

elif page == "Skills":
    logging.info("Loading Skills Page")
    load_page("skills")

elif page == "Projects":
     logging.info("Loading Projects Page")
     load_page("projects")  

elif page == "About":
     logging.info("Loading About Page")
    load_page("about")  

elif page == "Contact":
     logging.info("Loading Contact Page")
      load_page("contact")

elif page == "Resume":
     logging.info("Loading Resume Page")
     load_page("resume")
