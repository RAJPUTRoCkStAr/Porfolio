import streamlit as st

def certif():
    st.subheader("🎓 Certifications & Achievements", divider="rainbow")
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
        .stLinkButton button {
                background-color: #1E9E35 !important;
                color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    def display_certificate(certificate_title, image_url, verification_url, unique_key):
        with st.container():
            st.markdown(f"<div style='display: flex; justify-content: center;' class='certificate-container'><h3>{certificate_title}</h3>", unsafe_allow_html=True)
            st.image(image_url, use_column_width='auto') 
            st.link_button("Verify Certificate",url=verification_url,type="primary",use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
 
    certificates = [
        {
            "title": "Deep Learning with TensorFlow",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/tennsorflow.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/SN-COURSE-V1:BIGDATAUNIVERSITY+ML0120EN+V2"   
        },
        {
            "title": "Natural Language Processing and Computer Vision",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/nlp.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/MDL-214"  
        },
        {
            "title": "Machine Learning and Deep Learning",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/ml_dl.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/MDL-212"  
        },
        {
            "title": "AI And Machine Learning Full Course",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/ai_ml.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/URL-WNQKFPCPK1G"  
        },
        {
            "title": "Deep Learning",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/deep_learn.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/URL-1AE76ADD4550"  
        },
        {
            "title": "Elements of AI",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/elements_ai.jpg",  
            "verification": "https://skills.yourlearning.ibm.com/certificate/URL-332C7DE56AB8"  
        },
        {
            "title": "Data Analysis with Python",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/data_an.jpg",  
            "verification": "https://courses.skillsbuild.skillsnetwork.site/certificates/e18291aef7954f3e810aa7e9c610232b#"  
        },
        {
            "title": "Data Visualization with Python",
            "image": "https://raw.githubusercontent.com/RAJPUTRoCkStAr/VisionaryStocks/main/lottie/data_vis.jpg",  
            "verification": "https://courses.skillsbuild.skillsnetwork.site/certificates/bff44b8874ab40d0904f4f5574e0c73f#"  
        },
    ]

    columns = st.columns(4)


    for index, cert in enumerate(certificates):
        with columns[index % 4]: 
            display_certificate(cert["title"], cert["image"], cert["verification"], unique_key=f"verify_{index}")


