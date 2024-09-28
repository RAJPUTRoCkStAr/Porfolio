import streamlit as st
from streamlit_lottie import st_lottie
from Lotti import lottie_me
def intro():
    st.subheader("👋 Welcome to the Introduction!", divider="rainbow")
    col1, col2 = st.columns([2, 1])  

    with col1:
        st.markdown("""
        <h1 style="color: #ff7f50; font-family: 'Trebuchet MS', sans-serif; font-size: 40px;">
        🚀 I'm Sumit! 👨‍💻
        </h1>
        """, unsafe_allow_html=True)

        
        st.write("""
        **👋 Hi there!** I'm currently a **first-semester BCA** (Bachelor of Computer Applications) student, building on a strong foundation with an **Advanced Diploma in IT**. My passion for technology and problem-solving continues to guide me along an exciting journey, and I'm thrilled about the road ahead. 🚀

        ---
        ### 💻 My Tech Journey
        My journey into the tech world began early, and each step has been both rewarding and transformative. During my **6-month internship at IBM** 🌍, I gained invaluable experience tackling real-world IT challenges and deepening my understanding of **enterprise-level solutions**. This opportunity shaped my technical foundation and sparked a desire to explore the **endless potential** of computer science and applications.

        ### 🔍 A Continuous Learner
        My enthusiasm for technology goes beyond academics — I'm constantly seeking to **learn and apply new skills**, from mastering **programming languages** to solving complex problems with practical implementations.

        ### 👨‍💻 Hands-On Experience
        The **Advanced Diploma in IT** gave me hands-on experience across various domains. As I embark on my **BCA journey**, I'm excited to dive deeper into **software development**, **data structures**, and emerging technologies like **AI** and **machine learning**.

        ---
        Whether it's **architecting efficient backend systems**, exploring **AI-driven solutions**, or experimenting with **innovative frameworks**, I'm always eager to **innovate, create**, and push the boundaries of what's possible.

        I'm excited to connect with like-minded individuals as I continue my journey of **learning**, **building**, and making a meaningful impact in the **tech world**. Let's collaborate and share ideas! 🌟
        """)

    
    with col2:
        st_lottie(lottie_me, speed=1, reverse=False, loop=True, quality='high', height=400, width=400)


