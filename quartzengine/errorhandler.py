
__all__ = (
  
  "QuartzEngineException",
    "SceneException",
    "RestException",
  
  "DisplayException",
    "SetFontException",
  
  "MapException",
  
  "ToolsException",
    "PoolException"

)

class QuartzEngineException(Exception):
  pass

class SceneException(QuartzEngineException):

  def __init__(self, scene, message="Scene: {}, not a valid scene."):
    self.scene = scene
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message.format(self.scenee)

class RestException(QuartzEngineException):

  def __init__(self, duration, message="Duration you provided: {}, is not a valid duration."):
    self.duration = duration
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message.format(self.duration)



class DisplayException(Exception):
  pass

class SetFontException(DisplayException):

  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message
    


class MapException(Exception):

  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message



class ToolsException(Exception):
  pass

class PoolException(ToolsException):

  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message