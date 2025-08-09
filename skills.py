import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import json
import random
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

def show_skills():
    st.title("🧠 Technical Skills & AI Demonstrations")
    st.markdown("---")

    # Skills Overview Dashboard
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("AI/ML Projects", "15+", "3 this month")

    with col2:
        st.metric("Programming Languages", "8+", "Always learning")

    with col3:
        st.metric("Years Experience", "5+", "Growing daily")

    with col4:
        st.metric("Certifications", "12+", "2 recent")

    st.markdown("---")

    # Interactive Skills Categories
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🤖 AI/ML Live Demos", 
        "💻 Programming Skills", 
        "📊 Data Science", 
        "🔧 Tools & Frameworks",
        "🏆 Certifications"
    ])

    with tab1:
        show_ai_ml_demos()

    with tab2:
        show_programming_skills()

    with tab3:
        show_data_science_skills()

    with tab4:
        show_tools_frameworks()

    with tab5:
        show_certifications()

def show_ai_ml_demos():
    """Interactive AI/ML demonstrations"""
    st.header("🤖 Live AI/ML Demonstrations")
    st.write("Experience my AI/ML skills through interactive demonstrations:")

    # Demo selection
    demo_type = st.selectbox(
        "Choose a demonstration:",
        ["Classification Model Demo", "Regression Analysis", "Data Preprocessing Pipeline", "Model Comparison"]
    )

    if demo_type == "Classification Model Demo":
        st.subheader("🎯 Real-time Classification Model")

        # Model parameters
        col1, col2 = st.columns(2)
        with col1:
            n_samples = st.slider("Number of samples", 100, 1000, 500)
            n_features = st.slider("Number of features", 2, 10, 4)

        with col2:
            n_classes = st.slider("Number of classes", 2, 5, 3)
            test_size = st.slider("Test size (%)", 10, 40, 20) / 100

        if st.button("Generate & Train Model", type="primary"):
            # Generate synthetic dataset
            X, y = make_classification(
                n_samples=n_samples, 
                n_features=n_features, 
                n_classes=n_classes,
                n_redundant=0,
                random_state=42
            )

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

            # Train model with progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            status_text.text('Initializing model...')
            progress_bar.progress(25)
            time.sleep(0.5)

            # Train Random Forest
            rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
            status_text.text('Training Random Forest...')
            progress_bar.progress(50)

            rf_model.fit(X_train, y_train)
            progress_bar.progress(75)

            # Make predictions
            status_text.text('Making predictions...')
            y_pred = rf_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            progress_bar.progress(100)
            status_text.text('Model training complete!')

            # Display results
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Model Accuracy", f"{accuracy:.3f}", f"{(accuracy-0.5)*100:.1f}% above random")

                # Feature importance
                if n_features <= 6:  # Only show for reasonable number of features
                    importance_df = pd.DataFrame({
                        'Feature': [f'Feature_{i+1}' for i in range(n_features)],
                        'Importance': rf_model.feature_importances_
                    }).sort_values('Importance', ascending=True)

                    fig = px.bar(importance_df, x='Importance', y='Feature', orientation='h',
                                title="Feature Importance", color='Importance',
                                color_continuous_scale='viridis')
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Confusion matrix visualization (for reasonable number of classes)
                if n_classes <= 4:
                    from sklearn.metrics import confusion_matrix
                    cm = confusion_matrix(y_test, y_pred)

                    fig = px.imshow(cm, text_auto=True, aspect="auto",
                                   title="Confusion Matrix",
                                   labels=dict(x="Predicted", y="Actual"))
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("Confusion matrix hidden for clarity with >4 classes")

            # Model insights
            st.subheader("🔍 Model Insights")
            insights = [
                f"✅ Trained on {len(X_train)} samples with {n_features} features",
                f"✅ Achieved {accuracy:.1%} accuracy on test set",
                f"✅ Used Random Forest with 100 decision trees",
                f"✅ Model complexity: {n_features} inputs → {n_classes} class predictions"
            ]

            for insight in insights:
                st.write(insight)

    elif demo_type == "Regression Analysis":
        st.subheader("📈 Real-time Regression Analysis")

        # Parameters
        col1, col2 = st.columns(2)
        with col1:
            n_samples = st.slider("Dataset size", 100, 500, 200, key="reg_samples")
            noise = st.slider("Noise level", 0.1, 2.0, 0.5, key="reg_noise")

        with col2:
            n_features = st.slider("Number of features", 1, 5, 2, key="reg_features")
            model_type = st.selectbox("Model type", ["Linear Regression", "Random Forest"])

        if st.button("Generate & Analyze", type="primary", key="reg_button"):
            # Generate regression data
            X, y = make_regression(n_samples=n_samples, n_features=n_features, 
                                 noise=noise*10, random_state=42)

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            if model_type == "Linear Regression":
                model = LinearRegression()
            else:
                model = RandomForestRegressor(n_estimators=50, random_state=42)

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            # Visualizations
            col1, col2 = st.columns(2)

            with col1:
                st.metric("R² Score", f"{r2:.3f}", "Higher is better")

                # Actual vs Predicted scatter plot
                fig = px.scatter(x=y_test, y=y_pred, 
                               title="Actual vs Predicted Values",
                               labels={'x': 'Actual Values', 'y': 'Predicted Values'})

                # Add perfect prediction line
                min_val, max_val = min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())
                fig.add_traces(px.line(x=[min_val, max_val], y=[min_val, max_val]).data)
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Residuals plot
                residuals = y_test - y_pred
                fig = px.scatter(x=y_pred, y=residuals,
                               title="Residuals Plot",
                               labels={'x': 'Predicted Values', 'y': 'Residuals'})
                fig.add_hline(y=0, line_dash="dash", line_color="red")
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)

            # Model summary
            st.subheader("📊 Analysis Summary")
            summary_cols = st.columns(3)

            with summary_cols[0]:
                st.metric("Training Samples", len(X_train))
                st.metric("Test Samples", len(X_test))

            with summary_cols[1]:
                st.metric("Model Type", model_type)
                st.metric("Features Used", n_features)

            with summary_cols[2]:
                st.metric("Mean Absolute Error", f"{np.mean(np.abs(residuals)):.2f}")
                st.metric("Prediction Quality", "Excellent" if r2 > 0.8 else "Good" if r2 > 0.6 else "Fair")

def show_programming_skills():
    """Programming skills with interactive code examples"""
    st.header("💻 Programming Skills Portfolio")

    # Programming languages radar chart
    languages = ['Python', 'JavaScript', 'SQL', 'R', 'Java', 'C++', 'HTML/CSS', 'Bash']
    proficiency = [95, 80, 90, 75, 70, 65, 85, 80]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=proficiency,
        theta=languages,
        fill='toself',
        name='Proficiency Level',
        line_color='rgb(32, 201, 151)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Programming Languages Proficiency",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # Interactive code examples
    st.subheader("🔧 Interactive Code Demonstrations")

    code_category = st.selectbox(
        "Select a programming concept:",
        ["Data Structures", "Algorithms", "Web APIs", "Database Operations", "Machine Learning Code"]
    )

    if code_category == "Data Structures":
        st.subheader("📚 Advanced Data Structures Implementation")

        with st.expander("🌳 Binary Search Tree Implementation"):
            st.code(""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert value into BST with O(log n) average complexity"""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def search(self, val):
        """Search for value with O(log n) complexity"""
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node is not None

        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
            """, language='python')

        with st.expander("🔍 Hash Table with Collision Resolution"):
            st.code("""
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Simple hash function using modulo"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert with chaining collision resolution"""
        index = self._hash(key)
        bucket = self.table[index]

        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair
        bucket.append((key, value))

    def get(self, key):
        """Retrieve value by key with O(1) average complexity"""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(f"Key '{key}' not found")
            """, language='python')

def show_data_science_skills():
    """Data Science skills with interactive visualizations"""
    st.header("📊 Data Science & Analytics Portfolio")

    # Skills heatmap
    skills_data = {
        'Skill': ['Data Cleaning', 'EDA', 'Statistical Analysis', 'ML Modeling', 
                 'Feature Engineering', 'Data Visualization', 'A/B Testing', 'Time Series'],
        'Proficiency': [95, 90, 85, 90, 88, 92, 80, 75],
        'Experience (Years)': [4, 4, 3, 4, 3, 4, 2, 2],
        'Projects': [15, 15, 10, 12, 10, 15, 5, 3]
    }

    df = pd.DataFrame(skills_data)

    # Interactive skills visualization
    viz_type = st.selectbox("Choose visualization:", ["Skills Radar", "Experience Timeline", "Interactive Demo"])

    if viz_type == "Skills Radar":
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=df['Proficiency'],
            theta=df['Skill'],
            fill='toself',
            name='Proficiency',
            line_color='rgb(255, 99, 71)'
        ))

        fig.add_trace(go.Scatterpolar(
            r=[x*20 for x in df['Experience (Years)']],  # Scale for visibility
            theta=df['Skill'],
            fill='toself',
            name='Experience (scaled)',
            line_color='rgb(32, 201, 151)',
            opacity=0.6
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Data Science Skills Profile"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Interactive Demo":
        st.subheader("🔬 Live Data Analysis Demo")

        # Generate sample dataset
        np.random.seed(42)
        n_samples = st.slider("Dataset size", 100, 1000, 500)

        # Create synthetic business dataset
        data = {
            'customer_id': range(1, n_samples + 1),
            'age': np.random.normal(35, 12, n_samples).astype(int),
            'income': np.random.lognormal(10.5, 0.5, n_samples).astype(int),
            'spending_score': np.random.randint(1, 101, n_samples),
            'purchase_amount': np.random.exponential(50, n_samples),
            'days_since_last_purchase': np.random.exponential(30, n_samples).astype(int),
            'is_premium': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
        }

        df_demo = pd.DataFrame(data)

        # Add derived features (feature engineering demo)
        df_demo['income_bracket'] = pd.cut(df_demo['income'], 
                                         bins=[0, 30000, 60000, 100000, float('inf')], 
                                         labels=['Low', 'Medium', 'High', 'Very High'])

        df_demo['customer_lifetime_value'] = (
            df_demo['purchase_amount'] * df_demo['spending_score'] / 
            (df_demo['days_since_last_purchase'] + 1)
        )

        # Data analysis tabs
        analysis_tab1, analysis_tab2, analysis_tab3 = st.tabs([
            "📈 Exploratory Analysis", 
            "🔍 Customer Segmentation", 
            "💰 Business Insights"
        ])

        with analysis_tab1:
            st.subheader("Dataset Overview")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Customers", f"{len(df_demo):,}")
                st.metric("Average Age", f"{df_demo['age'].mean():.1f}")

            with col2:
                st.metric("Premium Customers", f"{df_demo['is_premium'].sum():,}")
                st.metric("Average Income", f"${df_demo['income'].mean():,.0f}")

            with col3:
                st.metric("Avg Spending Score", f"{df_demo['spending_score'].mean():.1f}")
                st.metric("Total Revenue", f"${df_demo['purchase_amount'].sum():,.0f}")

            # Correlation heatmap
            numeric_cols = ['age', 'income', 'spending_score', 'purchase_amount', 'customer_lifetime_value']
            corr_matrix = df_demo[numeric_cols].corr()

            fig = px.imshow(corr_matrix, 
                           text_auto=True, 
                           aspect="auto",
                           title="Feature Correlation Matrix",
                           color_continuous_scale='RdBu')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

def show_tools_frameworks():
    
    st.header("🔧 Tools & Frameworks Expertise")

    # Create comprehensive tools data
    tools_data = {
        'Category': ['Machine Learning', 'Machine Learning', 'Machine Learning', 'Machine Learning',
                    'Data Processing', 'Data Processing', 'Data Processing', 'Data Processing',
                    'Visualization', 'Visualization', 'Visualization',
                    'Cloud & DevOps', 'Cloud & DevOps', 'Cloud & DevOps', 'Cloud & DevOps',
                    'Databases', 'Databases', 'Databases',
                    'Web Development', 'Web Development', 'Web Development'],
        'Tool': ['Scikit-learn', 'TensorFlow', 'PyTorch', 'XGBoost',
                'Pandas', 'NumPy', 'Apache Spark', 'Dask',
                'Plotly', 'Matplotlib', 'Seaborn',
                'AWS', 'Docker', 'Kubernetes', 'Git',
                'PostgreSQL', 'MongoDB', 'Redis',
                'Streamlit', 'Flask', 'FastAPI'],
        'Proficiency': [95, 80, 75, 85,
                       95, 95, 70, 65,
                       90, 90, 85,
                       75, 80, 70, 90,
                       85, 80, 75,
                       95, 85, 80],
        'Years_Experience': [4, 2, 1.5, 3,
                           4, 4, 1, 1,
                           3, 4, 3,
                           2, 2, 1, 4,
                           3, 2, 2,
                           2, 3, 1],
        'Projects_Used': [15, 5, 3, 8,
                         15, 15, 2, 1,
                         12, 12, 10,
                         6, 8, 3, 15,
                         10, 6, 4,
                         8, 10, 4]
    }

    tools_df = pd.DataFrame(tools_data)

    # Interactive tools exploration
    selected_category = st.selectbox(
        "Explore tools by category:",
        ['All Categories'] + list(tools_df['Category'].unique())
    )

    if selected_category != 'All Categories':
        display_df = tools_df[tools_df['Category'] == selected_category]
    else:
        display_df = tools_df

    # Tools proficiency visualization
    fig = px.scatter(display_df, 
                    x='Years_Experience', 
                    y='Proficiency',
                    size='Projects_Used',
                    color='Category',
                    hover_name='Tool',
                    title="Tools & Frameworks: Experience vs Proficiency",
                    labels={'Years_Experience': 'Years of Experience', 
                           'Proficiency': 'Proficiency Level (%)'},
                    size_max=30)

    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

def show_certifications():
    
    st.header("🏆 Professional Certifications & Achievements")

    # Certifications data
    certifications = [
        {
            "title": "AWS Certified Solutions Architect",
            "issuer": "Amazon Web Services",
            "date": "2023",
            "status": "Active",
            "category": "Cloud Computing",
            "description": "Expertise in designing distributed systems on AWS",
            "skills": ["EC2", "S3", "Lambda", "RDS", "VPC"]
        },
        {
            "title": "Google Cloud Professional Data Engineer",
            "issuer": "Google Cloud",
            "date": "2023",
            "status": "Active", 
            "category": "Data Engineering",
            "description": "Design and build data processing systems",
            "skills": ["BigQuery", "Dataflow", "Pub/Sub", "Cloud Storage"]
        },
        {
            "title": "Microsoft Azure AI Engineer Associate",
            "issuer": "Microsoft",
            "date": "2022",
            "status": "Active",
            "category": "Artificial Intelligence",
            "description": "Implement AI solutions using Azure Cognitive Services",
            "skills": ["Azure ML", "Cognitive Services", "Bot Framework"]
        },
        {
            "title": "Certified Analytics Professional (CAP)",
            "issuer": "INFORMS",
            "date": "2022",
            "status": "Active",
            "category": "Data Analytics",
            "description": "End-to-end analytics methodology and best practices",
            "skills": ["Analytics Strategy", "Data Mining", "Model Validation"]
        },
        {
            "title": "TensorFlow Developer Certificate",
            "issuer": "TensorFlow",
            "date": "2021",
            "status": "Active",
            "category": "Machine Learning",
            "description": "Building and training neural network models",
            "skills": ["Neural Networks", "CNN", "RNN", "Computer Vision"]
        }
    ]

    # Display certifications
    for cert in certifications:
        with st.expander(f"🎓 {cert['title']} - {cert['issuer']}"):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.write(f"**Description:** {cert['description']}")
                st.write(f"**Category:** {cert['category']}")
                st.write(f"**Date Earned:** {cert['date']}")
                st.write(f"**Status:** {'✅ ' + cert['status'] if cert['status'] == 'Active' else '⏰ ' + cert['status']}")

                # Skills tags
                st.write("**Key Skills:**")
                skills_html = " ".join([f'<span style="background-color: #f0f2f6; padding: 4px 8px; border-radius: 4px; margin: 2px; display: inline-block;">{skill}</span>' for skill in cert['skills']])
                st.markdown(skills_html, unsafe_allow_html=True)

            with col2:
                # Placeholder for certificate badge/image
                st.info(f"Certificate ID: {cert['issuer'][:3].upper()}-{cert['date']}-{random.randint(1000, 9999)}")

    # Certification statistics
    st.subheader("📊 Certification Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Certifications", len(certifications))

    with col2:
        active_certs = sum(1 for cert in certifications if cert['status'] == 'Active')
        st.metric("Active Certifications", active_certs)

    with col3:
        recent_certs = sum(1 for cert in certifications if int(cert['date']) >= 2022)
        st.metric("Recent (2022+)", recent_certs)

    with col4:
        categories = len(set(cert['category'] for cert in certifications))
        st.metric("Skill Categories", categories)

# Show the main skills page
show_skills()
