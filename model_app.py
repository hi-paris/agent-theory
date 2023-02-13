
### Import packages
import os
from pathlib import Path
import base64
import numpy as np

import graphviz

from PIL import Image, ImageDraw, ImageFont
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

import streamlit as st

from class_game import *
from back_end_CS import *
from front_end_CS import *

global page
st.set_page_config(
    page_title="Agent Theory", layout="wide", page_icon="images/flask.png"
)

### methods used within streamlit - to organize later on 


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

###Cases Studies

def display_page(page):
  if page==2:
    display_MCMAS()
  elif page==3:
    display_MS()
  else:
    nlp_steps = st.selectbox(' ', ['01 - Initialization',
                                        '02 - Strategy Example', '03 - ICGS','04 - Dining Cryptographers',
                                        '05 - Buchi  Automaton', '06 - Upload Configuration'])
    display_case(nlp_steps)

### Main Front

def main():
    def _max_width_():
        max_width_str = f"max-width: 1000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )


    # Hide the Streamlit header and footer
    def hide_header_footer():
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # increases the width of the text and tables/figures
    _max_width_()

    # hide the footer
    hide_header_footer()

    st.markdown("# VITAMIN 🔍 🖥")
    st.subheader(
        """
        VerIficaTion viA MultI ageNt system  🧪
        """
    )
    st.markdown("     ")




    selected_indices = []


    index_review = 0

    st.markdown(
        """
        [<img src='data:image/png;base64,{}' class='img-fluid' width=25 height=25>](https://github.com/hi-paris/agent-theory) <small> agent-theory 0.0.1 | September 2022</small>""".format(
            img_to_bytes("./images/github.png")
        ),
        unsafe_allow_html=True,
    )
    #Useful Session State
    if 'info_model' not in st.session_state:
      st.session_state.info_model=[]
    if 'cmpt_model' not in st.session_state:
      st.session_state.cmpt_model=0
    if 'page' not in st.session_state:
      st.session_state.page=1
    st.sidebar.header("Dashboard")
    st.sidebar.markdown("---")
    if st.sidebar.button('Cases Studies'):
      st.session_state.page=1
    if st.sidebar.button('Part for Devlopement '):
      st.session_state.page=2
      st.session_state.cmpt_model=-1
      st.session_state.info_model_test=[]
    if st.sidebar.button('Model Cheking for MAS'):
      st.session_state.cmpt_model=0
      st.session_state.info_model=[]
      st.session_state.mat_transi=[]
      st.session_state.page=3
    display_page(st.session_state.page)

    
    




if __name__=='__main__':
    main()

st.markdown(" ")
st.markdown("### ** 👨🏼‍💻 Télécom Paris Researcher: **")
st.image(['images/1.png'], width=230,caption=["Vadim Malvone"])

st.markdown('### Made by Hi!Paris')
images = Image.open('./images/hi-paris.png')
st.image(images, width=250)
st.write('    ')
st.markdown('### Contributors:')
PA=Image.open('./images/PA.jpg')
Pierre=Image.open('./images/Pierre.jpg')
GAE=Image.open('./images/gaetan.png')
st.image([PA,GAE,Pierre],width=110)



st.markdown(f"####  Link to Project Website [here]({'https://github.com/hi-paris/agent-theory'}) 🚀 ")



def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;background - color: white}
     .stApp { bottom: 80px; }
    </style>
    """
    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1,

    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer2():
    myargs = [
        " Made by ",
        link("https://engineeringteam.hi-paris.fr/", "Hi! PARIS Engineering Team"),
        " 👩🏼‍💻 👨🏼‍💻"
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer2()



