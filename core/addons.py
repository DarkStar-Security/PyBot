import re


class Commands:
    commands = {
        "&help": {"func": "bot_help"},
        "&authors": ["Credits for GPL development of this bot goes to r0073d, Woz & v1"],
        "&version": ["The current version is 1.3 Use &help to get some more information."],
        "pep8": ["Here is the URL for PEP8: https://www.python.org/dev/peps/pep-0008/"],
        "pip": ["pip is a python package manager similar to apt-get. It installs modules and packages,",
                "that you would not have by default in the standard library.",
                "Official Documentation here: https://pip.pypa.io//, when in doubt, uninstall pip and re-install.",
                "Don't forget to use pip for your python version!"],
        "py": ["You can find the Python Package Index here:  https://pypi.python.org/pypi"],
        "py3": ["0. There are many improvements made in python3 you will not find in python2.",
                "1. Socket handling, threading, better standard lib, the list goes on.",
                "2. Realize that if you learn 2.7.5, you will be almost 10 revisions behind!",
                "Docs you should have a look at: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html",
                "and https://docs.python.org/3/whatsnew/3.6.html"],
        "socket": ["Here is the doc for sockets: https://docs.python.org/3/library/socket.html"],
        "science": ["Science Bitches!!  https://www.youtube.com/watch?v=9Cd36WJ79z4"],
        "freedom": ["It is important that you watch this:  https://www.youtube.com/watch?v=Ag1AKIl_2GM"],
        "keylogger": ["Here is a basic KeyLogger:  https://www.youtube.com/watch?v=8BiOPBsXh0g"],
        "hack": ["Learning to 'hack' is like learning to invent. It doesn't work that way.",
                 "Hacking is a mindset, a form of discovery, not DOSing a random server.",
                 "You are not a hacker just because you can use nmap, hping3, etc.",
                 "If you are sincere about 'hacking', then learn2codepls"]
    }

    def __init__(self, config):
        self.config = config

    def add_command(self, entry, desc):
        if isinstance(desc, list):
            self.commands[entry] = desc
        else:
            self.commands[entry] = [desc]

    def exec_command(self, entry):
        info = self.commands[entry.lower()]
        if isinstance(info, list):
            msg = "\n".join(i for i in info)
        else:
            msg = globals()[info["func"]]()
        return msg

    def bot_help(self):
        info = ", ".join(c for c in self.commands)
        return info

    def join(self, data):
        nick = re.findall(r":((\w|-|.|_)+)!", data)
        if nick[0] == self.config["nick"]:
            msg = "Greetings! My name is {0}".format(str(self.config["nick"]))
        else:
            msg = "Welcome {0}!".format(nick[0])
        return msg
