from bread import Bread

class Flatbreads(Bread):
 def __init__(self, stove: bool, oil: bool, seasoning: str, bake: list):
        super().__init__(['flour', 'water', 'sugar', 'salt', 'yeast'])
        self.stove = stove 
        self.oil = oil 
        self.seasoning = seasoning 
        self.bake = bake 

          # Define an abstract class 
class breads(): 
        
        def seasoning(str): 
            pass # This is an abstract method, no implementation here. 

        # Concrete subclass of flatbreads 
        class flatbreads(): 

                def seasoning(str): 
                     return "seasoning"
    # Create instanct of bread 
def __int__(int, flour: int, oil: bool, seasoning: str, bake: list):
        int.flour = flour
        int.oil = oil
        int.seasoning = seasoning
        int.bake = bake 
#flatbread 
def flatbread(*args): 
    return sum(args)


 
