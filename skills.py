import os
import cv2
import librosa
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import torch 


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

# Styling for better presentation with hover effects
st.markdown("""
<style>
    .skills-category {
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        margin: 10px;
        text-align: center;
        background-color: #f9f9f9;
        transition: transform 0.2s, background-color 0.2s; 
        display: flex;
        flex-direction: column;
        align-items: center; 
        justify-content: center; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    }
    .skills-category:hover {
        transform: scale(1.05); 
        background-color: #e6f7ff; 
    }
    .skills-category:active {
        transform: scale(0.95); /* Scale down on click */
    }
    .skills-category h3 {
        margin-bottom: 10px;
        color: #0073e6; /* Header color */
    }
    .skill-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px; /* Increased margin for better spacing */
        transition: transform 0.2s; /* Smooth transition */
    }
    .skill-icon img {
        width: 50px;
        height: 50px;
    }
    .skill-icon:hover {
        transform: scale(1.1); /* Scale up on icon hover */
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)
@st.cache_data
def get_base64_image(image_path):
    """Convert an image to a base64 string."""
    import base64
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
# Display skills with icons in cards
cols = st.columns(len(skills_data))  # Create columns for each category

for col, category in zip(cols, skills_data):
    with col:
        st.markdown(f"<div class='skills-category'><h3>{category['category']}</h3>", unsafe_allow_html=True)
        for skill in category['skills']:
            if 'icon' in skill:  # For skills with icons
                st.markdown(f"<div class='skill-icon'><img src='data:image/svg+xml;base64,{get_base64_image(skill['icon'])}' width='50' height='50' alt='Icon'></div>", unsafe_allow_html=True)
            else:  # For skills without icons
                st.markdown(f"<div class='skill-icon'>{skill['name']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


    
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
    return f"BERT Prediction for: {text_data[:50]}..."  

def your_gpt3_prediction_function(text_data):
    # Placeholder for GPT-3 prediction logic
    return f"GPT-3 Prediction for: {text_data[:50]}..."

def your_lstm_prediction_function(text_data):
    # Placeholder for LSTM prediction logic
    return f"LSTM Prediction for: {text_data[:50]}..."
   
def your_rnn_prediction_function(text_data):
    # Placeholder for RNN prediction logic
  return f"RNN Prediction for: {text_data[:50]}..."  
  
def your_cnn_prediction_function(image):
    # Placeholder for CNN prediction logic
    return "CNN Prediction Result"
@st.cache_data
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

def your_wavenet_prediction_function(sound_data):
    # Convert the sound data (raw bytes) into a waveform using librosa
    audio, sr = librosa.load(sound_data, sr=None)

    # Normalize the audio
    audio = librosa.util.normalize(audio)

    # Convert the audio to PyTorch tensor and add batch dimension
    audio_tensor = torch.tensor(audio, dtype=torch.float32).unsqueeze(0)

    # Forward pass through the WaveNet model
    with torch.no_grad():
        prediction = wavenet_model(audio_tensor)

    # Assuming the model outputs probabilities or logits, you can apply softmax
    probabilities = torch.softmax(prediction, dim=1)

    # Return the predicted class or the output of the model
    return probabilities.argmax().item()

def your_convlstm_prediction_function(video_data):
    # Load video frames using OpenCV
    video = cv2.VideoCapture(video_data)

    frames = []
    success, frame = video.read()
    while success:
        # Resize the frame to match model input (e.g., 224x224)
        frame_resized = cv2.resize(frame, (224, 224))
        
        # Normalize the frame and convert it to a PyTorch tensor
        frame_tensor = torch.tensor(frame_resized, dtype=torch.float32).permute(2, 0, 1)  # HWC to CHW
        frames.append(frame_tensor)
        
        success, frame = video.read()
    
    # Stack frames to create a batch (sequence)
    video_tensor = torch.stack(frames).unsqueeze(0)  # Add batch dimension

    # Forward pass through the ConvLSTM model
    with torch.no_grad():
        prediction = convlstm_model(video_tensor)

    # Assuming the model outputs probabilities, apply softmax
    probabilities = torch.softmax(prediction, dim=1)

    # Return the predicted class or the output of the model
    return probabilities.argmax().item()
  
# Deep Learning Models Functionality
deep_learning_models = {
    "BERT": {
        "description": "Text classification using BERT.",
        "input_type": "text",
        "model": "model_epoch_5.pth",
        "function": your_bert_prediction_function,
    },
    "GPT-3": {
        "description": "Text generation using GPT-3.",
        "input_type": "text",
        "model": "tf_model.h5",
        "function": your_gpt3_prediction_function,
    },
    "LSTM": {
        "description": "Sequence prediction using LSTM.",
        "input_type": "text",
        "model": "SRmodelo_lstm.h5",
        "function": your_lstm_prediction_function,
    },
    "RNN": {
        "description": "Recurrent Neural Network for sequential data.",
        "input_type": "text",
        "model": "rnn_model.h5",
        "function": your_rnn_prediction_function,
    },
    "CNN": {
        "description": "Image classification using CNN.",
        "input_type": "image",
        "model": "CNNModel2.pkl",
        "function": your_cnn_prediction_function,
    },
    "U-Net": {
        "description": "Image segmentation using U-Net.",
        "input_type": "image",
        "model": "UNET_model.keras",
        "function": your_unet_prediction_function,
    },
    "ResNet": {
        "description": "Residual Neural Network for image classification.",
        "input_type": "image",
        "model": "resnet_model.pth",
        "function": your_resnet_prediction_function,
    },
    "VGG16": {
        "description": "VGG16 model for image classification.",
        "input_type": "image",
        "model": "vgg16.pth",
        "function": your_vgg16_prediction_function,
    },
    "EfficientNet": {
        "description": "EfficientNet model for image classification.",
        "input_type": "image",
        "model": "efficientnet_model.bin",
        "function": your_efficientnet_prediction_function,
    },
    "YOLO": {
        "description": "Object detection using YOLO.",
        "input_type": "image",
        "model": "yolov8m.pt",
        "function": your_yolo_prediction_function,
    },
    "GANs": {
        "description": "Generative Adversarial Networks for image generation.",
        "input_type": "image",
        "model": "gans_model.h5",
        "function": your_gan_prediction_function,
    },
    "VAEs": {
        "description": "Variational Autoencoders for image generation.",
        "input_type": "image",
        "model": "VAEsbest_model.pth",
        "function": your_vae_prediction_function,
    },
    "Transformer": {
        "description": "Transformer model for text tasks.",
        "input_type": "text",
        "model": "transformer_model.pth",
        "function": your_transformer_prediction_function,
    },
    "Siamese Networks": {
        "description": "Siamese networks for similarity tasks.",
        "input_type": "text",
        "model": "siamesemodelv2.h5",
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
        "model": "capsule_model.bin",
        "function": your_capsule_network_prediction_function,
    },
    "TGAN": {
        "description": "Temporal GAN for time series data generation.",
        "input_type": "image",
        "model": "tgan.safetensors",
        "function": your_tgan_prediction_function,
    },
    "FastGAN": {
        "description": "FastGAN for quick image generation.",
        "input_type": "image",
        "model": "fastgan_model.bin",
        "function": your_fastgan_prediction_function,
    },
    "WaveNet": {
        "description": "Sound generation using WaveNet.",
        "input_type": "sound",
        "model": "archive/WaveNet_Model/WaveNet_fold4.h5",
        "function": your_wavenet_prediction_function,
    },
    "ConvLSTM": {
        "description": "Video processing using ConvLSTM.",
        "input_type": "video",
        "model": "convlstm_model.h5",
        "function": your_convlstm_prediction_function,
    },
}

# Display deep learning models and handle functionalities

st.header("Deep Learning Models")

for model_name, model_data in deep_learning_models.items():
    st.subheader(model_name)
    st.write(model_data["description"])

    # Handle input based on input type
    if model_data["input_type"] == "text":
        # Text-based models (e.g., BERT, GPT-3)
        uploaded_file = st.file_uploader(f"Upload text file for {model_name}", type=["txt"], key=f"text_uploader_{model_name}")
        if uploaded_file is not None:
            text_data = uploaded_file.read().decode("utf-8")
            result = model_data["function"](text_data)  # Call the model's prediction function
            st.write(f"Prediction Result for {model_name}: {result}")

    elif model_data["input_type"] == "image":
        # Image-based models (e.g., CNN, U-Net)
        uploaded_file = st.file_uploader(f"Upload image file for {model_name}", type=["jpg", "jpeg", "png"], key=f"image_uploader_{model_name}")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            result = model_data["function"](image)  # Call the model's prediction function
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.write(f"Prediction Result for {model_name}: {result}")

    elif model_data["input_type"] == "sound":
        # Sound-based models (e.g., WaveNet)
        uploaded_file = st.file_uploader(f"Upload sound file for {model_name}", type=["wav", "mp3"], key=f"sound_uploader_{model_name}")
        if uploaded_file is not None:
            sound_data = uploaded_file.read()  # Assuming the model handles raw sound data
            result = model_data["function"](sound_data)
            st.write(f"Prediction Result for {model_name}: {result}")

    elif model_data["input_type"] == "video":
        # Video-based models (e.g., ConvLSTM)
        uploaded_file = st.file_uploader(f"Upload video file for {model_name}", type=["mp4", "avi", "mov"], key=f"video_uploader_{model_name}")
        if uploaded_file is not None:
            video_data = uploaded_file.read()  # Assuming the model handles raw video data
            result = model_data["function"](video_data)
            st.video(video_data)
            st.write(f"Prediction Result for {model_name}: {result}")


# Optional: Display plots for each category
st.subheader("Skill Distribution Visualizations")
st.plotly_chart(plot_programming_languages())
st.plotly_chart(plot_ml_frameworks())
st.plotly_chart(plot_deep_learning_models())
st.plotly_chart(plot_big_data_cloud())

# Footer

st.markdown('<div class="footer">© 2024 Karim Osman - Machine Learning Engineer</div>', unsafe_allow_html=True)

