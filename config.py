import sys
import configparser


class Config:
    def __init__(self, config_file="config.ini"):
        parser = configparser.ConfigParser()
        parser.read(config_file)
        if not parser.has_section("postgresql"):
            raise ConfigurationError(
                "One or more required Configuration sections are missing\n"
                f"Check your Configuration file: {parser.sections()}\ninstead of {self.config_sections}"
            )
        self.params = parser.items("postgresql")
        self.host = parser.get("postgresql", "host")
        self.database = parser.get("postgresql", "database")
        self.user = parser.get("postgresql", "user")
        self.password = parser.get("postgresql", "password")

    def as_dict(self):
        config = {}
        for field, value in self.params:
            config[field] = value
        return config
