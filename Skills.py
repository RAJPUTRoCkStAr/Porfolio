import streamlit as st
import plotly.graph_objects as go

def skil():
    st.subheader("💻 Technical Expertise", divider="rainbow")

    # Skill data with emojis
    data_analyst_skills = {
        "🐍 Python": 90,
        "🔢 SQL": 80,
        "📊 Pandas": 85,
        "📈 NumPy": 80,
        "📉 Matplotlib": 75,
        "📊 Seaborn": 70,
        "📊 Plotly": 75,
        "📊 Power BI": 70,
        "🧪 Postman": 60,
        "📊 Tableau": 65,
    }

    data_scientist_skills = {
        "🐍 Python": 90,
        "🧠 TensorFlow": 70,
        "🧠 Keras": 65,
        "🧠 PyTorch": 60,
        "📊 Scikit-learn": 75,
        "🔬 MLflow": 65,
        "🌐 Flask": 70,
        "⚡ FastAPI": 65,
    }

    python_developer_skills = {
        "🐍 Python": 90,
        "🌐 Django": 80,
        "🌐 Flask": 75,
        "⚡ FastAPI": 70,
        "👁️ OpenCV": 65,
        "📊 NumPy": 80,
        "📊 Pandas": 75,
        "📉 Matplotlib": 70,
        "📊 Scikit-learn": 65,
    }

    # Dark theme for Streamlit app
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #121212;  /* Dark background */
            color: #FFFFFF;  /* White text */
        }
        h1, h2, h3 {
            color: #1DA1F2;  /* Twitter Blue for headings */
        }
        .stPlotlyChart {
            margin-bottom: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Function to create animated skill charts
    def plot_skills_with_animation(skills, title):
        fig = go.Figure(data=[go.Bar(
            x=list(skills.values()),
            y=list(skills.keys()),
            orientation='h',
            marker_color='#1DA1F2',
            hoverinfo='x+y',
            text=list(skills.values()),
            textposition='auto'
        )])

        # Adding some animated transitions for the bars
        fig.update_traces(marker=dict(line=dict(color='#FFFFFF', width=2)))
        fig.update_layout(
            title=title,
            title_font_color='white',
            xaxis=dict(
                title='Proficiency (%)',
                showgrid=False,
                title_font=dict(color='white'),
                tickfont=dict(color='white'),
                range=[0, 100]  # Setting range for smooth animation
            ),
            yaxis=dict(
                title='Skills',
                title_font=dict(color='white'),
                tickfont=dict(color='white'),
            ),
            paper_bgcolor='#121212',
            plot_bgcolor='#121212',
            font=dict(color='white'),
            transition=dict(duration=500),  # Smooth transitions between skill bars
            margin=dict(l=50, r=50, b=50, t=50),
        )

        return fig

    st.subheader("Python Developer Skills")
    st.plotly_chart(plot_skills_with_animation(python_developer_skills, "Python Developer Skills"), use_container_width=True)


    st.subheader("Data Analyst Skills")
    st.plotly_chart(plot_skills_with_animation(data_analyst_skills, "Data Analyst Skills"), use_container_width=True)

    st.subheader("Data Scientist Skills")
    st.plotly_chart(plot_skills_with_animation(data_scientist_skills, "Data Scientist Skills"), use_container_width=True)


