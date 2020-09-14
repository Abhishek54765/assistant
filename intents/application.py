import os
import pyttsx3
class Application:

    def __init__(self, logger, applications, command):
        self.logger = logger
        self.applications = applications
        self.command = command
        self.engine = pyttsx3.init()

    def get_path(self):
        key = self.command.split(' ')[1].strip()
        print(key)
        if key in self.applications:

            for app, path in self.applications.items():
                if key in app:
                    return path
                else:
                    path = 'null'
                    continue
        else:
            return 'null'

    def launch(self):
        path = self.get_path()
        if path != 'null':
            self.logger.info('return path:' + path)
            cmd = 'explorer'
            direction = cmd + ' ' + path
            os.system(direction)
        else:
            self.engine.say('application not found')
            self.engine.runAndWait()


    def close(self):
        path = self.get_path()
        self.logger.info('closing path:' + path)
        cmd = 'taskkill'
        direction = cmd + ' ' + '/im' + ' ' + path
        os.system(direction)

