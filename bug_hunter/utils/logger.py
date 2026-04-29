import logging

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Set the default logging level

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create file handler and set level to debug
        fh = logging.FileHandler('bug_hunter.log')
        fh.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to handlers
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def debug(self, message: str):
        self.logger.debug(message)

# Example usage:
# logger = Logger(__name__)
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.debug('This is a debug message')
