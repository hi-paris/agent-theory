import streamlit as st
from back_end_CS import *
import os



def display_case(nlp_steps):


  ### 01

  if nlp_steps == "01 - Initialization":
    st.markdown("---")
    st.write(f"        ")

    st.header("01 - Initialization")
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### i - Quick Introduction: ')

    st.write("""Game theory is the study of mathematical models of strategic interactions among rational agents.
    It has applications in all fields of social science, as well as in logic, systems science and computer science.
    Originally, it addressed two-person zero-sum games, in which each participant's gains or losses are exactly balanced by those of other participants.
    In the 21st century, game theory applies to a wide range of behavioral relations; it is now an umbrella term for the science of logical decision making in humans, animals, as well as computers.""")

    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### ii - Diagram: ')

    Mat_transition=np.array([[3,1,2,0,0],
    [0,3,1,2,0],
    [0,0,3,1,2],
    [0,0,0,3,1],
    [0,0,0,0,3]])

    Istate=1

    Fstate=[4,5]
    t1,t2,t3 = Init(Mat_transition,Istate,Fstate)
    st.graphviz_chart(t1)

    st.write(f"        ")




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

    st.write(f"        ")
    st.write(f"        ")
    code_header_placeholder.markdown(f"#### iii - Code 01 - Initialization")
    snippet_placeholder.code(snippet)
    st.write("     ")
    st.write("     ")
    st.markdown("---")




  ### 04
  if nlp_steps == "04 - Dining Cryptographers":
    st.markdown("---")
    st.write(f"        ")

    st.header("04 - Dining Cryptographers")
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### i - Quick Introduction: ')
    st.write(f"        ")
    st.write(f"        ")

    st.write(""" In cryptography, the dining cryptographers problem studies how to perform a secure multi-party computation of the boolean-XOR function.
  David Chaum first proposed this problem in the early 1980s and used it as an illustrative example to show that it was possible to send anonymous messages with unconditional sender and recipient untraceability.
  Anonymous communication networks based on this problem are often referred to as DC-nets (where DC stands for "dining cryptographers""")
    st.write("""Three cryptographers gather around a table for dinner. The waiter informs them that the meal has been paid for by someone, who could be one of the cryptographers or the National Security Agency (NSA). The cryptographers respect each other's right to make an anonymous payment, but want to find out whether the NSA paid. So they decide to execute a two-stage protocol""")
    st.image("images/crypto.png", width=500,)



    ab=st.selectbox('A and B: Head or Tail',['Head','Tail'])
    ac=st.selectbox('A and C: Head or Tail',['Head','Tail'])
    bc=st.selectbox('B and C: Head or Tail',['Head','Tail'])
    wp=st.selectbox('Who Paid',['A','B','C','NSA','A and B'])
    if wp=='A':
      vwp=[1,0,0]
    if wp=='B':
      vwp=[0,1,0]
    if wp=='C':
      vwp=[0,0,1]
    if wp=='NSA':
      vwp=[0,0,0]
    if wp=='A and B':
      vwp=[1,1,0]
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### ii - Diagram: ')

    test=dining_crypt(ab=ab,ac=ac,bc=bc,who_paid=vwp)
    st.graphviz_chart(test)

    #st.write(f"        ")
    #st.write(f"        ")
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

    st.write(f"        ")
    st.write(f"        ")
    code_header_placeholder.markdown(f"#### iii - Code 02 - Dining Cryptographers")
    snippet_placeholder.code(snippet)
    st.write("     ")
    st.write("     ")
    st.markdown("---")



  ### 03
  if nlp_steps == "03 - ICGS":
    st.markdown("---")
    st.write(f"        ")

    st.header("03 - ICGS")
    st.write(f"        ")
    st.write(f"        ")
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
    
       
    st.write(f"        ")
    st.markdown('### ii Diagram Presentation')
    test=iCGS_train(boolean_Red=False)
    st.write(f"        ")
    st.graphviz_chart(test)
    st.write("       ")
    st.markdown('#### iii - Strategy')
    st.write("        ")
    st.write('     ')
    t1_act=st.selectbox('Action of t1 in the initial state',['right','left'])
    st.write('      ')
    t2_act=st.selectbox('Action of t2 in the initial state',['right','straight', 'left'])
    st.write('     ')
    c_act=st.selectbox('Action of controller in the state after',['6','5','4','3','2','1'])
    st.write('    ')
    cs1=st.selectbox('Action in s1',['a','o', 'e'])
    st.write('    ')
    cs2=st.selectbox('Action in s2',['a','o', 'e'])
    st.write('    ')
    cs3=st.selectbox('Action in s3',['o','a', 'e'])
    st.write('    ')
    cs4=st.selectbox('Action in s4',['o','a', 'e'])
    st.write('    ')
    cs5=st.selectbox('Action in s5',['e','a', 'o'])
    st.write('    ')
    cs6=st.selectbox('Action in s6',['e','a', 'o'])
    
    t1_act,t2_act=t1_act[0],t2_act[0]



    st.write(f"        ")
    st.write(f"        ")
    if st.button('Print Diagram'):
      st.markdown('#### iii - Diagram: ')
      test=iCGS_train(t1_act,t2_act,c_act,cs1,cs2,cs3,cs4,cs5,cs6)
      st.graphviz_chart(test)


    
    code_header_placeholder = st.empty()
    snippet_placeholder = st.empty()

    st.write(f"        ")
    st.write(f"        ")
    st.write("     ")
    st.markdown("---")



  ### 5
  if nlp_steps == '05 - Buchi  Automaton':
    st.markdown("---")
    st.write(f"        ")

    st.header('05 - Buchi  Automaton')
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### i - Quick Introduction: ')
    st.write(f"        ")
    st.write(f"        ")


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


    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### iii - Diagram: ')
    digraph_output = dfa.show_diagram("101")
    st.graphviz_chart(digraph_output)

    st.write(f"        ")
    st.write(f"        ")
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

    st.write(f"        ")
    st.write(f"        ")
    code_header_placeholder.markdown(f"#### v - Code 04 - Buchi  Automaton")
    snippet_placeholder.code(snippet)
    st.write("     ")
    st.write("     ")
    st.markdown("---")



  ### 02
  if nlp_steps == '02 - Strategy Example':
    st.markdown("---")
    st.write(f"        ")

    st.header("02 - Strategy Example")
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### i - Quick Introduction: ')
    st.text(''' This is an example of a game involving very simple states, but with a strategy system.   ''')
    
    
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### ii - Strategy')
    P10=st.selectbox('Action of P1 in the initial state',['A','B','Do nothing'])
    P11=st.selectbox('Action of P1 in the state 1',['A','B','Do nothing'])
    P12=st.selectbox('Action of P1 in the state 2',['A','B','Do nothing'])
    P13=st.selectbox('Action of P1 in the state 3',['A','B','Do nothing'])
    P20=st.selectbox('Action of P2 in the initial state',['C','D','Do nothing'])
    P21=st.selectbox('Action of P2 in the state 1',['C','D','Do nothing'])
    P22=st.selectbox('Action of P2 in the state 2',['C','D','Do nothing'])
    P23=st.selectbox('Action of P2 in the state 3',['C','D','Do nothing'])
    if P10=='Do nothing':
      P10='0'
    if P11=='Do nothing':
      P11='0'
    if P12=='Do nothing':
      P12='0'
    if P13=='Do nothing':
      P13='0'
    if P20=='Do nothing':
      P20='0'
    if P21=='Do nothing':
      P21='0'
    if P22=='Do nothing':
      P22='0'
    if P23=='Do nothing':
      P23='0'
    st.write(f"        ")
    st.write(f"        ")
    st.markdown('#### iii - Diagram: ')
    test=example_strategy(P10+P11+P12+P13,P20+P21+P22+P23)
    st.graphviz_chart(test)


    snippet = f"""


    """
    code_header_placeholder = st.empty()
    snippet_placeholder = st.empty()

    st.write(f"        ")
    st.write(f"        ")
    st.write("     ")
    st.write("     ")
    st.markdown("---")


  ### 6
  if nlp_steps == '06 - Upload Configuration':

    def file_select(folder='./data'):
        filelist=os.listdir(folder)
        st.markdown("OR")
        selectedfile=st.selectbox('Select a default dataset',filelist)
        return os.path.join(folder,selectedfile)
        

    st.markdown("---")
    st.write(f"        ")

    st.header('06 - Upload Configuration')
    st.write(f"        ")
    st.write(f"        ")
    st.markdown("Upload Txt File with config")
    st.button('Upload Data')
    uploaded_file=st.file_uploader('Upload Dataset in .txt',type=['TXT'])
    if uploaded_file is not None:
      st.write('hello world')
    else:
      filename=file_select()
      st.info('You selected {}'.format(filename))
      with open('data/test.txt', 'r') as f:
        s = f.read()

    st.write("     ")
    st.markdown("Example of config file")
    snippet = f"""
    Transition
    0 AC,AD BC,BD 0
    0 0 AD,BD AC,BC
    0 0 0 AD,BC
    0 0 0 *
    Name_State
    s0 s1 s2 s3
    Initial_State
    s0

    """
    snippet_placeholder = st.empty()

    st.write(f"        ")
    st.write(f"        ")
    snippet_placeholder.code(snippet)
    st.write("     ")
    st.markdown("---")






def D_parser_test():
  st.header("Parser")
  st.write(f"    ")
  print("logic")
  print(st.session_state.info_model_test[0][0])
  if st.session_state.info_model_test[0][0]=='LTL':
    print("formula")
    print(st.session_state.info_model_test[0][1])
    lexer = LTLLexer(st.session_state.info_model_test[0][1])
    print("lexer")
    print(lexer)
    stream = CommonTokenStream(lexer)
    print("stream")
    print(stream)
    parser = LTLParser(stream)
    print("parser")
    print(parser)
    tree = parser.ltlExpr()
    visitor = YOUR_VISITOR_CLASS()
    print(visitor.visit(tree))



def parser(formula):
    change=[[' ',''],['||','|'],['&&','&'],['or', '|'],['and','&'],['implies','>'],['->','>'],['next','X'],['eventually','F'],['always','G']]
    operatorSimpleL=[')',']']
    operatorSimpleR=['X','F','G','(','[']
    operatorDouble=['|','&','U','R','>']
    closeoperator=[')',']']
    openoperator=['(','[']
    operator=operatorSimpleL+operatorSimpleR+operatorDouble
    for operator_change in change:
        formula=formula.replace(operator_change[0],operator_change[1])
    def cut(formula):
        new_formula=[]
        tmp=''
        for letter in formula:
            if letter in operator:
                if tmp!='':
                    new_formula.append(tmp)
                new_formula.append(letter)
                tmp=''
            else:
                tmp+=letter
        new_formula.append(tmp)
        return new_formula
    cut_formula=cut(formula)
    def verif_paranthese(formula):
        cmpt=0
        for obj in formula:
            if obj in openoperator:
                cmpt+=1
            elif obj in closeoperator:
                cmpt+=-1
        return not(cmpt)
    if not(verif_paranthese(cut_formula)):
        return False
    
    cut_class=[]
    for obj in cut_formula:
        if obj in operatorDouble:
            cut_class.append('D')
        elif obj in operatorSimpleL:
            cut_class.append('L')
        elif obj in operatorSimpleR:
            cut_class.append('R')
        else:
            cut_class.append('AP')
    def verif(list_cut):
        if not(list_cut[0]=='AP' or list_cut[0]=='L'):
            return False
        for id_obj in range(len(list_cut)-1):
            print(id_obj)
            if list_cut[id_obj]=='R':
                if (list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='D'):
                    return False
            elif list_cut[id_obj]=='D':
                if (list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='D'):
                    return False
            elif list_cut[id_obj]=='AP':
                if (list_cut[id_obj+1]=='R' or list_cut[id_obj+1]=='AP') :
                    return False
            elif list_cut[id_obj]=='L':
                if (list_cut[id_obj+1]=='AP' or list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='R'):
                    return False
        if (list_cut[-1]=='R' or list_cut[-1]=='D'):
            return False
        return True     
    return verif(cut_class),cut_formula,cut_class





def display_MCMAS():
  if st.session_state.cmpt_model==-1:
    st.markdown("---")
    st.write(f"    ")
    st.header("Model Checking for MAS")
    st.write(f"    ")
    st.write(f"    ")
    st.markdown('Logic Selection ')
    Logic=st.selectbox('Selec your logic',['ATL','CTL','LTL','SL'])
    st.write(f"    ")
    st.write(f"    ")
    formula=st.text_input('Write your formula',' ')
    st.write("     ")
    st.write('Your formula with the '+Logic+' logic is '+formula)
    st.write("     ")
    Verif,list_pars,list_type=parser(formula)
    st.write(str(Verif))
    st.write(str(list_pars))
    st.write("     ")
    st.markdown("---")
    if st.button('Next : To Parser'):
      (st.session_state.info_model_test).append([Logic,formula])
      st.session_state.cmpt_model=-2
      st.experimental_rerun()
  if st.session_state.cmpt_model==-2:
    D_parser_test()




def display_MS():
  if st.session_state.cmpt_model<=0:
    D_agent()
  elif st.session_state.cmpt_model==1:
    D_state()
  elif st.session_state.cmpt_model==2:
    D_action()
  
  elif st.session_state.cmpt_model==3:
    Na=len(st.session_state.info_model[0][0])
    D_transition(Na-st.session_state.info_model[0][1]-1,Na)
  elif st.session_state.cmpt_model==4:
    st.session_state.mat_transi=[]
    st.session_state.info_model[0][1]=len(st.session_state.info_model[0][0])
    D_printgraph()
  elif st.session_state.cmpt_model==5:
    Na=len(st.session_state.info_model[0][0])
    D_strategy(Na-st.session_state.info_model[0][1]-1,Na)
  elif st.session_state.cmpt_model==6:
    D_logic()
  elif st.session_state.cmpt_model==7:
    D_parser()

  st.markdown("---")
  st.write(f"    ")
  st.header("Model design for User")
  st.write(f"    ")
  st.markdown("---")


def D_agent():
  st.write(f"    ")
  st.write(f"    ")
  Na=st.selectbox('Number of agent',['1','2','3','4'])
  st.write(f"    ")
  List_name_agent=[]
  for id_agent in range(int(Na)):
    tmp=st.text_input('Name of the agent number '+str(id_agent),'A'+str(id_agent))
    List_name_agent.append(tmp)
  st.write(f"    ")
  if st.button('Next : To Agent'):
    (st.session_state.info_model).append([List_name_agent,len(List_name_agent)-1])
    st.session_state.cmpt_model=1
    print(st.session_state.info_model[0])
    st.experimental_rerun()


def D_state():
  NS=st.selectbox('Number of State',['1','2','3','4','5'])
  st.write("     ")
  List_name_state=[]
  for id_state in range(int(NS)):
    tmp=st.text_input('Name of the state number '+str(id_state),'s'+str(id_state))
    List_name_state.append(tmp)
  st.write(f"     ")
  if st.button('Next : To Action'):
    (st.session_state.info_model).append(List_name_state)
    st.session_state.cmpt_model=2
    st.experimental_rerun()

def D_action():
  Nact=st.selectbox('Number of Action',['1','2','3','4','5','6','7'])
  Alphabet=['A','B','C','D','E','F','G']
  st.write("     ")
  List_name_action=['*','No Action']
  for id_action in range(int(Nact)):
    tmp=st.text_input('Name of the action number '+str(id_action),Alphabet[id_action])
    List_name_action.append(tmp)
  st.write(f"     ")
  if st.button('Next : To Transition'):
    (st.session_state.info_model).append(List_name_action)
    st.session_state.cmpt_model=3
    st.experimental_rerun()


def D_transition(act_input,Na):
  st.write('Design your graph')
  st.write('For each couple of state')
  st.write("     ")
  Mat_transition=[]
  List_name_state=st.session_state.info_model[1]
  NS=len(List_name_state)
  List_action=st.session_state.info_model[2]
  for id_state1 in range(NS):
    List_transition=[]
    for id_state2 in range(int(NS)):
      tmp=st.multiselect('Action of '+st.session_state.info_model[0][0][act_input]+ ' in the state '+List_name_state[id_state1]+' to '+List_name_state[id_state2]+'.',List_action,List_action[1])
      List_transition.append(tmp)
    Mat_transition.append(List_transition)
  st.write("     ")
  if (Na-act_input)>1:
    if st.button('Next : To '+st.session_state.info_model[0][0][act_input+1]):
      st.session_state.info_model[0][1]+=(-1)
      (st.session_state.mat_transi).append(Mat_transition)
      st.session_state.cmpt_model=3
      st.experimental_rerun()
  else:
    if st.button('Next : To Graph'):
      (st.session_state.mat_transi).append(Mat_transition)
      st.session_state.cmpt_model=4
      Mat_to_Label()
      st.experimental_rerun()


def Mat_to_Label():
  def concat(list_str):
    tmp1=''
    for stri in list_str:
      tmp1+=stri
    return tmp1
  
  print(st.session_state.mat_transi)
  Mat=[]
  for s_in in range(len(st.session_state.info_model[1])):
    Lis=[]
    for s_out in range(len(st.session_state.info_model[1])):
      tmp=''
      for mat_label in st.session_state.mat_transi:
        tmp+=concat(mat_label[s_in][s_out])
        tmp+='|'
      Lis.append(tmp[:-1])
    Mat.append(Lis)
  print(Mat)
  st.session_state.info_model.append(Mat)



def D_printgraph():
  st.write('Graph')
  st.write("     ")
  st.markdown('#### iii - Diagram: ')
  test=display_graph_MS(st.session_state.info_model[3],st.session_state.info_model[0][0],st.session_state.info_model[1])
  st.graphviz_chart(test)
  if st.button('Next : To Strategy'):
    (st.session_state.info_model).append(test)
    st.session_state.cmpt_model=5
    st.experimental_rerun()


def D_logic():
  st.header("Model Checking for MAS")
  st.write(f"    ")
  st.write(f"    ")
  st.markdown('Logic Selection ')
  Logic=st.selectbox('Selec your logic',['ATL','CTL','LTL','SL'])

  st.write(f"    ")
  st.write(f"    ")
  formula=st.text_input('Write your formula',' ')
  st.write("     ")
  st.write('Your formula with the '+Logic+' logic is '+formula)
  st.write("     ")
  Verif,list_pars,list_type=parser(formula)
  st.write(str(Verif))
  st.write(str(list_pars))
  st.write(str(list_type))
  if st.button('Next : To ...'):
    (st.session_state.info_model).append([Logic,formula])
    st.session_state.cmpt_model=6
    st.experimental_rerun()


#def D_parser():
#  st.header("Parser")
#  st.write(f"    ")
#  if st.session_state.info_model[5][0]=='LTL':
#    lexer = LTLLexer(st.session_state.info_model[5][1])
#    stream = CommonTokenStream(lexer)
#    parser = LTLParser(stream)
#    tree = parser.ltlExpr()
#    visitor = YOUR_VISITOR_CLASS()
#    print(visitor.visit(tree))


def D_strategy(act_input,id_state1):
  st.write('Design your strategy')
  st.write('For each agent in each state')
  st.write("     ")
  List_strategy=[]
  List_name_state=st.session_state.info_model[1]
  NS=len(List_name_state)
  List_action=st.session_state.info_model[2]
  for id_state1 in range(NS):
    tmp=st.selectbox('Action of '+st.session_state.info_model[0][0][act_input]+ ' in the state '+List_name_state[id_state1]+'.',List_action)
    print(tmp)
    List_strategy.append(tmp)
  st.write("     ")
  if (id_state1-act_input)>1:
    if st.button('Next : To '+st.session_state.info_model[0][0][act_input+1]):
      st.session_state.info_model[0][1]+=(-1)
      (st.session_state.mat_transi).append(List_strategy)
      st.session_state.cmpt_model=5
      st.experimental_rerun()
  else:
    if st.button('Next : To Logic'):
      (st.session_state.mat_transi).append(List_strategy)
      st.session_state.cmpt_model=6
      st.session_state.info_model.append(st.session_state.mat_transi)
      print(st.session_state.info_model)
      st.experimental_rerun()


