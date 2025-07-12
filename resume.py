import streamlit as st
from utils import tr 

# PDF Link and Preview Section
st.subheader(tr("RESUME_SUBHEADER"))
st.write(tr("RESUME_DESCRIPTION"))

# Use a direct link to the PDF file
pdf_url = "https://drive.google.com/file/d/1czMtC6Ee_OOrj-58NW5uHHzITDiJ16Zu/preview"  
# Embed the PDF for preview using an iframe
st.markdown(f'<iframe src="{pdf_url}#view=FitH" width="700" height="700" frameborder="0"></iframe>', unsafe_allow_html=True)

# Display a link for downloading the resume
st.markdown(f'### [{tr("RESUME_DOWNLOAD_LINK_TEXT")}]({pdf_url})')

# Footer Section
st.markdown("---")  
st.write(tr("RESUME_FOOTER"))
