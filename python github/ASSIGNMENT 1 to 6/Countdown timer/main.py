import time
import streamlit as st

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10  # Default time

def countdown_timer():
    st.session_state.running = True  # Set running flag to True
    placeholder = st.empty()
    
    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        progress = 1 - (st.session_state.remaining_time / st.session_state.initial_time)
        
        # Create a more visually appealing timer display with progress bar
        placeholder.markdown(f"""
        <div style='text-align: center;'>
            <div style='font-size: 48px; font-weight: bold; color: #FF5722; margin: 20px 0;'>
                ⏳ {mins:02}:{secs:02}
            </div>
            <div style='margin: 20px auto; width: 80%; background: #f0f2f6; border-radius: 10px;'>
                <div style='height: 20px; width: {progress*100}%; background: linear-gradient(90deg, #FF5722, #FF9800); border-radius: 10px; transition: width 1s;'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.remaining_time -= 1
    
    if st.session_state.running:
        # More celebratory completion message
        placeholder.markdown("""
        <div style='text-align: center; padding: 30px; background: #4CAF50; border-radius: 10px;'>
            <h2 style='color: white;'>🎉 Time's Up! 🎉</h2>
            <p style='color: white; font-size: 18px;'>The countdown has finished!</p>
            <div style='font-size: 40px;'>⏱️</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # More noticeable stopped message
        placeholder.markdown("""
        <div style='text-align: center; padding: 20px; background: #FFC107; border-radius: 10px;'>
            <h3 style='color: #333;'>⏹ Timer Stopped</h3>
            <p>Click 'Start' to resume the countdown</p>
        </div>
        """, unsafe_allow_html=True)

# Streamlit UI with enhanced styling
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# Main header with better styling
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #4CAF50, #8BC34A); padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
        <h1 style='color: white; margin: 0;'>⏳ Countdown Timer</h1>
        <p style='color: white; opacity: 0.9;'>Track your time with style!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Time input section with better layout
with st.container():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #333;'>Set Countdown Duration</h3>", unsafe_allow_html=True)
    
    # Only show time input if timer isn't running
    if not st.session_state.running:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.session_state.remaining_time = st.number_input(
                "Seconds:",
                min_value=1,
                step=1,
                value=st.session_state.remaining_time,
                format="%d",
                key="time_input",
                help="Set the countdown duration in seconds."
            )
            st.session_state.initial_time = st.session_state.remaining_time
    st.markdown("<br>", unsafe_allow_html=True)

# Button styling and layout
button_style = """
    <style>
        div.stButton > button {
            width: 100%;
            padding: 12px 0;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border: none;
        }
        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
        }
        div.stButton > button:first-child:hover {
            background-color: #45a049;
            transform: translateY(-2px);
        }
        div.stButton > button:last-child {
            background-color: #f44336;
            color: white;
        }
        div.stButton > button:last-child:hover {
            background-color: #d32f2f;
            transform: translateY(-2px);
        }
        .stButton button:focus {
            outline: none;
            box-shadow: 0 0 0 2px white, 0 0 0 4px #4CAF50;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Button layout
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Start Timer", help="Begin the countdown"):
        countdown_timer()
with col2:
    if st.button("⏹ Stop Timer", help="Pause the countdown"):
        st.session_state.running = False

# Additional features and styling
st.markdown("""
    <style>
        .stNumberInput input {
            text-align: center;
            font-size: 18px;
            padding: 12px;
        }
        .stNumberInput label {
            text-align: center;
            display: block;
            font-size: 16px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 40px; color: #666; font-size: 14px;'>
        <hr style='border: 0.5px solid #eee;'>
        <p>Countdown Timer App • Made with Streamlit</p>
    </div>
""", unsafe_allow_html=True)