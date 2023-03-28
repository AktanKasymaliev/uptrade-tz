from configparser import ConfigParser, NoOptionError, NoSectionError
import os

def load_conf(config: ConfigParser, section: str, name: str, default=None) -> str:
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError) as e:
        output = default
    return output

def config() -> None:
    config_parse = ConfigParser()
    config_parse.read("settings.ini")
    DATABASE = "DATABASE"
    SYSTEM = "SYSTEM"

    #DATABASE
    os.environ.setdefault("DATABASE_NAME", load_conf(config_parse, DATABASE, "NAME"))
    os.environ.setdefault("DATABASE_USER", load_conf(config_parse, DATABASE, "USER"))
    os.environ.setdefault("DATABASE_PASSWORD", load_conf(config_parse, DATABASE, "PASSWORD"))
    os.environ.setdefault("DATABASE_HOST", load_conf(config_parse, DATABASE, "HOST"))
    os.environ.setdefault("DATABASE_PORT", load_conf(config_parse, DATABASE, "PORT"))
    
    #SYSTEM
    os.environ.setdefault("DJANGO_DEBUG", load_conf(config_parse, SYSTEM, "DJANGO_DEBUG", "False"))
    os.environ.setdefault("DJANGO_KEY", load_conf(config_parse, SYSTEM, "DJANGO_KEY", "super_secret_key"))