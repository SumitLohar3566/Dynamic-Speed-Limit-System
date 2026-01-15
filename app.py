import streamlit as st
import datetime
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Dynamic Speed Limit System",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Function to add pink-themed background with proper text visibility
def set_background():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f9c5d1 0%, #f0b4d4 50%, #e7a3d7 100%);
        min-height: 100vh;
    }

    .main-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 30px;
        margin: 20px auto;
        box-shadow: 0 20px 60px rgba(214, 51, 132, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.3);
        max-width: 1200px;
    }

    /* UPDATED TITLE SECTION - Rectangular form with increased height/width */
    .title-section {
        text-align: center;
        margin-bottom: 40px;
        padding: 40px 20px;
        background: linear-gradient(135deg, #ffd6e7 0%, #ffc2d6 100%);
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.25);
        border: 4px solid #ff66b2;
        width: 100%;
        max-width: 100%;
        /* Rectangular shape - height adjusted */
        height: auto;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px; /* Reduced radius for more rectangular look */
    }

    .title-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 100%;
        background: linear-gradient(90deg, rgba(255, 182, 193, 0.3), rgba(255, 192, 203, 0.3));
        z-index: -1;
    }

    /* UPDATED TITLE TEXT - Black color for maximum visibility */
    .main-title {
        font-size: 3.8rem;
        font-weight: 900;
        margin-bottom: 10px;
        color: #000000 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        letter-spacing: 1.2px;
        line-height: 1.1;
        text-align: center;
        width: 100%;
    }

    .sub-title {
        font-size: 1.6rem;
        color: #333333 !important;
        font-weight: 600;
        opacity: 0.9;
        margin-bottom: 25px;
        text-align: center;
        width: 100%;
    }

    /* Features list styling */
    .features-list {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 20px;
        width: 100%;
    }

    .feature-item {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.1rem;
        font-weight: 500;
        color: #222222;
    }

    .feature-icon {
        font-size: 1.5rem;
        color: #ff0066;
    }

    .input-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255, 0, 102, 0.1);
        border: 2px solid #ffb6d9;
        transition: all 0.3s ease;
    }

    .input-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(255, 0, 102, 0.2);
        border-color: #ff0066;
    }

    .input-label {
        font-size: 1.2rem;
        font-weight: 700;
        color: #cc0066;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .speed-card {
        background: linear-gradient(135deg, #ff0066, #ff66b2);
        color: white;
        border-radius: 20px;
        padding: 30px;
        margin: 15px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(255, 0, 102, 0.4);
        transition: all 0.3s ease;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: 3px solid white;
    }

    .speed-card:hover {
        transform: scale(1.05);
        box-shadow: 0 20px 40px rgba(255, 0, 102, 0.6);
    }

    .speed-value {
        font-size: 4.5rem;
        font-weight: 800;
        margin: 15px 0;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        color: white;
    }

    .vehicle-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }

    .condition-card {
        background: linear-gradient(135deg, #ff3399, #ff66cc);
        color: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255, 51, 153, 0.4);
        border: 2px solid white;
    }

    .condition-icon {
        font-size: 3.5rem;
        margin-bottom: 15px;
        text-align: center;
    }

    .condition-text {
        font-size: 1.3rem;
        font-weight: 500;
        text-align: center;
        color: white;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    .warning-card {
        background: linear-gradient(135deg, #ff0066, #cc0066);
        color: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255, 0, 102, 0.5);
        border: 2px solid white;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    .stButton>button {
        background: linear-gradient(135deg, #ff0066, #ff66b2);
        color: white;
        border: none;
        padding: 20px 45px;
        border-radius: 15px;
        font-size: 1.3rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 20px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
        border: 2px solid white;
    }

    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(255, 0, 102, 0.5);
        background: linear-gradient(135deg, #ff1a75, #ff80cc);
    }

    .stSelectbox, .stDate_input {
        background: #fff5f9;
        border-radius: 12px;
        padding: 12px;
        border: 2px solid #ffb6d9;
        color: #660033;
        font-weight: 500;
    }

    .stSelectbox:focus, .stDate_input:focus {
        border-color: #ff0066;
        box-shadow: 0 0 0 3px rgba(255, 0, 102, 0.2);
    }

    .footer {
        text-align: center;
        color: #99004d;
        padding: 25px;
        margin-top: 40px;
        font-size: 1rem;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(255, 0, 102, 0.2);
    }

    .glowing-text {
        animation: glow 1.5s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #ff0066, 0 0 40px #ff0066;
        }
        to {
            text-shadow: 0 0 20px #fff, 0 0 30px #ff66b2, 0 0 40px #ff66b2, 0 0 50px #ff66b2;
        }
    }

    .chart-container {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255, 0, 102, 0.1);
        border: 2px solid #ffb6d9;
    }

    .info-bubble {
        display: inline-block;
        background: linear-gradient(135deg, #ff0066, #ff66b2);
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        margin: 8px;
        animation: float 3s ease-in-out infinite;
        border: 2px solid white;
        box-shadow: 0 5px 15px rgba(255, 0, 102, 0.3);
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    .highlight-text {
        background: linear-gradient(90deg, #ff0066, #ff66b2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .selected-details {
        background: linear-gradient(135deg, #ffe6f0, #ffccff);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        border-left: 8px solid #ff0066;
        box-shadow: 0 8px 25px rgba(255, 0, 102, 0.15);
    }

    .detail-item {
        font-size: 1.1rem;
        color: #660033;
        margin: 10px 0;
        font-weight: 600;
    }

    .detail-item strong {
        color: #ff0066;
    }

    /* Ensure all text is visible */
    .stMarkdown, .stText, .stTitle, .stHeader {
        color: #333333 !important;
    }

    /* Table styling */
    .dataframe {
        border: 2px solid #ffb6d9 !important;
        border-radius: 10px !important;
    }

    .dataframe th {
        background: linear-gradient(135deg, #ff0066, #ff66b2) !important;
        color: white !important;
        font-weight: 700 !important;
    }

    .dataframe td {
        background: #fff5f9 !important;
        color: #660033 !important;
        font-weight: 500 !important;
    }

    .highlight-row {
        background: linear-gradient(135deg, #ffe6f0, #ffccff) !important;
        color: #ff0066 !important;
        font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)


# Function to calculate speed limit based on time of day - ALGORITHM REMAINS CONSTANT
def calculate_speed_limit(time_of_day):
    if 6 <= time_of_day.hour < 9:
        return 60, 40, "Foggy weather reduces visibility. Speed limits are lowered for safety.", "🌫️", "Morning Fog"
    elif 9 <= time_of_day.hour < 12:
        return 100, 80, "Clear weather ideal for traveling at standard speed limits.", "☀️", "Clear Day"
    elif 12 <= time_of_day.hour < 15:
        return 80, 60, "Light rain reduces traction and visibility. Drive cautiously.", "🌧️", "Light Rain"
    elif 15 <= time_of_day.hour < 19:
        return 60, 40, "Heavy rainfall makes roads slippery. Reduce speed significantly.", "⛈️", "Heavy Rain"
    else:
        return 100, 80, "Clear weather for nighttime travel. Use headlights.", "🌙", "Night Time"


def main():
    set_background()

    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Header with UPDATED RECTANGULAR FORM
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <div class="title-section">
            <div class="main-title">🚗 DYNAMIC<br>SPEED LIMIT<br>SYSTEM 🚦</div>
            <div class="sub-title">Smart Speed Regulations for Enhanced Road Safety</div>
            <div class="features-list">
                <div class="feature-item">
                    <span class="feature-icon">⚡</span>
                    <span>Real-time Calculations</span>
                </div>
                <div class="feature-item">
                    <span class="feature-icon">🛡️</span>
                    <span>Safety First</span>
                </div>
                <div class="feature-item">
                    <span class="feature-icon">🚦</span>
                    <span>Smart Limits</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Car animation
        st.markdown("""
        <div style="text-align: center; margin: 20px 0;">
            <span style="font-size: 120px; display: inline-block; animation: float 2s ease-in-out infinite; color: #ff0066;">
                🚗💨
            </span>
        </div>
        """, unsafe_allow_html=True)

    # Input Section - Highway Selection
    st.markdown("""
    <div class="input-card">
        <div class="input-label">
            <span style="font-size: 1.8rem;">🏎️</span>
            SELECT YOUR HIGHWAY
        </div>
    """, unsafe_allow_html=True)

    # Highway selection with pink theme
    highways = [
        ("🚀 Mumbai-Pune Expressway", "Mumbai-Pune Expressway"),
        ("🌊 Yamuna Expressway", "Yamuna Expressway"),
        ("🏙️ Delhi-Meerut Expressway", "Delhi-Meerut Expressway"),
        ("🔄 Eastern Peripheral Expressway", "Eastern Peripheral Expressway"),
        ("🌀 Western Peripheral Expressway", "Western Peripheral Expressway"),
        ("🕌 Ahmedabad-Vadodara Expressway", "Ahmedabad-Vadodara Expressway"),
        ("🌉 Hyderabad Outer Ring Road", "Hyderabad Outer Ring Road"),
        ("🌴 Bangalore-Mysore Expressway", "Bangalore-Mysore Expressway"),
        ("🎯 Purvanchal Expressway", "Purvanchal Expressway"),
        ("⚡ Delhi-Mumbai Expressway", "Delhi-Mumbai Expressway"),
        ("🕌 Lucknow-Agra Expressway", "Lucknow-Agra Expressway"),
        ("🏖️ Chennai Peripheral Ring Road", "Chennai Peripheral Ring Road"),
        ("🌟 Dwarka Expressway", "Dwarka Expressway"),
        ("🌊 Ganga Expressway", "Ganga Expressway"),
        ("🏔️ Mumbai-Nagpur Expressway", "Mumbai-Nagpur Expressway"),
        ("🌄 Mumbai-Goa Highway", "Mumbai-Goa Highway"),
        ("🌇 Kolkata-Delhi Highway", "Kolkata-Delhi Highway"),
        ("🌉 Chennai-Bangalore Highway", "Chennai-Bangalore Highway"),
        ("🏰 Jaipur-Delhi Expressway", "Jaipur-Delhi Expressway"),
        ("🛣️ Amritsar-Jamnagar Expressway", "Amritsar-Jamnagar Expressway")
    ]

    highway_names = [h[0] for h in highways]
    highway_values = [h[1] for h in highways]

    selected_highway_display = st.selectbox("", highway_names, index=0, key="highway_select")
    selected_highway = highway_values[highway_names.index(selected_highway_display)]

    st.markdown("</div>", unsafe_allow_html=True)

    # Time and Date Selection
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="input-card">
            <div class="input-label">
                <span style="font-size: 1.8rem;">⏰</span>
                SELECT TRAVEL TIME
            </div>
        """, unsafe_allow_html=True)

        time_labels = [
            "🌅 Morning (6 AM - 9 AM)",
            "☀️ Day (9 AM - 12 PM)",
            "🌤️ Afternoon (12 PM - 3 PM)",
            "🌆 Evening (3 PM - 7 PM)",
            "🌙 Night (7 PM Onwards)"
        ]

        time_ranges = [(6, 9), (9, 12), (12, 15), (15, 19), (19, 24)]
        selected_time_label = st.selectbox("", time_labels, key="time_select")
        start_hour, end_hour = time_ranges[time_labels.index(selected_time_label)]
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="input-card">
            <div class="input-label">
                <span style="font-size: 1.8rem;">📅</span>
                SELECT TRAVEL DATE
            </div>
        """, unsafe_allow_html=True)

        # FIXED DATE HANDLING - Simplified approach
        today = datetime.date.today()
        max_date = datetime.date(2025, 12, 31)

        # Set default date to today if it's within range, otherwise use max_date
        if today <= max_date:
            default_date = today
        else:
            default_date = max_date

        # FIXED: Using simpler date_input without min_value/max_value constraints that might cause issues
        selected_date = st.date_input(
            "",
            value=default_date,
            key="date_input_unique"
        )

        # Ensure date is within reasonable range
        if selected_date > max_date:
            selected_date = max_date
            st.warning(f"Date adjusted to maximum allowed: {max_date}")

        st.markdown("</div>", unsafe_allow_html=True)

    # Selected Details Display
    st.markdown("""
    <div class="selected-details">
        <div style="font-size: 1.3rem; font-weight: 700; color: #ff0066; margin-bottom: 15px;">
            📋 SELECTED DETAILS
        </div>
        <div class="detail-item">
            <strong>🏎️ Highway:</strong> """ + selected_highway + """
        </div>
        <div class="detail-item">
            <strong>⏰ Time Slot:</strong> """ + selected_time_label.split(" (")[0] + """
        </div>
        <div class="detail-item">
            <strong>📅 Date:</strong> """ + selected_date.strftime("%d %B %Y") + """
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Calculate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        calculate_button = st.button("🚦 **CALCULATE SPEED LIMITS** 🚦", use_container_width=True, key="calculate_btn")

    if calculate_button:
        # Create datetime object
        selected_datetime = datetime.datetime.combine(selected_date, datetime.time(start_hour, 0))

        # Calculate speed limits - ALGORITHM REMAINS CONSTANT
        light_limit, heavy_limit, reason, emoji, condition_name = calculate_speed_limit(selected_datetime)

        # Results Header
        st.markdown("""
        <div style="text-align: center; margin: 40px 0;">
            <h2 style="color: #ff0066; font-size: 2.5rem; font-weight: 800; text-shadow: 2px 2px 4px rgba(255, 0, 102, 0.2);">
                📊 SPEED LIMIT RESULTS
            </h2>
            <div style="font-size: 1.2rem; color: #660033; margin-top: 10px;">
                Based on Time: """ + selected_time_label.split(" (")[0] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Speed Cards
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div class="speed-card">
                <div class="vehicle-icon">🚗</div>
                <div class="speed-value">{light_limit} km/h</div>
                <div style="font-size: 1.4rem; font-weight: 700; margin: 10px 0;">Light Vehicles</div>
                <div style="margin-top: 5px; font-size: 1rem; opacity: 0.9;">Cars • Bikes • SUVs</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="speed-card">
                <div class="vehicle-icon">🚛</div>
                <div class="speed-value">{heavy_limit} km/h</div>
                <div style="font-size: 1.4rem; font-weight: 700; margin: 10px 0;">Heavy Vehicles</div>
                <div style="margin-top: 5px; font-size: 1rem; opacity: 0.9;">Trucks • Buses • Trailers</div>
            </div>
            """, unsafe_allow_html=True)

        # Condition Display
        st.markdown(f"""
        <div class="condition-card">
            <div class="condition-icon">{emoji}</div>
            <div style="font-size: 1.8rem; font-weight: 800; text-align: center; margin-bottom: 15px;">
                {condition_name}
            </div>
            <div class="condition-text">{reason}</div>
        </div>
        """, unsafe_allow_html=True)

        # Safety Warnings (Only show for low speed limits)
        if light_limit <= 60:
            st.markdown("""
            <div class="warning-card">
                <h3 style="text-align: center; margin-bottom: 20px; font-size: 1.8rem;">
                    ⚠️ IMPORTANT SAFETY ALERT ⚠️
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                    <div style="background: rgba(255,255,255,0.25); padding: 15px; border-radius: 15px; text-align: center;">
                        <div style="font-size: 2rem;">🚫</div>
                        <div style="font-weight: 700; margin-top: 10px;">No Sudden Braking</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.25); padding: 15px; border-radius: 15px; text-align: center;">
                        <div style="font-size: 2rem;">💡</div>
                        <div style="font-weight: 700; margin-top: 10px;">Use Headlights</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.25); padding: 15px; border-radius: 15px; text-align: center;">
                        <div style="font-size: 2rem;">📏</div>
                        <div style="font-weight: 700; margin-top: 10px;">Increase Distance</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.25); padding: 15px; border-radius: 15px; text-align: center;">
                        <div style="font-size: 2rem;">👀</div>
                        <div style="font-weight: 700; margin-top: 10px;">Stay Alert</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Speed Limit Trends
        st.markdown("""
        <div class="chart-container">
            <h3 style="text-align: center; color: #ff0066; margin-bottom: 25px; font-size: 1.8rem;">
                📈 SPEED LIMIT TRENDS THROUGHOUT THE DAY
            </h3>
        """, unsafe_allow_html=True)

        # Create trend data
        trend_data = pd.DataFrame({
            'Time Slot': ['6-9 AM', '9-12 PM', '12-3 PM', '3-7 PM', '7 PM+'],
            'Light Vehicles (km/h)': [60, 100, 80, 60, 100],
            'Heavy Vehicles (km/h)': [40, 80, 60, 40, 80],
            'Condition': ['Foggy', 'Clear', 'Light Rain', 'Heavy Rain', 'Clear']
        })

        # Display table with pink styling
        st.dataframe(
            trend_data.style.apply(
                lambda x: ['background: linear-gradient(135deg, #ffe6f0, #ffccff)'
                           if v == selected_time_label.split(" ")[0]
                           else '' for v in trend_data['Time Slot']],
                axis=0
            ),
            use_container_width=True,
            height=250
        )

        st.markdown("""
        <div style="text-align: center; margin-top: 15px; color: #660033; font-weight: 600;">
            💡 Highlighted row shows your selected time slot
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)  # Close chart container

        # Info Bubbles
        st.markdown("""
        <div style="text-align: center; margin: 30px 0;">
            <span class="info-bubble">🚗 Drive Safe</span>
            <span class="info-bubble">📏 Follow Limits</span>
            <span class="info-bubble">⚠️ Stay Alert</span>
            <span class="info-bubble">💖 Save Lives</span>
        </div>
        """, unsafe_allow_html=True)

        # Download Report Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            report_data = {
                "Highway": [selected_highway],
                "Date": [selected_date.strftime("%Y-%m-%d")],
                "Time Slot": [selected_time_label],
                "Light Vehicle Limit (km/h)": [light_limit],
                "Heavy Vehicle Limit (km/h)": [heavy_limit],
                "Weather Condition": [condition_name],
                "Safety Message": [reason],
                "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            }

            df_report = pd.DataFrame(report_data)
            csv = df_report.to_csv(index=False)

            st.download_button(
                label="📥 DOWNLOAD SPEED LIMIT REPORT",
                data=csv,
                file_name=f"Speed_Limit_Report_{selected_date}.csv",
                mime="text/csv",
                use_container_width=True,
                key="download_btn"
            )

    st.markdown('</div>', unsafe_allow_html=True)  # Close main container

    # Footer
    st.markdown("""
    <div class="footer">
        <div style="font-size: 2rem; margin-bottom: 15px; color: #ff0066;">
            🚗 🚦 ⚡
        </div>
        <div style="font-size: 1.3rem; font-weight: 800; margin-bottom: 10px; color: #cc0066;">
            DYNAMIC SPEED LIMIT SYSTEM
        </div>
        <div style="font-size: 1rem; margin-bottom: 15px;">
            <span style="color: #ff0066;">⚡</span> Real-time Calculations
            <span style="margin: 0 15px;">•</span>
            <span style="color: #ff0066;">🛡️</span> Enhanced Road Safety
            <span style="margin: 0 15px;">•</span>
            <span style="color: #ff0066;">📊</span> Smart Regulations
        </div>
        <div style="font-size: 0.9rem; color: #99004d;">
            Drive Safe • Follow Traffic Rules • Save Lives
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()