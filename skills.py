import os
import streamlit as st
import plotly.graph_objects as go
from PIL import Image 

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Skills Data
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
            {"name": "DeepLab"},
            {"name": "Mask R-CNN"},
            {"name": "BART"},
            {"name": "T5"},
            {"name": "Stable Diffusion"},
            {"name": "OpenAI Codex"},
            {"name": "Deep Q-Network"},
            {"name": "DALL-E"},
            {"name": "Time Series Forecasting Models"},
            {"name": "Graph Neural Networks"},
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

# Header
st.title("🛠️ Core Skills and Technologies")

# Styling for better presentation
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

# Plotting Functions
def plot_skills(data):
    """Generates a Plotly bar or pie chart based on the provided data."""
    if isinstance(data[0], dict):  # If data contains dictionaries
        fig = go.Figure(data=go.Bar(x=[item['name'] for item in data], 
                                      y=[item['usage'] for item in data]))
        fig.update_layout(title='Skill Usage', xaxis_title='Skills', yaxis_title='Usage (%)')
    else:  # If data is not a dict (Assuming it's a list of strings)
        fig = go.Figure(data=go.Pie(labels=data, values=[1] * len(data)))
        fig.update_layout(title='Skill Distribution')
    return fig

# Define prediction functions
def placeholder_prediction_function(model_name, input_data):
    """Placeholder function for model predictions."""
    return f"{model_name} Prediction for: {input_data[:50]}..."  # Limit output for brevity

# Deep Learning Models Functionality
deep_learning_models = {
    "BERT": {
        "description": "Text classification using BERT.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("BERT", text),
    },
    "GPT-3": {
        "description": "Text generation using GPT-3.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("GPT-3", text),
    },
    "LSTM": {
        "description": "Sequence prediction using LSTM.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("LSTM", text),
    },
    "RNN": {
        "description": "Recurrent Neural Network for sequential data.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("RNN", text),
    },
    "CNN": {
        "description": "Image classification using CNN.",
        "input_type": "image",
        "function": lambda img: placeholder_prediction_function("CNN", "image"),
    },
    "U-Net": {
        "description": "Image segmentation using U-Net.",
        "input_type": "image",
        "function": lambda img: placeholder_prediction_function("U-Net", "image"),
    },
    "ResNet": {
        "description": "Residual Neural Network for image classification.",
        "input_type": "image",
        "function": lambda img: placeholder_prediction_function("ResNet", "image"),
    },
    "YOLO": {
        "description": "Object detection using YOLO.",
        "input_type": "image",
        "function": lambda img: placeholder_prediction_function("YOLO", "image"),
    },
    "GANs": {
        "description": "Generative Adversarial Networks for image generation.",
        "input_type": "image",
        "function": lambda img: placeholder_prediction_function("GANs", "image"),
    },
    "Transformer": {
        "description": "Transformers for various tasks.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("Transformer", text),
    },
    "Time Series Forecasting Models": {
        "description": "Models for forecasting time series data.",
        "input_type": "text",
        "function": lambda text: placeholder_prediction_function("Time Series", text),
    },
    # Add more models as needed...
}

def handle_model_selection():
    """Handles the model selection and user input."""
    selected_model = st.selectbox("Select a Deep Learning Model", list(deep_learning_models.keys()))
    model_info = deep_learning_models[selected_model]

    # Display model description
    st.write(f"**Description**: {model_info['description']}")

    # Input based on model type
    if model_info['input_type'] == 'text':
        input_text = st.text_area("Input Text")
        if st.button("Predict"):
            if input_text.strip():
                output = model_info['function'](input_text)
                st.success(f"Prediction: {output}")
            else:
                st.warning("Please enter some text.")
    elif model_info['input_type'] == 'image':
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image.', use_column_width=True)
                if st.button("Predict"):
                    output = model_info['function'](image)
                    st.success(f"Prediction: {output}")
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")

# Display Skills Categories
for category in skills_data:
    st.markdown(f"<div class='skills-category'><h3>{category['category']}</h3></div>", unsafe_allow_html=True)
    for skill in category['skills']:
        skill_icon = skill.get('icon', None)
        if skill_icon:
            st.markdown(f"<div class='skill-icon'><img src='{skill_icon}' width='50' alt='skill icon'></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='skill-icon'>{skill['name']}</div>", unsafe_allow_html=True)

# Add model handling section
st.markdown("<h3>Deep Learning Model Predictions</h3>", unsafe_allow_html=True)
handle_model_selection()

# Footer
st.markdown("<div class='footer'>Developed by Karim Osman</div>", unsafe_allow_html=True)
