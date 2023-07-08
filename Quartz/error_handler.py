
__all__: tuple[str, ...] = (
    "QuartzEngineException",
    "SceneException",
    "ColorException",
)

class QuartzEngineException(Exception):
    
    def __init__(self, arg=None, message: str="An error occured somewhere."):
        self.arg = arg
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.arg)
    
class SceneException(Exception):
    
    def __init__(self, arg=None, message: str="An error occured somewhere."):
        self.arg = arg
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.arg)
    
    
class ColorException(Exception):
    
    def __init__(self, arg=None, message: str="An error occured somewhere."):
        self.arg = arg
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.arg)