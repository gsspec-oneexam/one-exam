import configparser, logging


def getConfig():
    try:
        config = configparser.ConfigParser()
        config.read('D:\projects\pocs\poc\config.ini')
        return config
    except Exception as e:
        raise


def configureLogging(logConfig=getConfig()['log']):
    try:
        logging.basicConfig(filename=logConfig['dir_path'] + '/studentapp.log',
                            level=logConfig.getint('level'), format=logConfig['format'],
                            datefmt=logConfig['date_format'])

    except Exception as e:
        raise