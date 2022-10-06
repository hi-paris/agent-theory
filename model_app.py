## NLP App Theatre Reviews

### Import packages

import os
from pathlib import Path
import base64
import time
import math
import json
import ast

import pandas as pd
import numpy as np

import graphviz

import matplotlib.pyplot as plt
import matplotlib
import graphviz
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

from visual_automata.fa.dfa import VisualDFA
from visual_automata.fa.nfa import VisualNFA

import streamlit as st


st.set_page_config(
    page_title="Agent Theory", layout="wide", page_icon="images/flask.png"
)


### methods used within streamlit - to organize later on 


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded




### Initialization function
def Init(Mat_transition,Istate,Fstate):
  #State init
  state_i=[]
  N=len(Mat_transition)
  M=len(Mat_transition[0])
  for nn in range(N):
    state_i.append("q"+str(nn))
  state_i=set(state_i)

  #Name_Transitions
  list_trans_i=list(dict.fromkeys(Mat_transition.flatten()))
  trans_i=[]
  for ti in list_trans_i:
    if ti:
      trans_i.append(str(ti))
  trans_i=set(trans_i)
  Istate="q"+str(Istate-1)
  FS=[]
  for kk in range(len(Fstate)):
    FS.append("q"+str(Fstate[kk]-1))
  if len(FS)==1:
    Fstate={FS}
  else:
    Fstate=set(FS)
  dict_trans={}
  for id_state in range(N):
    dict_state={}
    for id_transition in range(M):
      value=Mat_transition[id_state][id_transition]
      if value:
        out="q"+str(id_transition)
        dict_state[str(value)]={out}
    dict_trans["q"+str(id_state)]=dict_state
  #return state_i,trans_i,dict_trans,Istate,Fstate
  nfa=VisualNFA(
      states=state_i,
      input_symbols=trans_i,
      transitions=dict_trans,
      initial_state=Istate,
      final_states=Fstate)

  table=nfa.table
  graph=nfa.show_diagram()
  return graph,table,nfa


### Not Important

def read_fun(path='graph1.txt'):
  with open(path) as f:
    lines = f.readlines()
  Istate=int(lines[0][:-1])
  Fstate=eval('['+(lines[1][:-1])+']')
  Mat=[]
  for l in lines[2:]:
    Mat.append((eval('['+(l[:-1])+']')))
  Mat=np.array(Mat)
  return Mat,Istate,Fstate


def word(naf,rep,word,pref="",suff="",boole=True):
  if boole:
    r1,r2,r3=naf.input_check(pref+rep*word+suff)
    return r1[0]=='[Accepted]'
  else:
    return naf.input_check(pref+rep*word+suff)

### Game Class
class game:
  def __init__(self,Ag=1,name_list=[],load_file=False,path1=""):
    if load_file:
      Mat_tansition,Mat_unknow,State,IState=self.load()
      self.name_list=State
      self.Ag=len(Mat_tansition)
      self.list_agent=[]
      self.build()
      self.make_transition(Mat_tansition)
      self.Unknow(Mat_unknow)
    else:
      self.name_list=name_list
      self.Ag=Ag
      self.list_agent=[]
      self.build()


  class agent:
    def __init__(self,name):
      self.name=name
      self.list_transition=[]
      self.unkown_transition=[]
    def make_agent_transition(self,list_transi):
      self.list_transition=list_transi
    def make_agent_UT(self,list_transi):
      self.unkown_transition=list_transi

  def build(self):
    self.list_agent=[]
    for ag in range(self.Ag):
      if self.name_list==[]:
        self.list_agent.append(self.agent(str(ag)))
      else:
        self.list_agent.append(self.agent(self.name_list[ag]))
  def make_transition(self,Mat_transition):
    for id_agent in range(len(Mat_transition)):
      (self.list_agent[id_agent]).make_agent_transition(Mat_transition[id_agent])
  def Unknow(self,Mat):
    for id_agent in range(len(Mat)):
      (self.list_agent[id_agent]).make_agent_UT(Mat[id_agent])

  def diagram_init(self,Special_node=-1):
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    f.attr('node', shape='circle')
    if Special_node!=-1:
      f.node(self.list_agent[Special_node].name,style='filled', fillcolor='red')
    for id_agent in range(self.Ag):
      for id_transition in range(len(self.list_agent[id_agent].list_transition)):
        if type(self.list_agent[id_agent].list_transition[id_transition])==str and self.list_agent[id_agent].list_transition[id_transition] !='0':
          f.edge(self.list_agent[id_agent].name,self.list_agent[id_transition].name,label=str(self.list_agent[id_agent].list_transition[id_transition]))
    f.view()
    return f

  def diagram_unk(self,col,f):
    for id_agent in range(self.Ag):
      for id_transition in range(len(self.list_agent[id_agent].unkown_transition)):
        if type(self.list_agent[id_agent].unkown_transition[id_transition])==str and self.list_agent[id_agent].unkown_transition[id_transition] !='0':
          f.edge(self.list_agent[id_agent].name,self.list_agent[id_transition].name,color=col,label=str(self.list_agent[id_agent].unkown_transition[id_transition]))
    f.view()
    return f

  def label_node(self,f,list_label):
    for ag in range(self.Ag):
      f.node(str(self.list_agent[ag].name),xlabel=str(list_label[ag]))
    return f

  def display_diagram(self,list_label=[],col='blue',mat_add=False,Special_node=-1):
    f=self.diagram_init(Special_node)
    if not(mat_add):
      f=self.diagram_unk(col,f)
    if list_label==[]:
      return f
    else:
      return self.label_node(f,list_label)

  def load(self):
    path='example_train_controller.txt'
    file=open(path, 'r', encoding = 'utf-8-sig')
    lines=file.readlines()
    file.close()
    Mat_tansition=[]
    Mat_unknow=[]
    IState=[]
    State=[]
    cmpt=0
    for line in lines:
      if line=="Transition\n" or line=="Unkown_Transition_by\n" or line=="Name_State\n" or line=="Initial_State\n" or line=="":
        cmpt+=1
      else:
        if cmpt==1:
          line = line.split(' ')
          line = [i.strip() for i in line]
          Mat_tansition.append(line)
        elif cmpt==2:
          line = line.split(' ')
          line = [i.strip() for i in line]
          Mat_unknow.append(line)
        elif cmpt==3:
          line = line.split(' ')
          State = [i.strip() for i in line]
        elif cmpt==4:
          line = line.split(' ')
          IState=[i.strip() for i in line]
          cmpt+=1
    return Mat_tansition,Mat_unknow,State,IState

### Dining Cryptographe

def dining_crypt(ab="Head",ac="Tail",bc="Head",who_paid=[0,0,0]):
  dining=game(3,["A","B","C"]) 
  ab=ab
  ac=ac
  bc=bc
  list_value=[ac,ab,bc]
  #mat=[[0,ab,ac],[ab,0,bc],[ac,bc,0]]
  mat=[[0,ab,ac],[0,0,0],[0,bc,0]]
  dining.make_transition(mat)

  for id in range(len(list_value)):
    if list_value[id]=="Head":
      list_value[id]=1
    else:
      list_value[id]=0
  list_XOR=[]
  for kk in range(3):
    if not(who_paid[kk]):
      list_XOR.append(list_value[kk]^list_value[(kk+1)%3])
    else:
      list_XOR.append(not(list_value[kk]^list_value[(kk+1)%3]))
    
  list_XOR_label=[]
  for XOR in list_XOR:
    if XOR:
      list_XOR_label.append("True")
    else:
      list_XOR_label.append("False")
  rez=list_XOR[0]^list_XOR[1]^list_XOR[2]
  f=dining.display_diagram(list_XOR_label)
  if rez==0:
    if sum(who_paid)==0:
      f.attr(label='Result:NSA paid. Good Prediction',frontcolor='red')
    else:
      f.attr(label='Result:NSA paid. Bad Prediction')
  else:
    if sum(who_paid)==0:
     f.attr(label='Result: Someone paid. Bad Prediction')
    else:
      f.attr(label='Result: Someone paid. Good Prediction')
  
  return f

### ICGS train

def iCGS_train(ActT1="r",ActT2="r",ActC="a"):
  #icgs: M=< Ag={t1,t2,c}, AP={p,b,d}, S={sI,s1,s2,s3,s4,s5,s6,s7?}, so=SI, Actt1={r,l,i}, Act2={r,l,s,i},Actc={1,2,3,4,5,6,a,e,o,i}> #We swich Agent and State
  test=game(load_file=True)
  if ActT1=="r":
    if ActT2=="r":
      if ActC=="a":
        SP=0
      elif ActC=="o":
        SP=7
      else:
        SP=4
    if ActT2=="s":
      if ActC=="e":
        SP=3
      elif ActC=="o":
        SP=7
      else:
        SP=6
    else: #ActT2=l
      if ActC=="e":
        SP=2
      elif ActC=="o":
        SP=7
      else:
        SP=3
  else:#ActT2=l
    if ActT2=="r":
      if ActC=="a":
        SP=0
      elif ActC=="o":
        SP=7
      elif ActC=="e":
        SP=5
      else:
        SP=5
    if ActT2=="s":
      if ActC=="a":
        SP=I
      elif ActC=="o":
        SP=7
      else:
        SP=1
    else: #ActT2=l
      if ActC=="o":
        SP=7
      else:
        SP=2

  graph=test.display_diagram(Special_node=SP)

  return graph



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

    st.sidebar.header("Select Approach")
    nlp_steps = st.sidebar.selectbox('', ['01 - Initialization',
                                          '02 - Dining Cryptographers', '03 - ICGS','04 - Buchi  Automaton',
                                          '05 - New Approach (In Progress)'])



    st.sidebar.header("Upload Txt File with config")


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



### 01

    if nlp_steps == "01 - Initialization":
        st.markdown("---")
        st.write(f"                                          ")

        st.header("01 - Initialization")
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
 
        st.write("""Game theory is the study of mathematical models of strategic interactions among rational agents.
        It has applications in all fields of social science, as well as in logic, systems science and computer science.
        Originally, it addressed two-person zero-sum games, in which each participant's gains or losses are exactly balanced by those of other participants.
        In the 21st century, game theory applies to a wide range of behavioral relations; it is now an umbrella term for the science of logical decision making in humans, animals, as well as computers.""")

        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iii - Diagram: ')
 
        Mat_transition=np.array([[3,1,2,0,0],
        [0,3,1,2,0],
        [0,0,3,1,2],
        [0,0,0,3,1],
        [0,0,0,0,3]])

        Istate=3

        Fstate=[4,5]
        t1,t2,t3 = Init(Mat_transition,Istate,Fstate)
        t1

        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iv - Input Table: ')
        t2

  

        snippet = f"""

        def Init(Mat_transition,Istate,Fstate):
            #State init
            state_i=[]
            N=len(Mat_transition)
            M=len(Mat_transition[0])
            for nn in range(N):
                state_i.append("q"+str(nn))
            state_i=set(state_i)

            #Name_Transitions
            list_trans_i=list(dict.fromkeys(Mat_transition.flatten()))
            trans_i=[]
            for ti in list_trans_i:
                if ti:
                trans_i.append(str(ti))
            trans_i=set(trans_i)
            Istate="q"+str(Istate-1)
            FS=[]
            for kk in range(len(Fstate)):
                FS.append("q"+str(Fstate[kk]-1))
            if len(FS)==1:
                Fstate=dic(FS)
            else:
                Fstate=set(FS)
            dict_trans=dic()
            for id_state in range(N):
                dict_state=dic()
                for id_transition in range(M):
                value=Mat_transition[id_state][id_transition]
                if value:
                    out="q"+str(id_transition)
                    dict_state[str(value)]=dic(out)
                dict_trans["q"+str(id_state)]=dict_state
            #return state_i,trans_i,dict_trans,Istate,Fstate
            nfa=VisualNFA(
                states=state_i,
                input_symbols=trans_i,
                transitions=dict_trans,
                initial_state=Istate,
                final_states=Fstate)

            table=nfa.table
            graph=nfa.show_diagram()
            return graph,table,nfa

        """
        code_header_placeholder = st.empty()
        snippet_placeholder = st.empty()

        st.write(f"                                          ")
        st.write(f"                                          ")
        code_header_placeholder.markdown(f"#### v - Code 01 - Initialization")
        snippet_placeholder.code(snippet)
        st.write("                     ")
        st.write("                     ")
        st.markdown("---")




### 02
    if nlp_steps == "02 - Dining Cryptographers":
        st.markdown("---")
        st.write(f"                                          ")

        st.header("02 - Dining Cryptographers")
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
        st.write(f"                                          ")
        st.write(f"                                          ")

        st.write(""" In cryptography, the dining cryptographers problem studies how to perform a secure multi-party computation of the boolean-XOR function.
 David Chaum first proposed this problem in the early 1980s and used it as an illustrative example to show that it was possible to send anonymous messages with unconditional sender and recipient untraceability.
Anonymous communication networks based on this problem are often referred to as DC-nets (where DC stands for "dining cryptographers""")
        st.write("""Three cryptographers gather around a table for dinner. The waiter informs them that the meal has been paid for by someone, who could be one of the cryptographers or the National Security Agency (NSA). The cryptographers respect each other's right to make an anonymous payment, but want to find out whether the NSA paid. So they decide to execute a two-stage protocol""")
        st.image("images/crypto.png", width=500,)

 


        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iii - Diagram: ')

        f=dining_crypt(ab="Head",ac="Tail",bc="Head",who_paid=[1,0,1])
        f

        #st.write(f"                                          ")
        #st.write(f"                                          ")
        #st.markdown('#### iv - Input Table: ')


        snippet = f"""
def dining_crypt(ab="Head",ac="Tail",bc="Head",who_paid=[0,0,0]):
  dining=game(3,["A","B","C"]) 
  ab=ab
  ac=ac
  bc=bc
  list_value=[ac,ab,bc]
  #mat=[[0,ab,ac],[ab,0,bc],[ac,bc,0]]
  mat=[[0,ab,ac],[0,0,0],[0,bc,0]]
  dining.make_transition(mat)

  for id in range(len(list_value)):
    if list_value[id]=="Head":
      list_value[id]=1
    else:
      list_value[id]=0
  list_XOR=[]
  for kk in range(3):
    if not(who_paid[kk]):
      list_XOR.append(list_value[kk]^list_value[(kk+1)%3])
    else:
      list_XOR.append(not(list_value[kk]^list_value[(kk+1)%3]))
    
  list_XOR_label=[]
  for XOR in list_XOR:
    if XOR:
      list_XOR_label.append("True")
    else:
      list_XOR_label.append("False")
  rez=list_XOR[0]^list_XOR[1]^list_XOR[2]
  f=dining.display_diagram(list_XOR_label)
  if rez==0:
    if sum(who_paid)==0:
      f.attr(label='Result:NSA paid. Good Prediction',frontcolor='red')
    else:
      f.attr(label='Result:NSA paid. Bad Prediction')
  else:
    if sum(who_paid)==0:
     f.attr(label='Result: Someone paid. Bad Prediction')
    else:
      f.attr(label='Result: Someone paid. Good Prediction')
  
  return f
    
        """
        code_header_placeholder = st.empty()
        snippet_placeholder = st.empty()

        st.write(f"                                          ")
        st.write(f"                                          ")
        code_header_placeholder.markdown(f"#### v - Code 02 - Dining Cryptographers")
        snippet_placeholder.code(snippet)
        st.write("                     ")
        st.write("                     ")
        st.markdown("---")



### 03
    if nlp_steps == "03 - ICGS":
        st.markdown("---")
        st.write(f"                                          ")

        st.header("03 - ICGS")
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
        st.text('''
        Impartial combinatorial games (ICGs)

        Integration: We have to initialze three parameters: 
        ActT1: T1's action, ="r" (right) or "l" (left) 
        ActT2: T2's action, ="r" (right) or "s" (straight) or "l" (left) 
        ActC: Controller's action, ="e" or "a" or "o" (see description below)
        The blue connection are the state that cannot be distinguish for the agent in the label.
        The red node is the final state after all the actions
        The iCGS describes a variant of the Train Gate Controller scenario (Alur, Henzinger, and Kupferman 2002).
        Two trains t1 and t2 pass through a crossroad. Due to agreements between the railway companies, train t1 can choose between the right (r) or left (l) track,
        while t2 can choose between the right (r), left (l) or straight (s) track.
        At the same time, controller c has to select the right combination of tracks. For example, if t1 and t2 choose the joint action r, then c has to select action 1 to proceed to the next step.
        Moreover, train t1 has partial observability on the choices of t2. For instance, if t1 chooses l, then she cannot distinguish whether t2 selects r or s, but she would observe if t2 chose l as well. 
        After this first step, c can still change her mind. Specifically, she can change arbitrarily the selection of tracks (e), request a new choice to the trains (a), or execute their selection (o). 
        The controller c has partial observability, she cannot distinguish between s2 and s3, i.e.
        she does not distinguish r and l of t1 when t2 selects l. Moreover, ∗ denotes any tuple of actions for which a transition is not given explicitly.''')
        
        
        st.write(f"                                          ")
        st.write(f"                                          ")





        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iii - Diagram: ')
        test=iCGS_train("r","l","e")
        test

        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iv - Input Table: ')

  

        snippet = f"""

    
        """
        code_header_placeholder = st.empty()
        snippet_placeholder = st.empty()

        st.write(f"                                          ")
        st.write(f"                                          ")
        code_header_placeholder.markdown(f"#### v - Code 03 - ICGS")
        snippet_placeholder.code(snippet)
        st.write("                     ")
        st.write("                     ")
        st.markdown("---")



### 4
    if nlp_steps == '04 - Buchi  Automaton':
        st.markdown("---")
        st.write(f"                                          ")

        st.header('04 - Buchi  Automaton')
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
        st.write(f"                                          ")
        st.write(f"                                          ")


        st.markdown("#### ii - Select Parameters: ")

        with open('data/test.txt', 'r') as f:
            s = f.read()
            input_ast_format = ast.literal_eval(s)


        input_initial_state = st.selectbox(
        'Select initial state:',
        list(input_ast_format.keys()))


        input_final_states = st.multiselect(
        'Select final states:',
        list(input_ast_format.keys()),list(np.random.choice(list(input_ast_format.keys()),2)))


        dfa = VisualDFA(
        states={"q0", "q1", "q2", "q3", "q4"},
        input_symbols={"0", "1"},
        transitions=input_ast_format,
        initial_state=input_initial_state,
        final_states=set(input_final_states),
        )


        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iii - Diagram: ')
        digraph_output = dfa.show_diagram("101")
        st.graphviz_chart(digraph_output)

        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iv - Input Table: ')
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

        st.write(f"                                          ")
        st.write(f"                                          ")
        code_header_placeholder.markdown(f"#### v - Code 04 - Buchi  Automaton")
        snippet_placeholder.code(snippet)
        st.write("                     ")
        st.write("                     ")
        st.markdown("---")



### 5
    if nlp_steps == '05 - New Approach (In Progress)':
        st.markdown("---")
        st.write(f"                                          ")

        st.header('05 - New Approach (In Progress)')
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### i - Quick Introduction: ')
        st.write(f"                                          ")
        st.write(f"                                          ")
        st.write(f"Work in Progress")


        st.markdown("#### ii - Select Parameters: ")

        with open('data/test.txt', 'r') as f:
            s = f.read()
            input_ast_format = ast.literal_eval(s)


        input_initial_state = st.selectbox(
        'Select initial state:',
        list(input_ast_format.keys()))


        input_final_states = st.multiselect(
        'Select final states:',
        list(input_ast_format.keys()),list(np.random.choice(list(input_ast_format.keys()),2)))



        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iii - Diagram: ')


        st.write(f"                                          ")
        st.write(f"                                          ")
        st.markdown('#### iv - Input Table: ')

  

        snippet = f"""

        Work in Progress

        """
        code_header_placeholder = st.empty()
        snippet_placeholder = st.empty()

        st.write(f"                                          ")
        st.write(f"                                          ")
        code_header_placeholder.markdown(f"#### v - Code 05 - New Approach (In Progress)")
        snippet_placeholder.code(snippet)
        st.write("                     ")
        st.write("                     ")
        st.markdown("---")




if __name__=='__main__':
    main()

st.markdown(" ")
st.markdown("### ** 👨🏼‍💻 Télécom Paris Researcher: **")
st.image(['images/1.png'], width=150,caption=["Vadim Malvone"])

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



