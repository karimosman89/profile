import streamlit as st

# Common styling for better presentation
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


@st.cache_data
# What I Do Section
st.header("🚀 What I Do")
st.write("""
As a specialist in **Artificial Intelligence** and **Data Engineering**, I focus on building **scalable solutions** that harness the power of machine learning and data analytics. My work encompasses a wide range of applications, including:
""")
st.markdown("""
- 🔍 **Deep Learning:** Creating advanced models for **Natural Language Processing** and **Computer Vision**.
- 📊 **Data Pipeline Development:** Designing robust ETL processes to ensure data quality and accessibility.
- 🔗 **AI Research:** Staying ahead of trends in **Reinforcement Learning** and exploring the latest advancements in **AI technologies**.
""")
@st.cache_data
# Why Work With Me Section
st.header("🌟 Why Work With Me?")
st.write("""
I believe that collaboration fuels innovation. Here’s what I bring to the table:
""")
st.markdown("""
- 🤝 **Collaborative Spirit:** I thrive in team environments and value diverse perspectives, enabling us to tackle challenges creatively.
- 💡 **Innovative Mindset:** My commitment to continuous learning allows me to adopt the latest technologies and methodologies to solve complex problems.
- 📈 **Results-Driven Approach:** I focus on delivering tangible outcomes, using data to inform decisions and measure success.
""")
@st.cache_data
# My Journey Section
st.header("📈 My Journey")
st.write("""
With a solid foundation in computer science and a passion for data, I've worked on numerous projects that range from predictive analytics to machine learning model deployment. Some key highlights of my journey include:
""")
st.markdown("""
- **Master's in Data Science**: Gained in-depth knowledge of statistical modeling, machine learning, and data visualization.
- **Industry Experience**: Collaborated with cross-functional teams to deliver data-driven solutions in [Your Industry/Field].
- **Continuous Learning**: I actively participate in workshops, webinars, and courses to stay updated on the latest trends and technologies in AI and Data Science.
""")
@st.cache_data
# Let's Connect Section
st.header("🌐 Let’s Connect!")
st.write("""
I’m always open to new opportunities and collaborations. Whether you’re looking to partner on an exciting project or discuss the latest trends in AI, feel free to reach out! Together, we can create solutions that not only meet business needs but also push the boundaries of what’s possible.
""")


# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
