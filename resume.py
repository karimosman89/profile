import streamlit as st




# PDF Link and Preview Section
st.subheader("Resume")
st.write("You can view or download my detailed resume below.")

# Use a direct link to the PDF file
pdf_url = "https://drive.google.com/file/d/18SLECTaOP9vgHKqGrgRdVotPRWu_V7nZ/preview"  
# Embed the PDF for preview using an iframe
st.markdown(f'<iframe src="{pdf_url}#view=FitH" width="700" height="700" frameborder="0"></iframe>', unsafe_allow_html=True)

# Display a link for downloading the resume
st.markdown(f'### [Download]({pdf_url})')



# Footer Section
st.markdown("---")  # Horizontal line for separation
st.write("© 2024 Karim Osman - Machine Learning Engineer")
