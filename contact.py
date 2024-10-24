import streamlit as st

# Common styling for a more modern presentation
def set_style():
    st.markdown("""
    <style>
        body {
            background-color: #f9f9f9; /* Soft background color */
            font-family: 'Arial', sans-serif;
        }
        .main {
            text-align: center;
            padding: 40px;
            margin: auto;
            max-width: 800px; /* Constrain width for better readability */
            background-color: #ffffff; /* White background for contrast */
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
        }
        h1 {
            color: #2e6e91; 
            font-size: 2.5em;
            margin-bottom: 10px; /* More space below the title */
        }
        h3 {
            color: #3e3e3e; 
            margin-top: 20px;
        }
        p {
            font-size: 1.1em; 
            line-height: 1.6; 
            color: #555;
        }
        .contact-button {
            background-color: #2e6e91; /* Button color */
            color: #ffffff; 
            border-radius: 5px; 
            padding: 15px; 
            margin: 10px; 
            display: flex; 
            align-items: center; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
            transition: all 0.3s;
            text-decoration: none; /* Remove underline from links */
        }
        .contact-button:hover {
            background-color: #1e4e66; /* Darker shade on hover */
            transform: translateY(-2px); /* Slight lift effect */
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-size: 0.9em;
        }
        .testimonial {
            background-color: #e0f7fa; /* Light cyan background */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
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

# Create buttons for contact methods
for platform, link in contact_buttons.items():
    st.markdown(f"""
    <a href="{link}" target="_blank" class="contact-button">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" style="width: 30px; height: 30px; margin-right: 10px;"> {platform}
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
<div class="testimonial">
    <h3 style="text-align: center; color: #2e6e91;">What Others Say</h3>
    <p style="text-align: center; font-style: italic; color: #3e3e3e;">
        "Karim is an exceptional data scientist who brings innovative solutions to every project." 
        - A former colleague
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)
