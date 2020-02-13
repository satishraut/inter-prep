# Docstrings versus Block comments
# For debuging purpose in comment cannot print on console but docstring do

# This is the string

class Test:
    '''
    This is the multiline sting or we can said that is test class information
    it is good way to understand more advance way
    to impliments the thinks
    '''

    def trying(self):
        return 'testing the way'


obj=Test()

print(obj.__doc__)

