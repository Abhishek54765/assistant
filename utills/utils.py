import pyttsx3
import speech_recognition as sr
import re
import random


class Utils:

    def __init__(self, logger):
        self.logger = logger
        self.engine = pyttsx3.init()

    def playsound(self,  text):
        self.engine.say(text)
        self.engine.runAndWait()

    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for u in utterances:
            normalized += u.lower() + '|'
        return normalized[:-1]

    def match_utterances(self, voice_input, utterances):
        self.logger.info('Normalizing utterances.....')
        normalized = Utils.normalize_utterances(utterances)
        compile = re.compile(normalized)
        return compile.search(voice_input)

        #"tony/wake up tony/hello tony/hi tony"

    @staticmethod
    def choose(responses):
        return random.choice(responses)



