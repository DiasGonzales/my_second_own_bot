import time
from main import cmd_await30


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time.sleep(1)
        time_sec -= 1

        if time_sec == 0:
            cmd_await30()



countdown(2) # Example 2 min >> countdown(120)