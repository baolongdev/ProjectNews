from streamlit_elements import *
import streamlit as st
from modules import *
from datetime import datetime
def sidebarConfig(sidebar):
    with sidebar:
        pass

def main():
    news_db = UserDatabase("News")
    news = news_db.fetch_all_users()
    list_news = st.empty()
    if 'open_news' not in st.session_state:
        open_news = None
    else:
        open_news = st.session_state.open_news
    if open_news is None:
        with list_news.container():
            Custom_Code(st, """
                <div class="main__title"> 
                    <h3> Ở đây có thông tin hót <h3>
                <div/>        
            """)
            for i, new in enumerate(news):
                title = new['key']
                subtitle = new['subtitle']
                content = new['content']
                image = new['banner']
                show(title, subtitle, image, content, i)
    else:
        with list_news.container():
            data = news_db.get_user(open_news["key"])
            with elements("toppage"):
                with mui.IconButton(
                        size="medium", 
                        color="success",
                        onClick=lambda : (
                            update_open_news(),
                        )
                    ):
                        mui.icon.KeyboardArrowLeft()
                with mui.Typography():
                    html.h2(data["key"], css={"textAlign":"center"})
            setup_quill(open_news["content"])
            with elements("endpage"):
                mui.Divider("End")
                with html.div(
                    css={
                        "display": "flex",
                        "justifyContent": "space-between",
                        "alignItems": "flex-start"
                    }
                ):
                    with mui.Button(
                        size="medium", 
                        color="primary",
                        onClick=lambda : (
                            update_open_news(),
                        )
                        
                    ):
                        mui.Typography("Quay trở lại")
                    with html.div(
                        css={
                            "display": "flex",
                            "flexDirection": "column",
                            "alignItems": "flex-end",
                        }
                    ):
                        time_obj = datetime.strptime(data["date_joined"], "%Y-%m-%d %H:%M:%S.%f")
                        date_format = "%d %b %Y %H:%M"
                        formatted_time = time_obj.strftime(date_format)
                        with mui.Button(size="medium", color="success",):
                            mui.icon.AccessTime()
                            mui.Typography(" "+formatted_time)
                            
                        with mui.Button(
                            size="medium", 
                            color="success",                    
                        ):
                            mui.icon.Visibility()
                            mui.Typography(" : 100")
                    
            pass

def Documentation(sidebar):
    sidebarConfig(sidebar)
    # st.title("Documentation")
    main()