import numpy as np
class nuron:
    def __init__(self,x,y):
        self.x_input=np.array(x)
        self.y_input=np.array(y)
        self.w=np.random.rand(self.x_input.shape[1],self.y_input.shape[1]) 
        self.b=np.random.rand(1,self.y_input.shape[1])
        
        
    def f_prp(self):
        self.out=(np.dot(self.x_input,self.w)+self.b)
    def b_prp(self,l_rate):
        error=self.out-self.y_input
        b_new=error
        
        w_new=np.dot(self.x_input.T,b_new)
        self.w-=l_rate*w_new
        for i in b_new:
            self.b-=l_rate*i
    def run(self,l_rate,ep):
        for i in range(0,ep):
            
            self.f_prp()
            self.b_prp(l_rate)
    def prd(self,x):
        self.x_input=np.array(x)
        self.f_prp()
        print(self.out)
a=nuron([[-1.0], [0.0], [1.0], [2.0], [3.0], [4.0]],[[-2.0],[1.0],[4.0],[7.0],[10.0],[13.0]])        
a.run(0.05,500)
a.prd(100)
