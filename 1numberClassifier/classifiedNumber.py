class ClassifiedNumber:
    
    __number = 0
    __classifiedAs = 3
    
    def __init__(self, number):
        
        self.__number = number
        
        if number == 0:
            
            self.__classifiedAs = 0 # zero
            
        elif number > 0:
            
            self.__classifiedAs = 1 # positive
            
        elif number < 0:
            
            self.__classifiedAs = 2 # negative
            
    def number(self):
        
        return self.__number
    
    def classifiedAs(self):
        
        return self.__classifiedAs
    
def classifiedAsString(classifiedAs):
    
    if classifiedAs == 0:
        
        return "Zero"
    
    elif classifiedAs == 1:
        
        return "Positive"
    
    elif classifiedAs == 2:
        
        return "Negative"