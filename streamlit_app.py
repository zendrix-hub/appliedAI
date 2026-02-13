import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
import os

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Zendrix | Systems & Data Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---------------------------
# SESSION STATE
# ---------------------------
if "streak" not in st.session_state:
    st.session_state.streak = 12

if "missions_done" not in st.session_state:
    st.session_state.missions_done = 3

# ---------------------------
# HELPER: LOAD LOCAL IMAGE
# ---------------------------
def get_image_base64(path):
    """Encodes a local image to base64 for HTML embedding."""
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded_string}"
    return None

# ---------------------------
# CUSTOM THEME (BLACK WHITE + BLUE) & UI POLISH
# ---------------------------
st.markdown("""
<style>
    /* Global Settings */
    html, body, [class*="css"] {
        background-color: #0a0a0a;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    /* Typography */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    p {
        line-height: 1.6;
        font-size: 1.05rem;
    }
    
    .section-title {
        color: #4da6ff;
        font-size: 26px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 20px;
        border-bottom: 2px solid #003366;
        padding-bottom: 8px;
        display: inline-block;
        letter-spacing: 0.5px;
    }

    /* Professional Cards */
    .card {
        background-color: #111111;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #222;
        border-left: 5px solid #0066ff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,102,255,0.15);
        border-color: #333;
    }
    
    .card h3 {
        margin-top: 0;
        color: #fff;
    }
    
    .card-subtitle {
        color: #4da6ff;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 10px;
        display: block;
    }

    /* Buttons */
    .stButton>button {
        background-color: #0066ff;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 12px 28px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0052cc;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.4);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #1a1a1a;
    }
    
    /* Profile Image Container */
    .profile-img-container {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
        margin-top: 20px;
    }
    .profile-img {
        border-radius: 50%;
        border: 3px solid #0066ff; /* Thicker border for photo */
        padding: 3px;
        background: #111;
        width: 140px;
        height: 140px;
        object-fit: cover; /* Ensures your photo fills the circle perfectly */
        box-shadow: 0 0 25px rgba(0, 102, 255, 0.3);
    }
    
    /* Log Entry Style */
    .log-entry {
        background-color: #0f0f0f;
        border-left: 3px solid #333;
        padding: 15px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 15px;
        color: #ccc;
    }
    .log-date {
        color: #4da6ff;
        font-weight: bold;
        font-size: 0.85em;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR NAV
# ---------------------------
with st.sidebar:
    st.markdown('<div class="section-title" style="font-size: 20px; border: none;">💻 Command Center</div>', unsafe_allow_html=True)
    
    # --- Profile Section Logic ---
    # 1. Try to load local 'id.jpg'
    # 2. Fallback to default avatar if file is missing
    local_img_path = "id.jpg"
    img_src = get_image_base64(local_img_path)
    
    if img_src is None:
        # Fallback URL if id.jpg isn't uploaded to GitHub yet
        img_src = "https://api.dicebear.com/9.x/avataaars/svg?seed=Felix&backgroundColor=0a0a0a"

    st.markdown(f"""
        <div class="profile-img-container">
            <img src="{img_src}" class="profile-img">
        </div>
        <div style="text-align: center; margin-bottom: 20px;">
            <h3 style="margin:0; font-size: 1.2rem;">Zendrix Riva</h3>
            <span style="color: #666; font-size: 0.9rem;">System Architect</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        [
            "Home",
            "About",
            "Skills",
            "Portfolio",
            "System Check",
            "Growth Tracker",
            "Future Vision",
            "Contact"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("System Status: **ONLINE** 🟢")
    
    st.markdown("---")
    with st.expander("🛠️ Components Used"):
        st.markdown("""
        - `st.set_page_config`
        - `st.markdown` (Custom CSS)
        - `st.sidebar`
        - `st.metric`
        - `st.tabs`
        - `st.bar_chart`
        - `st.dataframe`
        - `st.toast`
        - `st.status`
        - `st.link_button`
        """)

# ---------------------------
# HOME
# ---------------------------
if page == "Home":
    st.title("Zendrix Riva")
    st.markdown("### Systems • Data • AI • Real-World Solutions")

    st.markdown("<br>", unsafe_allow_html=True)

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Discipline", "High", border=True)
    col2.metric("Consistency", "Strong", border=True)
    col3.metric("System Logic", "Advanced", border=True)
    col4.metric("Focus", "Long-Term", border=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Mission Card
    st.markdown("""
    <div class="card">
        <h3>🚀 Mission Statement</h3>
        <p>Technology is best when it solves real problems. I focus on building systems that combine 
        <b>data analytics, automation, and decision intelligence</b>. My work targets real-world environments 
        such as agriculture optimization, business operations, and smart monitoring infrastructures.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Two Column Details
    col_a, col_b = st.columns(2)
    with col_a:
         st.markdown("""
         <div class="card" style="min-height: 200px;">
             <h4>📍 Current Focus</h4>
             <p>Creating robust data pipelines that translate raw inputs into actionable business intelligence. Bridging the gap between theory and deployment.</p>
         </div>
         """, unsafe_allow_html=True)
    with col_b:
         st.markdown("""
         <div class="card" style="min-height: 200px;">
             <h4>🏆 Latest Milestone</h4>
             <p>Achieved N4 Japanese Proficiency while maintaining full-time CS studies. Demonstrating capacity for complex language acquisition alongside technical growth.</p>
         </div>
         """, unsafe_allow_html=True)

# ---------------------------
# ABOUT
# ---------------------------
elif page == "About":
    st.markdown('<p class="section-title">About Me</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
            <p>I am an IT student focused on <b>data analytics, applied AI, and real-world system development</b>.</p>
            <p>I enjoy building solutions that connect technology with practical domains like <b>agriculture and business decision systems</b>. My long-term goal is to build technology that helps people make smarter decisions using data.</p>
            <p>I value <b>clear learning, discipline, and continuous skill growth</b>. Outside academics, I focus on fitness, running, and structured daily improvement.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional "Personal Philosophy" to balance the UI
        st.markdown("""
        <div class="card" style="border-left-color: #333;">
            <h4>Personal Philosophy</h4>
            <p><i>"I prefer learning that is practical, concise, and easy to understand. I enjoy transforming complex ideas into simpler, clearer forms."</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Using a professional placeholder image for the "System Architecture" concept
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=600", caption="Architecture & Design")
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=600", caption="Global Connectivity")

# ---------------------------
# SKILLS
# ---------------------------
elif page == "Skills":
    st.markdown('<p class="section-title">Core Skills & Direction</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🧠 Mindset", "⚙️ Technical", "🔭 Future"])

    with tab1:
        st.markdown("""
        <div class="card">
            <h3>Core Technical Mindset</h3>
            <ul style="line-height: 1.8;">
                <li><b>Data Analytics Thinking:</b> Decision-focused data interpretation rather than just gathering numbers.</li>
                <li><b>Systems Integration:</b> Connecting data sources to automation logic to produce real-world outcomes.</li>
                <li><b>Applied AI Curiosity:</b> Exploring AI not just for novelty, but for automation and decision support systems.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="card">
            <h3>Development Stack</h3>
            <ul style="line-height: 1.8;">
                <li><b>Python:</b> Data workflow, Pandas, Streamlit, Automation scripting.</li>
                <li><b>Java:</b> Object Oriented Programming, System Architecture, Swing UI.</li>
                <li><b>SQL:</b> Database schema design, normalization, and efficient retrieval.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="card">
            <h3>Growth Direction</h3>
            <ul style="line-height: 1.8;">
                <li>Data Science Pipeline Construction</li>
                <li>Smart Monitoring Systems (IoT concepts)</li>
                <li>Agriculture + Business Intelligence Integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Skill Radar")
    radar = pd.DataFrame({
        "Skill": ["Python", "Data Logic", "System Design", "AI Concepts", "Database"],
        "Level": [85, 90, 85, 75, 88]
    })
    st.bar_chart(radar.set_index("Skill"), color="#0066ff")

# ---------------------------
# PORTFOLIO
# ---------------------------
elif page == "Portfolio":
    st.markdown('<p class="section-title">Project Showcase</p>', unsafe_allow_html=True)

    # Project 1
    st.markdown("""
    <div class="card">
        <h3>🎓 Student Record Management System</h3>
        <span class="card-subtitle">Python • Django • MySQL</span>
        <p>A comprehensive web application for managing student data with structured storage and strict validation logic. 
        Designed to handle data integrity issues and provide a seamless administrative experience.</p>
    </div>
    """, unsafe_allow_html=True)

    # Project 2
    st.markdown("""
    <div class="card">
        <h3>💧 Daloy Aqua (Concept)</h3>
        <span class="card-subtitle">IoT • Data Analytics • Environmental Science</span>
        <p>Smart monitoring vision for water quality. Focuses on collecting environmental data (pH, turbidity, flow) 
        to drive decision-making for local communities and ensure sustainable water resource management.</p>
    </div>
    """, unsafe_allow_html=True)

    # Project 3
    st.markdown("""
    <div class="card">
        <h3>🌾 Future Agri-Business Systems</h3>
        <span class="card-subtitle">Research • System Design</span>
        <p>Integrating accounting intelligence with agricultural output monitoring. The goal is to help farmers 
        understand profit margins in real-time by correlating crop yield data with market prices and operational costs.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# SYSTEM CHECK
# ---------------------------
elif page == "System Check":
    st.markdown('<p class="section-title">Command Center</p>', unsafe_allow_html=True)

    st.code("""
> SYSTEM STATUS: OPERATIONAL
> CURRENT MODE: LEARNING + BUILDING
> PRIORITY: LONG TERM SYSTEM MASTERY
> DISCIPLINE LEVEL: CONSISTENT
    """, language="bash")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Run Diagnostics", use_container_width=True):
            with st.status("Checking System Integrity...", expanded=True):
                st.write("Checking Data Pipelines...")
                time.sleep(0.5)
                st.write("Verifying Logic Gates...")
                time.sleep(0.5)
                st.write("Optimizing Mental State...")
                time.sleep(0.5)
                st.success("All Systems Nominal")
    
    with col2:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 20px;">
            <h2 style="color: #4da6ff;">99.9%</h2>
            <p>System Uptime</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# GROWTH TRACKER
# ---------------------------
elif page == "Growth Tracker":
    st.markdown('<p class="section-title">Growth & Discipline</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Streak", f"{st.session_state.streak} Days")
    with col2:
        st.metric("Missions Complete", st.session_state.missions_done)

    st.markdown("<br>", unsafe_allow_html=True)
    st.write("### Daily Progress Cycle")
    st.progress(min(st.session_state.streak / 30, 1.0))
    st.caption("Target: 30 Day Consistency Cycle")

    if st.button("✅ Mark Today Complete", use_container_width=True):
        st.session_state.streak += 1
        st.session_state.missions_done += 1
        st.toast("Growth Recorded! Keep going.", icon="🔥")
        time.sleep(0.5)
        st.rerun()

# ---------------------------
# FUTURE VISION
# ---------------------------
elif page == "Future Vision":
    st.markdown('<p class="section-title">Future Vision</p>', unsafe_allow_html=True)

    goals = {
        "Goal": [
            "Become Data Scientist",
            "Build Real Monitoring Systems",
            "Integrate Agri + Business Intelligence",
            "Contribute to Sustainable Tech"
        ],
        "Progress": [60, 40, 35, 45]
    }
    
    df_goals = pd.DataFrame(goals)
    
    st.dataframe(
        df_goals,
        column_config={
            "Progress": st.column_config.ProgressColumn(
                "Completion %",
                format="%d%%",
                min_value=0,
                max_value=100,
            ),
        },
        use_container_width=True,
        hide_index=True
    )

# ---------------------------
# CONTACT (REPLACED INPUTS)
# ---------------------------
elif page == "Contact":
    st.markdown('<p class="section-title">Establish Connection</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <p>I am currently open to collaborations on <b>Data Analytics</b> and <b>System Development</b> projects.</p>
    <p>If you are interested in building sustainable technology solutions or need assistance with data-driven decision systems, please establish a connection via the channels below.</p>
    </div>
    """, unsafe_allow_html=True)

    # Changed from 3 columns to 2 columns to remove LinkedIn
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("📧 Email Protocol", "mailto:rivazendrix@gmail.com", use_container_width=True)
    with col2:
        st.link_button("🐙 GitHub Repos", "https://github.com/zendrix-hub/appliedAI.git", use_container_width=True)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555; font-size: 12px; margin-bottom: 20px;'>SYSTEM VERSION 2.2 | ZENDRIX RIVA</div>", 
    unsafe_allow_html=True
)