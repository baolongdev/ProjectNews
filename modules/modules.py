from streamlit_elements import *
from modules.controls import *
from modules.database import *
import streamlit as st

def InitPageSetting(st, path, PAGE_NAME, PAGE_ICON, name_file_css="", name_file_js=""):
    current_dir = path
    CSS_MAIN = current_dir / "assets" / "styles" / "main.css"
    js_MAIN = current_dir / "assets" / "js" / "main.js"
    st.set_page_config(PAGE_NAME, PAGE_ICON)
    # Custom_Code(st, """
    #     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"/>            
    # """)
    if name_file_css:
        css_file = current_dir/"assets" / "styles" / name_file_css
        Custom_CSS(st, CSS_MAIN)
        Custom_CSS(st, css_file)
    else:
        Custom_CSS(st, CSS_MAIN)

    if name_file_js:
        js_file = current_dir/"assets" / "js" / name_file_js
        Custom_JS(st, js_MAIN)
        Custom_JS(st, js_file)
    else:
        Custom_JS(st, js_MAIN)


def Custom_CSS(st, css_file):
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)


def Custom_Code(st, data):
    st.markdown(data, unsafe_allow_html=True)


def Custom_JS(st, js_file):
    with open(js_file) as f:
        st.markdown("<script>{}</script>".format(f.read()),
                    unsafe_allow_html=True)


def Custom_Title(st, title):
    st.subheader(title)
    st.markdown("#")

    
def readClick(event, title, subtitle):
    print("\n"*5)
    print(f"Clicked on: Title - {title}, Subtitle - {subtitle}")

def handleButtonClick(title):
    print("test", title)
    print("tét")
    
def update_open_news(title=None, content=None):
    if title is None or content is None:
        st.session_state['open_news'] = None
    else:
        st.session_state['open_news'] = {"key": title, "content": content}
def show(title, subtitle, banner, content=None, key="card", btnDelete=False):
    with elements(key):
        with mui.Card( ):
            with mui.CardActionArea():
                mui.CardMedia(
                    component="img",
                    height={"300"},
                    image=banner,
                    alt="image error",
                )
                with mui.CardContent():
                    mui.Typography(title, gutterBottom=True, variant="h5", component="div")
                    mui.Typography(subtitle, variant="body2", color="text.secondary")
                pass
            with mui.Paper(
                sx={
                    "display": "flex",
                    "flexDirection": "row",
                    "justifyContent": "flex-end",
                }
                
            ):
                if btnDelete:
                    news_db = UserDatabase("News")
                    with mui.IconButton(
                        size="medium", 
                        color="error",
                        onClick=lambda : (
                            news_db.delete_user(title),
                            st.toast("Delete success")
                        )
                    ):
                        mui.icon.Delete()
                else:
                    with mui.Button(
                        size="medium", 
                        color="primary"
                    ):
                        mui.icon.Share()
                        mui.Typography("Share")
                    with mui.Button(
                        size="medium", 
                        color="primary",
                        onClick=lambda : (
                            update_open_news(title, content)
                        )
                        
                    ):
                        mui.Typography("Read")
                        # print(f"Button clicked: title={title}, subtitle={subtitle}")
                pass
            
            
def setup_quill(content):
    current_dir = get_from_control_reference("current_dir")
    style_quill = current_dir / "assets" / "styles" / "quill.css"
    Custom_CSS(st, style_quill)
    st.markdown(content.replace("&lt;", "<").replace("&gt;", ">"), unsafe_allow_html=True)