"""Various helper functions, lazily dumped in one file for now"""
import json


PARAMS = {
    "SECRETS_PATH": ".env",  # Path to file with tokens
}


def load_secrets():
    """Read in secrets from file - includes client ID and client secret"""
    with open(PARAMS["SECRETS_PATH"], "r") as fhand:
        return json.loads(fhand.read())

