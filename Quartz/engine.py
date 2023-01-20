from .graphicsEngine import GraphicsEngine
from .errorHandler import *

import os

__all__ = ["Engine", "GameObject", "RigidBody"]



def RigidBody(**kwargs):
    is_collidible = kwargs.get("is_collidible", False)
    collides_with = kwargs.get("collides_with", [])
    uses_gravity = kwargs.get("uses_gravity", True)

class GameObject:

    def __init__(self, texture: str="#", rigidbody=RigidBody()):
        self.texture = texture
        self.rigidbody = RigidBody()

        self.X = 0
        self.Y = 0
        self.Vector2 = [self.X, self.Y]



class SceneManager:

    def __init__(self, display, default_scene):
        self.display = display
        
        self.scenes = [default_scene]
        self.current_scene = 1

    def AddScene(self, scene=None):
        if scene == None:
            raise SceneException(scene, "Scene: {} not Provided!")
        else:
            try:
                self.scenes.append(scene)
            except:
                raise SceneException(scene, "Scene: {}, failed to load")
    
    def LoadScene(self, scene=None):
        if scene == None:
            raise SceneException(scene, "Scene: {} Not Provided!")
        elif scene == "++":
            self.current_scene += 1
            self.display.clear()
            self.scenes[self.current_scene-1]()
        else:
            try:
                self.current_scene = scene
                self.scenes[scene]()
            except:
                raise SceneException(scene, f"Could not execute: {scene}.")



class Engine:

    @property
    def title(self):
        return self.name

    @title.setter
    def title(self, value: str):
        self.name = value

    def __init__(self):
        self.name = f"QuartzEngine | {os.path.basename(__file__)}"

        self.GraphicsEngine = GraphicsEngine()

        self.SceneManager = SceneManager(self.GraphicsEngine, self.root)

    def setup(self):
        pass

    def root(self):
        """
        The default scene QuartzEngine will use when no others are defined.
        """
        
        print("Default Scene")

    def wait(self, duration=None):
        timedict = {"s": 1, "m": 60, "h": 3600}

        if duration == None:
            raise WaitException(duration)
        elif duration[-1:] not in timedict:
            raise WaitException(duration[-1:])
        else:
            time = int(duration[:-1])
            smh = duration[-1:]
            return sleep(timedict.get(smh, 1) * time)

    def run(self):
        self.setup()
        
        if os.name == "nt":
            os.system(f"title {self.name}")
        else:
            os.system(f"printf \033]0;{self.name}\007")