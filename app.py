import streamlit as st
import pickle
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Iris Classifier",
    page_icon="🌸",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header   { visibility: hidden; }

/* ── App shell ── */
.stApp {
    background: #0c0e13;
    color: #e4e0d8;
}

/* Constrain & center the whole page */
.block-container {
    max-width: 560px !important;
    padding: 0 1.5rem 3rem !important;
    margin: 0 auto !important;
}

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 3rem 0 2.4rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
.hero-eyebrow {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #7c6ef0;
    margin-bottom: 0.8rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    line-height: 1.05;
    color: #f0ece4;
    margin: 0 0 0.6rem;
}
.hero-title em {
    font-style: italic;
    color: #b8a9f8;
}
.hero-subtitle {
    font-size: 0.88rem;
    color: #a09cb8;
    font-weight: 400;
    line-height: 1.65;
    margin: 0 auto 1.8rem;
    max-width: 360px;
    text-align: center;
    width: 100%;
}
.divider {
    width: 36px;
    height: 2px;
    background: linear-gradient(90deg, #7c6ef0, #b8a9f8);
    margin: 0 auto 1.8rem;
    border-radius: 2px;
}
.species-row {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
}
.badge {
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.07em;
    padding: 0.28rem 0.72rem;
    border-radius: 999px;
    border: 1px solid;
}
.badge-s { color: #a78bfa; border-color: #3d306e; background: #17132a; }
.badge-v { color: #5eead4; border-color: #1a4a44; background: #0d2420; }
.badge-g { color: #86efac; border-color: #1c4530; background: #0c2118; }

/* ── Section label above a card ── */
.section-label {
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #48435c;
    margin: 2rem 0 0.55rem;
}

/* ── Input row (pure HTML, no Streamlit columns) ── */
.input-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.85rem;
    background: #13151c;
    border: 1px solid #1e2030;
    border-radius: 14px;
    padding: 1.4rem 1.4rem 1.2rem;
}
.input-group {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}
.input-group label {
    font-size: 0.75rem;
    font-weight: 500;
    color: #7a7090;
    letter-spacing: 0.02em;
}
.input-group input[type=number] {
    background: #0c0e13;
    border: 1px solid #252338;
    border-radius: 8px;
    color: #e4e0d8;
    font-family: 'Inter', sans-serif;
    font-size: 0.92rem;
    padding: 0.52rem 0.8rem;
    width: 100%;
    box-sizing: border-box;
    -moz-appearance: textfield;
    outline: none;
    transition: border-color 0.18s, box-shadow 0.18s;
}
.input-group input[type=number]::-webkit-inner-spin-button,
.input-group input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; }
.input-group input[type=number]:focus {
    border-color: #7c6ef0;
    box-shadow: 0 0 0 3px rgba(124,110,240,0.14);
}

/* ── Classify button ── */
.stButton { margin-top: 1.4rem; }
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #6d44e8 0%, #5a68f0 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    padding: 0.8rem 1rem !important;
    cursor: pointer !important;
    transition: opacity 0.18s, transform 0.1s !important;
}
.stButton > button:hover  { opacity: 0.86 !important; transform: translateY(-1px) !important; }
.stButton > button:active { transform: translateY(0)  !important; }

/* ── Result ── */
.result-wrap {
    margin-top: 1.6rem;
    background: linear-gradient(140deg, #17132a 0%, #0d1e2a 100%);
    border: 1px solid #2b2460;
    border-radius: 14px;
    padding: 1.8rem 1.6rem;
    text-align: center;
    animation: slideUp 0.35s cubic-bezier(.22,.68,0,1.2);
}
@keyframes slideUp {
    from { opacity:0; transform:translateY(14px) scale(0.98); }
    to   { opacity:1; transform:translateY(0)    scale(1);    }
}
.result-tag {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #514b7a;
    margin-bottom: 0.45rem;
}
.result-name {
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: 2.1rem;
    line-height: 1.15;
    margin-bottom: 0.35rem;
}
.result-note {
    font-size: 0.8rem;
    color: #5a5478;
    line-height: 1.5;
}

/* ── Footer ── */
.footnote {
    text-align: center;
    font-size: 0.68rem;
    color: #6b6485;
    margin-top: 2.6rem;
    letter-spacing: 0.05em;
}
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        return pickle.load(open("models/iris_model.pkl", "rb"))
    except FileNotFoundError:
        st.error("Model file not found. Please train the model first.")
        st.stop()

model = load_model()

with st.sidebar:
    st.title("🌸 About Project")

    st.markdown("""
    ### Iris Flower Classification

    This Machine Learning model predicts
    the species of an Iris flower using:

    - Sepal Length
    - Sepal Width
    - Petal Length
    - Petal Width

    ### Model
    K-Nearest Neighbors (KNN)

    ### Dataset
    - Fisher Iris Dataset
    - 150 Samples
    - 3 Classes
    """)

SPECIES = {
    0: {"name": "Iris setosa",     "desc": "Small, compact blooms native to arctic and subarctic regions.", "color": "#a78bfa"},
    1: {"name": "Iris versicolor", "desc": "The harlequin blue flag, common across eastern North America.", "color": "#5eead4"},
    2: {"name": "Iris virginica",  "desc": "The southern blue flag, flourishing in US Southeast wetlands.", "color": "#86efac"},
}

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Botanical Classification · ML</div>
  <h1 class="hero-title">Identify an <em>Iris</em></h1>
  <p class="hero-subtitle">Enter four measurements below and the model will tell you which of three Iris species you're holding.</p>
  <div class="divider"></div>
  <div class="species-row">
    <span class="badge badge-s">I. setosa</span>
    <span class="badge badge-v">I. versicolor</span>
    <span class="badge badge-g">I. virginica</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Inputs ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Sepal</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="medium")
with col1:
    sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, max_value=20.0,
                                   value=5.1, step=0.1, label_visibility="visible")
with col2:
    sepal_width  = st.number_input("Sepal width (cm)",  min_value=0.0, max_value=20.0,
                                   value=3.5, step=0.1, label_visibility="visible")

st.markdown('<div class="section-label">Petal</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2, gap="medium")
with col3:
    petal_length = st.number_input("Petal length (cm)", min_value=0.0, max_value=20.0,
                                   value=1.4, step=0.1, label_visibility="visible")
with col4:
    petal_width  = st.number_input("Petal width (cm)",  min_value=0.0, max_value=20.0,
                                   value=0.2, step=0.1, label_visibility="visible")

# ── Extra CSS to style native Streamlit number inputs ─────────────────────────
st.markdown("""
<style>
.stNumberInput label p {
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    color: #7a7090 !important;
    letter-spacing: 0.02em !important;
    margin-bottom: 0.28rem !important;
}
.stNumberInput input {
    background: #0c0e13 !important;
    border: 1px solid #252338 !important;
    border-radius: 8px !important;
    color: #e4e0d8 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.52rem 0.8rem !important;
    height: auto !important;
}
.stNumberInput input:focus {
    border-color: #7c6ef0 !important;
    box-shadow: 0 0 0 3px rgba(124,110,240,0.14) !important;
}
.stNumberInput [data-baseweb="input"] div {
    background: transparent !important;
    border: none !important;
}
[data-testid="column"] { padding: 0 0.3rem !important; }
[data-testid="column"]:first-child { padding-left: 0 !important; }
[data-testid="column"]:last-child  { padding-right: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Button & result ───────────────────────────────────────────────────────────
if st.button("Classify Species →"):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = int(model.predict(features)[0])

    # FIX: safely compute confidence; default to None if model lacks predict_proba
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = max(model.predict_proba(features)[0]) * 100

    sp = SPECIES[pred]

    # Build confidence line conditionally so we never format None
    conf_line = f"<br><br>Prediction Confidence: {confidence:.2f}%" if confidence is not None else ""

    st.markdown(f"""
    <div class="result-wrap">
      <div class="result-tag">Predicted species</div>
      <div class="result-name" style="color:{sp['color']}">{sp['name']}</div>
      <div class="result-note">{sp['desc']}{conf_line}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # FIX: metrics are inside the if-block so confidence is always defined here
    c1, c2 = st.columns(2)
    with c1:
        # FIX: show "N/A" gracefully if model has no predict_proba
        st.metric("Prediction Confidence", f"{confidence:.2f}%" if confidence is not None else "N/A")
    with c2:
        st.metric("Model", "KNN")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="footnote">Developed by Pranjal Srivastava • Fisher Iris Dataset • Scikit-Learn</div>',
    unsafe_allow_html=True
)

st.download_button(
    label="📄 Download Sample Input",
    data="Sepal Length: 5.1\nSepal Width: 3.5\nPetal Length: 1.4\nPetal Width: 0.2\n",
    file_name="sample_input.txt"
)
