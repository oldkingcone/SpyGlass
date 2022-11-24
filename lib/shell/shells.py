import cmd
import os

import getpass
from requests import get
from os import environ, system
from json import dumps
from lib.secure_storage.encrypt_key import AESCipher
from lib.graphics.main_graphics import CGGraphics
from lib.prompt.prom import CgPrompt
from lib.plugins.dynamicLoadClasses import DynamicLoad
from lib.presets.preset_values import CGPresets

plugins = DynamicLoad()
presets = CGPresets()
cg_prompt = CgPrompt()
store_safe = AESCipher(getpass.getpass("Enter password to encrypt/decrypt your API key store this password in a "
                                       "password manager, make sure its secure.\n->").strip())
system(presets.clear)
if not os.path.isdir(presets.CG_API_HOME):
    os.mkdir(presets.CG_API_HOME)
if os.path.isfile(presets.CG_API_HOME + '/.cg_key'):
    with open(f"{presets.CG_API_HOME}/.cg_key", 'r') as f:
        environ.setdefault('API_IPKEY', store_safe.decrypt(f.read()))


class CgShell(cmd.Cmd):
    graphics = CGGraphics()
    file = None
    prompt = cg_prompt
    intro = cg_prompt.intro + "\n" + graphics.random_graphics()
    ruler = cg_prompt.ruler

    def default(self, line):
        if line == 'x' or line == 'q':
            return self.do_exit(line)
        else:
            self.do_command(line)

    def do_help(self, arg: str) -> bool or None:
        cg_prompt.lastcmd = self.lastcmd
        if arg:
            try:
                doc = getattr(self, 'do_' + arg).__doc__
                if doc:
                    print(doc)
                    return
            except AttributeError:
                pass
            print(self.nohelp % (arg,))
        else:
            print(self.intro)
            names = self.get_names()
            commands = []
            for name in names:
                if name[:3] == 'do_':
                    commands.append(name[3:])
            commands.sort()
            self.print_topics(self.doc_header, commands, 15, 80)
        return None

    def do_exit(self, arg):
        """
        Exit the application. Shorthand: Ctrl-D.
        """
        print('Thank you for using Spyglass')
        exit(0)

    def do_clear(self, arg):
        """
        Clear the screen
        """
        cg_prompt.lastcmd = self.lastcmd
        system(presets.clear)

    def do_activate(self, arg):
        """
        Activate your API Key, required for searching. Requirements pre-shared/purchased API key. example:
        activate <API_KEY>
        """
        cg_prompt.lastcmd = self.lastcmd
        if not os.path.isfile(f"{presets.CG_API_HOME}/.cg_key") or not os.path.isfile(f"{presets.CG_API_HOME}/.cg_key"):
            key = parse_arg(arg)
            headers = { "X-Api-Key": f"{key[0]}", "User-Agent": CGPresets().user_agent }
            resp = get(
                f"https://redirecthost.online:8443/",
                headers = headers
                )
            if "invite only." not in resp.text:
                print("\033[0;32m[ + ] API Key Activated [ + ]\033[0m")
                environ.setdefault('API_IPKEY', f"{key[0]}")
                with open(f"{presets.CG_API_HOME}/.cg_key", 'w') as f:
                    f.write(store_safe.encrypt(key[0]).decode())
                os.chmod(f"{presets.CG_API_HOME}/.cg_key", 0o600)
            else:
                print("[ ! ]\033[0;31mAPI Key not activated or valid\033[0m, please reach out to the developer for "
                      "more information.\nIf you "
                      "dont know who the developer is, you probably dont have a valid key. [ ! ]")
        else:
            print("\033[0;34m[ - ] API Key already activated [ - ]\033[0m")

    def emptyline(self):
        if self.lastcmd:
            cg_prompt.lastcmd = self.lastcmd
            self.lastcmd = ''
            return self.onecmd('\n')

    def do_multi(self, arg):
        """
        Search multiple IP Addresses, separated by a comma. example: multi <IP1>,<IP2>,<IP3>
        """
        cg_prompt.lastcmd = self.lastcmd
        i = parse_arg(arg)
        if 'API_IPKEY' in environ:
            headers = { "X-Api-Key": environ.get('API_IPKEY'), "User-Agent": CGPresets().user_agent}
            for x in str(i[0]).split(','):
                print('Searching for IP Address: ' + x)
                resp = get(
                    f"https://redirecthost.online:8443/C5XTVFX7MaS0ZA/IN662nSM03AvJUm6lYRZ?ip={x}",
                    headers = headers
                    )
                j_data = resp.json()
                print("{")
                for da in j_data.__iter__():
                    print(f"\t\033[0;34m{da}\033[0m : \033[2;35m{j_data[da]}\033[0m")
                print("}")
                input('Press Enter to continue...')
        else:
            print("API Key not activated, please activate your API Key using the activate command, if you need "
                  "assistance please use the command: help activate")

    def do_readfromfile(self, arg):
        """
        Read IP Addresses from a file, separated by a new line. Example: readfromfile <FILE_PATH>
        """
        cg_prompt.lastcmd = self.lastcmd
        f = parse_arg(arg)
        if 'API_IPKEY' in environ:
            with open(f[0], 'r') as file:
                for line in file:
                    headers = { "X-Api-Key": environ.get('API_IPKEY'), "User-Agent": CGPresets().user_agent }
                    print('Searching for IP Address: ' + line)
                    resp = get(f"https://redirecthost.online:8443/C5XTVFX7MaS0ZA/IN662nSM03AvJUm6lYRZ?ip={line}",
                               headers = headers)
                    j_data = resp.json()
                    print("{")
                    for da in j_data.__iter__():
                        print(f"\t\033[0;34m{da}\033[0m : \033[2;35m{j_data[da]}\033[0m")
                    print("}")
                    input('Press Enter to continue...')
        else:
            print("API Key not activated, please activate your API Key using the activate command, if you need "
                  "assistance please use the command: help activate")

    def do_single(self, arg):
        """
        Search a single IP Address. Example: single <IP>
        """
        cg_prompt.lastcmd = self.lastcmd
        i = parse_arg(arg)
        if 'API_IPKEY' in environ:
            headers = { "X-Api-Key": environ.get('API_IPKEY'), "User-Agent": CGPresets().user_agent }
            print('Searching for IP Address: ' + i[0])
            resp = get(f"https://redirecthost.online:8443/C5XTVFX7MaS0ZA/IN662nSM03AvJUm6lYRZ?ip={i[0]}",
                       headers = headers)
            j_data = resp.json()
            print("{")
            for da in j_data.__iter__():
                print(f"\t\033[0;34m{da}\033[0m : \033[2;35m{j_data[da]}\033[0m")
            print("}")
        else:
            print("API Key not activated, please activate your API Key using the activate command, if you need "
                  "assistance please use the command: help activate")

    def do_reload(self, arg):
        """
        Reload the API Key
        """
        cg_prompt.lastcmd = self.lastcmd
        if 'API_IPKEY' in environ:
            del environ['API_IPKEY']
            os.remove(f"{presets.CG_API_HOME}/.cg_key")
            print("API Key env variable has been deleted, please feel free to utilize the activate command to "
                  "re-activate your key.")
        else:
            print("API Key not activated, please activate your API Key using the activate command, if you need "
                  "assistance please use the command: help activate")

    def do_command(self, arg):
        """
        Run a local shell command, example: command <COMMAND>
        """
        cg_prompt.lastcmd = "local -> " + self.lastcmd
        c = parse_arg(arg)
        system(f"{' '.join(c)}")

    def do_plugins(self, arg):
        """
        List all plugins
        """
        a = parse_arg(arg)
        print(a)
        cg_prompt.lastcmd = self.lastcmd
        if a[0] == 'list':
            plugins.list()
        elif a[0] == 'load':
            plugins.load(a[1])
        elif a[0] == "load_all":
            plugins.load_all()


def parse_arg(arg):
    return tuple(map(str, arg.split()))