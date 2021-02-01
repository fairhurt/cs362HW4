# #Command to run the code:
# #python3 average_elements.py
def average_elements_list(arg):
    try:
       if len(arg) == 0:
            return ('List cannot be empty divide by zero error')
            raise ValueError
        
    except ValueError:
        return('Must be list of integers')

    try:
        if all(isinstance(i, (int)) for i in arg)== False:
                return ('Must be integer')
                raise ValueError
    except ValueError:
        return ('Must be list of intgers')

    
  

    return sum(arg) / len(arg)

