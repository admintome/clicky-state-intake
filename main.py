from clicky import Clicky
from mykafka import MyKafka
import logging
import time
import os
from logging.config import dictConfig


class Main(object):

    def __init__(self):
        if 'KAFKA_BROKERS' in os.environ:
            kafka_brokers = os.environ['KAFKA_BROKERS'].split(',')
        else:
            raise ValueError('KAFKA_BROKERS environment variable not set')

        if 'SITE_ID' in os.environ:
            self.site_id = os.environ['SITE_ID']
        else:
            raise ValueError('SITE_ID environment variable not set')

        if 'SITEKEY' in os.environ:
            self.sitekey = os.environ['SITEKEY']
        else:
            raise ValueError('SITEKEY environment variable not set')

        logging_config = dict(
            version=1,
            formatters={
                'f': {'format':
                      '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
            },
            handlers={
                'h': {'class': 'logging.StreamHandler',
                      'formatter': 'f',
                      'level': logging.DEBUG}
            },
            root={
                'handlers': ['h'],
                'level': logging.DEBUG,
            },
        )
        self.logger = logging.getLogger()

        dictConfig(logging_config)
        self.logger.info("Initializing Kafka Producer")
        self.logger.info("KAFKA_BROKERS={0}".format(kafka_brokers))
        self.mykafka = MyKafka(kafka_brokers)

    def init_clicky(self):
        self.clicky = Clicky(self.site_id, self.sitekey)
        self.logger.info("Clicky Stats Polling Initialized")

    def run(self):
        self.init_clicky()
        starttime = time.time()
        while True:
            data = self.clicky.get_pages_data()
            self.logger.info("Successfully polled Clicky pages data")
            self.mykafka.send_page_data(data)
            self.logger.info("Published page data to Kafka")
            time.sleep(300.0 - ((time.time() - starttime) % 300.0))


if __name__ == "__main__":
    logging.info("Initializing Clicky Stats Polling")
    main = Main()
    main.run()
