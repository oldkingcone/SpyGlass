import platform
import time
from os import environ, getlogin
from requests import get
from re import compile, search
from ..presets.preset_values import CGPresets


class CgPrompt:
    def __init__(self):
        self.intro = "Welcome to the SpyGlass! \n\n(Please note, this api requires an API key. Right now there is no " \
                     "way " \
                     "to sign up for one, all API keys are pre shared with the community, after purchase. If you " \
                    "have any questions, please contact me on discord: \n\033[0;32mhttps://discord.gg/TCxMjQNrW5\033[" \
                     "0m)"
        self.doc_header = "Available Commands (type help <command>):"
        self.undoc_header = "Undocumented Commands:"
        self.ruler = "*"
        self.last_status = None
        self.lastcmd = None
        self.prompt = "\033[0;35mᕮ spyglass ꩜ \033[0m\033[0;36m{}\033[0m@{}\033[0;35m ᕭ\033[0m\033[3;33m[\033[0m {} " \
                      "\033[3;33m - \033[0;34mLast Status Check at {}\033[0m \033[3;33m]\033[0;36m(Last Command: {" \
                      "})\033[0m\033[0m\n\033[1;36mᐕ\033[0m"

    def get_status(self):
        if environ.get('API_IPKEY'):
            if self.last_status is None:
                self.last_status = time.strftime("%H:%M:%S", time.localtime())
                d = get("https://redirecthost.online:8443/", headers = {"x-Api-Key": environ.get('API_IPKEY'),
                        "User-Agent": CGPresets().user_agent}).text
                if search(compile("has been banned"), d):
                    return "Key status: \033[0;31mBANNED\033[0m"
            elif int(time.strftime("%H:%M:%S", time.localtime()).split(":")[1]) - int(self.last_status.split(":")[1])\
                    > 10 or int(time.strftime("%H:%M:%S", time.localtime()).split(":")[0]) - int(
                    self.last_status.split(":")[0]) == 1:
                self.last_status = time.strftime("%H:%M:%S", time.localtime())
                d = get("https://redirecthost.online:8443/", headers = {"x-Api-Key": environ.get('API_IPKEY'),
                        "User-Agent": CGPresets().user_agent}).text
                if search(compile("has been banned"), d):
                    return "Key status: \033[0;31mBANNED\033[0m"
            return "Key status: \033[0;32mActive\033[0m"
        else:
            return "Key status: \033[1;31mInactive\033[0m"

    def __str__(self):
        return self.prompt.format(getlogin(), platform.node(), self.get_status(), self.last_status,
                                  self.lastcmd)
