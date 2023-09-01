from typing import Optional, Literal

from sys import stdout
from threading import Thread, Event
from time import sleep

from .graphics_engine import *
from .error_handler import *

try:
    from getkey import getkey, keys
except ImportError:
    raise QuartzEngineException("You must have 'getkey' installed to use 'tools.py' refer to the docs.")

__all__: tuple[str, ...] = (
    "Menu",
    "Switch",
    "Loops",
    "Pool"
)

class Menu(object):

    def __init__(self, options: list[tuple[str, callable]], display: Literal["vertical", "horizontal"], select_color: type[Color.RGB], previous_key: type[keys], next_key: type[keys]):
        
        if not isinstance(select_color, Color.RGB):
           raise ValueError("Must be a valid 'graphics_engine.Color.RGB' object.")

        if display not in ["vertical", "horizontal"]:
           raise ValueError("Must be 'vertical' or 'horizontal'.")
        
        self.options = options
        self.display = display
        self.select_color = select_color

        self.previous_key = previous_key
        self.next_key = next_key

    def __del__(self):
        pass

    def run(self):
        selected_idx: int = 0

        while(True):
            for idx in self.options:
                if self.options[selected_idx][0] == idx[0]:
                    print(Color.set_foreground(self.select_color) + f"{idx[0]}" + Color.reset(), end="   " if self.display == "horizontal" else "\n")
                else:
                    print(f"{idx[0]}", end="   " if self.display == "horizontal" else "\n")
            if self.display == "horizontal":  print()

            key = getkey()

            if key == self.next_key:
               selected_idx = (selected_idx + 1) % len(self.options)
            elif key == self.previous_key:
               selected_idx = (selected_idx - 1) % len(self.options)
            elif key == keys.ENTER:
                _, target_func = self.options[selected_idx]
                target_func()
                del self
                break
            
            if self.display == "vertical":
                for idx in self.options:
                    stdout.write("\033[F \r")
            else:
                stdout.write("\033[F \r")



class Switch:
    """
    A class to manage toggling between different options.

    Args:
        *options: Variable number of options to be toggled.

    Attributes:
        options (list): List of available options.
        current_index (int): Index of the currently selected option.

    Methods:
        get(): Returns the currently selected option.
        toggle(): Toggles to the next option.
        set_option(option): Sets the switch to a specific option.
    """

    def __init__(self, *options):
        """
        Initialize the Switch instance with given options.

        Args:
            *options: Variable number of options to be toggled.

        Raises:
            ValueError: If the number of options is less than 2.
        """

        if len(options) < 2:
            raise ValueError("A Switch should have at least two options.")
        
        self.options = options
        self.current_index = 0

    def get(self):
        """
        Get the currently selected option.

        Returns:
            The currently selected option.
        """
        return self.options[self.current_index]

    def toggle(self):
        """
        Toggle to the next option and return it.

        Returns:
            The newly toggled option.
        """
        self.current_index = (self.current_index + 1) % len(self.options)
        return self.options[self.current_index]

    def set_option(self, option):
        """
        Set the switch to a specific option.

        Args:
            option (Any): The option to set the switch to.

        Raises:
            ValueError: If the provided option is not in the list of options.
        """
        if option in self.options:
            self.current_index = self.options.index(option)
        else:
            raise ValueError(f"'{option}' is not a valid option.")

    def __str__(self):
        """
        Return a string representation of the Switch instance.

        Returns:
            A string representation of the Switch.
        """
        return f"Switch({', '.join(map(str, self.options))})"



class Loops:
    """
    A class for running a looping process with adjustable delay.

    Args:
        loop_function (callable): The function to be executed in each loop iteration.
        initial_delay (float): Initial delay in seconds before the loop starts.
        delay (float): Delay in seconds between loop iterations.

    Methods:
        loop_process(): Runs the loop process indefinitely.
        start(): Starts the loop process in a separate thread.
    """
  
    def __init__(self, loop_function, initial_delay=0.0, delay=1.0):
        """
        Initialize the Loops instance.

        Args:
            loop_function (callable): The function to be executed in each loop iteration.
            initial_delay (float): Initial delay in seconds before the loop starts.
            delay (float): Delay in seconds between loop iterations.
        """
        self._loop_function = loop_function
        self._stop_event = Event()
        self._initial_delay = initial_delay
        self._delay = delay

    def loop_process(self):
        """
        Runs the loop process indefinitely.
        """
        sleep(self._initial_delay)
        while not self._stop_event.is_set():
            self._loop_function()
            sleep(self._delay)

    def start(self):
        """
        Start the loop process in a separate thread.
        """
        thread = Thread(target=self.loop_process, daemon=True)
        thread.start()

    def stop(self):
        """
        Stop the loop process by setting the stop event.
        """
        self._stop_event.set()



class Pool:
    """
    A class for simulating a pool of items with different drop chances.

    Args:
        loot_table (dict): A dictionary containing items as keys and their drop chances as values.

    Methods:
        roll(): Randomly selects an item from the pool based on drop chances.
    """
    
    def __init__(self, loot_table: type[dict] = None):
        """
        Initialize the Pool instance.

        Args:
            loot_table (dict): A dictionary containing items as keys and their drop chances as values.
        """

        if loot_table is None:
            raise PoolException("loot_pool not provided.")

        total = sum(loot_table.values())
        if total < 100:
            raise PoolException("Pool total is under 100; please keep the total loot pool at 100")
        if total > 100:
            raise PoolException("Pool total is over 100; please keep the total loot pool at 100")

        self.loot_table = loot_table

    def roll(self):
        """
        Randomly select an item from the pool based on drop chances.

        Returns:
            Any: The selected item.
        """

        chances = []
        for key, percent in self.loot_table.items():
            self.chances.extend([key] * percent)

        return random.choice(self.chances)
