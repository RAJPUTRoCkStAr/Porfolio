import streamlit as st

def certif():
    st.subheader("🎓 Certifications & Achievements", divider="rainbow")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #121212;  /* Dark background */
            color: #FFFFFF;  /* White text */
        }
        h1, h2 {
            color: #1DA1F2;  /* Twitter Blue for headings */
        }
        .certificate-container {
            padding: 10px;
            border-radius: 8px;
            background-color: #1E1E1E;  /* Slightly lighter background for the certificate */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
            text-align: center;  /* Center align the text and images */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Function to display a single certificate
    def display_certificate(certificate_title, image_url, verification_url, unique_key):
        with st.container():
            st.markdown(f"<div class='certificate-container'><h3>{certificate_title}</h3>", unsafe_allow_html=True)
            st.image(image_url, use_column_width='auto')  # Centered image
            if st.button("Verify Certificate", key=unique_key):
                st.markdown(f"**Verification URL:** [Click Here]({verification_url})", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)  # Close the certificate container

    st.header("My Certificates")

    certificates = [
        {
            "title": "Deep Learning with TensorFlow",
            "image": "https://example.com/certificate1.png",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/SN-COURSE-V1:BIGDATAUNIVERSITY+ML0120EN+V2"   
        },
        {
            "title": "Data Science Certification",
            "image": "https://example.com/certificate2.png",  # Replace with your image URL
            "verification": "https://example.com/verify2"  # Replace with your verification URL
        },
        {
            "title": "Advanced Diploma in IT",
            "image": "https://example.com/certificate3.png",  # Replace with your image URL
            "verification": "https://example.com/verify3"  # Replace with your verification URL
        },
        {
            "title": "Certificate of Excellence - Machine Learning",
            "image": "https://example.com/certificate4.png",  # Replace with your image URL
            "verification": "https://example.com/verify4"  # Replace with your verification URL
        },
    ]

    # Create columns for each certificate
    columns = st.columns(4)

    # Loop through the certificates and display each in a column
    for index, cert in enumerate(certificates):
        with columns[index % 4]:  # Use modulo to cycle through the columns
            display_certificate(cert["title"], cert["image"], cert["verification"], unique_key=f"verify_{index}")


