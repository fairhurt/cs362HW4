# #Command to run the code:
# #python3 average_elements.py
def combine_first_and_last(first, last):
    if isinstance(first,str) == False:
        return ("First name is not a string")
    if isinstance(last,str) == False:
        return ("Last name is not a string")
    fullname= first +' '+ last 
    return fullname