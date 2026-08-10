import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI ML Lab | Dattaraj Shinde",
    page_icon="⌘",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).parent

STUDENT_NAME = "Dattaraj Shinde"
ENROLLMENT_NO = "ADT24SOCB0343"
UNIVERSITY = "MIT ADT University"

PROGRAM_INFO = {
    "bfs.py": {
        "title": "Breadth First Search",
        "short": "BFS",
        "description": "Traversal of a graph using the Breadth First Search algorithm.",
    },
    "dfs.py": {
        "title": "Depth First Search",
        "short": "DFS",
        "description": "Traversal of a graph using the Depth First Search algorithm.",
    },
}

st.markdown(
    """
    <style>

    /* ---------- General ---------- */

    .block-container {
        max-width: 1150px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                     Roboto, Helvetica, Arial, sans-serif;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    .sidebar-title {
        font-size: 1.15rem;
        font-weight: 650;
        color: #111827;
        margin-bottom: 0.2rem;
    }

    .sidebar-subtitle {
        font-size: 0.82rem;
        color: #6b7280;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }

    /* ---------- Header ---------- */

    .page-title {
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 700;
        letter-spacing: -0.04em;
        color: #111827;
        line-height: 1.1;
        margin-bottom: 0.6rem;
    }

    .page-subtitle {
        font-size: 1rem;
        color: #6b7280;
        max-width: 680px;
        line-height: 1.65;
        margin-bottom: 2rem;
    }

    /* ---------- Student Information ---------- */

    .student-info {
        border-top: 1px solid #e5e7eb;
        border-bottom: 1px solid #e5e7eb;
        padding: 1rem 0;
        margin-bottom: 2.5rem;
    }

    .student-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9ca3af;
        margin-bottom: 0.2rem;
    }

    .student-value {
        font-size: 0.92rem;
        color: #374151;
    }

    /* ---------- Section Titles ---------- */

    .section-title {
        font-size: 1.25rem;
        font-weight: 650;
        color: #111827;
        margin-bottom: 0.35rem;
    }

    .section-description {
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 1.25rem;
    }

    /* ---------- Program Header ---------- */

    .program-number {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 650;
        color: #6b7280;
        background: #f3f4f6;
        padding: 0.3rem 0.55rem;
        border-radius: 5px;
        margin-bottom: 0.75rem;
    }

    .program-title {
        font-size: clamp(1.5rem, 3vw, 2rem);
        font-weight: 700;
        letter-spacing: -0.025em;
        color: #111827;
        margin-bottom: 0.45rem;
    }

    .program-description {
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }

    /* ---------- Code ---------- */

    div[data-testid="stCode"] {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
    }

    /* ---------- Footer ---------- */

    .footer {
        border-top: 1px solid #e5e7eb;
        margin-top: 4rem;
        padding-top: 1.2rem;
        color: #9ca3af;
        font-size: 0.78rem;
        text-align: center;
    }

    /* ---------- Mobile ---------- */

    @media (max-width: 768px) {

        .block-container {
            padding: 1.5rem 1rem 2.5rem;
        }

        .page-title {
            font-size: 2rem;
        }

        .page-subtitle {
            font-size: 0.92rem;
        }

        .student-info {
            margin-bottom: 2rem;
        }

        .program-title {
            font-size: 1.5rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)

def get_program_files():
    """Return Python program files from the repository root."""
    excluded_files = {"app.py"}

    return sorted(
        [
            file
            for file in ROOT_DIR.glob("*.py")
            if file.name not in excluded_files
        ],
        key=lambda file: file.name.lower(),
    )


def get_program_info(filename):
    """Return program information, with a fallback for new programs."""
    if filename in PROGRAM_INFO:
        return PROGRAM_INFO[filename]

    title = filename.replace(".py", "").replace("_", " ").replace("-", " ").title()

    return {
        "title": title,
        "short": title[:3].upper(),
        "description": "Python implementation completed as part of the AI ML Lab.",
    }

program_files = get_program_files()

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">AI ML Lab</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        "MIT ADT University<br>"
        "Artificial Intelligence & Machine Learning"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Practicals")

    if not program_files:
        st.info("No Python programs found.")
        selected_file = None

    else:
        program_options = {
            get_program_info(file.name)["title"]: file
            for file in program_files
        }

        selected_title = st.radio(
            "Select a program",
            options=list(program_options.keys()),
            label_visibility="collapsed",
        )

        selected_file = program_options[selected_title]

    st.divider()

    st.caption(STUDENT_NAME)
    st.caption(ENROLLMENT_NO)

st.markdown(
    '<div class="page-title">AI ML Lab</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="page-subtitle">'
    "Practical implementations completed as part of the "
    "Artificial Intelligence & Machine Learning Lab at MIT ADT University."
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="student-info">
        <div class="student-label">Student</div>
        <div class="student-value">
            {STUDENT_NAME} &nbsp; · &nbsp; {ENROLLMENT_NO}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


if selected_file is not None:

    program = get_program_info(selected_file.name)

    program_index = program_files.index(selected_file) + 1

    st.markdown(
        f'<div class="program-number">PRACTICAL {program_index:02d}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="program-title">{program["title"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="program-description">'
        f'{program["description"]}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Program Code</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        "Python implementation"
        "</div>",
        unsafe_allow_html=True,
    )

    try:
        code = selected_file.read_text(encoding="utf-8")

        st.code(
            code,
            language="python",
            line_numbers=True,
        )

    except Exception as error:
        st.error(f"Unable to read the program: {error}")

st.markdown(
    f"""
    <div class="footer">
        {STUDENT_NAME} · {ENROLLMENT_NO} · {UNIVERSITY}
    </div>
    """,
    unsafe_allow_html=True,
)