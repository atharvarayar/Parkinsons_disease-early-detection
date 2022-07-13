import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('model2.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

def prediction(MDVP_fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
       MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
       MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA,
       spread1, spread2, D2):
    
    prediction = classifier.predict( 
        [[MDVP_fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
       MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
       MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA,
       spread1, spread2, D2]])
     
    if prediction == 0:
        pred = 'Patient is Healthy'
    else:
        pred = 'Patient should consult with a Neuorologist'
    return pred
    
    
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Parkinsons Prediction ML App</h1> 
    </div> 
    
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    MDVP_fo=st.number_input("MDVP:Fo(Hz)", step=1e-6,format="%.5f")
    MDVP_Fhi=st.number_input("MDVP:Fhi(Hz)", step=1e-6,
    format="%.5f",key="0")
    MDVP_Flo= st.number_input("MDVP:Flo(Hz)", step=1e-6,
    format="%.5f", key="1")
    MDVP_Jitter= st.number_input("MDVP:Jitter(%)",key="2",  step=1e-6,
    format="%.5f")
    MDVP_Jitter_Abs= st.number_input("MDVP:Jitter(Abs)",key="3", step=1e-6,
    format="%.5f")
    MDVP_RAP= st.number_input("MDVP:RAP",key="4", step=1e-6,
    format="%.5f")
    MDVP_PPQ= st.number_input("MDVP:PPQ",key="5",  step=1e-6,
    format="%.5f")
    Jitter_DDP=st.number_input("Jitter:DDP",key="6", step=1e-6,
    format="%.5f")
    MDVP_Shimmer= st.number_input("MDVP:Shimmer",key="7", step=1e-6,
    format="%.5f")
    MDVP_Shimmer_dB= st.number_input("MDVP:Shimmer(dB)",key="8", step=1e-6,
    format="%.5f")
    Shimmer_APQ3= st.number_input("Shimmer:APQ3",key="9", step=1e-6,
    format="%.5f")
    Shimmer_APQ5=st.number_input("Shimmer:APQ5",key="10", step=1e-6,
    format="%.5f")
    MDVP_APQ= st.number_input("MDVP:APQ",key="11", step=1e-6,
    format="%.5f")
    Shimmer_DDA= st.number_input("Shimmer:DDA",key="12", step=1e-6,
    format="%.5f")
    NHR= st.number_input("NHR",key="13", step=1e-6,
    format="%.5f")
    HNR= st.number_input("HNR",key="14", step=1e-6,
    format="%.5f")
    RPDE= st.number_input("RPDE",key="16", step=1e-6,
    format="%.5f")
    DFA=st.number_input("DFA",key="17", step=1e-6,
    format="%.5f")
    spread1= st.number_input("Spread1",key="18", step=1e-6,
    format="%.5f")
    spread2= st.number_input("Spread2",key="19", step=1e-6,
    format="%.5f")
    D2= st.number_input("D2",key="20", step=1e-6,
    format="%.5f")
    #PPE=st.number_input("PPE",key="21")
    
    if st.button("Predict"): 
        result =prediction(MDVP_fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
       MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
       MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA,
       spread1, spread2, D2)    
        st.success(result)
    
if __name__=='__main__': 
    main()
    
    