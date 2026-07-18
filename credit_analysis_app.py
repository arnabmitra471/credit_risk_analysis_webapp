import streamlit as st
import joblib
st.set_page_config(page_title="Credit Risk intelligence dashboard",
                   page_icon="🔐",
                   initial_sidebar_state="expanded",layout="wide")

st.markdown("""
            <style>
            .main-title{
                font-size: 2.5rem;
                font-weight: bold;
                color: #1E3A8A;
            
            }
            .subtitle { font-size: 1.1rem; 
            color: #4B5563; 
            margin-bottom: 25px; 
            }
            div[data-testid="stMetricValue"] { font-size: 2rem; font-weight: 700; color: #1E3A8A; }
            </style>
            """,unsafe_allow_html=True)

st.markdown('<div class="main-title">Credit risk intelligence and ensemble analytics dashboard</div>',unsafe_allow_html=True)
st.markdown('<div class="subtitle">An interactive deployment showcasing structural feature transformations, operational evaluation cutoffs, and transparent Random Forest tree tracking.</div>', unsafe_allow_html=True)

# Loading the resources
@st.cache_resource
def load_pipeline_assets():
    try:
        rf_model = joblib.load("final_rf_model.pkl")
        preprocessor = joblib.load("preprocessor_pipeline.pkl")
        feature_selector = joblib.load("feature_selector.pkl")
        return rf_model,preprocessor,feature_selector
    except:
        return None,None,None
final_rf,preprocessor,selector = load_pipeline_assets()

st.sidebar.header("Control Panel")
app_mode = st.sidebar.radio("Navigate Workspace",["Single applicant","Random forest structural inspector"])

if app_mode == "Single applicant":
    pass
else:
    pass



