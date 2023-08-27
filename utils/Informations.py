import streamlit as st

def Authors():
    st.title("Authors")
    # st.markdown("""
    #     1. Le Bao Long longle12042006a@gmail.com            
    # """)    

def Changelog():
    st.title("Changelog")
    
    
def Resources():
    st.title("Resources")
    
    
def sidebarConfig(sidebar) -> None:
    with sidebar:
        pass


def Informations(sidebar):
    sidebarConfig(sidebar)
    
    Authors()
    st.markdown("#")
    st.divider()
    Changelog()
    st.markdown("#")
    st.divider()
    Resources()
    
    
    