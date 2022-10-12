import graphviz

### Game Class
class game:
  def __init__(self,Ag=1,name_list=[],load_file=False,path1="", AW=False):
    self.AW=AW
    if load_file:
      if path1=="":
        Mat_tansition,Mat_unknow,State,IState=self.load()
      else:
        Mat_tansition,Mat_unknow,State,IState=self.load(path1)
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
    f = graphviz.Digraph('finite_state_machine',{'arrowhead' : 'none'})
    f.attr('node', shape='circle')
    f.attr('edge',{'arrowhead':'none'})
    if self.AW:
      f.attr('edge',{'arrowhead':'normal'})
    if Special_node!=-1:
      f.node(self.list_agent[Special_node].name,style='filled', fillcolor='red')
    for id_agent in range(self.Ag):
      for id_transition in range(len(self.list_agent[id_agent].list_transition)):
        if type(self.list_agent[id_agent].list_transition[id_transition])==str and self.list_agent[id_agent].list_transition[id_transition] !='0':
          f.edge(self.list_agent[id_agent].name,self.list_agent[id_transition].name,label=str(self.list_agent[id_agent].list_transition[id_transition]))
    return f

  def diagram_unk(self,col,f):
    f.attr('edge',{'arrowhead' :'none', 'style' :'dotted'})
    for id_agent in range(self.Ag):
      for id_transition in range(len(self.list_agent[id_agent].unkown_transition)):
        if type(self.list_agent[id_agent].unkown_transition[id_transition])==str and self.list_agent[id_agent].unkown_transition[id_transition] !='0':
          f.edge(self.list_agent[id_agent].name,self.list_agent[id_transition].name,color=col,label=str(self.list_agent[id_agent].unkown_transition[id_transition]))
    f.attr('edge', {'arrowhead' :'Normal', 'style':'solid'})
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

  def load(self,path='example_train_controller.txt'):
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
