## NLP App Theatre Reviews

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
        VerIficaTion of A MultI ageNt system  🧪
        """
    )
    st.markdown("     ")




    selected_indices = []
    master_review = "DEFAULT REVIEW - This is the season in which theatres revisit their histories. In the crumbling glory of Wilton’s Music Hall, east London, Fiona Shaw is reprising her wild version of The Waste Land, talking about death in the City, with the aid of Music Hall voices. Hackney Empire has burst into its traditional life with rousing panto. Meanwhile, the Orange Tree is producing The Lady or the Tiger, which had its premiere at the theatre in 1975 and was revived there in 1989. Now it’s back again; I wish it wasn’t. Based on a whimsical 1882 story by Frank Stockton, the show has words by Michael Richmond and Jeremy Paul and music by Nola York, who once sang with the Chantelles and was the first woman to write a complete score for a West End musical. It has a few good mots, a dash of sauce, but hardly any point It features one despotic ruler who follows his subjects’ every wiggle “from sperm to worm”, one reluctantly virgin daughter (“Think of your position”; “I am, I wish it was horizontal”), one drippy suitor and one multipurpose character who flips from role to role by changing his hat. Riona O’Connor has a suitably 70s Lulu-like shout of a voice but does too much gurgling to be really convincing as a grown-up: she sings better than she swings. As the naughty king - ooh what a scamp that tyrant is - Howard Samuels dispenses oeillades, pecks on the cheeks and pats on the knees to the ladies in the front row. Sam Walters’s production is almost eerily pleasant. It’s like a panto that doesn’t yell but quietly chortles."









    index_review = 0

    st.markdown(
        """
        [<img src='data:image/png;base64,{}' class='img-fluid' width=25 height=25>](https://github.com/hi-paris/agent-theory) <small> agent-theory 0.0.1 | September 2022</small>""".format(
            img_to_bytes("./images/github.png")
        ),
        unsafe_allow_html=True,
    )
    if 'page' not in st.session_state:
      st.session_state.page=1
    st.sidebar.header("Dashboard")
    st.sidebar.markdown("---")
    if st.sidebar.button('Cases Studies'):
      st.session_state.page=1
    if st.sidebar.button('Model Cheking for MAS'):
      st.session_state.page=2
    if st.sidebar.button('Model and Strategy'):
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



