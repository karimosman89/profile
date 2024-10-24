import os
import streamlit as st
import plotly.graph_objects as go

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
        ],
    },
    {
        "category": "Big Data & Cloud Technologies",
        "skills": [
            {"icon": os.path.join(current_dir, "icons", "hadoop.svg")},
            {"icon": os.path.join(current_dir, "icons", "Apache Spark.svg")},
            {"icon": os.path.join(current_dir, "icons", "Dask.svg")},
            {"icon": os.path.join(current_dir, "icons", "hive.svg")},
            {"icon": os.path.join(current_dir, "icons", "flink.svg")},
            {"icon": os.path.join(current_dir, "icons", "apachekafka.svg")},
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

# Skills Grid
for section in skills_data:
    st.markdown(f"<div class='skills-category'><h3>{section['category']}</h3></div>", unsafe_allow_html=True)
    
    # Create a grid layout
    cols = st.columns(4)  # Adjust number of columns as needed
    
    for i, skill in enumerate(section["skills"]):
        col = cols[i % 4]  # Cycle through columns
        if "icon" in skill:
            # Display icon if it exists
            col.image(skill["icon"], width=50, caption="")
        else:
            # Display skill name
            col.markdown(f"<span style='font-weight: bold;'>{skill.get('name', '')}</span>", unsafe_allow_html=True)

    # Display corresponding Plotly graph for each category
    if section["category"] == "Programming Languages":
        st.plotly_chart(plot_programming_languages())
    elif section["category"] == "Machine Learning & Data Science Frameworks":
        st.plotly_chart(plot_ml_frameworks())
    elif section["category"] == "Deep Learning Models":
        st.plotly_chart(plot_deep_learning_models())
    elif section["category"] == "Big Data & Cloud Technologies":
        st.plotly_chart(plot_big_data_cloud())

# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
