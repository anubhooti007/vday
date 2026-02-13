import streamlit as st
import os

# Page config
st.set_page_config(
    page_title="Will you be my Valentine?",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1

# Get directory for local assets
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Custom CSS
st.markdown("""
<style>
    
    .stApp {
        background: #ffffff;
    }
    
    #MainMenu, footer, header { visibility: hidden; }
    
    .main .block-container {
        padding: 0.5rem 1rem 0.5rem !important;
        max-width: 700px;
        margin: 0 auto;
    }
    
    [data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
    }
    
    div[data-testid="stVerticalBlock"] {
        gap: 0.25rem !important;
    }
    
    .page-container {
        min-height: auto;
        padding: 0.25rem 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main-heading {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: clamp(1.8rem, 5vw, 2.8rem);
        font-weight: 700;
        color: #2d2d2d;
        margin: 0 0 0.75rem 0;
        line-height: 1.3;
    }
    
    .reason-heading {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: clamp(1.4rem, 4vw, 2rem);
        font-weight: 600;
        color: #2d2d2d;
        margin: 0 0 0.5rem 0;
        line-height: 1.4;
    }
    
    .stButton > button {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .yes-btn > button {
        background: linear-gradient(135deg, #e91e63 0%, #f06292 100%) !important;
        color: white !important;
    }
    
    .grey-btn > button {
        background: #9e9e9e !important;
        color: white !important;
    }
    
    .proposal-text {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: clamp(2rem, 6vw, 3.5rem);
        font-weight: 700;
        color: #2d2d2d;
        margin: 0 0 0.75rem 0;
    }
    
    .success-text {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 1.1rem;
        color: #4a4a4a;
        line-height: 1.6;
        margin: 0.5rem auto 0;
        max-width: 500px;
    }
    
    .gif-container {
        margin: 0.5rem 0;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    }
    
    .gif-container img {
        max-width: 100%;
        height: auto;
        display: block;
    }
    
    .hearts-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 9999;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 20px;
        opacity: 0.4;
        animation: floatHeart 4s ease-in-out infinite;
    }
    
    @keyframes floatHeart {
        0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 0.4; }
        90% { opacity: 0.4; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
    
    .button-row {
        display: flex;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 2rem;
    }
    
    [data-testid="column"] { padding: 0 0.25rem !important; }
    .stMarkdown { padding: 0 !important; }
    [data-testid="stMarkdownContainer"] { padding: 0 !important; }
    [data-testid="stHorizontalBlock"] > div { gap: 0.25rem !important; }
    [data-testid="stImage"] { margin: 0 !important; }
    .stImage img { margin: 0 !important; }
</style>
""", unsafe_allow_html=True)


def load_image(path: str):
    """Load image/GIF from same folder as app.py"""
    full_path = os.path.join(SCRIPT_DIR, path)
    if os.path.exists(full_path):
        return full_path
    return None


def render_intro():
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        '<p class="main-heading">4 Reasons why you should be my Valentine</p>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Next ❤️", key="intro_next"):
            st.session_state.page = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def render_reason(page_num: int, heading: str, gif_name: str, next_page: int):
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(f'<p class="reason-heading">{heading}</p>', unsafe_allow_html=True)
    
    gif_path = load_image(gif_name)
    if gif_path:
        st.markdown('<div class="gif-container">', unsafe_allow_html=True)
        st.image(gif_path, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.caption(f"Place {gif_name} in the same folder as app.py")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Next ❤️", key=f"reason{page_num}_next"):
            st.session_state.page = next_page
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def render_proposal():
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        '<p class="proposal-text">Will you be my Valentine?</p>',
        unsafe_allow_html=True
    )
    
    col_yes, col_no = st.columns(2)
    with col_yes:
        st.markdown('<div class="yes-btn" style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        if st.button("Yes ❤️", key="proposal_yes"):
            st.session_state.page = 7
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_no:
        st.markdown("""
        <div id="no-wrapper" style="position: relative; width: 100%; min-height: 70px; display: flex; align-items: center; justify-content: center;">
            <button id="runaway-no" style="
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                padding: 0.75rem 1.5rem;
                font-size: 1.1rem;
                border-radius: 50px;
                border: none;
                background: #9e9e9e;
                color: white;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                transition: left 0.12s ease-out, top 0.12s ease-out;
                white-space: nowrap;
                user-select: none;
            ">No 😒</button>
        </div>
        <script>
        (function() {
            function init() {
            var btn = document.getElementById('runaway-no');
            if (!btn) { setTimeout(init, 50); return; }
            var wrapper = document.getElementById('no-wrapper');
            var pos = { x: 0, y: 0 };
            var lastMove = 0;
            var wrapperW = 0, wrapperH = 0;
            var btnW = 120, btnH = 48;
            
            function updateBounds() {
                if (wrapper.offsetWidth) {
                    wrapperW = wrapper.offsetWidth;
                    wrapperH = wrapper.offsetHeight;
                }
            }
            
            function getPointer(e) {
                var t = e.touches && e.touches[0];
                return { x: (t || e).clientX, y: (t || e).clientY };
            }
            
            function moveButton(e) {
                var now = Date.now();
                if (now - lastMove < 40) return;
                lastMove = now;
                updateBounds();
                if (wrapperW < 10) return;
                var ptr = getPointer(e);
                var wr = wrapper.getBoundingClientRect();
                var br = btn.getBoundingClientRect();
                var btnCx = br.left - wr.left + br.width / 2;
                var btnCy = br.top - wr.top + br.height / 2;
                var ptrX = ptr.x - wr.left;
                var ptrY = ptr.y - wr.top;
                var dx = ptrX - btnCx;
                var dy = ptrY - btnCy;
                var dist = Math.sqrt(dx*dx + dy*dy) || 1;
                var speed = Math.min(90, 2500 / dist);
                var moveX = -dx / dist * speed;
                var moveY = -dy / dist * speed;
                var maxOff = Math.min(80, (wrapperW - btnW) / 2, (wrapperH - btnH) / 2);
                pos.x = Math.max(-maxOff, Math.min(maxOff, pos.x + moveX));
                pos.y = Math.max(-maxOff, Math.min(maxOff, pos.y + moveY));
                btn.style.left = '50%';
                btn.style.top = '50%';
                btn.style.transform = 'translate(calc(-50% + ' + pos.x + 'px), calc(-50% + ' + pos.y + 'px))';
            }
            
            ['mousemove', 'touchmove'].forEach(function(ev) {
                document.addEventListener(ev, moveButton, { passive: false });
            });
            btn.addEventListener('click', function(e) { e.preventDefault(); e.stopPropagation(); });
            }
            if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
            else init();
        })();
        </script>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_success():
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    
    # Floating hearts
    st.markdown("""
    <div class="hearts-container" id="hearts">
        <span class="floating-heart" style="left: 10%; animation-delay: 0s;">❤️</span>
        <span class="floating-heart" style="left: 20%; animation-delay: 0.5s;">❤️</span>
        <span class="floating-heart" style="left: 30%; animation-delay: 1s;">❤️</span>
        <span class="floating-heart" style="left: 40%; animation-delay: 1.5s;">❤️</span>
        <span class="floating-heart" style="left: 50%; animation-delay: 2s;">❤️</span>
        <span class="floating-heart" style="left: 60%; animation-delay: 2.5s;">❤️</span>
        <span class="floating-heart" style="left: 70%; animation-delay: 3s;">❤️</span>
        <span class="floating-heart" style="left: 80%; animation-delay: 3.5s;">❤️</span>
        <span class="floating-heart" style="left: 90%; animation-delay: 4s;">❤️</span>
    </div>
    """, unsafe_allow_html=True)
    
    gif_path = load_image("success.gif")
    if gif_path:
        st.markdown('<div class="gif-container">', unsafe_allow_html=True)
        st.image(gif_path, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.caption("Place success.gif in the same folder as app.py")
    
    st.markdown("""
    <p class="success-text">
        I mean whatever... god you are so clingy.<br>
        But real stuff — so happy to have you in my life.<br>
        Happy Valentine's baby 😌❤️
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


# Main routing
page = st.session_state.page

if page == 1:
    render_intro()
elif page == 2:
    render_reason(
        2,
        "Reason 1: Big guns coming sooon 💪",
        "reason1.gif",
        3
    )
elif page == 3:
    render_reason(
        3,
        "Reason 2: Broke so can't run far 😌",
        "reason2.gif",
        4
    )
elif page == 4:
    render_reason(
        4,
        "Reason 3: I'll take care of you (Heat radiator mode for winter cuddles 🔥)",
        "reason3.gif",
        5
    )
elif page == 5:
    render_reason(
        5,
        "Reason 4: Extremely useful. Can do chores like acche ghar ki bahu. Will keep you hydrated 💧",
        "reason4.gif",
        6
    )
elif page == 6:
    render_proposal()
elif page == 7:
    render_success()
