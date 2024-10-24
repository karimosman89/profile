import os
import streamlit as st
import plotly.graph_objects as go
from PIL import Image  # Import PIL for image handling

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

# Functions to create Plotly graphs for each skill category
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

# Define deep learning model functionalities
def your_bert_prediction_function(text_data):
    # Placeholder for BERT prediction logic
    return f"BERT Prediction for: {text_data[:50]}..."  # Limit output for brevity

def your_gpt3_prediction_function(text_data):
    # Placeholder for GPT-3 prediction logic
    return f"GPT-3 Prediction for: {text_data[:50]}..."

def your_lstm_prediction_function(text_data):
    # Placeholder for LSTM prediction logic
    return f"LSTM Prediction for: {text_data[:50]}..."

def your_cnn_prediction_function(image):
    # Placeholder for CNN prediction logic
    return "CNN Prediction Result"

def your_unet_prediction_function(image):
    # Placeholder for U-Net prediction logic
    return "U-Net Prediction Result"

def your_resnet_prediction_function(image):
    # Placeholder for ResNet prediction logic
    return "ResNet Prediction Result"

def your_vgg16_prediction_function(image):
    # Placeholder for VGG16 prediction logic
    return "VGG16 Prediction Result"

def your_efficientnet_prediction_function(image):
    # Placeholder for EfficientNet prediction logic
    return "EfficientNet Prediction Result"

def your_yolo_prediction_function(image):
    # Placeholder for YOLO prediction logic
    return "YOLO Prediction Result"

def your_gan_prediction_function(image):
    # Placeholder for GAN prediction logic
    return "GAN Prediction Result"

def your_vae_prediction_function(image):
    # Placeholder for VAE prediction logic
    return "VAE Prediction Result"

def your_transformer_prediction_function(text_data):
    # Placeholder for Transformer prediction logic
    return f"Transformer Prediction for: {text_data[:50]}..."

def your_siamese_prediction_function(text_data):
    # Placeholder for Siamese Networks prediction logic
    return f"Siamese Networks Prediction for: {text_data[:50]}..."

def your_deep_reinforcement_learning_prediction_function(text_data):
    # Placeholder for Deep Reinforcement Learning prediction logic
    return f"Deep Reinforcement Learning Prediction for: {text_data[:50]}..."

def your_capsule_network_prediction_function(image):
    # Placeholder for Capsule Networks prediction logic
    return "Capsule Network Prediction Result"

def your_tgan_prediction_function(image):
    # Placeholder for TGAN prediction logic
    return "TGAN Prediction Result"

def your_fastgan_prediction_function(image):
    # Placeholder for FastGAN prediction logic
    return "FastGAN Prediction Result"

# Deep Learning Models Functionality
deep_learning_models = {
    "BERT": {
        "description": "Text classification using BERT.",
        "input_type": "text",
        "model": "path_to_your_bert_model",
        "function": your_bert_prediction_function,
    },
    "GPT-3": {
        "description": "Text generation using GPT-3.",
        "input_type": "text",
        "model": "path_to_your_gpt3_model",
        "function": your_gpt3_prediction_function,
    },
    "LSTM": {
        "description": "Sequence prediction using LSTM.",
        "input_type": "text",
        "model": "path_to_your_lstm_model",
        "function": your_lstm_prediction_function,
    },
    "RNN": {
        "description": "Recurrent Neural Network for sequential data.",
        "input_type": "text",
        "model": "path_to_your_rnn_model",
        "function": your_lstm_prediction_function,
    },
    "CNN": {
        "description": "Image classification using CNN.",
        "input_type": "image",
        "model": "path_to_your_cnn_model",
        "function": your_cnn_prediction_function,
    },
    "U-Net": {
        "description": "Image segmentation using U-Net.",
        "input_type": "image",
        "model": "path_to_your_unet_model",
        "function": your_unet_prediction_function,
    },
    "ResNet": {
        "description": "Residual Neural Network for image classification.",
        "input_type": "image",
        "model": "path_to_your_resnet_model",
        "function": your_resnet_prediction_function,
    },
    "VGG16": {
        "description": "VGG16 model for image classification.",
        "input_type": "image",
        "model": "path_to_your_vgg16_model",
        "function": your_vgg16_prediction_function,
    },
    "EfficientNet": {
        "description": "EfficientNet model for image classification.",
        "input_type": "image",
        "model": "path_to_your_efficientnet_model",
        "function": your_efficientnet_prediction_function,
    },
    "YOLO": {
        "description": "Object detection using YOLO.",
        "input_type": "image",
        "model": "path_to_your_yolo_model",
        "function": your_yolo_prediction_function,
    },
    "GANs": {
        "description": "Generative Adversarial Networks for image generation.",
        "input_type": "image",
        "model": "path_to_your_gans_model",
        "function": your_gan_prediction_function,
    },
    "VAEs": {
        "description": "Variational Autoencoders for image generation.",
        "input_type": "image",
        "model": "path_to_your_vaes_model",
        "function": your_vae_prediction_function,
    },
    "Transformer": {
        "description": "Transformer model for text tasks.",
        "input_type": "text",
        "model": "path_to_your_transformer_model",
        "function": your_transformer_prediction_function,
    },
    "Siamese Networks": {
        "description": "Siamese networks for similarity tasks.",
        "input_type": "text",
        "model": "path_to_your_siamese_model",
        "function": your_siamese_prediction_function,
    },
    "Deep Reinforcement Learning": {
        "description": "Deep reinforcement learning for decision making.",
        "input_type": "text",
        "model": "path_to_your_drl_model",
        "function": your_deep_reinforcement_learning_prediction_function,
    },
    "Capsule Networks": {
        "description": "Capsule networks for image classification.",
        "input_type": "image",
        "model": "path_to_your_capsule_model",
        "function": your_capsule_network_prediction_function,
    },
    "TGAN": {
        "description": "Temporal GAN for time series data generation.",
        "input_type": "image",
        "model": "path_to_your_tgan_model",
        "function": your_tgan_prediction_function,
    },
    "FastGAN": {
        "description": "FastGAN for quick image generation.",
        "input_type": "image",
        "model": "path_to_your_fastgan_model",
        "function": your_fastgan_prediction_function,
    },
}

# Display skills and functionalities
for section in skills_data:
    st.markdown(f"<h3 class='skills-category'>{section['category']}</h3>", unsafe_allow_html=True)

    # Display icons for skills
    if section["category"] == "Programming Languages" or section["category"] == "Machine Learning & Data Science Frameworks" or section["category"] == "Big Data & Cloud Technologies":
        cols = st.columns(len(section["skills"]))
        for i, skill in enumerate(section["skills"]):
            cols[i].image(skill["icon"], width=50)  # Adjust width as necessary

    # Handle Deep Learning Models
    if section["category"] == "Deep Learning Models":
        for model in deep_learning_models:
            st.subheader(model)
            st.write(deep_learning_models[model]["description"])

            # Upload input data
            if deep_learning_models[model]["input_type"] == "text":
                uploaded_file = st.file_uploader("Upload your text file", type=["txt"])
            elif deep_learning_models[model]["input_type"] == "image":
                uploaded_file = st.file_uploader("Upload your image file", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:
                if deep_learning_models[model]["input_type"] == "text":
                    text_data = uploaded_file.read().decode("utf-8")
                    result = deep_learning_models[model]["function"](text_data)
                    st.write("Prediction Result:", result)
                elif deep_learning_models[model]["input_type"] == "image":
                    image = Image.open(uploaded_file)
                    result = deep_learning_models[model]["function"](image)
                    st.image(image, caption="Uploaded Image", use_column_width=True)
                    st.write("Prediction Result:", result)

# Optional: Display plots for each category
st.subheader("Skill Distribution Visualizations")
st.plotly_chart(plot_programming_languages())
st.plotly_chart(plot_ml_frameworks())
st.plotly_chart(plot_deep_learning_models())
st.plotly_chart(plot_big_data_cloud())

# Footer
st.markdown("<div class='footer'>Developed by Karim Osman</div>", unsafe_allow_html=True)
