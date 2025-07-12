import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px

# Enhanced styling for a more modern and engaging look
def set_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        .hero-about {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .story-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
        }
        
        .philosophy-section {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            text-align: center;
        }
        
        .value-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .value-card:hover {
            transform: translateY(-5px);
        }
        
        .timeline-item {
            background: linear-gradient(135deg, #74b9ff, #0984e3);
            color: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            position: relative;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -10px;
            top: 50%;
            transform: translateY(-50%);
            width: 20px;
            height: 20px;
            background: #667eea;
            border-radius: 50%;
        }
        
        h1 {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        h2 {
            color: #2c3e50;
            font-weight: 600;
            margin: 2rem 0 1rem 0;
        }
        
        .quote-section {
            background: #f8f9fa;
            border-left: 5px solid #667eea;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 10px;
            font-style: italic;
            font-size: 1.2rem;
            text-align: center;
        }
        
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
        }
        
        .stat-item {
            text-align: center;
            padding: 1rem;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #667eea;
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown("""
<div class="hero-about">
    <h1>The Story Behind the Code 🚀</h1>
    <p style="font-size: 1.3rem; color: #555; margin-top: 2rem;">
        From curiosity-driven student to impact-focused AI engineer - 
        here's how I transform complex challenges into intelligent solutions
    </p>
</div>
""", unsafe_allow_html=True)

# Personal Philosophy Section
st.markdown("""
<div class="philosophy-section">
    <h2 style="color: white; margin-bottom: 2rem;">💡 My Philosophy</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        "AI isn't just about algorithms and data - it's about understanding human needs and creating technology that amplifies human potential."
    </p>
    <p style="font-size: 1.1rem;">
        I believe the best AI solutions are those that feel intuitive, solve real problems, and make people's lives better.
    </p>
</div>
""", unsafe_allow_html=True)

# What Drives Me Section
st.markdown("## 🎯 What Drives Me")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="story-card">
        <h3>🔍 Curiosity-Driven Innovation</h3>
        <p>
            I'm fascinated by the "why" behind every problem. Whether it's understanding why a model fails 
            or discovering hidden patterns in data, my curiosity drives me to dig deeper and find better solutions. 
            This approach has led me to develop unique methodologies that often outperform standard practices.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="story-card">
        <h3>🚀 Impact-First Mindset</h3>
        <p>
            Every line of code I write, every model I build, is designed with real-world impact in mind. 
            I don't just create technically impressive solutions - I create solutions that solve actual business 
            problems and improve people's experiences. My track record shows consistent delivery of measurable results.
        </p>
    </div>
    """, unsafe_allow_html=True)

# My Journey Timeline
st.markdown("## 📈 My Journey: From Curiosity to Expertise")

timeline_events = [
    {
        "year": "2010-2014",
        "title": "🎓 Foundation Years",
        "description": "Started with Computer Science at University of Cairo. Built my first recommendation system for movies - sparked my passion for AI that understands user behavior."
    },
    {
        "year": "2020-2022",
        "title": "🧠 AI Specialization",
        "description": "Master's in AI Engineering at University of Pisa. Developed emotion detection models that outperformed existing benchmarks by 15% - learned that innovation comes from understanding the problem deeply."
    },
    {
        "year": "2021-2024",
        "title": "💼 Industry Impact",
        "description": "At Configuratori, transformed theoretical knowledge into practical solutions. Improved predictive performance by 20% and workflow efficiency by 30% - discovered my talent for bridging research and business value."
    },
    {
        "year": "2024-Present",
        "title": "🚀 AI Innovation Leader",
        "description": "At Bakerhughes, pioneering RAG and LLM services. Building the future of document interaction and AI accessibility - proving that the best AI solutions are those that empower everyone."
    }
]

for event in timeline_events:
    st.markdown(f"""
    <div class="timeline-item">
        <h4>{event['year']}: {event['title']}</h4>
        <p>{event['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Core Values Section
st.markdown("## 🌟 My Core Values")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="value-card">
        <h3>🤝 Collaboration</h3>
        <p>The best solutions emerge when diverse minds work together. I actively seek different perspectives and believe that explaining complex concepts simply is a superpower.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="value-card">
        <h3>📚 Continuous Learning</h3>
        <p>AI evolves rapidly, and so do I. I dedicate time weekly to learning new techniques, reading research papers, and experimenting with emerging technologies.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="value-card">
        <h3>🎯 Results Focus</h3>
        <p>Beautiful code means nothing without real impact. I measure success by business outcomes, user satisfaction, and the tangible value my solutions create.</p>
    </div>
    """, unsafe_allow_html=True)

# Skills Evolution Chart
st.markdown("## 📊 My Skills Evolution Over Time")

# Create a skills evolution chart
years = [2014, 2016, 2018, 2020, 2022, 2024]
python_skills = [20, 40, 60, 80, 90, 95]
ml_skills = [0, 10, 30, 60, 85, 95]
ai_engineering = [0, 0, 20, 50, 80, 95]
cloud_devops = [0, 0, 10, 40, 70, 90]

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=python_skills, mode='lines+markers', name='Python & Programming', line=dict(color='#667eea')))
fig.add_trace(go.Scatter(x=years, y=ml_skills, mode='lines+markers', name='Machine Learning', line=dict(color='#ff6b6b')))
fig.add_trace(go.Scatter(x=years, y=ai_engineering, mode='lines+markers', name='AI Engineering', line=dict(color='#74b9ff')))
fig.add_trace(go.Scatter(x=years, y=cloud_devops, mode='lines+markers', name='Cloud & DevOps', line=dict(color='#00b894')))

fig.update_layout(
    title='My Technical Skills Journey',
    xaxis_title='Year',
    yaxis_title='Proficiency Level (%)',
    hovermode='x unified',
    template='plotly_white'
)

st.plotly_chart(fig, use_container_width=True)

# Personal Insights Section
st.markdown("""
<div class="quote-section">
    "The most rewarding moments in my career have been when I've helped non-technical stakeholders understand 
    and leverage AI to solve their biggest challenges. Technology should empower, not intimidate."
</div>
""", unsafe_allow_html=True)

# What I'm Working On Now
st.markdown("## 🔬 What I'm Exploring Now")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="story-card">
        <h3>🤖 AI Agents & Automation</h3>
        <p>
            Exploring how AI agents can automate complex workflows while maintaining human oversight. 
            Currently experimenting with multi-agent systems that can collaborate to solve business problems.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="story-card">
        <h3>🧠 Explainable AI</h3>
        <p>
            Working on making AI decisions more transparent and interpretable. Because the best AI is AI that 
            humans can understand, trust, and improve upon.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="philosophy-section">
    <h2 style="color: white; margin-bottom: 2rem;">🤝 Let's Build Something Amazing Together</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        I'm always excited to discuss new challenges, share insights, or explore how AI can transform your business.
    </p>
    <p style="font-size: 1.1rem;">
        Whether you're looking for technical expertise, strategic AI guidance, or just want to chat about the future of technology - I'm here for it!
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #666; margin-top: 2rem;'>© 2024 Karim Osman - Passionate about AI, Driven by Impact</p>", unsafe_allow_html=True)
