import streamlit as st
import plotly.graph_objects as go
def skil():
    st.subheader("💻 Technical Expertise",divider="rainbow")
    data_analyst_skills = {
        "Python": 90,
        "SQL": 80,
        "Pandas": 85,
        "NumPy": 80,
        "Matplotlib": 75,
        "Seaborn": 70,
        "Plotly": 75,
        "Power BI": 70,
        "Postman": 60,
        "Tableau": 65,
    }

    data_scientist_skills = {
        "Python": 90,
        "TensorFlow": 70,
        "Keras": 65,
        "PyTorch": 60,
        "Scikit-learn": 75,
        "MLflow": 65,
        "Flask": 70,
        "FastAPI": 65,
    }

    python_developer_skills = {
        "Python": 90,
        "Django": 80,
        "Flask": 75,
        "FastAPI": 70,
        "OpenCV": 65,
        "NumPy": 80,
        "Pandas": 75,
        "Matplotlib": 70,
        "Scikit-learn": 65,
    }

    # Streamlit CSS for dark theme
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
        </style>
        """,
        unsafe_allow_html=True
    )

    def plot_skills(skills, title):
        fig = go.Figure(data=[go.Bar(
            x=list(skills.keys()),
            y=list(skills.values()),
            marker_color='#1DA1F2'  # Twitter Blue
        )])

        fig.update_layout(
            title=title,
            title_font_color='white',
            xaxis_title='Skills',
            xaxis_title_font_color='white',
            yaxis_title='Proficiency (%)',
            yaxis_title_font_color='white',
            paper_bgcolor='#121212',  # Dark background
            plot_bgcolor='#121212',   # Dark background for plot area
            font=dict(color='white'),  # Set font color to white
        )

        return fig
    st.subheader("Python Developer Skills")
    st.plotly_chart(plot_skills(python_developer_skills, "Python Developer Skills"))
    
    st.subheader("Data Analyst Skills")
    st.plotly_chart(plot_skills(data_analyst_skills, "Data Analyst Skills"))

    st.subheader("Data Scientist Skills")
    st.plotly_chart(plot_skills(data_scientist_skills, "Data Scientist Skills"))

