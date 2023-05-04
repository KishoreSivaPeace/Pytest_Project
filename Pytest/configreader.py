from configparser import ConfigParser


def readconfig(section, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)

