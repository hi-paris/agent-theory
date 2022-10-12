#Case Studies
from class_game import *
import ast
from visual_automata.fa.dfa import VisualDFA
from visual_automata.fa.nfa import VisualNFA


import numpy as np

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




#### Dining Cryptographe

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

def iCGS_train(ActT1="r",ActT2="r",ActC="6",boolean_Red=True,cs1='a',cs2='a',cs3='o',cs4='o',cs5='e',cs6='e'):
  #icgs: M=< Ag={t1,t2,c}, AP={p,b,d}, S={sI,s1,s2,s3,s4,s5,s6,s7?}, so=SI, Actt1={r,l,i}, Act2={r,l,s,i},Actc={1,2,3,4,5,6,a,e,o,i}> #We swich Agent and State
  test=game(load_file=True,AW=True)
  if ActC=='6' and ActT1=='r' and ActT2=='r':
    if cs6=='e':
      SP=3
    elif cs6=='o':
      SP=7
    else:
      SP=6
  elif ActC=='2' and ActT1=='l' and ActT2=='l':
    if cs2=='o':
      SP=7
    else:
      SP=2
  elif ActC=='3' and ActT1=='r' and ActT2=='l':
    if cs3=='e':
      SP=2
    elif cs3=='o':
      SP=7
    else:
      SP=3
  elif ActC=='4' and ActT1=='r' and ActT2=='s':
    if cs4=='a':
      SP=0
    elif cs4=='o':
      SP=7
    else:
      SP=4
  elif ActC=='5' and ActT1=='l' and ActT2=='r':
    if cs5=='a':
      SP=0
    elif cs5=='o':
      SP=7
    else:
      SP=5
  elif ActC=='1' and ActT1=='l' and ActT2=='s':
    if cs1=='a':
      SP=0
    elif cs1=='o':
      SP=7
    else:
      SP=1
  else:
    SP=0
  if boolean_Red:
    graph=test.display_diagram(Special_node=SP)
  else:
    graph=test.display_diagram()
  return graph


### Example Graph
def example_strategy(h1,h2):
  game_strategy=game(load_file=True,path1='example_strategy.txt')
  if h1[0]=='A' and h2[0]!='0':
    if h2[1]=='D':
      if (h1[2]=='A' and h2[2]=='D') or (h1[2]=='B' and h2[2]=='C'):
        SP=3
      else:
        SP=2
    elif h2[1]=='C':
      SP=3
    else:
      SP=1
  elif h1[0]=='B' and h2[0]!='0':
    if (h1[2]=='A' and h2[2]=='D') or (h1[2]=='B' and h2[2]=='C'):
      SP=3
    else:
      SP=2
  else:
    SP=0
  graph=game_strategy.display_diagram(Special_node=SP)
  return graph


def display_graph_MS(Mat_transition,List_name_agent,List_name_stat):
  test=game(len(List_name_stat),List_name_stat,AW=True)
  test.make_transition(Mat_transition)
  test=test.display_diagram()
  return test


