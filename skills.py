import os
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Skills Data (Paths to icon files)
skills_data = [
    {
        "category": "Programming Languages",
        "skills": [
            {"icon": os.path.join(current_dir, "icons", "python.svg")},
            {"icon": os.path.join(current_dir, "icons", "R.svg")},
            {"icon": os.path.join(current_dir, "icons", "java.svg")},
            {"icon": os.path.join(current_dir, "icons", "CPlusPlus.svg")},
            {"icon": os.path.join(current_dir, "icons", "csharp.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Groovy.svg")},
            {"icon": os.path.join(current_dir, "icons", "sql-azure.svg")},
            {"icon": os.path.join(current_dir, "icons", "javascript.svg")},
            {"icon": os.path.join(current_dir, "icons", "PHP.svg")},
            {"icon": os.path.join(current_dir, "icons", "Bash.svg")},
            {"icon": os.path.join(current_dir, "icons", "Go.svg")},
        ],
    },
    {
        "category": "Machine Learning & Data Science Frameworks",
        "skills": [
            {"icon": os.path.join(current_dir, "icons", "scikit-learn.svg")},
            {"icon": os.path.join(current_dir, "icons", "XGBoost.svg")},
            {"icon": os.path.join(current_dir, "icons", "LightGBM.svg")},
            {"icon": os.path.join(current_dir, "icons", "CatBoost.svg")},
            {"icon": os.path.join(current_dir, "icons", "tensorflow.svg")},
            {"icon": os.path.join(current_dir, "icons", "Keras.svg")},
            {"icon": os.path.join(current_dir, "icons", "pytorch.svg")},
            {"icon": os.path.join(current_dir, "icons", "mxnet.svg")},
            {"icon": os.path.join(current_dir, "icons", "coffee.svg")},
            {"icon": os.path.join(current_dir, "icons", "pandas.svg")},
            {"icon": os.path.join(current_dir, "icons", "numpy.svg")},
            {"icon": os.path.join(current_dir, "icons", "SciPy.svg")},
            {"icon": os.path.join(current_dir, "icons", "statsmodels.svg")},
            {"icon": os.path.join(current_dir, "icons", "tableau.svg")},
            {"icon": os.path.join(current_dir, "icons", "Matplotlib.svg")},
            {"icon": os.path.join(current_dir, "icons", "seaborn.svg")},
            {"icon": os.path.join(current_dir, "icons", "Ploty.svg")},
            {"icon": os.path.join(current_dir, "icons", "bokeh.svg")},
        ],
    },
    {
        "category": "Deep Learning Models",
        "skills": [
            {"name": "BERT"},
            {"name": "GPT-3"},
            {"name": "LSTM"},
            {"name": "RNN"},
            {"name": "CNN"},
            {"name": "U-Net"},
            {"name": "ResNet"},
            {"name": "VGG16"},
            {"name": "EfficientNet"},
            {"name": "YOLO"},
            {"name": "GANs"},
            {"name": "VAEs"},
            {"name": "Transformer"},
            {"name": "Siamese Networks"},
            {"name": "Deep Reinforcement Learning"},
            {"name": "Capsule Networks"},
            {"name": "TGAN"},
            {"name": "FastGAN"},
        ],
    },
    {
        "category": "Big Data & Cloud Technologies",
        "skills": [
            {"icon": os.path.join(current_dir, "icons", "hadoop.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Spark.svg")},
            {"icon": os.path.join(current_dir, "icons", "Dask.svg")},
            {"icon": os.path.join(current_dir, "icons", "Hive.svg")},
            {"icon": os.path.join(current_dir, "icons", "flink.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Kafka.svg")},
            {"icon": os.path.join(current_dir, "icons", "aws.svg")},
            {"icon": os.path.join(current_dir, "icons", "gcp.svg")},
            {"icon": os.path.join(current_dir, "icons", "azure.svg")},
            {"icon": os.path.join(current_dir, "icons", "Docker.svg")},
            {"icon": os.path.join(current_dir, "icons", "kubernetes.svg")},
            {"icon": os.path.join(current_dir, "icons", "MLflow.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Airflow.svg")},
            {"icon": os.path.join(current_dir, "icons", "kubeflow.svg")},
            {"icon": os.path.join(current_dir, "icons", "postgresql.svg")},
            {"icon": os.path.join(current_dir, "icons", "mysql.svg")},
            {"icon": os.path.join(current_dir, "icons", "mongodb.svg")},
            {"icon": os.path.join(current_dir, "icons", "dbs-redis.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Cassandra.svg")},
            {"icon": os.path.join(current_dir, "icons", "Redshift.svg")},
            {"icon": os.path.join(current_dir, "icons", "bigquery.svg")},
            {"icon": os.path.join(current_dir, "icons", "snowflake.svg")},
            {"icon": os.path.join(current_dir, "icons", "talend.svg")},
            {"icon": os.path.join(current_dir, "icons", "nifi.svg")},
        ],
    },
]

# Header Section
st.title("🛠️ Core Skills and Technologies")

# Custom CSS for styling
st.markdown("""
<style>
    .skills-category {
        padding: 10px;
        border-bottom: 1px solid #ccc;
    }
    .skills-category h3 {
        margin-bottom: 10px;
    }
    .skill-icon {
        display: inline-block;
        margin: 5px;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Plot Functions for Skill Distribution
def plot_programming_languages():
    languages = ["Python", "R", "Java", "C++", "C#", "Groovy", "SQL", "JavaScript", "PHP", "Bash", "Go"]
    usage = [50, 10, 15, 20, 25, 10, 30, 35, 20, 15, 5]  # Hypothetical usage percentages
    fig = go.Figure(data=go.Bar(x=languages, y=usage))
    fig.update_layout(title='Programming Languages Usage', xaxis_title='Languages', yaxis_title='Usage (%)')
    return fig

def plot_ml_frameworks():
    frameworks = ["Scikit-learn", "XGBoost", "LightGBM", "CatBoost", "TensorFlow", "Keras", "PyTorch", "MXNet"]
    popularity = [30, 20, 15, 10, 25, 20, 35, 10]  # Hypothetical popularity percentages
    fig = go.Figure(data=go.Pie(labels=frameworks, values=popularity))
    fig.update_layout(title='Machine Learning Frameworks Popularity')
    return fig

def plot_deep_learning_models():
    models = ["BERT", "GPT-3", "LSTM", "CNN", "ResNet", "YOLO"]
    applications = [25, 35, 15, 20, 25, 10]  # Hypothetical application areas
    fig = go.Figure(data=go.Scatter(x=models, y=applications, mode='markers', marker=dict(size=15), text=models))
    fig.update_layout(title='Deep Learning Models Applications', xaxis_title='Models', yaxis_title='Application Areas')
    return fig

def plot_big_data_cloud():
    technologies = ["Hadoop", "Spark", "AWS", "GCP", "Azure"]
    usage = [50, 70, 60, 55, 45]  # Hypothetical usage percentages
    fig = go.Figure(data=go.Bar(x=technologies, y=usage))
    fig.update_layout(title='Big Data & Cloud Technologies Usage', xaxis_title='Technologies', yaxis_title='Usage (%)')
    return fig

# Functions for Deep Learning Models
deep_learning_models = {
    "BERT": {
        "description": "Text classification using BERT.",
        "input_type": "text",
        "function": lambda text_data: f"BERT Prediction for: {text_data[:50]}...",
    },
    "GPT-3": {
        "description": "Text generation using GPT-3.",
        "input_type": "text",
        "function": lambda text_data: f"GPT-3 Generated Text: {text_data[:50]}...",
    },
    "CNN": {
        "description": "Image classification using CNN.",
        "input_type": "image",
        "function": lambda image_data: f"CNN Image Classification Result",
    },
    # Add more models and their configurations as needed
}

# Render Categories and Skills
for category in skills_data:
    st.markdown(f'<div class="skills-category"><h3>{category["category"]}</h3>', unsafe_allow_html=True)
    for skill in category["skills"]:
        if "icon" in skill:
            icon_path = skill["icon"]
            img = Image.open(icon_path)
            st.image(img, width=50, caption=os.path.basename(icon_path).split(".")[0], use_column_width=False)
        elif "name" in skill:
            st.write(f"- {skill['name']}")
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar: Model Demos
st.sidebar.title("Deep Learning Model Demos")
selected_model = st.sidebar.selectbox("Choose a model", options=deep_learning_models.keys())

# Get selected model details
model_info = deep_learning_models[selected_model]
st.sidebar.write(f"**Model:** {selected_model}")
st.sidebar.write(f"**Description:** {model_info['description']}")

# Input uploader with unique keys to avoid StreamlitDuplicateElementId
if model_info["input_type"] == "text":
    user_input = st.sidebar.text_area("Enter text for prediction", key=f"text_{selected_model}")
    if st.sidebar.button("Run Prediction", key=f"run_text_{selected_model}"):
        prediction = model_info["function"](user_input)
        st.sidebar.write(prediction)
elif model_info["input_type"] == "image":
    uploaded_image = st.sidebar.file_uploader("Upload an image", type=["jpg", "png"], key=f"image_{selected_model}")
    if uploaded_image and st.sidebar.button("Run Image Classification", key=f"run_image_{selected_model}"):
        prediction = model_info["function"](uploaded_image)
        st.sidebar.write(prediction)

# Footer
st.markdown('<div class="footer">Core Skills and Technologies Demo</div>', unsafe_allow_html=True)
