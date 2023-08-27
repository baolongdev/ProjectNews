import pathlib
import streamlit as st
from modules import *
from utils import *


def App(current_dir):
    css__custom = current_dir / "assets" / "styles" / "custom.css"
    Custom_CSS(st, css__custom)
    Sidebar(current_dir)
    pass


if __name__ == '__main__':
    # add path main
    current_dir = pathlib.Path(__file__).parent.resolve()
    add_to_control_reference("current_dir", current_dir)
    InitPageSetting(st, current_dir, "doantruongctdnhotnews", "⭐")
    App(current_dir)