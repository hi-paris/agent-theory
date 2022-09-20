## NLP App Theatre Reviews

### Import packages

import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import json
import ast
from PIL import Image
from PIL import Image, ImageDraw, ImageFont

from pathlib import Path


from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

from pathlib import Path
import base64
import time

import numpy as np
import matplotlib as mp
from visual_automata.fa.dfa import VisualDFA





st.set_page_config(
    page_title="Agent Theory", layout="wide", page_icon="./images/flask.png"
)





def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded



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

    images = Image.open('./images/hi-paris.png')
    st.image(images, width=400)

    st.markdown("# Behind the Agent Theory 🔍 🖥")
    st.subheader(
        """
        This is a place where you can get familiar with the Agent Theory  🧪
        """
    )
    st.markdown("     ")




    selected_indices = []
    master_review = "DEFAULT REVIEW - This is the season in which theatres revisit their histories. In the crumbling glory of Wilton’s Music Hall, east London, Fiona Shaw is reprising her wild version of The Waste Land, talking about death in the City, with the aid of Music Hall voices. Hackney Empire has burst into its traditional life with rousing panto. Meanwhile, the Orange Tree is producing The Lady or the Tiger, which had its premiere at the theatre in 1975 and was revived there in 1989. Now it’s back again; I wish it wasn’t. Based on a whimsical 1882 story by Frank Stockton, the show has words by Michael Richmond and Jeremy Paul and music by Nola York, who once sang with the Chantelles and was the first woman to write a complete score for a West End musical. It has a few good mots, a dash of sauce, but hardly any point It features one despotic ruler who follows his subjects’ every wiggle “from sperm to worm”, one reluctantly virgin daughter (“Think of your position”; “I am, I wish it was horizontal”), one drippy suitor and one multipurpose character who flips from role to role by changing his hat. Riona O’Connor has a suitably 70s Lulu-like shout of a voice but does too much gurgling to be really convincing as a grown-up: she sings better than she swings. As the naughty king - ooh what a scamp that tyrant is - Howard Samuels dispenses oeillades, pecks on the cheeks and pats on the knees to the ladies in the front row. Sam Walters’s production is almost eerily pleasant. It’s like a panto that doesn’t yell but quietly chortles."


   # def file_select(folder='./datasets'):
   #     filelist = os.listdir(folder)
   #     selectedfile = st.sidebar.selectbox('', filelist)
   #     return os.path.join(folder, selectedfile)







    index_review = 0

    st.markdown(
        """
        [<img src='data:image/png;base64,{}' class='img-fluid' width=25 height=25>](https://github.com/hi-paris/agent-theory) <small> agent-theory 0.0.1 | September 2022</small>""".format(
            img_to_bytes("./images/github.png")
        ),
        unsafe_allow_html=True,
    )


    st.sidebar.header("Dashboard")
    st.sidebar.markdown("---")

    st.sidebar.header("01 - Select Approach")
    nlp_steps = st.sidebar.selectbox('', ['01 - Buchi  Automaton',
                                          '02 - Approach 02', '03 - Approach 03','04 - Approach 04',
                                          '05 - Approach 05'])
    st.sidebar.header("02 - Select Parameters")

    with open('data/test.txt', 'r') as f:
        s = f.read()
        input_ast_format = ast.literal_eval(s)


    input_initial_state = st.sidebar.selectbox(
    'Select initial state:',
    list(input_ast_format.keys()))


    input_final_states = st.sidebar.multiselect(
    'Select final states:',
    list(input_ast_format.keys()),list(np.random.choice(list(input_ast_format.keys()),2)))


    st.sidebar.header("03 - Upload Txt File with config")


    def file_select(folder='./data'):
        filelist=os.listdir(folder)
        st.sidebar.markdown("OR")
        selectedfile=st.sidebar.selectbox('Select a default dataset',filelist)
        return os.path.join(folder,selectedfile)
        

    st.sidebar.button('Upload Data')
    uploaded_file=st.sidebar.file_uploader('Upload Dataset in .txt',type=['TXT'])
    if uploaded_file is not None:
        st.write('hello world')


    else:
        filename=file_select()
        st.sidebar.info('You selected {}'.format(filename))
        with open('data/test.txt', 'r') as f:
            s = f.read()
            input_ast_format = ast.literal_eval(s)




    st.markdown("---")
    st.write(f"                                          ")
    if nlp_steps == "01 - Buchi  Automaton":

        st.header("01 - Buchi  Automaton")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
        st.write(f"                                          ")


        dfa = VisualDFA(
        states={"q0", "q1", "q2", "q3", "q4"},
        input_symbols={"0", "1"},
        transitions=input_ast_format,
        initial_state=input_initial_state,
        final_states=set(input_final_states),
        )
        
        st.markdown('#### ii - Diagram: ')
        digraph_output = dfa.show_diagram("101")
        st.graphviz_chart(digraph_output)

        st.markdown('#### iii - Input Table: ')
        digraph_table = dfa.input_check("10011")
        st.table(digraph_table)
  

        snippet = f"""
        dfa = VisualDFA(
        states={"q0", "q1", "q2", "q3", "q4"},
        input_symbols={"0", "1"},
        transitions=input_ast_format,
        initial_state=input_initial_state,
        final_states=set(input_final_states),
        )
    
    
        """
        code_header_placeholder = st.empty()
        snippet_placeholder = st.empty()
        code_header_placeholder.subheader(f"**Code for the step: 01 - Buchi  Automaton**")
        snippet_placeholder.code(snippet)
    st.write("                     ")
    st.write("                     ")
    st.markdown("---")





if __name__=='__main__':
    main()

st.markdown(" ")
st.markdown("### ** 👨🏼‍💻 Télécom Paris Researcher: **")
st.image(['images/vadim.png'], width=100,caption=["Vadim Malvone"])

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



