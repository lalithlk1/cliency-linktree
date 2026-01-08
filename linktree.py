import streamlit as st

# 1. PAGE SETUP
# We set the page title and icon (what you see in the browser tab)
st.set_page_config(page_title="Lalith | Cliency", page_icon="⚡", layout="centered")

# 2. PROFILE SECTION
# We use columns to center the image perfectly
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Make sure you have a file named 'profile.png' in your folder!
    # If not, comment out the next line by adding a # at the start
    # st.image("profile.png", width=150) 
    pass # Remove this 'pass' when you uncomment the image line above

st.markdown("""
    <div style='text-align: center;'>
        <h1>Lalith.io</h1>
        <p><b>Co-Founder, Cliency ⚡</b></p>
        <p>Building High-Leverage Personal Brands for Founders.</p>
        <p>GTM Engineer & Content Strategist.</p>
    </div>
""", unsafe_allow_html=True)

st.write("---") # A subtle divider line

# 3. THE LINKS (The Meat)
# We use a dictionary so it's easy to add/remove links later
links = [
    {"title": "🌐 Visit our Website", "url": "https://www.cliency.in"},
    {"title": "💬 WhatsApp Me (Direct)", "url": "https://wa.me/919941726252"}, # Replace with your number
    {"title": "📺 Watch My Latest YouTube Video", "url": "https://youtube.com/@lalith.io1"},
    {"title": "👔 Connect on LinkedIn", "url": "https://linkedin.com/in/lalithlk1"},
    {"title": "💬 DM me on Insta","url": "https://instagram.com/lalith.io"},
    {"title": "📩 Book a Discovery Call", "url": "https://calendly.com/lalith-cliency"}
]

# Loop through the links and create buttons
for link in links:
    # use_container_width=True makes the button stretch full width (Mobile friendly)
    st.link_button(label=link["title"], url=link["url"], use_container_width=True)

st.write("---")

# 4. SOCIAL FOOTER
st.markdown("""
    <div style='text-align: center; color: grey;'>
        <small>© 2026 Cliency Media. Built with Python 🐍</small>
    </div>
""", unsafe_allow_html=True)