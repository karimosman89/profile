import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import pandas as pd
import numpy as np
from utils import tr 
import cv2
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Enhanced Skills Data with proficiency levels and business impact
skills_data = [
    {
        "category": tr("SKILLS_PROGRAMMING_LANGUAGES_CATEGORY"),
        "description": tr("SKILLS_PROGRAMMING_LANGUAGES_DESC"),
        "skills": [
            {"name": "Python", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "python.svg")},
            {"name": "R", "proficiency": 80, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "R.svg")},
            {"name": "Java", "proficiency": 75, "years": 5, "projects": 12, "icon": os.path.join(current_dir, "icons", "java.svg")},
            {"name": "C++", "proficiency": 70, "years": 3, "projects": 8, "icon": os.path.join(current_dir, "icons", "CPlusPlus.svg")},
            {"name": "SQL", "proficiency": 90, "years": 6, "projects": 35, "icon": os.path.join(current_dir, "icons", "sql-azure.svg")},
            {"name": "JavaScript", "proficiency": 85, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "javascript.svg")},
        ]
    },
    {
        "category": tr("SKILLS_ML_FRAMEWORKS_CATEGORY"),
        "description": tr("SKILLS_ML_FRAMEWORKS_DESC"),
        "skills": [
            {"name": "TensorFlow", "proficiency": 90, "years": 7, "projects": 40, "icon": os.path.join(current_dir, "icons", "tensorflow.svg")},
            {"name": "PyTorch", "proficiency": 88, "years": 6, "projects": 30, "icon": os.path.join(current_dir, "icons", "pytorch.svg")},
            {"name": "Scikit-learn", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "scikitlearn.svg")},
            {"name": "Keras", "proficiency": 92, "years": 6, "projects": 35, "icon": os.path.join(current_dir, "icons", "keras.svg")},
            {"name": "XGBoost/LightGBM", "proficiency": 87, "years": 5, "projects": 25, "icon": os.path.join(current_dir, "icons", "xgboost.svg")},
        ]
    },
    {
        "category": tr("SKILLS_DATA_TOOLS_CATEGORY"),
        "description": tr("SKILLS_DATA_TOOLS_DESC"),
        "skills": [
            {"name": "Pandas", "proficiency": 98, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "pandas.svg")},
            {"name": "NumPy", "proficiency": 97, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "numpy.svg")},
            {"name": "Spark", "proficiency": 85, "years": 5, "projects": 18, "icon": os.path.join(current_dir, "icons", "spark.svg")},
            {"name": "Kafka", "proficiency": 80, "years": 4, "projects": 10, "icon": os.path.join(current_dir, "icons", "kafka.svg")},
            {"name": "Tableau", "proficiency": 75, "years": 3, "projects": 8, "icon": os.path.join(current_dir, "icons", "tableau.svg")},
        ]
    },
    {
        "category": tr("SKILLS_CLOUD_DEVOPS_CATEGORY"),
        "description": tr("SKILLS_CLOUD_DEVOPS_DESC"),
        "skills": [
            {"name": "AWS", "proficiency": 90, "years": 6, "projects": 30, "icon": os.path.join(current_dir, "icons", "aws.svg")},
            {"name": "GCP", "proficiency": 85, "years": 5, "projects": 20, "icon": os.path.join(current_dir, "icons", "gcp.svg")},
            {"name": "Docker", "proficiency": 92, "years": 5, "projects": 25, "icon": os.path.join(current_dir, "icons", "docker.svg")},
            {"name": "Kubernetes", "proficiency": 80, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "kubernetes.svg")},
            {"name": "MLflow", "proficiency": 88, "years": 4, "projects": 12, "icon": os.path.join(current_dir, "icons", "mlflow.svg")},
            {"name": "Git", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "git.svg")},
        ]
    },
    {
        "category": tr("SKILLS_NLP_LLM_CATEGORY"),
        "description": tr("SKILLS_NLP_LLM_DESC"),
        "skills": [
            {"name": "Hugging Face", "proficiency": 90, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "huggingface.svg")},
            {"name": "LangChain", "proficiency": 85, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "langchain.svg")},
            {"name": "Vector DBs", "proficiency": 87, "years": 3, "projects": 15, "icon": os.path.join(current_dir, "icons", "vectordb.svg")},
            {"name": "RAG", "proficiency": 90, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "rag.svg")},
        ]
    }
]

# Cache models for better performance
@st.cache_resource
def load_sentiment_model():
    """Load sentiment analysis model"""
    try:
        return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    except:
        return pipeline("sentiment-analysis")

@st.cache_resource
def load_text_classifier():
    """Load text classification model"""
    try:
        return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    except:
        return None

@st.cache_resource
def load_emotion_model():
    """Load emotion detection model"""
    try:
        return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
    except:
        return None

# Set page style
def set_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        .skills-hero {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .metric-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
        }
        .metric-card h3 {
            color: #4a4a4a;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }
        .metric-card p {
            color: #667eea;
            font-size: 2.2rem;
            font-weight: 700;
        }
        
        .skill-category-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        .skill-category-card h3 {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        .skill-item {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .skill-item img {
            width: 30px;
            height: 30px;
            margin-right: 1rem;
        }
        .skill-item span {
            font-size: 1.1rem;
            color: #333;
        }
        
        .business-value-card {
            background: linear-gradient(145deg, #e6e6fa, #d0b3ff);
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .business-value-card h3 {
            color: #5d3f6a;
            margin-bottom: 1.5rem;
        }
        .business-value-card p {
            font-size: 1.05rem;
            line-height: 1.6;
        }
        
        .interactive-demo {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
            border-left: 5px solid #667eea;
        }
        .interactive-demo h3 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
        
        .demo-result {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 1rem;
            border-left: 4px solid #28a745;
        }
        
        .demo-error {
            background: #f8d7da;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 1rem;
            border-left: 4px solid #dc3545;
            color: #721c24;
        }
        
        .confidence-bar {
            background-color: #e9ecef;
            border-radius: 10px;
            height: 20px;
            margin: 0.5rem 0;
        }
        
        .confidence-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.3s ease;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="skills-hero">
    <h1>{tr('SKILLS_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('SKILLS_HERO_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Skills Overview Metrics
st.markdown(f"## {tr('SKILLS_OVERVIEW_TITLE')}")
col1, col2, col3, col4 = st.columns(4)

total_years = sum(skill['years'] for category in skills_data for skill in category['skills']) / len(skills_data) if skills_data else 0
total_projects = sum(skill['projects'] for category in skills_data for skill in category['skills'])
total_technologies = sum(len(category['skills']) for category in skills_data)
avg_proficiency = np.mean([skill['proficiency'] for category in skills_data for skill in category['skills']])

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_EXPERIENCE')}</h3>
        <p>{total_years:.1f}+</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_PROJECTS')}</h3>
        <p>{total_projects}+</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_TECHNOLOGIES')}</h3>
        <p>{total_technologies}+</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_AVG_PROFICIENCY')}</h3>
        <p>{avg_proficiency:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

# Interactive AI Demos Section
st.markdown("## 🚀 Interactive AI Demonstrations")
st.markdown("**Experience my AI skills in action! Try these live demos to see the quality of solutions I can build.**")

# Demo tabs
demo_tab1, demo_tab2, demo_tab3, demo_tab4 = st.tabs([
    "🧠 Sentiment Analysis", 
    "📝 Text Classification", 
    "😊 Emotion Detection",
    "☁️ Word Cloud Generator"
])

with demo_tab1:
    st.markdown("""
    <div class="interactive-demo">
        <h3>🧠 Advanced Sentiment Analysis</h3>
        <p>This demo uses a state-of-the-art RoBERTa model fine-tuned on Twitter data to analyze sentiment with high accuracy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    sentiment_text = st.text_area(
        "Enter text to analyze sentiment:",
        placeholder="Type your text here... (e.g., 'I love working with AI technologies!')",
        height=100
    )
    
    if st.button("🔍 Analyze Sentiment", key="sentiment_btn"):
        if sentiment_text.strip():
            try:
                with st.spinner("Analyzing sentiment..."):
                    sentiment_model = load_sentiment_model()
                    result = sentiment_model(sentiment_text)
                    
                    sentiment = result[0]['label']
                    confidence = result[0]['score']
                    
                    # Map labels to more readable format
                    sentiment_mapping = {
                        'LABEL_0': 'Negative',
                        'LABEL_1': 'Neutral', 
                        'LABEL_2': 'Positive',
                        'NEGATIVE': 'Negative',
                        'POSITIVE': 'Positive'
                    }
                    
                    readable_sentiment = sentiment_mapping.get(sentiment, sentiment)
                    
                    # Color coding
                    color = "#28a745" if readable_sentiment == "Positive" else "#dc3545" if readable_sentiment == "Negative" else "#ffc107"
                    
                    st.markdown(f"""
                    <div class="demo-result">
                        <h4>Analysis Result:</h4>
                        <p><strong>Sentiment:</strong> <span style="color: {color}; font-weight: bold;">{readable_sentiment}</span></p>
                        <p><strong>Confidence:</strong> {confidence:.2%}</p>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {confidence*100}%; background-color: {color};"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Business application note
                    st.info("💼 **Business Application:** This technology can be used for customer feedback analysis, social media monitoring, and automated content moderation.")
                    
            except Exception as e:
                st.markdown(f"""
                <div class="demo-error">
                    <h4>Error:</h4>
                    <p>Unable to analyze sentiment. This might be due to model loading issues in the demo environment.</p>
                    <p><em>In a production environment, this would work seamlessly with proper model hosting.</em></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to analyze.")

with demo_tab2:
    st.markdown("""
    <div class="interactive-demo">
        <h3>📝 Zero-Shot Text Classification</h3>
        <p>This demo uses BART to classify text into custom categories without prior training on those specific categories.</p>
    </div>
    """, unsafe_allow_html=True)
    
    classification_text = st.text_area(
        "Enter text to classify:",
        placeholder="Type your text here... (e.g., 'I need help with my account billing')",
        height=100,
        key="classification_text"
    )
    
    categories = st.text_input(
        "Enter categories (comma-separated):",
        placeholder="e.g., technical support, billing, sales, general inquiry",
        value="technical support, billing, sales, general inquiry"
    )
    
    if st.button("🏷️ Classify Text", key="classification_btn"):
        if classification_text.strip() and categories.strip():
            try:
                with st.spinner("Classifying text..."):
                    classifier = load_text_classifier()
                    if classifier:
                        category_list = [cat.strip() for cat in categories.split(",")]
                        result = classifier(classification_text, category_list)
                        
                        st.markdown("""
                        <div class="demo-result">
                            <h4>Classification Results:</h4>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for i, (label, score) in enumerate(zip(result['labels'], result['scores'])):
                            color_intensity = int(score * 255)
                            color = f"rgba(102, 126, 234, {score})"
                            
                            st.markdown(f"""
                            <div style="margin: 0.5rem 0;">
                                <p><strong>{i+1}. {label}:</strong> {score:.2%}</p>
                                <div class="confidence-bar">
                                    <div class="confidence-fill" style="width: {score*100}%; background-color: {color};"></div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.info("💼 **Business Application:** Perfect for customer service ticket routing, content categorization, and automated workflow management.")
                    else:
                        st.error("Classification model not available in demo environment.")
                        
            except Exception as e:
                st.markdown(f"""
                <div class="demo-error">
                    <h4>Error:</h4>
                    <p>Unable to classify text. This might be due to model loading issues in the demo environment.</p>
                    <p><em>In a production environment, this would work seamlessly with proper model hosting.</em></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter both text and categories.")

with demo_tab3:
    st.markdown("""
    <div class="interactive-demo">
        <h3>😊 Emotion Detection</h3>
        <p>This demo detects emotions in text using a fine-tuned DistilRoBERTa model trained on emotion datasets.</p>
    </div>
    """, unsafe_allow_html=True)
    
    emotion_text = st.text_area(
        "Enter text to detect emotions:",
        placeholder="Type your text here... (e.g., 'I am so excited about this new project!')",
        height=100,
        key="emotion_text"
    )
    
    if st.button("😊 Detect Emotions", key="emotion_btn"):
        if emotion_text.strip():
            try:
                with st.spinner("Detecting emotions..."):
                    emotion_model = load_emotion_model()
                    if emotion_model:
                        result = emotion_model(emotion_text)
                        
                        # Emotion emoji mapping
                        emotion_emojis = {
                            'joy': '😊',
                            'sadness': '😢',
                            'anger': '😠',
                            'fear': '😨',
                            'surprise': '😲',
                            'disgust': '🤢',
                            'love': '❤️'
                        }
                        
                        st.markdown("""
                        <div class="demo-result">
                            <h4>Emotion Detection Results:</h4>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for emotion_result in result:
                            emotion = emotion_result['label'].lower()
                            score = emotion_result['score']
                            emoji = emotion_emojis.get(emotion, '😐')
                            
                            color = f"rgba(102, 126, 234, {score})"
                            
                            st.markdown(f"""
                            <div style="margin: 0.5rem 0;">
                                <p><strong>{emoji} {emotion.title()}:</strong> {score:.2%}</p>
                                <div class="confidence-bar">
                                    <div class="confidence-fill" style="width: {score*100}%; background-color: {color};"></div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.info("💼 **Business Application:** Useful for mental health applications, customer experience analysis, and personalized content recommendation.")
                    else:
                        st.error("Emotion detection model not available in demo environment.")
                        
            except Exception as e:
                st.markdown(f"""
                <div class="demo-error">
                    <h4>Error:</h4>
                    <p>Unable to detect emotions. This might be due to model loading issues in the demo environment.</p>
                    <p><em>In a production environment, this would work seamlessly with proper model hosting.</em></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to analyze.")

with demo_tab4:
    st.markdown("""
    <div class="interactive-demo">
        <h3>☁️ Word Cloud Generator</h3>
        <p>Generate beautiful word clouds to visualize text data and identify key themes and patterns.</p>
    </div>
    """, unsafe_allow_html=True)
    
    wordcloud_text = st.text_area(
        "Enter text for word cloud:",
        placeholder="Paste a large text here... (e.g., customer reviews, survey responses, etc.)",
        height=150,
        key="wordcloud_text"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        max_words = st.slider("Maximum words:", 50, 200, 100)
    with col2:
        colormap = st.selectbox("Color scheme:", ['viridis', 'plasma', 'inferno', 'magma', 'Blues', 'Reds'])
    
    if st.button("☁️ Generate Word Cloud", key="wordcloud_btn"):
        if wordcloud_text.strip():
            try:
                with st.spinner("Generating word cloud..."):
                    # Create word cloud
                    wordcloud = WordCloud(
                        width=800, 
                        height=400, 
                        background_color='white',
                        max_words=max_words,
                        colormap=colormap,
                        relative_scaling=0.5,
                        random_state=42
                    ).generate(wordcloud_text)
                    
                    # Create matplotlib figure
                    fig, ax = plt.subplots(figsize=(10, 5))
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis('off')
                    
                    # Display the word cloud
                    st.pyplot(fig)
                    
                    # Text analysis
                    blob = TextBlob(wordcloud_text)
                    word_count = len(wordcloud_text.split())
                    sentence_count = len(blob.sentences)
                    
                    st.markdown(f"""
                    <div class="demo-result">
                        <h4>Text Analysis:</h4>
                        <p><strong>Total Words:</strong> {word_count}</p>
                        <p><strong>Sentences:</strong> {sentence_count}</p>
                        <p><strong>Most Frequent Words:</strong> {', '.join([word for word, freq in wordcloud.words_.items()][:5])}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.info("💼 **Business Application:** Perfect for analyzing customer feedback, survey responses, social media mentions, and market research data.")
                    
            except Exception as e:
                st.markdown(f"""
                <div class="demo-error">
                    <h4>Error:</h4>
                    <p>Unable to generate word cloud: {str(e)}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to generate a word cloud.")

# Skills Radar Chart
st.markdown(f"## {tr('SKILLS_RADAR_TITLE')}")
categories = [category['category'] for category in skills_data]
avg_proficiencies = [np.mean([skill['proficiency'] for skill in category['skills']]) for category in skills_data]

fig = go.Figure(data=go.Scatterpolar(
    r=avg_proficiencies,
    theta=categories,
    fill='toself',
    name='Proficiency',
    hovertemplate='<b>%{theta}</b><br>Proficiency: %{r:.1f}%<extra></extra>',
    marker=dict(color='#764ba2'),
    line_color='#667eea',
))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            color='#333',
            linecolor='#555',
            gridcolor='#ccc'
        ),
        angularaxis=dict(
            linecolor='#555',
            gridcolor='#ccc',
            tickfont=dict(size=12, color='#333')
        )
    ),
    showlegend=False,
    height=400,
    margin=dict(l=70, r=70, t=70, b=70),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Inter', color='#333')
)
st.plotly_chart(fig, use_container_width=True)

# Detailed Technical Skills
st.markdown(f"## {tr('SKILLS_DETAILED_TITLE')}")
for category_data in skills_data:
    st.markdown(f"""
    <div class="skill-category-card">
        <h3>{category_data['category']}</h3>
        <p style="color: #666; margin-bottom: 1.5rem;">{category_data['description']}</p>
        <div class="skill-list">
    """, unsafe_allow_html=True)
    
    # Create columns for skills within each category
    cols_per_row = 3
    skill_cols = st.columns(cols_per_row)
    
    for i, skill in enumerate(category_data['skills']):
        with skill_cols[i % cols_per_row]:
            st.markdown(f"""
            <div class="skill-item">
                <span>{skill['name']}</span>
                <div style="flex-grow: 1; margin-left: 1rem; background-color: #eee; border-radius: 5px;">
                    <div style="width: {skill['proficiency']}%; background-color: #667eea; height: 10px; border-radius: 5px;"></div>
                </div>
                <span style="margin-left: 0.5rem; font-weight: bold;">{skill['proficiency']}%</span>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

# Deep Learning & AI Model Expertise
st.markdown(f"## {tr('SKILLS_DL_TITLE')}")
st.markdown(f"<h3>{tr('SKILLS_DL_APPLICATIONS')}</h3>")
st.markdown(f"""
<div class="interactive-demo">
    <ul style="list-style-type: disc; padding-left: 20px;">
        <li>{tr('SKILLS_DL_APP_CV')}</li>
        <li>{tr('SKILLS_DL_APP_NLP')}</li>
        <li>{tr('SKILLS_DL_APP_TSA')}</li>
        <li>{tr('SKILLS_DL_APP_GENAI')}</li>
        <li>{tr('SKILLS_DL_APP_RL')}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# How these skills create business value
st.markdown(f"## {tr('SKILLS_BUSINESS_TITLE')}")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_TIME_TO_MARKET')}</h3>
        <p>{tr('SKILLS_BUSINESS_TIME_TO_MARKET_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_COST')}</h3>
        <p>{tr('SKILLS_BUSINESS_COST_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_ACCURACY')}</h3>
        <p>{tr('SKILLS_BUSINESS_ACCURACY_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_ROBUST')}</h3>
        <p>{tr('SKILLS_BUSINESS_ROBUST_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)

# Continuous Learning and Innovation
st.markdown(f"## {tr('SKILLS_LEARNING_TITLE')}")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="interactive-demo">
        <h3>{tr('SKILLS_EXPLORING_TITLE')}</h3>
        <ul style="list-style-type: disc; padding-left: 20px;">
            <li>{tr('SKILLS_EXPLORING_LLMS')}</li>
            <li>{tr('SKILLS_EXPLORING_MULTIMODAL_AI')}</li>
            <li>{tr('SKILLS_EXPLORING_EDGE_AI')}</li>
            <li>{tr('SKILLS_EXPLORING_AI_SAFETY_ETHICS')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="interactive-demo">
        <h3>{tr('SKILLS_LEARNING_METHOD_TITLE')}</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>📖 <strong>{tr('SKILLS_LEARNING_METHOD_RESEARCH')}</strong> - {tr('SKILLS_LEARNING_METHOD_RESEARCH_DESC')}</li>
            <li>🛠️ <strong>{tr('SKILLS_LEARNING_METHOD_HANDS_ON')}</strong> - {tr('SKILLS_LEARNING_METHOD_HANDS_ON_DESC')}</li>
            <li>🤝 <strong>{tr('SKILLS_LEARNING_METHOD_COMMUNITY')}</strong> - {tr('SKILLS_LEARNING_METHOD_COMMUNITY_DESC')}</li>
            <li>🎓 <strong>{tr('SKILLS_LEARNING_METHOD_EDUCATION')}</strong> - {tr('SKILLS_LEARNING_METHOD_EDUCATION_DESC')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="skills-hero">
    <h2>{tr('SKILLS_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        {tr('SKILLS_CALL_TEXT')}
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        {tr('SKILLS_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('SKILLS_FOOTER')}</p>", unsafe_allow_html=True)

