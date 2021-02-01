# #Command to run the code:
# #python3 volume_of_cube.py
def volume_cube(arg):
    try:
        arg2=int(arg)
        if arg2 < 0:
            return('Value must be greater than zero')
            raise ValueError
    
    except ValueError:
        return('Not a proper input. Please input a integer');
    return arg2*arg2*arg2

