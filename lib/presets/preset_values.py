import platform
import os


class CGPresets:
    def __init__(self):
        self.user_agent = "SpyGlassClient(1.0)"
        if platform.platform().startswith('Windows'):
            self.CG_API_HOME = os.environ.get('APPDATA') + '/.cg_api'
            self.clear = 'cls'
        else:
            self.CG_API_HOME = os.environ.get('HOME') + '/.cg_api'
            self.clear = 'clear'