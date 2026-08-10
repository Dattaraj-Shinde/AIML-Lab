import sys
import asyncio
import subprocess
import html
from pathlib import Path

# Prevent Windows asyncio ConnectionResetError (WinError 10054)
if sys.platform == 'win32':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# Configuration
# ============================================================
st.set_page_config(
    page_title="AI ML Lab | Dattaraj Shinde",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).parent
STUDENT_NAME = "Dattaraj Shinde"
ENROLLMENT_NO = "ADT24SOCB0343"

PROGRAM_INFO = {
    "bfs.py": {
        "title": "Breadth First Search",
        "code": "BFS-01",
        "description": "Level-order graph traversal algorithm exploring nodes systematically layer by layer.",
    },
    "dfs.py": {
        "title": "Depth First Search",
        "code": "DFS-02",
        "description": "Deep-dive graph traversal algorithm exploring as far as possible along each branch before backtracking.",
    },
}

# ============================================================
# Dynamic CSS (Dark & Light Mode Support)
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* -----------------------------
       Default Theme (Dark)
    ----------------------------- */
    :root {
        --bg-primary: #09090b;
        --bg-secondary: #000000;
        --text-main: #fafafa;
        --text-muted: #a1a1aa;
        --border-color: #27272a;
        --card-bg: rgba(24, 24, 27, 0.4);
        --code-bg: #000000;
        --btn-bg: #ffffff;
        --btn-text: #000000;
        --dot-color: rgba(255,255,255,0.03);
        --title-grad-start: #ffffff;
        --title-grad-end: #a1a1aa;
        --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        --toast-bg: rgba(24, 24, 27, 0.9);
        --toast-text: #fafafa;
    }

    /* -----------------------------
       Light Theme Overrides
    ----------------------------- */
    @media (prefers-color-scheme: light) {
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --card-bg: rgba(255, 255, 255, 0.8);
            --code-bg: #f1f5f9;
            --btn-bg: #0f172a;
            --btn-text: #ffffff;
            --dot-color: rgba(0,0,0,0.05);
            --title-grad-start: #0f172a;
            --title-grad-end: #64748b;
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
            --toast-bg: rgba(255, 255, 255, 0.95);
            --toast-text: #0f172a;
        }
    }

    /* -----------------------------
       Core Layout & Elements
    ----------------------------- */
    header[data-testid="stHeader"] { background: transparent !important; }

    /* Hide injected Streamlit anchor links on headers */
    .stMarkdown a.heading-anchor { display: none !important; pointer-events: none !important; }

    .stApp {
        background-color: var(--bg-primary);
        background-image: radial-gradient(circle at center, var(--dot-color) 1px, transparent 1px);
        background-size: 40px 40px;
        transition: background-color 0.3s ease;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1000px;
    }

    /* -----------------------------
       Sidebar
    ----------------------------- */
    section[data-testid="stSidebar"] {
        background-color: var(--bg-secondary) !important;
        border-right: 1px solid var(--border-color);
        transition: background-color 0.3s ease;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }
    
    .brand-logo {
        font-weight: 800;
        font-size: 1.35rem;
        color: var(--text-main);
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 2rem;
    }

    .nav-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: var(--text-muted);
        font-weight: 700;
        margin-bottom: 1rem;
        margin-top: 1rem;
    }

    div[data-testid="stRadio"] > label { display: none; }
    div[data-testid="stRadio"] div[role="radiogroup"] { gap: 0.5rem; }
    
    div[data-testid="stRadio"] label {
        border-radius: 8px;
        padding: 0.85rem 1rem !important;
        background: transparent;
        border: 1px solid transparent;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    div[data-testid="stRadio"] label:hover {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
    }
    div[data-testid="stRadio"] label[data-checked="true"] {
        background: color-mix(in srgb, var(--text-main) 5%, transparent);
        border: 1px solid color-mix(in srgb, var(--text-main) 15%, transparent);
    }
    div[data-testid="stRadio"] label > div:first-child { display: none; }
    div[data-testid="stRadio"] label p {
        color: var(--text-main) !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }

    /* -----------------------------
       Main Hero Section
    ----------------------------- */
    .hero-section {
        margin-top: 1rem;
        margin-bottom: 3rem;
        animation: fadeIn 0.8s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Removed pointer-events to completely disable any accidental linking */
    .main-title {
        font-size: clamp(3rem, 6vw, 4.5rem);
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -0.04em;
        margin: 0 0 1rem 0;
        color: var(--text-main);
        pointer-events: none; 
    }
    .title-gradient {
        background: linear-gradient(135deg, var(--title-grad-start) 0%, var(--title-grad-end) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .main-subtitle {
        font-size: 1.15rem;
        color: var(--text-muted);
        line-height: 1.7;
    }

    /* -----------------------------
       Practical Info Cards
    ----------------------------- */
    .practical-container {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: var(--shadow);
        margin-bottom: 2rem;
        backdrop-filter: blur(20px);
    }

    .practical-meta {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .meta-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: var(--code-bg);
        border: 1px solid var(--border-color);
        padding: 0.4rem 0.85rem;
        border-radius: 8px;
        font-size: 0.85rem;
    }
    .meta-label {
        color: var(--text-muted);
        font-weight: 600;
    }
    .meta-value {
        color: var(--text-main);
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }

    .practical-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-main);
        letter-spacing: -0.02em;
        margin-bottom: 1rem;
    }
    .practical-desc {
        color: var(--text-muted);
        font-size: 1.05rem;
        line-height: 1.7;
        margin-bottom: 2.5rem;
        padding-bottom: 2.5rem;
        border-bottom: 1px solid var(--border-color);
    }

    /* -----------------------------
       Code & Terminal Output
    ----------------------------- */
    div[data-testid="stCodeBlock"] {
        border-radius: 12px !important;
        border: 1px solid var(--border-color) !important;
        background: var(--code-bg) !important;
        overflow-x: auto !important;
    }
    div[data-testid="stCodeBlock"] pre {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.9rem !important;
        padding: 1.5rem !important;
    }

    /* Sleek Terminal Output */
    .terminal-wrapper {
        margin-top: 2rem;
        background: var(--code-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        overflow: hidden;
    }
    .terminal-header {
        display: flex;
        align-items: center;
        padding: 0.75rem 1.25rem;
        background: color-mix(in srgb, var(--code-bg) 95%, var(--text-main));
        border-bottom: 1px solid var(--border-color);
    }
    .terminal-dots {
        display: flex;
        gap: 6px;
    }
    .dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .dot.red { background: #ff5f56; }
    .dot.yellow { background: #ffbd2e; }
    .dot.green { background: #27c93f; }
    .terminal-title {
        margin-left: 1rem;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .terminal-body {
        padding: 1.5rem;
        max-height: 400px;
        overflow-y: auto;
    }
    .terminal-body pre {
        margin: 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: var(--text-main);
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    /* -----------------------------
       Buttons & Footer
    ----------------------------- */
    .btn-github {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: var(--btn-bg);
        color: var(--btn-text) !important;
        padding: 0.85rem 1.5rem;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 0.9rem;
        margin-top: 2.5rem;
        transition: transform 0.2s ease, opacity 0.2s ease;
    }
    .btn-github:hover {
        transform: translateY(-2px);
        opacity: 0.9;
    }
    
    .footer-bar {
        margin-top: 4rem;
        padding-top: 2.5rem;
        border-top: 1px solid var(--border-color);
        text-align: center;
        color: var(--text-muted);
        font-size: 0.95rem;
    }
    .footer-highlight {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background: linear-gradient(135deg, var(--title-grad-start) 0%, var(--title-grad-end) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        letter-spacing: 0.02em;
    }

    /* Mobile adjustments */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem; padding-left: 1rem; padding-right: 1rem; }
        .practical-container { padding: 1.5rem; }
        .main-title { font-size: 2.5rem; }
        .meta-badge { width: 100%; justify-content: flex-start; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Javascript Hacks (Toast UI & Ctrl+C fix)
# ============================================================
components.html(
    """
    <script>
    const doc = window.parent.document;
    
    // Stop Ctrl+C from triggering Streamlit's "Clear Cache" dialog
    doc.addEventListener('keydown', function(e) {
        if (e.key.toLowerCase() === 'c' && !e.ctrlKey && !e.metaKey) {
            const tag = doc.activeElement.tagName.toLowerCase();
            if (tag !== 'input' && tag !== 'textarea') {
                e.stopPropagation();
                e.preventDefault();
            }
        }
    }, true);

    // Create a beautiful popup when "Copy to clipboard" is clicked
    doc.addEventListener('click', function(e) {
        const btn = e.target.closest('button[title="Copy to clipboard"]');
        if (btn) {
            const toast = doc.createElement('div');
            toast.innerHTML = '✨ Code copied successfully!';
            
            // Getting dynamic colors from the root
            const rootStyles = getComputedStyle(doc.documentElement);
            const bgColor = rootStyles.getPropertyValue('--toast-bg').trim() || 'rgba(24, 24, 27, 0.9)';
            const textColor = rootStyles.getPropertyValue('--toast-text').trim() || '#fafafa';
            const borderColor = rootStyles.getPropertyValue('--border-color').trim() || '#27272a';
            
            toast.style.cssText = `position:fixed;bottom:40px;right:40px;background:${bgColor};backdrop-filter:blur(10px);color:${textColor};padding:14px 28px;border-radius:10px;border:1px solid ${borderColor};box-shadow:0 10px 30px rgba(0,0,0,0.2);font-family:sans-serif;font-weight:600;font-size:14px;z-index:9999;opacity:0;transform:translateY(10px);transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1);`;
            doc.body.appendChild(toast);
            
            requestAnimationFrame(() => {
                toast.style.opacity = '1';
                toast.style.transform = 'translateY(0)';
            });
            
            setTimeout(() => { 
                toast.style.opacity = '0'; 
                toast.style.transform = 'translateY(10px)';
                setTimeout(() => doc.body.removeChild(toast), 300);
            }, 2500);
        }
    });
    </script>
    """,
    height=0,
    width=0,
)

# ============================================================
# Logic & File Mapping
# ============================================================
@st.cache_data
def get_program_info(filename: str):
    if filename in PROGRAM_INFO:
        return PROGRAM_INFO[filename]
    
    title = filename.replace(".py", "").replace("_", " ").replace("-", " ").title()
    return {
        "title": title,
        "code": f"EXP-{title[:2].upper()}",
        "description": "Python implementations of practical programs for the Artificial Intelligence & Machine Learning Lab at my university.",
    }

def fetch_files():
    try:
        files = [f for f in ROOT_DIR.glob("*.py") if f.name != Path(__file__).name]
        return sorted(files, key=lambda f: f.name.lower())
    except Exception:
        return []

program_files = fetch_files()
file_map = {get_program_info(f.name)["title"]: f for f in program_files}

# ============================================================
# Sidebar
# ============================================================
with st.sidebar:
    st.markdown(
        """
        <div class="brand-logo">
            📂 <span>AI ML Lab</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="nav-label">Practicals</div>', unsafe_allow_html=True)

    selected_file = None
    if file_map:
        selected_title = st.radio("Practicals", list(file_map.keys()), label_visibility="collapsed")
        selected_file = file_map.get(selected_title)
    else:
        st.markdown("<p style='color:var(--text-muted);font-size:0.85rem;'>No practical files found.</p>", unsafe_allow_html=True)

# ============================================================
# Main Content
# ============================================================
st.markdown(
    """
    <div class="hero-section">
        <h1 class="main-title"><span class="title-gradient">AI ML Lab</span></h1>
        <p class="main-subtitle">Python implementations of practical programs for the Artificial Intelligence & Machine Learning Lab at my university.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if selected_file:
    program = get_program_info(selected_file.name)

    # Practical Header
    st.markdown(
        f"""
        <div class="practical-container">
            <div class="practical-meta">
                <div class="meta-badge">
                    <span class="meta-label">Experiment:</span>
                    <span class="meta-value">{program["code"]}</span>
                </div>
                <div class="meta-badge">
                    <span class="meta-label">File:</span>
                    <span class="meta-value">{selected_file.name}</span>
                </div>
            </div>
            <div class="practical-title">{program["title"]}</div>
            <div class="practical-desc">{program["description"]}</div>
        """,
        unsafe_allow_html=True,
    )

    # Python Code Block
    try:
        with open(selected_file, "r", encoding="utf-8") as file:
            code_content = file.read()
        st.code(code_content, language="python", line_numbers=True)
    except Exception:
        pass

    # Terminal Output Execution block
    try:
        # Run the script and capture the output safely (with a timeout so it never hangs)
        result = subprocess.run([sys.executable, str(selected_file)], capture_output=True, text=True, timeout=5)
        output_data = result.stdout if result.returncode == 0 else result.stderr
        
        if not output_data.strip():
            output_data = "Program executed successfully with no print outputs."
            
    except subprocess.TimeoutExpired:
        output_data = "Execution stopped: Script timed out (Exceeded 5 seconds)."
    except Exception as e:
        output_data = f"Execution error: {str(e)}"
        
    escaped_output = html.escape(output_data)

    st.markdown(
        f"""
            <div class="terminal-wrapper">
                <div class="terminal-header">
                    <div class="terminal-dots">
                        <span class="dot red"></span>
                        <span class="dot yellow"></span>
                        <span class="dot green"></span>
                    </div>
                    <div class="terminal-title">Live Output</div>
                </div>
                <div class="terminal-body">
                    <pre><code>{escaped_output}</code></pre>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # GitHub Button
    github_url = f"https://github.com/Dattaraj-Shinde/AIML-Lab/blob/main/{selected_file.name}"
    st.markdown(
        f"""
            <a href="{github_url}" target="_blank" class="btn-github">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                View Source on GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    f"""
    <div class="footer-bar">
        Created with 🧠 by <span class="footer-highlight">{STUDENT_NAME} | {ENROLLMENT_NO}</span>
    </div>
    """,
    unsafe_allow_html=True,
)