from bread import Bread

class Flatbreads(Bread):
 def __init__(self, stove: bool, oil: bool, seasoning: str):
        super().__init__(['flour', 'water', 'sugar', 'salt', 'yeast'])
        self.stove = stove 
        self.oil = oil 
        self.seasoning = seasoning 
 
