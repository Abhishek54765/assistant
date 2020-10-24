import os
class Volume:

    def __init__(self, logger, key):
        self.key = key
        self.logger = logger
    @staticmethod
    def increase_volume():
        cmd = 'nircmd.exe'
        direction = cmd + ' ' + 'changesysvolume' + ' ' + '5000'
        os.system(direction)