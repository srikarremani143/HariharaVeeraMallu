import streamlit as st
import pandas as pd
import base64
import numpy as np

# Set page configuration for wide layout and dark theme
st.set_page_config(page_title="Hari Hara Veera Mallu - Movie Premiere Dashboard", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for movie-themed styling with black background
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap');

    .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Oswald', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e63939;
        transform: scale(1.05);
    }
    .stDataFrame {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #ff4b4b;
    }
    .stDataFrame table {
        color: #ffffff;
        border-collapse: collapse;
        width: 100%;
    }
    .stDataFrame th, .stDataFrame td {
        border: 1px solid #ff4b4b;
        padding: 12px;
        text-align: left;
    }
    .stDataFrame th {
        background-color: #ff4b4b;
        color: #ffffff;
        font-weight: bold;
        text-transform: uppercase;
    }
    .stDataFrame td {
        background-color: #2c2c2c;
    }
    .poster-container {
        text-align: center;
        margin: 30px 0;
        padding: 20px;
    }
    .header {
        font-size: 3.5rem;
        color: #ff4b4b;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 20px;
        text-shadow: 3px 3px 6px rgba(255,75,75,0.3);
    }
    .subheader {
        font-size: 1.8rem;
        color: #cccccc;
        text-align: center;
        margin-bottom: 30px;
    }
    .movie-info {
        background-color: #1a1a1a;
        border: 2px solid #ff4b4b;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        text-align: center;
    }
    .movie-title {
        font-size: 2.5rem;
        color: #ff4b4b;
        margin-bottom: 15px;
        text-transform: uppercase;
        font-weight: bold;
    }
    .actor-name {
        font-size: 1.8rem;
        color: #ffffff;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .release-date {
        font-size: 1.5rem;
        color: #ffd700;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .movie-description {
        font-size: 1.1rem;
        color: #cccccc;
        line-height: 1.6;
        text-align: justify;
        margin: 15px 0;
    }
    .grandeur-section {
        background: linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%);
        border: 2px solid #ff4b4b;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
    }
    .grandeur-title {
        font-size: 2rem;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 20px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Function to load and encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load data
@st.cache_data
def load_data():
    city_data = pd.read_csv("city_summary_2025-07-21_730.csv")
    theater_data = pd.read_csv("theatre_shows_2025-07-21 _730.csv")
    return city_data, theater_data

city_data, theater_data = load_data()

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #ff4b4b; font-family: Oswald;'>Premiere Data</h2>", unsafe_allow_html=True)
    
    # Main platform selection
    platform = st.selectbox("Select Platform", ["Show Movie Info", "BookMyShow", "Paytm"], index=0)
    
    # Secondary dropdown for data type (only show if platform is selected)
    if platform in ["BookMyShow", "Paytm"]:
        data_type = st.selectbox("Select Data Type", ["City Data", "Theater Data"], index=0)

# Enhanced CSS for bold, white text in tables and stats
st.markdown("""
    <style>
    .stDataFrame th, .stDataFrame td {
        color: #fff !important;
        font-weight: bold !important;
    }
    /* Make metric values and labels thick red */
    div[data-testid="stMetric"] {
        color: #ff4b4b !important;
        font-weight: bold !important;
        border-radius: 10px;
        padding: 10px 0;
    }
    div[data-testid="stMetric"] > label, div[data-testid="stMetric"] > div {
        color: #ff4b4b !important;
        font-weight: bold !important;
        font-size: 1.3rem !important;
    }
    div[data-testid="stMetricValue"] {
        color: #ff4b4b !important;
        font-weight: bold !important;
        font-size: 2.5rem !important;
        text-shadow: 1px 1px 2px #000;
    }
    </style>
""", unsafe_allow_html=True)

if platform == "Show Movie Info":
    # Main content (only show movie info at the top)
    st.markdown("<h1 class='header'>Movie Premiere Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Experience the Grandeur of Indian Cinema</p>", unsafe_allow_html=True)

    # Movie Information Section
    st.markdown("""
        <div class='movie-info'>
            <div class='movie-title'>Hari Hara Veera Mallu</div>
            <div class='actor-name'>Starring: Pawan Kalyan</div>
            <div class='release-date'>🎬 Releasing in Theatres: July 24th, 2025 🎬</div>
        </div>
    """, unsafe_allow_html=True)

    # Display movie poster
    try:
        img_base64 = get_base64_image("HHVM.jpeg")
        st.markdown(
            f"<div class='poster-container'><img src='data:image/jpeg;base64,{img_base64}' width='400' style='border-radius: 15px; box-shadow: 0 10px 30px rgba(255,75,75,0.3);'></div>",
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("Movie poster image not found. Please ensure 'HHVM.jpeg' is in the app directory.")

    # Movie Description and Grandeur
    st.markdown("""
        <div class='grandeur-section'>
            <div class='grandeur-title'>About the Film</div>
            <div class='movie-description'>
                "Hari Hara Veera Mallu" is an epic historical action drama that promises to be one of the most grandiose films in Indian cinema. 
                Set against the backdrop of ancient India, this magnum opus brings to life the legendary tale of valor, sacrifice, and heroism.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='grandeur-section'>
            <div class='grandeur-title'>The Power Star: Pawan Kalyan</div>
            <div class='movie-description'>
                Konidela Pawan Kalyan, popularly known as the "Power Star," is one of the most influential actors in Indian cinema. 
                Born on September 2, 1971, Pawan Kalyan has carved a niche for himself with his unique style, powerful performances, 
                and charismatic screen presence. With over 25 years in the film industry, he has delivered numerous blockbusters 
                and has a massive fan following across the globe.
            </div>
            <div class='movie-description'>
                Known for his dedication to his craft, Pawan Kalyan has undergone extensive training in martial arts and horse riding 
                for his role in "Hari Hara Veera Mallu." His commitment to authenticity and his ability to bring historical characters 
                to life makes him the perfect choice for this epic role.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='grandeur-section'>
            <div class='grandeur-title'>The Grandeur of the Film</div>
            <div class='movie-description'>
                "Hari Hara Veera Mallu" is being made on an unprecedented scale with state-of-the-art technology and world-class production values. 
                The film features elaborate sets, stunning visual effects, and authentic period costumes that transport audiences to a bygone era. 
                With a stellar cast, breathtaking cinematography, and a compelling storyline, this film is set to redefine the standards of 
                Indian historical cinema.
            </div>
            <div class='movie-description'>
                The film's production team has left no stone unturned in ensuring historical accuracy while maintaining cinematic excellence. 
                From the majestic battle sequences to the intimate character moments, every frame is crafted with meticulous attention to detail, 
                making "Hari Hara Veera Mallu" a visual spectacle that audiences will remember for generations to come.
            </div>
        </div>
    """, unsafe_allow_html=True)

elif platform == "BookMyShow":
    if data_type == "City Data":
        # Clean city data: drop rows where all key columns are NaN or occupancy/gross is missing
        city_clean = city_data.dropna(subset=["TotalShows", "BookedGross", "TotalOccupancy"], how="any")
        city_clean = city_clean.replace({np.nan: "", "NaN%": ""})
        # Calculate stats for BookMyShow City Data
        total_shows = city_clean['TotalShows'].sum()
        gross_booked = city_clean['BookedGross'].sum()
        occ_values = city_clean['TotalOccupancy'].replace('', np.nan).dropna().str.replace('%','').astype(float)
        occupancy_avg = occ_values.mean() if not occ_values.empty else 0

        # Show stat boxes
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Shows", f"{int(total_shows):,}")
        col2.metric("Gross Booked", f"₹{gross_booked:,.0f}")
        col3.metric("Occupancy Avg", f"{occupancy_avg:.2f}%")

        # Dataframe
        st.markdown("<h2 style='color: #ff4b4b; text-align: center; margin: 30px 0; font-weight: bold;'>BookMyShow - City Data</h2>", unsafe_allow_html=True)
        st.dataframe(
            city_clean.style.set_properties(**{
                'background-color': '#2c2c2c',
                'color': '#fff',
                'border-color': '#ff4b4b',
                'font-size': '14px',
                'text-align': 'center',
                'font-weight': 'bold'
            }).set_table_styles([
                {'selector': 'th', 'props': [
                    ('background-color', '#ff4b4b'),
                    ('color', '#fff'),
                    ('font-weight', 'bold'),
                    ('text-align', 'center'),
                    ('text-transform', 'uppercase'),
                    ('border', '2px solid #ff4b4b')
                ]},
                {'selector': 'td', 'props': [
                    ('background-color', '#2c2c2c'),
                    ('color', '#fff'),
                    ('text-align', 'center'),
                    ('border', '1px solid #ff4b4b'),
                    ('padding', '12px'),
                    ('font-weight', 'bold')
                ]}
            ]),
            use_container_width=True
        )
    else:  # Theater Data
        # Clean theater data: drop rows where all key columns are NaN or occupancy/gross is missing
        theater_clean = theater_data.dropna(subset=["BookedGross", "Occupancy"], how="any")
        theater_clean = theater_clean.replace({np.nan: "", "NaN%": ""})
        # Calculate stats for BookMyShow Theater Data
        total_shows = theater_clean.shape[0]
        gross_booked = theater_clean['BookedGross'].sum()
        occ_values = theater_clean['Occupancy'].replace('', np.nan).dropna().str.replace('%','').astype(float)
        occupancy_avg = occ_values.mean() if not occ_values.empty else 0

        # Show stat boxes
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Shows", f"{int(total_shows):,}")
        col2.metric("Gross Booked", f"₹{gross_booked:,.0f}")
        col3.metric("Occupancy Avg", f"{occupancy_avg:.2f}%")

        # Dataframe
        st.markdown("<h2 style='color: #ff4b4b; text-align: center; margin: 30px 0; font-weight: bold;'>BookMyShow - Theater Data</h2>", unsafe_allow_html=True)
        st.dataframe(
            theater_clean.style.set_properties(**{
                'background-color': '#2c2c2c',
                'color': '#fff',
                'border-color': '#ff4b4b',
                'font-size': '14px',
                'text-align': 'center',
                'font-weight': 'bold'
            }).set_table_styles([
                {'selector': 'th', 'props': [
                    ('background-color', '#ff4b4b'),
                    ('color', '#fff'),
                    ('font-weight', 'bold'),
                    ('text-align', 'center'),
                    ('text-transform', 'uppercase'),
                    ('border', '2px solid #ff4b4b')
                ]},
                {'selector': 'td', 'props': [
                    ('background-color', '#2c2c2c'),
                    ('color', '#fff'),
                    ('text-align', 'center'),
                    ('border', '1px solid #ff4b4b'),
                    ('padding', '12px'),
                    ('font-weight', 'bold')
                ]}
            ]),
            use_container_width=True
        )

elif platform == "Paytm":
    # Placeholder for Paytm data
    st.markdown("<h2 style='color: #ff4b4b; text-align: center; margin: 30px 0; font-weight: bold;'>Paytm Data</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background-color: #1a1a1a; border: 2px solid #ff4b4b; border-radius: 15px; padding: 25px; margin: 20px 0; text-align: center;'>
            <h3 style='color: #ff4b4b; font-size: 1.5rem; margin-bottom: 15px;'>Paytm Data Coming Soon</h3>
            <p style='color: #cccccc; font-size: 1.1rem; line-height: 1.6;'>
                Paytm booking data will be available here once the CSV files are provided.
                <br><br>
                <strong>Selected Data Type:</strong> {data_type}
            </p>
        </div>
    """.format(data_type=data_type), unsafe_allow_html=True)
