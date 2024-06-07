from base_set import BaseSet

# class for representing the string text of various set representation and operations
class StringSet(BaseSet):
    def __init__(self, elements=None):
        super().__init__(elements)
    
    def __str__(self):
        return '{' + ', '.join(map(str, self.elements)) + '}'