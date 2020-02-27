import json
import logging
import os
import re
from logging import config as log_config


class LambdaLogFormatter(logging.Formatter):
    """
    Rewrites multiline log messages so that we get a single CloudWatch log event
    """

    def __init__(self, inner):
        super().__init__(self)
        self.inner = inner

    def format(self, record):
        msg = self.inner.format(record)
        if msg:
            # this line makes leading spaces show up in Cloudwatch Logs
            msg = re.sub(r'(?m)^\s+', lambda x: '\u2003' * len(x.group()), msg)
            # this line replaces newlines, so the entire msg will be captured as a single log event
            msg = msg.replace('\n', '\r')
        return msg


# merge app log configuration into base configuration
config = json.load(open(os.path.join(os.path.dirname(__file__), "logging.json"), 'rb'))
log_config.dictConfig(config)

# hack formatters
for handler in logging.getLogger().handlers:
    formatter = LambdaLogFormatter(handler.formatter)
    handler.setFormatter(formatter)

# root application log
logger = logging.getLogger("jts")
