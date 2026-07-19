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
app_mode = st.sidebar.radio("Navigate Workspace",["Single applicant mode","Random forest structural inspector mode"])

# Helper column lists for reconstruction
ordinal_cols = ["Saving accounts","Checking Account"]
categorical_cols = ["Sex","Housing","Purpose"]
numeric_cols = ["Age","Credit amount","Duration"]

if app_mode == "Single applicant mode":
    st.subheader("Live Applicant Profiling")
    with st.expander("Open applicant metrics entry form"):
        row_1_1,row_1_2,row_1_3 = st.columns(3)
        with row_1_1:
            age = st.number_input("Enter your age",min_value=18,max_value=100)
            sex = st.selectbox("Biological sex",options=["male","female"])
        with row_1_2:
            duration = st.number_input("Loan duration(Months)",min_value=4,max_value=72,value=24)
            housing = st.selectbox("Housing Tenure Status",options=["own","rent","free"])
        with row_1_3:
            credit_amount = st.number_input("Enter your loan amount",min_value=250,max_value=20000,step=50)
            purpose = st.selectbox("Select your loan purpose",options=["car","radio/TV","business","furniture/equipment","education","repairs","vacation/others"])
        st.markdown("**Hierarchical risk tiering**")
        
        row_2_1,row_2_2,row_2_3 = st.columns(3)
        with row_2_1:
            saving_accounts = st.selectbox("Savings balance tier",options=["none","little","moderate","quite rich","rich"])
        with row_2_2:
            checking_acount = st.selectbox("Checking account liquidity tier",options=["none","little","moderate","quite rich","rich"])
        with row_2_3:
            job = st.selectbox("Employment status",options=[0,1,2,3],format_func= lambda x: {0: "0: Unskilled/ Non resident",1:"1: Unskilled/Resident",2: "2: Skilled staff",3: "3: Highly silled"}[x])

        
        
        
else:
    pass



