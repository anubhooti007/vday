import streamlit as st
import streamlit.components.v1 as components
import os

# Page config
st.set_page_config(
    page_title="Sooo, Will you be my Valentine!?",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1

# Get directory for local assets
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Custom CSS — Pinterest Valentine aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #fff5f7 0%, #ffe4ec 35%, #fcd5e0 70%, #fce4ec 100%) !important;
        background-attachment: fixed !important;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(255,182,193,0.15) 0%, transparent 8%),
            radial-gradient(circle at 90% 80%, rgba(255,182,193,0.12) 0%, transparent 8%),
            radial-gradient(circle at 50% 50%, rgba(255,192,203,0.08) 0%, transparent 12%);
        pointer-events: none;
        z-index: 0;
    }
    
    .bg-hearts {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
        opacity: 0.12;
    }
    
    .bg-hearts span {
        position: absolute;
        font-size: 24px;
        animation: bgFloat 12s ease-in-out infinite;
    }
    
    @keyframes bgFloat {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.3; }
        25% { transform: translate(10px, -20px) scale(1.1); opacity: 0.5; }
        50% { transform: translate(-5px, -40px) scale(0.9); opacity: 0.4; }
        75% { transform: translate(15px, -60px) scale(1.05); opacity: 0.35; }
    }
    
    #MainMenu, footer, header { visibility: hidden; }
    
    .main .block-container {
        padding: 1.5rem 1.5rem !important;
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
        text-align: justify !important;
    }
    
    [data-testid="stAppViewContainer"] { padding-top: 0 !important; }
    
    div[data-testid="stVerticalBlock"] { gap: 0.5rem !important; }
    
    .page-container {
        min-height: auto;
        padding: 1.5rem 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: justify;
        animation: pageFadeIn 0.7s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    
    @keyframes pageFadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main-heading {
        font-family: 'Quicksand', sans-serif !important;
        font-size: clamp(3rem, 5vw, 4.4rem) !important;
        font-weight: 700 !important;
        color: #8b3a62 !important;
        margin: 0 0 1.5rem 0 !important;
        line-height: 1.25 !important;
        letter-spacing: 0.02em !important;
        text-shadow: 0 2px 20px rgba(219, 112, 147, 0.15) !important;
        animation: textFadeIn 0.8s ease-out 0.2s both !important;
        text-align: justify !important;
    }
    
    .reason-heading {
        font-family: 'Quicksand', sans-serif !important;
        font-size: clamp(2.25rem, 4vw, 3.25rem) !important;
        font-weight: 700 !important;
        color: #7d3c5c !important;
        margin: 0 0 1.5rem 0 !important;
        line-height: 1.35 !important;
        letter-spacing: 0.015em !important;
        text-shadow: 0 2px 15px rgba(219, 112, 147, 0.12) !important;
        animation: textFadeIn 0.8s ease-out 0.2s both !important;
        text-align: justify !important;
    }
    
    @keyframes textFadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stButton > button {
        font-family: 'Quicksand', sans-serif !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        padding: 0.9rem 2.5rem !important;
        border-radius: 30px !important;
        border: none !important;
        box-shadow: 0 6px 25px rgba(219, 112, 147, 0.35) !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease, filter 0.2s ease !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 35px rgba(219, 112, 147, 0.45) !important;
        filter: brightness(1.05) !important;
    }
    
    .stButton > button:active {
        transform: scale(0.98) !important;
    }
    
    .yes-btn > button, .next-btn > button {
        background: linear-gradient(135deg, #e91e63 0%, #f06292 50%, #f8bbd9 100%) !important;
        color: white !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }
    
    .grey-btn > button { background: #b8a9b8 !important; color: white !important; }
    
    .proposal-text {
        font-family: 'Quicksand', sans-serif !important;
        font-size: clamp(2.25rem, 5vw, 3.5rem) !important;
        font-weight: 700 !important;
        color: #8b3a62 !important;
        margin: 0 0 1.5rem 0 !important;
        letter-spacing: 0.02em !important;
        text-shadow: 0 2px 25px rgba(219, 112, 147, 0.2) !important;
        animation: textFadeIn 0.8s ease-out 0.2s both !important;
        text-align: justify !important;
    }
    
    .gif-spacer { margin: 1.25rem 0 !important; }
    
    div[data-testid="stImage"] {
        margin: 1.25rem auto !important;
        max-width: 70% !important;
        border-radius: 24px !important;
        overflow: hidden !important;
        box-shadow: 0 12px 40px rgba(219, 112, 147, 0.25), 0 4px 15px rgba(0,0,0,0.08) !important;
    }
    
    @media (max-width: 768px) {
        div[data-testid="stImage"] { max-width: 90% !important; }
    }
    
    div[data-testid="stImage"] img {
        border-radius: 24px !important;
        display: block !important;
    }
    
    .btn-spacer { margin-top: 1.5rem !important; }
    
    .success-page .page-container { padding: 2rem 0 !important; }
    
    .success-text {
        font-family: 'Quicksand', sans-serif !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        color: #7d3c5c !important;
        line-height: 1.8 !important;
        margin: 1.25rem auto 0 !important;
        max-width: 520px !important;
        width: 100% !important;
        text-shadow: 0 0 30px rgba(255, 182, 193, 0.6) !important;
        animation: successBounce 1s ease-out 0.3s both !important;
        text-align: justify !important;
        text-align-last: left !important;
    }
    
    @keyframes successBounce {
        0% { opacity: 0; transform: translateY(20px) scale(0.95); }
        60% { opacity: 1; transform: translateY(-5px) scale(1.02); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .hearts-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 9999;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 22px;
        opacity: 0.5;
        animation: floatHeart 5s ease-in-out infinite;
        filter: drop-shadow(0 0 8px rgba(255, 182, 193, 0.5));
    }
    
    @keyframes floatHeart {
        0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        8% { opacity: 0.5; }
        92% { opacity: 0.5; }
        100% { transform: translateY(-80px) rotate(360deg); opacity: 0; }
    }
    
    .sparkle {
        display: inline-block;
        animation: sparkle 1.5s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.1); }
    }
    
    [data-testid="column"] { padding: 0 0.5rem !important; }
    .stMarkdown { padding: 0 !important; text-align: justify !important; }
    [data-testid="stMarkdownContainer"] { padding: 0 !important; text-align: justify !important; }
    [data-testid="stHorizontalBlock"] > div { gap: 0.5rem !important; }
    [data-testid="stImage"] { margin: 0 auto !important; }
    .stImage img { margin: 0 auto !important; }
</style>
""", unsafe_allow_html=True)

# Subtle background hearts (all pages)
st.markdown("""
<div class="bg-hearts">
    <span style="left: 5%; top: 10%;">💕</span>
    <span style="left: 85%; top: 25%; animation-delay: 2s;">💗</span>
    <span style="left: 15%; top: 60%; animation-delay: 4s;">💖</span>
    <span style="left: 75%; top: 70%; animation-delay: 1s;">💕</span>
    <span style="left: 50%; top: 40%; animation-delay: 3s;">💗</span>
</div>
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
        '<p class="main-heading">4 Reasons why you should choose me as your Valentine......!</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="btn-spacer"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="next-btn">', unsafe_allow_html=True)
        if st.button("Next ❤️", key="intro_next"):
            st.session_state.page = 2
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_reason(page_num: int, heading: str, gif_name: str, next_page: int):
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(f'<p class="reason-heading">{heading}</p>', unsafe_allow_html=True)
    st.markdown('<div class="gif-spacer"></div>', unsafe_allow_html=True)
    
    gif_path = load_image(gif_name)
    if gif_path:
        st.image(gif_path, use_container_width=True)
    else:
        st.caption(f"Place {gif_name} in the same folder as app.py")
    
    st.markdown('<div class="btn-spacer"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div class="next-btn">', unsafe_allow_html=True)
        if st.button("Next ❤️", key=f"reason{page_num}_next"):
            st.session_state.page = next_page
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_proposal():
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        '<p class="proposal-text">Will you be my Valentine?</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="btn-spacer"></div>', unsafe_allow_html=True)
    
    col_yes, col_no = st.columns(2)
    with col_yes:
        st.markdown('<div class="yes-btn" style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        if st.button("Yes ❤️", key="proposal_yes"):
            st.session_state.page = 7
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_no:
        runaway_html = """
        <div id="no-wrapper" style="position:relative;width:100%;min-height:90px;display:flex;align-items:center;justify-content:center;background:transparent;">
            <button id="runaway-no" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);padding:0.9rem 1.75rem;font-size:1.2rem;font-family:Quicksand,sans-serif;font-weight:600;border-radius:30px;border:none;background:linear-gradient(135deg,#b8a9b8 0%,#c9b8c9 100%);color:white;cursor:pointer;box-shadow:0 4px 20px rgba(150,130,150,0.3);transition:transform 0.08s ease-out;white-space:nowrap;user-select:none;">No 😒</button>
        </div>
        <script>
        (function(){
            function run(){var btn=document.getElementById('runaway-no');
            if(!btn){setTimeout(run,30);return;}
            var wrapper=document.getElementById('no-wrapper');
            var pos={x:0,y:0}, lastMove=0, wrapperW=0, wrapperH=0, btnW=130, btnH=52;
            function updateBounds(){if(wrapper.offsetWidth){wrapperW=wrapper.offsetWidth;wrapperH=wrapper.offsetHeight;}}
            function getPtr(e){var t=e.touches&&e.touches[0];return{x:(t||e).clientX,y:(t||e).clientY};}
            function moveBtn(e){
                var now=Date.now(); if(now-lastMove<16)return; lastMove=now;
                updateBounds(); if(wrapperW<10)return;
                var ptr=getPtr(e), wr=wrapper.getBoundingClientRect(), br=btn.getBoundingClientRect();
                var btnCx=br.left-wr.left+br.width/2, btnCy=br.top-wr.top+br.height/2;
                var ptrX=ptr.x-wr.left, ptrY=ptr.y-wr.top;
                var dx=ptrX-btnCx, dy=ptrY-btnCy, dist=Math.sqrt(dx*dx+dy*dy)||1;
                var speed=Math.min(140,5000/dist);
                var mx=-dx/dist*speed, my=-dy/dist*speed;
                var maxOff=Math.min(100,(wrapperW-btnW)/2,(wrapperH-btnH)/2);
                pos.x=Math.max(-maxOff,Math.min(maxOff,pos.x+mx));
                pos.y=Math.max(-maxOff,Math.min(maxOff,pos.y+my));
                btn.style.left='50%';btn.style.top='50%';
                btn.style.transform='translate(calc(-50% + '+pos.x+'px),calc(-50% + '+pos.y+'px))';
            }
            document.addEventListener('mousemove',moveBtn,{passive:false});
            document.addEventListener('touchmove',moveBtn,{passive:false});
            btn.onclick=function(e){e.preventDefault();e.stopPropagation();};}
            if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);
            else run();
        })();
        """ + "</scr" + "ipt>"
        components.html(runaway_html, height=95, scrolling=False)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_success():
    st.markdown('<div class="page-container success-page">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hearts-container" id="hearts">
        <span class="floating-heart" style="left: 8%; animation-delay: 0s;">❤️</span>
        <span class="floating-heart" style="left: 22%; animation-delay: 0.6s;">💕</span>
        <span class="floating-heart" style="left: 38%; animation-delay: 1.2s;">❤️</span>
        <span class="floating-heart" style="left: 55%; animation-delay: 1.8s;">💗</span>
        <span class="floating-heart" style="left: 72%; animation-delay: 2.4s;">❤️</span>
        <span class="floating-heart" style="left: 88%; animation-delay: 3s;">💕</span>
    </div>
    """, unsafe_allow_html=True)
    
    gif_path = load_image("success.gif")
    if gif_path:
        st.image(gif_path, use_container_width=True)
    else:
        st.caption("Place success.gif in the same folder as app.py")
    
    st.markdown("""
    <p class="success-text" style="text-align: justify !important;">
        I mean......whatever... god you are so clingy. {pretending to be macho}<br>
        But real stuff, so happy to have you in my life.<br>
        Happy Valentine's baby <span class="sparkle">😌</span><span class="sparkle">❤️</span>
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
        "Reason 1<br>Big guns coming sooon 💪",
        "reason1.gif",
        3
    )
elif page == 3:
    render_reason(
        3,
        "Reason 2<br>Broke......so can't run far 😌",
        "reason2.gif",
        4
    )
elif page == 4:
    render_reason(
        4,
        "Reason 3<br>Will always take care of you (Eg. Heat radiator to keep you warm during winter cuddles)",
        "reason3.gif",
        5
    )
elif page == 5:
    render_reason(
        5,
        "Reason 4<br>Useful. Can do chores like acche ghar ki bahu. Will keep you hydrated 💧",
        "reason4.gif",
        6
    )
elif page == 6:
    render_proposal()
elif page == 7:
    render_success()
