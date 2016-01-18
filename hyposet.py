
'''
class HypData
has two attributes, its id, and the text
'''

class HypData(object):
    def __init__(self,id,text,value,parent):
        self.id=id
        self.text=text
        self.value=value
        self.parent=parent

    def __gt__(self,other): # useful for sorting, designing pairs
        return self.value > other.value
    def __eq__(self,other): #useful for equality
        return self.value == other.value

    def __hash__(self):
        return hash(self.id)
    def isValid(self): # By default all are valid unless otherwise specified
        return True
'''
class HypSet
a class to store different hypotheses grouped by their parent (gold)
e.g. for MT Eval, parents are references, and hypotheses are corresponding translations
'''

class HypSet(object):
    def __init__(self,gold): #create object with a question
        self.id=gold.id
        self.hyps=[]
        self.gold=gold

    def addHypothesis(self,hyp): #add hypotheses
        
        if self.id != hyp.parent_id:
            raise ValueError

        self.hyps.append(hyp)

    def __len__(self): #compute len
        return len(self.hyps)
    def __getitem__(self,item):
        return self.hyps[item]
    def __hash__(self):
        return hash(self.id)
'''
class HypSetGroup
a class to store all hypothesis groups for different parents.
This is the full training set, indexed by the parent id
e.g. for MT Eval, parents are references
'''
class HypSetGroup():
    def __init__(self):
        self.sets={}
        self.features=[]


    def addItem(self,parent,hyp):
        try:
            self.sets[parent.id].addHypothesis(hyp)
        except KeyError:
            self.sets[parent.id]=HypSet(parent)
            self.sets[parent.id].addHypothesis(hyp)
    def addFeature(self,feature):
        self.features.append(feature)

    def dumpTextToFile(self,filename):
        with open(filename,'w') as fh:
            for parent in self:
                fh.write("%s\t%s\t%s\n"%(parent.gold.id, parent.gold.id, parent.gold.text))
                for hyp in parent:
                    fh.write("%s\t%s\t%s\n"%(hyp.parent.id,hyp.id,hyp.text))

    def eval(self):
        for feature in self.features:
            for parent in self:
                if feature.applyParent :
                    ft= feature(parent.gold)
                    ft.eval()
                    print ft.value

                for child in parent:
                
                    ft = feature(child)
                    ft.eval()
                    print ft.value

            
    def __getitem__(self,item):
        return self.sets[item]            

    def __len__(self):
        return len(self.sets)
    def __iter__(self):
        return (self.sets[x] for x in self.sets)

'''
class CQAHypData
a class to store different hypotheses for community question answering
here: 
the parent is the question
the text is the body of the response
the tag is the type of answer: "Good", "Bad",
'''
class CQAHypData(HypData):
    values={'Good':2,'Bad':0,'Not Applicable':-1,'Potential':0,'GOLD':-1,'Dialogue':-1,'Other':-1,'Not English':-1}
    def __init__(self, id, subj,body,tag="GOLD",parent=None):
        super(self.__class__,self).__init__(id,body,CQAHypData.values[tag],parent)
        if parent != None:
            self.parent_id = parent.id
        else:
            self.parent_id= self.id
        self.subj=subj
        self.tag=tag

    def isValid(self): # Only hyps with valid tags are eligible for sampling
        return self.value >=0
    
'''
class CQAHypSet
a class to store different answers corresponding to a same question
'''

class CQAQHypSet(HypSet):
    def __init__(self,question): #create object with a question
        super(self.__class__,self).__init__(question)
