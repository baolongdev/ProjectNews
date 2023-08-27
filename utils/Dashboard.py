import time
import streamlit as st
from modules import *
import streamlit_authenticator as stauth
from streamlit_quill import st_quill

def sidebarConfig(sidebar):
    with sidebar:
        pass

def customsGroup():
    current_dir = get_from_control_reference("current_dir")
    css__custom = f'{current_dir}/assets/styles/custom.css'
    Custom_CSS(st, css__custom)
    Custom_Code(st, """
            <div class="main__title"> 
                <h3> Bảng điều khiển <h3>
            <div/>        
        """)


def sign_in():    
    user_db = UserDatabase("StreamlitAuth")
    users = user_db.fetch_all_users()
    # hashed_passwords = stauth.Hasher(["doantruong123"]).generate()
    # user_db.insert_user("doantruong", "doantruong", hashed_passwords[0])
    
    credentials = {"usernames":{}}
    for i, user in enumerate(users):
        credentials['usernames'][user['name']] = {'name': user['name'], 'password': user['password']}
    Authenticator = stauth.Authenticate(credentials, cookie_name="streamlit", key="abcdef", cookie_expiry_days=4)
    email, authentication_status, username = Authenticator.login(":green[login]", 'main')
    if authentication_status:
        main()
        Authenticator.logout('Logout', 'main')
    elif authentication_status == False:
        st.error("""
            Username/password is incorrect \n
            Vui lòng liên hệ Quản trị để được hỗ trợ
        """)
    elif authentication_status == None:
        st.warning("""
            Please enter your username and password       
        """)
    

def main():
    t1, t2, t3 = st.tabs(["editor", "preview", "Danh sách bài viết"])
    with t1:
        with st.container():
            title = st.text_input('Title', placeholder="")
            subtitle = st.text_area('Subtitle', placeholder="")
            image = st.text_input('link image', placeholder="")
                
        content = st_quill(
            placeholder="Write your text here",
            html=True,
            key="quill",
            toolbar=[
                [
                    {"header": [1, 2, 3, 4, 5, 6, False]},
                    {"size": ["small", False, "large", "huge"]},
                ],
                [
                    "bold", "italic", "underline", "strike",
                ],
                [
                    {"color": [] },
                    {"background": []},
                ],          
                [
                    {"script": "sub"},
                    {"script": "super"},
                ],
                [
                    {"header": 1},
                    {"header": 2},
                    "blockquote", "code", "code-block", "clean"
                ],
                [
                    {"list": "ordered"},
                    {"list": "bullet"},
                    {"indent": "-1"},
                    {"indent": "+1"},
                    { 'direction': 'rtl' },
                    {"align": []},
                ],
                [
                    "link", "image","video","formula", 
                ],
                [
                    {"font": []}
                ],
            ]
        )
        if content and st.checkbox("show code"):
            st.write(content)
        
    with t2:
        show(title, subtitle, image)
        if content:
            setup_quill(content)
            btn_upload = st.button("upload")
            if btn_upload:
                data = UserDatabase("News")
                data.insert_news(title, subtitle, image, content)
                st.toast("upload success")

    with t3:
        news_db = UserDatabase("News")
        news = news_db.fetch_all_users()
        for i, new in enumerate(news):
            title = new['key']
            subtitle = new['subtitle']
            content = new['content']
            image = new['banner']
            show(title, subtitle, image, content, i, True)
        pass
    

def Dashboard(sidebar):
    sidebarConfig(sidebar)
    customsGroup()
    sign_in()