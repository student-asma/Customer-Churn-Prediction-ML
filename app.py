import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px


# ====================================================
# PAGE CONFIGURATION
# ====================================================

st.set_page_config(
    page_title="Customer Churn Prediction | ML Dashboard",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ====================================================
# CUSTOM STYLING
# ====================================================

st.markdown("""
    <style>
        .stApp {
            background-color: #f4f7fb;
        }

        #MainMenu, footer, header {visibility: hidden;}

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        /* ---------- Animated Hero Banner ---------- */

        @keyframes gradientShift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes floatShape {
            0%   { transform: translateY(0px) translateX(0px); }
            50%  { transform: translateY(-14px) translateX(8px); }
            100% { transform: translateY(0px) translateX(0px); }
        }

        @keyframes fadeInUp {
            0%   { opacity: 0; transform: translateY(16px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulseDot {
            0%   { box-shadow: 0 0 0 0 rgba(53, 214, 143, 0.55); }
            70%  { box-shadow: 0 0 0 9px rgba(53, 214, 143, 0); }
            100% { box-shadow: 0 0 0 0 rgba(53, 214, 143, 0); }
        }

        .hero-banner {
            position: relative;
            overflow: hidden;
            background: linear-gradient(120deg, #0b1f3a 0%, #123a5c 45%, #0f6b4f 100%, #123a5c 140%);
            background-size: 300% 300%;
            animation: gradientShift 10s ease infinite;
            padding: 2.2rem 2.5rem;
            border-radius: 18px;
            margin-bottom: 1.6rem;
            box-shadow: 0 10px 30px rgba(11, 31, 58, 0.25);
        }

        .hero-shape {
            position: absolute;
            border-radius: 50%;
            filter: blur(2px);
            opacity: 0.18;
            animation: floatShape 6s ease-in-out infinite;
        }

        .hero-shape.s1 {
            width: 90px; height: 90px;
            background: #35d68f;
            top: 10%; right: 8%;
            animation-delay: 0s;
        }

        .hero-shape.s2 {
            width: 50px; height: 50px;
            background: #ffffff;
            top: 55%; right: 18%;
            animation-delay: 1.5s;
        }

        .hero-shape.s3 {
            width: 30px; height: 30px;
            background: #35d68f;
            top: 25%; right: 30%;
            animation-delay: 3s;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            animation: fadeInUp 0.8s ease-out;
        }

        .hero-tag {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255,255,255,0.12);
            color: #7be0b4;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 0.9rem;
        }

        .live-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #35d68f;
            animation: pulseDot 1.8s infinite;
        }

        .hero-title {
            color: #ffffff;
            font-size: 2.3rem;
            font-weight: 800;
            margin: 0;
            line-height: 1.15;
        }

        .hero-title span {
            color: #35d68f;
        }

        .hero-sub {
            color: #cbd9e8;
            font-size: 0.95rem;
            margin-top: 0.6rem;
            max-width: 640px;
        }

        /* ---------- Sections & Cards ---------- */

        .section-card {
            background: #ffffff;
            padding: 1.4rem 1.6rem;
            border-radius: 14px;
            box-shadow: 0 2px 14px rgba(20, 30, 60, 0.06);
            border: 1px solid #eef1f6;
            margin-bottom: 1.2rem;
            animation: fadeInUp 0.5s ease-out;
        }

        .section-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0b1f3a;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .section-icon-chip {
            width: 34px;
            height: 34px;
            border-radius: 10px;
            background: linear-gradient(135deg, #35d68f, #0f6b4f);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            box-shadow: 0 4px 10px rgba(15, 157, 99, 0.28);
            animation: pulseDot 2.6s infinite;
        }

        /* Real bordered containers (st.container(border=True)) act as our cards.
           This actually wraps the widgets inside, unlike a raw markdown div. */

        div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-anchor) {
            background: #ffffff;
            border-radius: 16px !important;
            border: 1px solid #eef1f6 !important;
            border-left: 4px solid #35d68f !important;
            box-shadow: 0 3px 16px rgba(20, 30, 60, 0.07);
            margin-bottom: 1.2rem;
            animation: fadeInUp 0.5s ease-out;
            transition: box-shadow 0.25s ease, transform 0.25s ease, border-left-color 0.25s ease;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(div.card-anchor):hover {
            box-shadow: 0 8px 24px rgba(15, 157, 99, 0.16);
            transform: translateY(-2px);
            border-left-color: #0f9d63 !important;
        }

        .kpi-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 1.1rem 1.3rem;
            border: 1px solid #eef1f6;
            box-shadow: 0 2px 14px rgba(20, 30, 60, 0.06);
            text-align: left;
            animation: fadeInUp 0.5s ease-out;
            transition: transform 0.2s ease;
        }

        .kpi-card:hover {
            transform: translateY(-3px);
        }

        .kpi-label {
            font-size: 0.78rem;
            color: #6b7688;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .kpi-value {
            font-size: 1.6rem;
            font-weight: 800;
            color: #0b1f3a;
            margin-top: 4px;
        }

        .kpi-green { color: #0f9d63; }
        .kpi-red { color: #d64545; }

        /* Mini live-snapshot chips under Customer Information */

        .mini-stat {
            display: flex;
            align-items: center;
            gap: 10px;
            background: linear-gradient(135deg, rgba(53,214,143,0.07), rgba(15,157,99,0.03));
            border: 1px solid rgba(53,214,143,0.25);
            border-radius: 10px;
            padding: 10px 12px;
            margin-top: 4px;
        }

        .mini-stat-icon {
            font-size: 1.2rem;
        }

        .mini-stat-label {
            font-size: 0.7rem;
            color: #6b7688;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        .mini-stat-val {
            font-size: 0.92rem;
            font-weight: 700;
            color: #0b1f3a;
        }

        .badge-risk-high {
            background: #fdecec;
            color: #c0392b;
            padding: 10px 18px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 1rem;
            border: 1px solid #f3c6c6;
        }

        .badge-risk-low {
            background: #eafaf1;
            color: #0f9d63;
            padding: 10px 18px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 1rem;
            border: 1px solid #bdeed6;
        }

        div.stButton > button {
            background: linear-gradient(90deg, #0f9d63, #0b7a4d);
            color: white;
            font-weight: 700;
            border-radius: 10px;
            padding: 0.7rem 1rem;
            border: none;
            width: 100%;
            font-size: 1rem;
            box-shadow: 0 6px 16px rgba(15, 157, 99, 0.25);
        }

        div.stButton > button:hover {
            background: linear-gradient(90deg, #0b7a4d, #0f9d63);
            color: white;
        }

        .footer-note {
            text-align: center;
            color: #8b93a3;
            font-size: 0.8rem;
            margin-top: 2rem;
        }

        /* ---------- Sidebar ---------- */

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b1f3a 0%, #0e2a4a 100%);
        }

        section[data-testid="stSidebar"] * {
            color: #dbe4f0 !important;
        }

        .sb-profile {
            text-align: center;
            padding: 1.2rem 0 1rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.12);
            margin-bottom: 1.1rem;
        }

        .sb-avatar {
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: linear-gradient(135deg, #35d68f, #0f6b4f);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin: 0 auto 0.6rem auto;
            box-shadow: 0 4px 14px rgba(53, 214, 143, 0.3);
        }

        .sb-title {
            font-weight: 700;
            font-size: 0.95rem;
            color: #ffffff !important;
        }

        .sb-subtitle {
            font-size: 0.75rem;
            color: #8fa3bf !important;
        }

        .sb-section-label {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 1px;
            color: #7be0b4 !important;
            text-transform: uppercase;
            margin: 1rem 0 0.5rem 0;
        }

        .sb-metric-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 0;
            font-size: 0.85rem;
            border-bottom: 1px dashed rgba(255,255,255,0.08);
        }

        .sb-metric-val {
            font-weight: 700;
            color: #35d68f !important;
        }

        .sb-badge {
            display: inline-block;
            background: rgba(53, 214, 143, 0.15);
            color: #7be0b4 !important;
            border: 1px solid rgba(53, 214, 143, 0.35);
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 600;
            margin-top: 4px;
        }

        section[data-testid="stSidebar"] code {
            background: rgba(255,255,255,0.08) !important;
            border-radius: 6px;
        }

        /* Fix low-contrast hyperparameter code box in sidebar */
        section[data-testid="stSidebar"] div[data-testid="stCode"],
        section[data-testid="stSidebar"] .stCodeBlock,
        section[data-testid="stSidebar"] pre {
            background: rgba(53, 214, 143, 0.08) !important;
            border: 1px solid rgba(53, 214, 143, 0.3) !important;
            border-radius: 10px !important;
        }

        section[data-testid="stSidebar"] pre code,
        section[data-testid="stSidebar"] pre code span {
            color: #b7f5d8 !important;
            background: transparent !important;
            -webkit-text-fill-color: #b7f5d8 !important;
        }

        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.1);
        }

        /* ---------- Sidebar animated progress bars ---------- */

        @keyframes growBar {
            0%   { width: 0%; }
            100% { width: var(--target-width); }
        }

        .sb-stat-block {
            margin-bottom: 0.85rem;
        }

        .sb-stat-top {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            margin-bottom: 4px;
        }

        .sb-stat-icon {
            margin-right: 6px;
        }

        .sb-stat-val {
            font-weight: 700;
            color: #35d68f !important;
        }

        .sb-bar-track {
            width: 100%;
            height: 6px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            overflow: hidden;
        }

        .sb-bar-fill {
            height: 100%;
            border-radius: 10px;
            background: linear-gradient(90deg, #0f6b4f, #35d68f);
            animation: growBar 1.4s ease-out forwards;
            background-size: 200% 100%;
        }

        /* ---------- Sidebar animated confidence ring ---------- */

        @keyframes spinRing {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes ringPulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(53, 214, 143, 0.35); }
            50%      { box-shadow: 0 0 0 10px rgba(53, 214, 143, 0); }
        }

        .sb-ring-wrap {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem 0 0.4rem 0;
        }

        .sb-ring {
            position: relative;
            width: 96px;
            height: 96px;
            border-radius: 50%;
            background: conic-gradient(#35d68f 0deg, #35d68f 299deg, rgba(255,255,255,0.1) 299deg);
            display: flex;
            align-items: center;
            justify-content: center;
            animation: ringPulse 2.4s ease-in-out infinite;
        }

        .sb-ring::before {
            content: "";
            position: absolute;
            width: 76px;
            height: 76px;
            border-radius: 50%;
            background: #0e2a4a;
        }

        .sb-ring-orbit {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            animation: spinRing 5s linear infinite;
        }

        .sb-ring-orbit::after {
            content: "";
            position: absolute;
            top: -3px;
            left: 50%;
            width: 8px;
            height: 8px;
            margin-left: -4px;
            border-radius: 50%;
            background: #ffffff;
            box-shadow: 0 0 6px 2px rgba(255,255,255,0.6);
        }

        .sb-ring-label {
            position: relative;
            z-index: 2;
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff !important;
        }

        .sb-ring-caption {
            font-size: 0.72rem;
            color: #8fa3bf !important;
            margin-top: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
    </style>
""", unsafe_allow_html=True)


# ====================================================
# LOAD MODEL & PREPROCESSOR
# ====================================================

@st.cache_resource
def load_model():
    model = joblib.load("customer_churn_model.pkl")
    preprocessor = joblib.load("customer_churn_preprocessor.pkl")
    return model, preprocessor


try:
    model, preprocessor = load_model()
    MODEL_LOADED = True
except Exception:
    MODEL_LOADED = False


# ====================================================
# HERO HEADER
# ====================================================

st.markdown("""
    <div class="hero-banner">
        <div class="hero-shape s1"></div>
        <div class="hero-shape s2"></div>
        <div class="hero-shape s3"></div>
        <div class="hero-content">
            <div class="hero-tag"><span class="live-dot"></span> TELECOM ANALYTICS • ML POWERED</div>
            <div class="hero-title">Customer Churn <span>Prediction Dashboard</span></div>
            <div class="hero-sub">
                Identify customers at risk of leaving before they do. Enter customer details
                below to get an instant, model-driven churn risk assessment with actionable
                retention insights.
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

if not MODEL_LOADED:
    st.warning(
        "⚠️ Model files (`customer_churn_model.pkl` / `customer_churn_preprocessor.pkl`) "
        "were not found in this directory. Place them alongside `app.py` to enable live predictions."
    )


# ====================================================
# SIDEBAR — MODEL INFO
# ====================================================

with st.sidebar:

    st.markdown("""
        <div class="sb-profile">
            <div class="sb-avatar">📉</div>
            <div class="sb-title">Churn Predictor</div>
            <div class="sb-subtitle">v1.0 · Production Model</div>
            <div class="sb-badge">🟢 Model Online</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section-label">Model Performance</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="sb-stat-block">
            <div class="sb-stat-top"><span><span class="sb-stat-icon">🎯</span>ROC-AUC Score</span><span class="sb-stat-val">0.83</span></div>
            <div class="sb-bar-track"><div class="sb-bar-fill" style="--target-width: 83%;"></div></div>
        </div>
        <div class="sb-stat-block">
            <div class="sb-stat-top"><span><span class="sb-stat-icon">✅</span>Accuracy</span><span class="sb-stat-val">80%</span></div>
            <div class="sb-bar-track"><div class="sb-bar-fill" style="--target-width: 80%;"></div></div>
        </div>
        <div class="sb-stat-block">
            <div class="sb-stat-top"><span><span class="sb-stat-icon">⚖️</span>Precision</span><span class="sb-stat-val">76%</span></div>
            <div class="sb-bar-track"><div class="sb-bar-fill" style="--target-width: 76%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section-label">Model Configuration</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="sb-metric-row"><span>⚙️ Algorithm</span><span class="sb-metric-val">Logistic Reg.</span></div>
        <div class="sb-metric-row"><span>📏 Scaling</span><span class="sb-metric-val">StandardScaler</span></div>
        <div class="sb-metric-row"><span>🔤 Encoding</span><span class="sb-metric-val">OneHotEncoder</span></div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section-label">Best Hyperparameters</div>', unsafe_allow_html=True)
    st.code("C = 0.1\nsolver = 'liblinear'", language="text")

    st.markdown('<div class="sb-section-label">Tech Stack</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="sb-metric-row"><span>🧩 Framework</span><span class="sb-metric-val">Streamlit</span></div>
        <div class="sb-metric-row"><span>🧠 ML Library</span><span class="sb-metric-val">Scikit-learn</span></div>
        <div class="sb-metric-row"><span>📊 Charts</span><span class="sb-metric-val">Plotly</span></div>
    """, unsafe_allow_html=True)

    # Animated confidence ring — sits at the very bottom of the sidebar
    st.markdown("""
        <div class="sb-ring-wrap">
            <div class="sb-ring">
                <div class="sb-ring-orbit"></div>
                <div class="sb-ring-label">83%</div>
            </div>
            <div class="sb-ring-caption">Model Confidence</div>
        </div>
    """, unsafe_allow_html=True)

    st.caption("© 2026 · Customer Churn Analytics")


# ====================================================
# INPUT FORM — CUSTOMER INFORMATION
# ====================================================

customer_info_box = st.container(border=True)
with customer_info_box:
    st.markdown('<div class="card-anchor"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title"><span class="section-icon-chip">👤</span> Customer Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (Months)", min_value=0, max_value=72, value=12)

    with col2:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

    with col3:
        tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

    # Quick live snapshot strip — makes the card feel less like a bare form
    active_addons = sum([
        online_security == "Yes", online_backup == "Yes", device_protection == "Yes",
        tech_support == "Yes", streaming_tv == "Yes", streaming_movies == "Yes"
    ])
    snap1, snap2, snap3 = st.columns(3)
    snap1.markdown(
        f'<div class="mini-stat"><span class="mini-stat-icon">📄</span>'
        f'<div><div class="mini-stat-label">Contract Type</div>'
        f'<div class="mini-stat-val">{contract}</div></div></div>',
        unsafe_allow_html=True
    )
    snap2.markdown(
        f'<div class="mini-stat"><span class="mini-stat-icon">🧩</span>'
        f'<div><div class="mini-stat-label">Add-ons Active</div>'
        f'<div class="mini-stat-val">{active_addons} / 6</div></div></div>',
        unsafe_allow_html=True
    )
    snap3.markdown(
        f'<div class="mini-stat"><span class="mini-stat-icon">⏱️</span>'
        f'<div><div class="mini-stat-label">Tenure</div>'
        f'<div class="mini-stat-val">{tenure} months</div></div></div>',
        unsafe_allow_html=True
    )


# ====================================================
# BILLING + ADDITIONAL FEATURES
# ====================================================

col_billing, col_extra = st.columns([1.3, 1])

with col_billing:
    billing_box = st.container(border=True)
    with billing_box:
        st.markdown('<div class="card-anchor"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-title"><span class="section-icon-chip">💳</span> Billing Information</div>',
            unsafe_allow_html=True
        )

        b1, b2, b3 = st.columns(3)

        with b1:
            payment_method = st.selectbox(
                "Payment Method",
                ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
            )

        with b2:
            monthly_charges = st.number_input("Monthly Charges (PKR)", min_value=0.0, value=70.0, step=1.0)

        with b3:
            total_charges = st.number_input("Total Charges (PKR)", min_value=0.0, value=1000.0, step=10.0)

with col_extra:
    extra_box = st.container(border=True)
    with extra_box:
        st.markdown('<div class="card-anchor"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-title"><span class="section-icon-chip">📈</span> Additional Features</div>',
            unsafe_allow_html=True
        )

        satisfaction_score = st.slider("Satisfaction Score", min_value=1, max_value=5, value=3)
        total_services = st.slider("Total Services Subscribed", min_value=0, max_value=6, value=2)

        if tenure <= 6:
            tenure_group = "New"
        elif tenure <= 24:
            tenure_group = "Short-term"
        elif tenure <= 48:
            tenure_group = "Medium-term"
        else:
            tenure_group = "Long-term"

        st.info(f"📅 Tenure Group: **{tenure_group}**")


# ====================================================
# BUILD CUSTOMER DATAFRAME
# ====================================================

customer_data = pd.DataFrame({
    "Gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "Tenure": [tenure],
    "PhoneService": [phone_service],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],
    "SatisfactionScore": [satisfaction_score],
    "TenureGroup": [tenure_group],
    "TotalServices": [total_services]
})


# ====================================================
# PREDICTION
# ====================================================

st.markdown("<br>", unsafe_allow_html=True)
predict_clicked = st.button("🚀  Predict Customer Churn", use_container_width=True)

if predict_clicked:

    if not MODEL_LOADED:
        st.error("Model files not found — cannot generate a prediction. Add the `.pkl` files and rerun.")
    else:
        customer_processed = preprocessor.transform(customer_data)
        prediction = model.predict(customer_processed)[0]
        probability = model.predict_proba(customer_processed)[0][1]
        retention_probability = 1 - probability
        status = "High Churn Risk" if prediction == 1 else "Low Churn Risk"

        st.markdown("<br>", unsafe_allow_html=True)
        result_box = st.container(border=True)
        with result_box:
            st.markdown('<div class="card-anchor"></div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="section-title"><span class="section-icon-chip">🔮</span> Prediction Result</div>',
                unsafe_allow_html=True
            )

            badge_class = "badge-risk-high" if prediction == 1 else "badge-risk-low"
            badge_text = "⚠️ Likely to Churn" if prediction == 1 else "✅ Unlikely to Churn"
            st.markdown(f'<span class="{badge_class}">{badge_text} — {status}</span>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # KPI Cards
            k1, k2, k3, k4 = st.columns(4)

            with k1:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Prediction</div>
                        <div class="kpi-value {'kpi-red' if prediction == 1 else 'kpi-green'}">
                            {"Churn" if prediction == 1 else "No Churn"}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            with k2:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Churn Probability</div>
                        <div class="kpi-value kpi-red">{probability * 100:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)

            with k3:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Retention Probability</div>
                        <div class="kpi-value kpi-green">{retention_probability * 100:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)

            with k4:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-label">Monthly Revenue</div>
                        <div class="kpi-value">PKR {monthly_charges:,.0f}</div>
                    </div>
                """, unsafe_allow_html=True)

        # ------------------------------------------------
        # CHARTS
        # ------------------------------------------------
        chart_box = st.container(border=True)
        with chart_box:
            st.markdown('<div class="card-anchor"></div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="section-title"><span class="section-icon-chip">📊</span> Risk Breakdown</div>',
                unsafe_allow_html=True
            )

            chart_col1, chart_col2 = st.columns([1, 1])

            with chart_col1:
                gauge_fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    number={'suffix': "%", 'font': {'size': 36, 'color': "#0b1f3a"}},
                    gauge={
                        'axis': {'range': [0, 100], 'tickcolor': "#0b1f3a"},
                        'bar': {'color': "#d64545" if probability >= 0.5 else "#0f9d63"},
                        'bgcolor': "white",
                        'steps': [
                            {'range': [0, 40], 'color': "#eafaf1"},
                            {'range': [40, 70], 'color': "#fff6e0"},
                            {'range': [70, 100], 'color': "#fdecec"}
                        ],
                        'threshold': {
                            'line': {'color': "#0b1f3a", 'width': 3},
                            'thickness': 0.8,
                            'value': probability * 100
                        }
                    },
                    title={'text': "Churn Risk Meter", 'font': {'size': 14, 'color': "#6b7688"}}
                ))
                gauge_fig.update_layout(height=280, margin=dict(l=20, r=20, t=50, b=10))
                st.plotly_chart(gauge_fig, use_container_width=True)

            with chart_col2:
                bar_fig = px.bar(
                    x=["Retention Probability", "Churn Probability"],
                    y=[retention_probability * 100, probability * 100],
                    color=["Retention", "Churn"],
                    color_discrete_map={"Retention": "#0f9d63", "Churn": "#d64545"},
                    text=[f"{retention_probability*100:.1f}%", f"{probability*100:.1f}%"]
                )
                bar_fig.update_traces(textposition="outside")
                bar_fig.update_layout(
                    height=280,
                    showlegend=False,
                    xaxis_title="",
                    yaxis_title="Probability (%)",
                    margin=dict(l=20, r=20, t=30, b=10),
                    plot_bgcolor="white"
                )
                st.plotly_chart(bar_fig, use_container_width=True)

        st.caption("Prediction generated using the trained Logistic Regression model.")


# ====================================================
# MODEL INFORMATION (BOTTOM EXPANDER)
# ====================================================

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("ℹ️ About This Model"):
    st.markdown("""
    | Detail | Value |
    |---|---|
    | **Algorithm** | Logistic Regression |
    | **Preprocessing** | ColumnTransformer |
    | **Numerical Processing** | StandardScaler |
    | **Categorical Processing** | OneHotEncoder |
    | **ROC-AUC** | 0.83 |
    | **Best Parameters** | C = 0.1, solver = liblinear |
    """)

st.markdown(
    '<div class="footer-note">Customer Churn Prediction Dashboard · Built with Streamlit, Scikit-learn & Plotly</div>',
    unsafe_allow_html=True
)