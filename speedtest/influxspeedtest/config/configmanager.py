import configparser
import os
import sys


class ConfigManager():

    def __init__(self, config):
        print('Loading Configuration File {}'.format(config))
        self.servers = []
        config_file = os.path.join(os.getcwd(), config)
        if os.path.isfile(config_file):
            self.config = configparser.ConfigParser()
            self.config.read(config_file)
        else:
            print('ERROR: Unable To Load Config File: {}'.format(config_file))
            sys.exit(1)

        self._load_config_values()
        print('Configuration Successfully Loaded')

    def _load_config_values(self):

        # General
        self.delay = self.config['GENERAL'].getint('Delay', fallback=2)

        # InfluxDB
        self.influx_version = self.config['INFLUXDB'].getint('Version', fallback=1)
        self.influx_address = self.config['INFLUXDB']['Address']
        self.influx_org = self.config['INFLUXDB'].get('Organization', fallback='No_Organization_Defined')
        self.influx_token = self.config['INFLUXDB'].get('Token', fallback='No_Token_Defined')
        self.influx_bucket = self.config['INFLUXDB'].get('Bucket', fallback='speedtests')
        self.influx_timeout = self.config['INFLUXDB'].getint('Timeout', fallback=6000)
        self.influx_port = self.config['INFLUXDB'].getint('Port', fallback=8086)
        self.influx_database = self.config['INFLUXDB'].get('Database', fallback='speedtests')
        self.influx_user = self.config['INFLUXDB'].get('Username', fallback='')
        self.influx_password = self.config['INFLUXDB'].get('Password', fallback='')
        self.influx_ssl = self.config['INFLUXDB'].getboolean('SSL', fallback=False)
        self.influx_verify_ssl = self.config['INFLUXDB'].getboolean('Verify_SSL', fallback=True)

        # Logging
        self.logging_level = self.config['LOGGING'].get('Level', fallback='debug')
        self.logging_level = self.logging_level.upper()

        # Speedtest
        test_server = self.config['SPEEDTEST'].get('Server', fallback=None)
        if test_server:
            self.servers = test_server.split(',')
        self.share = self.config['SPEEDTEST'].getboolean('Share', fallback=False)
