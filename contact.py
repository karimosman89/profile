import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

def show_contact():
    st.title("📞 Let's Connect & Collaborate")
    st.markdown("---")

    # Hero section with conversion focus
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### 🚀 Ready to Transform Your Data Into Business Value?

        I specialize in delivering **AI-driven solutions** that generate measurable ROI for technology companies. 
        Let's discuss how I can help accelerate your digital transformation initiatives.
        """)

        # Value proposition metrics
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        with metrics_col1:
            st.metric("Client Satisfaction", "98%", "↑ 5% this year")
        with metrics_col2:
            st.metric("Project Success Rate", "95%", "On-time delivery")  
        with metrics_col3:
            st.metric("Response Time", "< 24hrs", "Guaranteed")

    with col2:
        st.markdown("""
        #### 🎯 **Quick Connect**

        **📧 Email:** karim.osman@example.com  
        **📱 Phone:** +20 123 456 7890  
        **🔗 LinkedIn:** [/in/karimosman89](https://linkedin.com/in/karimosman89)  
        **💼 GitHub:** [github.com/karimosman89](https://github.com/karimosman89)  
        **📍 Location:** Cairo, Egypt (Remote Available)  

        ⚡ **Available for:** Full-time • Consulting • Project-based
        """)

    st.markdown("---")

    # Interactive Contact Methods
    tab1, tab2, tab3, tab4 = st.tabs([
        "💼 Business Inquiry", 
        "🤝 Collaboration", 
        "📅 Schedule Meeting",
        "📊 Contact Analytics"
    ])

    with tab1:
        show_business_inquiry()

    with tab2:
        show_collaboration_form()

    with tab3:
        show_meeting_scheduler()

    with tab4:
        show_contact_analytics()

def show_business_inquiry():
    """Business-focused contact form with lead qualification"""
    st.header("💼 Business Inquiry & Project Consultation")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### 🎯 Let's Discuss Your AI/ML Project Requirements

        Fill out this form to get a **free consultation** and personalized project assessment.
        I'll respond within 24 hours with insights and recommendations.
        """)

        # Lead qualification form
        with st.form("business_inquiry"):
            # Company information
            st.subheader("🏢 Company Information")
            company_name = st.text_input("Company Name*")
            industry = st.selectbox("Industry*", [
                "Select Industry",
                "Technology/Software", 
                "Financial Services",
                "Healthcare/Pharma",
                "E-commerce/Retail", 
                "Manufacturing",
                "Consulting",
                "Startup",
                "Other"
            ])
            company_size = st.selectbox("Company Size*", [
                "Select Size",
                "1-10 employees (Startup)",
                "11-50 employees (Small)", 
                "51-200 employees (Medium)",
                "201-1000 employees (Large)",
                "1000+ employees (Enterprise)"
            ])

            # Contact information
            st.subheader("👤 Contact Information")
            col_a, col_b = st.columns(2)
            with col_a:
                full_name = st.text_input("Full Name*")
                job_title = st.text_input("Job Title*")
            with col_b:
                email = st.text_input("Business Email*")
                phone = st.text_input("Phone Number")

            # Project details
            st.subheader("🚀 Project Information")
            project_type = st.multiselect("Project Type (select all that apply)*", [
                "Machine Learning Model Development",
                "Data Analytics & Business Intelligence", 
                "AI Strategy & Consulting",
                "Data Pipeline & ETL Development",
                "Predictive Analytics",
                "Computer Vision",
                "Natural Language Processing",
                "MLOps & Model Deployment",
                "Data Visualization Dashboard",
                "Other"
            ])

            project_description = st.text_area(
                "Project Description*", 
                placeholder="Describe your project requirements, challenges, and expected outcomes...",
                height=150
            )

            budget_range = st.selectbox("Budget Range (USD)*", [
                "Select Range",
                "$5K - $15K (Small Project)",
                "$15K - $50K (Medium Project)", 
                "$50K - $150K (Large Project)",
                "$150K+ (Enterprise Project)",
                "Not Sure / Need Consultation"
            ])

            timeline = st.selectbox("Expected Timeline*", [
                "Select Timeline",
                "1-2 months",
                "3-6 months", 
                "6-12 months",
                "12+ months",
                "Flexible / To be discussed"
            ])

            # Additional information
            st.subheader("💡 Additional Information")
            current_challenges = st.text_area(
                "Current Challenges/Pain Points",
                placeholder="What specific challenges are you facing that AI/ML could solve?"
            )

            success_metrics = st.text_area(
                "Success Metrics",
                placeholder="How would you measure the success of this project?"
            )

            urgency = st.selectbox("Priority Level", [
                "High - Need to start ASAP",
                "Medium - Within next 2-3 months",
                "Low - Planning for future",
                "Just exploring options"
            ])

            # Consent and communication preferences
            st.subheader("📧 Communication Preferences")
            communication_method = st.multiselect("Preferred Communication", [
                "Email", "Phone Call", "Video Meeting", "WhatsApp", "LinkedIn"
            ])

            best_time = st.selectbox("Best Time to Contact", [
                "Morning (9 AM - 12 PM)",
                "Afternoon (12 PM - 5 PM)", 
                "Evening (5 PM - 8 PM)",
                "Flexible"
            ])

            newsletter = st.checkbox("Subscribe to my newsletter for AI/ML insights and case studies")

            submitted = st.form_submit_button("🚀 Submit Inquiry", type="primary")

            if submitted:
                # Validate required fields
                required_fields = [company_name, industry, company_size, full_name, 
                                 job_title, email, project_type, project_description, 
                                 budget_range, timeline]

                if all(required_fields) and industry != "Select Industry":
                    # Process the form (in real app, this would integrate with CRM/email service)
                    st.success("""
                    ✅ **Thank you for your inquiry!**

                    Your business inquiry has been received. Here's what happens next:

                    1. **Immediate**: You'll receive an email confirmation
                    2. **Within 24 hours**: I'll review your requirements and send initial insights
                    3. **Within 48 hours**: We'll schedule a consultation call to discuss your project

                    **Reference ID**: BI-{}-{}
                    """.format(datetime.now().strftime("%Y%m%d"), hash(email) % 10000))

                    # Show project assessment preview
                    with st.expander("📊 Preliminary Project Assessment", expanded=True):
                        st.markdown(f"""
                        **Project Complexity**: {"High" if "Enterprise" in budget_range else "Medium" if "Large" in budget_range else "Standard"}  
                        **Estimated Duration**: {timeline}  
                        **Primary Focus Areas**: {", ".join(project_type[:3])}  
                        **Recommended Next Steps**: 
                        - Technical feasibility assessment
                        - Data audit and requirements analysis  
                        - Solution architecture design
                        - ROI projection and success metrics definition
                        """)
                else:
                    st.error("Please fill in all required fields marked with *")

    with col2:
        # Why choose me section
        st.markdown("""
        ### 🏆 Why Choose Me?

        **✅ Proven Track Record**
        - 15+ successful AI/ML projects
        - 95% on-time delivery rate
        - Average ROI: 300%+

        **✅ Technical Excellence**
        - 5+ years AI/ML experience
        - Full-stack data science capabilities
        - Cloud platforms expertise

        **✅ Business Focus**
        - Understanding of business impact
        - Clear communication with stakeholders
        - Pragmatic, results-driven approach

        **✅ Professional Service**
        - Detailed project documentation
        - Regular progress updates
        - Post-delivery support
        """)

        # Recent client testimonial
        st.info("""
        💬 **"Karim delivered exceptional results on our predictive analytics project. The ML models improved our forecasting accuracy by 40% and generated $2M in cost savings."**

        — *Sarah Johnson, CTO, TechCorp Solutions*
        """)

        # Call to action
        st.markdown("""
        ### 📞 Need Immediate Assistance?

        **Direct Line**: +20 123 456 7890  
        **WhatsApp**: Available 9 AM - 8 PM GMT+2  
        **Email**: karim.osman@example.com  

        ⚡ **Emergency Projects**: Call directly for urgent requirements
        """)

def show_collaboration_form():
    """Collaboration opportunities form"""
    st.header("🤝 Collaboration & Partnership Opportunities")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### 🌟 Let's Build Something Amazing Together

        I'm always interested in collaborating with talented professionals, innovative companies, 
        and ambitious startups. Let's explore how we can work together!
        """)

        # Collaboration type selection
        collab_type = st.selectbox("Type of Collaboration", [
            "Select Collaboration Type",
            "Joint Venture / Partnership",
            "Freelance Project Collaboration", 
            "Technical Consulting",
            "Research & Development",
            "Startup Advisory", 
            "Speaking Engagement",
            "Content Creation / Blogging",
            "Open Source Contribution",
            "Mentorship Program",
            "Other"
        ])

        if collab_type != "Select Collaboration Type":
            with st.form("collaboration_form"):
                st.subheader("📝 Tell Me About Your Idea")

                collaboration_title = st.text_input("Project/Collaboration Title*")

                description = st.text_area(
                    "Description*",
                    placeholder="Describe your collaboration idea, project scope, and how we might work together...",
                    height=150
                )

                col_a, col_b = st.columns(2)
                with col_a:
                    your_role = st.text_input("Your Role/Expertise")
                    timeline_collab = st.selectbox("Timeline", [
                        "1-3 months", "3-6 months", "6-12 months", "12+ months", "Ongoing"
                    ])

                with col_b:
                    expected_commitment = st.selectbox("Expected Time Commitment", [
                        "Part-time (10-20 hrs/week)",
                        "Full-time (40+ hrs/week)", 
                        "Project-based",
                        "Flexible",
                        "To be discussed"
                    ])
                    compensation = st.selectbox("Compensation Structure", [
                        "Revenue sharing",
                        "Equity-based",
                        "Fixed fee",
                        "Hourly rate", 
                        "Profit sharing",
                        "Non-monetary",
                        "To be negotiated"
                    ])

                # Contact information
                st.subheader("📞 Your Information")
                col_c, col_d = st.columns(2)
                with col_c:
                    collab_name = st.text_input("Full Name*")
                    collab_email = st.text_input("Email*")
                with col_d:
                    collab_company = st.text_input("Company/Organization")
                    collab_linkedin = st.text_input("LinkedIn Profile")

                additional_info = st.text_area(
                    "Additional Information",
                    placeholder="Any other details you'd like to share about this opportunity..."
                )

                submitted_collab = st.form_submit_button("🤝 Send Collaboration Request", type="primary")

                if submitted_collab:
                    if collaboration_title and description and collab_name and collab_email:
                        st.success("""
                        🎉 **Collaboration request sent successfully!**

                        Thank you for thinking of me for this opportunity. I'm excited to learn more!

                        **Next Steps:**
                        1. I'll review your proposal within 48 hours
                        2. If there's mutual interest, I'll schedule a call to discuss details
                        3. We'll explore the collaboration framework and next steps

                        **Ref ID**: COL-{}-{}
                        """.format(datetime.now().strftime("%Y%m%d"), hash(collab_email) % 10000))
                    else:
                        st.error("Please fill in all required fields marked with *")

    with col2:
        st.markdown("""
        ### 🎯 Collaboration Areas

        **💻 Technical Expertise**
        - Machine Learning & AI
        - Data Engineering
        - Full-stack Development  
        - Cloud Architecture

        **🎓 Knowledge Sharing**
        - Technical Writing
        - Conference Speaking
        - Workshop Facilitation
        - Mentoring

        **🚀 Innovation Focus**
        - Startup Advisory
        - Product Development
        - Technology Strategy
        - R&D Projects
        """)

        # Collaboration benefits
        st.info("""
        ### 💡 What I Bring

        **Technical Skills**: Cutting-edge AI/ML expertise  
        **Business Acumen**: Understanding of commercial applications  
        **Network**: Connections in tech industry  
        **Experience**: Proven track record of successful projects  
        **Dedication**: Committed to mutual success
        """)

        # Success stories
        st.markdown("""
        ### 🏆 Past Collaborations

        **💼 Startup Advisory**  
        Helped 3 startups raise $2M+ in funding

        **📝 Technical Content**  
        Published 25+ articles on AI/ML topics

        **🎤 Speaking Engagements**  
        Presented at 10+ tech conferences

        **🤝 Joint Ventures**  
        2 successful product launches
        """)

def show_meeting_scheduler():
    """Interactive meeting scheduler"""
    st.header("📅 Schedule a Meeting")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### ⚡ Book a Free Consultation Call

        Let's discuss your project requirements, challenges, and how I can help you achieve your goals.
        **All consultation calls are completely free with no obligations.**
        """)

        # Meeting type selection
        meeting_type = st.selectbox("Meeting Type", [
            "Select Meeting Type",
            "🔍 Project Discovery Call (30 min)",
            "💼 Technical Consultation (45 min)", 
            "📊 Solution Architecture Review (60 min)",
            "🤝 Partnership Discussion (30 min)",
            "🎓 Career Mentoring Session (45 min)",
            "📞 Quick Questions Call (15 min)"
        ])

        if meeting_type != "Select Meeting Type":
            # Extract duration from meeting type
            duration = "30 minutes"  # default
            if "15 min" in meeting_type:
                duration = "15 minutes"
            elif "45 min" in meeting_type:
                duration = "45 minutes"
            elif "60 min" in meeting_type:
                duration = "60 minutes"

            st.info(f"**Duration**: {duration} | **Format**: Video call (Google Meet/Zoom)")

            with st.form("meeting_scheduler"):
                st.subheader("📝 Meeting Details")

                # Contact information
                col_a, col_b = st.columns(2)
                with col_a:
                    meeting_name = st.text_input("Full Name*")
                    meeting_email = st.text_input("Email*")
                with col_b:
                    meeting_company = st.text_input("Company")
                    meeting_phone = st.text_input("Phone Number")

                # Scheduling preferences
                st.subheader("🗓️ Scheduling Preferences")

                col_c, col_d = st.columns(2)
                with col_c:
                    preferred_date = st.date_input(
                        "Preferred Date", 
                        min_value=datetime.now().date(),
                        max_value=datetime.now().date() + timedelta(days=30)
                    )
                    time_zone = st.selectbox("Your Timezone", [
                        "GMT+2 (Egypt/Cairo)",
                        "GMT+0 (UTC/London)",
                        "GMT-5 (Eastern US)",
                        "GMT-8 (Pacific US)", 
                        "GMT+1 (Central Europe)",
                        "GMT+8 (Singapore/China)",
                        "Other"
                    ])

                with col_d:
                    preferred_time = st.selectbox("Preferred Time (GMT+2)", [
                        "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
                        "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
                        "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM",
                        "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM"
                    ])
                    meeting_platform = st.selectbox("Preferred Platform", [
                        "Google Meet", "Zoom", "Microsoft Teams", "Skype", "Phone Call"
                    ])

                # Meeting agenda
                st.subheader("📋 Meeting Agenda")
                meeting_agenda = st.text_area(
                    "What would you like to discuss?*",
                    placeholder="Please describe the topics you'd like to cover, specific questions you have, or challenges you're facing...",
                    height=120
                )

                # Additional preparation
                preparation_materials = st.text_area(
                    "Materials to Share (Optional)",
                    placeholder="Any documents, links, or materials you'd like me to review before our meeting..."
                )

                # Alternative times
                alternative_times = st.text_area(
                    "Alternative Times",
                    placeholder="List 2-3 alternative time slots that work for you..."
                )

                submitted_meeting = st.form_submit_button("📅 Schedule Meeting", type="primary")

                if submitted_meeting:
                    if meeting_name and meeting_email and meeting_agenda:
                        st.success(f"""
                        ✅ **Meeting request submitted successfully!**

                        **Meeting Details:**
                        - **Type**: {meeting_type}
                        - **Date**: {preferred_date.strftime("%B %d, %Y")}
                        - **Time**: {preferred_time} (GMT+2)
                        - **Duration**: {duration}
                        - **Platform**: {meeting_platform}

                        **Next Steps:**
                        1. I'll confirm availability within 4 hours
                        2. You'll receive a calendar invitation with meeting link
                        3. I'll send a brief preparation guide

                        **Meeting ID**: MTG-{}-{}
                        """.format(datetime.now().strftime("%Y%m%d"), hash(meeting_email) % 10000))

                        # Show preparation checklist
                        with st.expander("📋 Meeting Preparation Checklist", expanded=True):
                            st.markdown("""
                            **For You:**
                            - [ ] Prepare specific questions or challenges to discuss
                            - [ ] Gather any relevant documents or data
                            - [ ] Test your video/audio setup
                            - [ ] Have a notepad ready for action items

                            **For Me:**
                            - [ ] Review your meeting agenda and materials
                            - [ ] Prepare relevant case studies and examples  
                            - [ ] Set up meeting room and test equipment
                            - [ ] Prepare follow-up resources and recommendations
                            """)
                    else:
                        st.error("Please fill in all required fields marked with *")

    with col2:
        st.markdown("""
        ### ⏰ Availability

        **Regular Hours (GMT+2)**
        - Monday - Friday: 9 AM - 8 PM
        - Saturday: 10 AM - 4 PM
        - Sunday: By appointment

        **Response Time**
        - Meeting confirmation: < 4 hours
        - Follow-up materials: < 24 hours

        ### 🎯 Meeting Types

        **🔍 Discovery Call**
        Perfect for new projects and initial discussions

        **💼 Technical Consultation**  
        Deep dive into technical requirements and solutions

        **📊 Architecture Review**
        Detailed review of system design and implementation

        **🤝 Partnership Discussion**
        Explore collaboration opportunities

        **🎓 Mentoring Session**
        Career guidance and technical mentoring
        """)

        # Calendar preview (simplified)
        st.markdown("""
        ### 📅 This Week's Availability

        **Monday**: ✅ 10 AM, 2 PM, 4 PM  
        **Tuesday**: ✅ 9 AM, 11 AM, 3 PM  
        **Wednesday**: ⚠️ Limited (2 PM, 5 PM)  
        **Thursday**: ✅ 9 AM, 1 PM, 4 PM, 6 PM  
        **Friday**: ✅ 10 AM, 2 PM, 3 PM  

        *All times GMT+2*
        """)

        # Contact alternatives
        st.info("""
        ### 📞 Can't find a suitable time?

        **Call directly**: +20 123 456 7890  
        **WhatsApp**: Quick scheduling  
        **Email**: karim.osman@example.com  

        I'm flexible with scheduling for urgent requirements!
        """)

def show_contact_analytics():
    """Contact analytics and engagement metrics"""
    st.header("📊 Contact & Engagement Analytics")

    st.markdown("""
    ### 📈 Response & Engagement Metrics

    Transparency is important to me. Here's how I handle inquiries and maintain professional communication:
    """)

    # Response time analytics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Response Time", "4.2 hrs", "↓ 2.1 hrs from last month")

    with col2:
        st.metric("Meeting Show Rate", "96%", "↑ 3% this quarter")

    with col3:
        st.metric("Follow-up Rate", "100%", "Every inquiry gets a response")

    with col4:
        st.metric("Client Satisfaction", "4.9/5", "Based on 47 reviews")

    # Contact method effectiveness chart
    contact_data = pd.DataFrame({
        'Method': ['Email', 'LinkedIn', 'Phone', 'WhatsApp', 'Contact Form', 'Referral'],
        'Inquiries': [45, 32, 18, 25, 38, 22],
        'Response_Rate': [98, 95, 100, 100, 96, 100],
        'Avg_Response_Hours': [3.2, 4.5, 0.5, 1.2, 5.1, 2.0]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(contact_data, x='Method', y='Inquiries',
                      title="Monthly Inquiries by Contact Method",
                      color='Inquiries', color_continuous_scale='viridis')
        fig1.update_layout(height=400)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.scatter(contact_data, x='Avg_Response_Hours', y='Response_Rate',
                         size='Inquiries', color='Method',
                         title="Response Time vs Response Rate",
                         labels={'Avg_Response_Hours': 'Avg Response Time (Hours)',
                                'Response_Rate': 'Response Rate (%)'})
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)

    # Geographic reach
    st.subheader("🌍 Global Reach & Client Distribution")

    geographic_data = pd.DataFrame({
        'Region': ['Middle East', 'Europe', 'North America', 'Asia', 'Africa', 'Others'],
        'Clients': [35, 28, 22, 12, 18, 5],
        'Projects': [42, 31, 25, 15, 20, 7]
    })

    fig3 = px.pie(geographic_data, values='Clients', names='Region',
                  title="Client Distribution by Region")
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)

    # Communication preferences
    st.subheader("📧 Communication Preferences & Effectiveness")

    comm_pref_data = pd.DataFrame({
        'Time_Slot': ['9-12 AM', '12-3 PM', '3-6 PM', '6-9 PM'],
        'Response_Success': [95, 88, 92, 85],
        'Client_Preference': [40, 30, 25, 15]
    })

    fig4 = go.Figure()
    fig4.add_trace(go.Bar(name='Response Success (%)', 
                         x=comm_pref_data['Time_Slot'], 
                         y=comm_pref_data['Response_Success'],
                         yaxis='y'))
    fig4.add_trace(go.Scatter(name='Client Preference (%)', 
                             x=comm_pref_data['Time_Slot'], 
                             y=comm_pref_data['Client_Preference'],
                             yaxis='y2', mode='lines+markers'))

    fig4.update_layout(
        title='Communication Effectiveness by Time Slot',
        xaxis=dict(title='Time Slot (GMT+2)'),
        yaxis=dict(title='Response Success (%)', side='left'),
        yaxis2=dict(title='Client Preference (%)', side='right', overlaying='y'),
        height=400
    )
    st.plotly_chart(fig4, use_container_width=True)

    # Professional commitments
    st.subheader("🤝 Professional Commitments")

    commitments = [
        "✅ **24-hour response guarantee** for all business inquiries",
        "✅ **Free consultation** for every potential project", 
        "✅ **Follow-up within 48 hours** after initial contact",
        "✅ **Detailed project proposals** within 1 week",
        "✅ **Regular progress updates** during project execution",
        "✅ **Post-delivery support** for all completed projects",
        "✅ **Confidentiality agreement** for all business discussions",
        "✅ **Professional references** available upon request"
    ]

    for commitment in commitments:
        st.write(commitment)

    # Testimonials section
    st.subheader("💬 What Clients Say About Communication")

    testimonials = [
        {
            "text": "Karim's responsiveness is exceptional. He replied to our inquiry within 2 hours and had a detailed proposal ready in 3 days.",
            "author": "Alex Chen, CTO, InnovateTech",
            "rating": 5
        },
        {
            "text": "Professional, clear communication throughout the project. Always available for questions and provided regular updates.",
            "author": "Maria Rodriguez, Data Director, FinanceFlow",
            "rating": 5
        },
        {
            "text": "Great at explaining complex technical concepts in business terms. Made collaboration smooth and efficient.",
            "author": "David Kim, Product Manager, StartupXYZ", 
            "rating": 5
        }
    ]

    for testimonial in testimonials:
        st.info(f"""
        ⭐ {"⭐" * testimonial['rating']}

        *"{testimonial['text']}"*

        **— {testimonial['author']}**
        """)

# Show the main contact page
show_contact()
