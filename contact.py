import streamlit as st

# Common styling for better presentation
def set_style():
    st.markdown("""
    <style>
        .main { 
            text-align: center; 
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5; /* Light background for contrast */
            padding: 20px; 
            border-radius: 8px;
        }
        h1 {
            color: #2e6e91; 
        }
        h3 {
            color: #3e3e3e; 
        }
        p {
            font-size: 1.1em; 
            line-height: 1.6; 
            color: #555;
        }
        .contact-button {
            background-color: #1e1e1e; 
            color: #d1d1d1; 
            border-radius: 8px; 
            padding: 12px; 
            margin: 8px; 
            display: flex; 
            align-items: center; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
            transition: transform 0.2s;
            text-decoration: none; /* Remove underline from links */
        }
        .contact-button:hover {
            transform: scale(1.05); /* Slight zoom effect on hover */
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()  # Apply styles

# Header
st.title("🌍 Let's Connect")

# Introductory Text
st.write("""
I am passionate about data and technology and eager to engage in meaningful conversations 
about innovative projects, ideas, and opportunities. Please feel free to connect with me through the following platforms:
""")

# Contact Methods Section
contact_buttons = {
    "LinkedIn": "https://linkedin.com/in/karimosman89",
    "Email": "mailto:karim.programmer2020@gmail.com",
    "GitHub": "https://github.com/karimosman89"
}

for platform, link in contact_buttons.items():
    st.markdown(f"""
    <a href="{link}" target="_blank" class="contact-button">
        <div>
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" style="width: 40px; height: 40px; margin-right: 10px;"> {platform}
        </div>
    </a>
    """, unsafe_allow_html=True)

# Additional Section: Call to Action
st.markdown("""
### I'm Open to Opportunities!
If you're interested in collaborating on projects or discussing new opportunities, 
don't hesitate to reach out. I look forward to connecting with like-minded professionals!
""")

# Testimonial Section (Optional)
st.markdown("""
<div style="background-color: #1e1e1e; padding: 16px; border-radius: 8px; margin-top: 16px;">
    <h3 style="text-align: center; color: #d1d1d1;">What Others Say</h3>
    <p style="text-align: center; font-style: italic; color: #d1d1d1;">
        "Karim is an exceptional data scientist who brings innovative solutions to every project." 
        - A former colleague
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
