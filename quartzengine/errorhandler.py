
__all__ = (
  "QuartzEngineException",
    "RestException",
  "ClientException"
)

class QuartzEngineException(Exception):
  pass

# If duration is not provided
class RestException(QuartzEngineException):

  def __init__(self, duration, message="Duration you provided: {}, is not a valid duration."):
    self.duration = duration
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return self.message.format(self.duration)
  
#idk the errors to add
class ClientException(QuartzEngineException):
  pass