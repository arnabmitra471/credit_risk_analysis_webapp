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

uploaded_model = st.sidebar.file_uploader("Upload random forest model(.pkl)",type=[".pkl"])
uploaded_preprocessor = st.sidebar.file_uploader("Upload Preprocessor(.pkl)",type=[".pkl"])
uploaded_feat_selector = st.sidebar.file_uploader("Upload Feature Selector(.pkl)",type=[".pkl"])
# Loading the resources
@st.cache_resource
def load_updated_pipeline(model_file,prep_file,sel_file):
    try:
        rf_model = joblib.load(model_file)
        preprocessor = joblib.load(prep_file)
        feature_selector = joblib.load(sel_file)
        return rf_model,preprocessor,feature_selector
    except Exception as e:
        return None,None,None
if uploaded_model and uploaded_feat_selector and uploaded_feat_selector:
    final_rf,preprocessor,selector = load_updated_pipeline(uploaded_model,uploaded_preprocessor,uploaded_feat_selector)
    st.sidebar.success("All three pipeline assets loaded into memory")
else:
    final_rf,preprocessor,selector = None,None,None
    st.sidebar.info("Please upload all the 3 .pkl files to unlock the full experience")

st.sidebar.header("Control Panel")
app_mode = st.sidebar.radio("Navigate Workspace",["Single applicant","Random forest structural inspector"])

if app_mode == "Single applicant":
    pass
else:
    pass



