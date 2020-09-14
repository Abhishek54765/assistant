from asistant.tony import Tony
import logging
import json
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s:%(message)s',datefmt='%y-%n-%d %M:%M:%S')

    with open('config/config.json') as file:
        config = json.load(file)
        logging.info('tony is initializing...')
        Tony(config=config, logger=logging).run()