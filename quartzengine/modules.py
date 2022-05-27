import os

def checkForUpdates():
  try:  import colorama
  except:  os.system('pip install colorama')
  
  return "Finished Update Wheel"