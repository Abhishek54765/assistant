import speech_recognition as sr
from utills.utils import Utils
from intents.application import Application


class Tony:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.speech = sr.Recognizer()
        self.utils = Utils(self.logger) #object
        self.application = Application

    def read_voice_input(self):
        with sr.Microphone() as source:
            self.logger.info('listening.....')
            try:
                audio = self.speech.listen(source, timeout=10, phrase_time_limit=5 )  # it will return byte code of what we speak.

                voice_input = self.speech.recognize_google(audio_data=audio).lower()
                return voice_input
            except sr.RequestError as e:
                self.logger.info("network error,")
            except Exception as e:
                pass

    def run(self):
        self.logger.info('Running thread....')
        while True:
            input = self.read_voice_input()
            if input:
                self.logger.info('voice input: {}'.format(input))
                for key in self.config:
                    matched = self.utils.match_utterances(input, self.config[key]['utterances'])
                    if matched:
                        break
                    else:
                        key = 'null'
                        continue

                self.logger.info('executed indent:' + key)
                if key == 'intent_greeting':
                    response = Utils.choose(self.config[key]['responses'])
                    self.logger.info(response)
                    self.utils.playsound(response)

                elif key == 'intent_applications':
                    apps = self.config[key]['applications']
                    Application(logger=self.logger, command=input, applications=apps).launch()
                    if  Application(logger=self.logger, command=input, applications=apps).get_path() == 'null':
                        pass
                    else:
                        response = Utils.choose(self.config[key]['responses'])
                        self.logger.info(response)
                        self.utils.playsound(response)

                elif key == 'intent_close':
                    apps = self.config[key]['applications']
                    Application(logger=self.logger, command=input, applications=apps).close()
                    response = Utils.choose(self.config[key]['responses'])
                    self.logger.info(response)
                    self.utils.playsound(response)
