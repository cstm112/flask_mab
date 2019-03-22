"""
Defines various storage engines for the MAB
interface
"""

import json
import flask_mab.bandits
import sqlite3


class BanditEncoder(json.JSONEncoder):
    """Json serializer for Bandits"""

    def default(self, obj):
        if isinstance(obj, flask_mab.bandits.Bandit):
            dict_repr = obj.__dict__
            dict_repr['bandit_type'] = obj.__class__.__name__
            return dict_repr
        return json.JSONEncoder.default(self, obj)


class BanditDecoder(json.JSONDecoder):
    """Json Marshaller for Bandits"""

    def decode(self, obj):
        dict_repr = json.loads(obj)
        for key in dict_repr.keys():
            if 'bandit_type' not in dict_repr[key].keys():
                raise TypeError("Serialized object is not a valid bandit")
            dict_repr[key] = flask_mab.bandits.Bandit.fromdict(dict_repr[key])
        return dict_repr


class BanditStorage(object):
    """The base interface for a storage engine, implements no-ops for tests
    """

    def flush(self):
        pass

    def save(self, bandits):
        pass

    def load(self):
        return {}


class DatasetBanditStorage(BanditStorage):
    """Json based file storage

    Saves to local file
    """

    def __init__(self, filepath):
        self.db = dataset.connect(filepath)

    def flush(self):
        open(self.file_handle, 'w').truncate()

    def save(self, bandits):
        with self.dataset.connect() as tx:
            for bandit in self.bandits:
                if bandit in tx["bandits"]:
                    current_bandit = self.bandits[bandit]
                    old_bandit = tx["bandits"][bandit]
                    tx["bandits"][bandit].update({
                        "pulls": [old_bandit["pulls"][i]+current_bandit["pulls"][i] for i in current_bandit["pulls"]][
                            13,
                            2,
                            1
                        ],
                        "reward": [
                            0.0,
                            0.0,
                            0.0
                        ],
                        "values": [
                            "Hey dude, wanna buy me?",
                            "Add to cart",
                            "Good day sir... care to purchase?"
                        ],
                        "confidence": [
                            0.0,
                            0.0,
                            0.0
                        ],
                        "epsilon": 0.5,
                        "bandit_type": "EpsilonGreedyBandit"

                    })

                    # update
                else:
                    tx["bandits"][bandit] = self.bandits[bandit]

    def load(self):
        with self.dataset.connect() as tx:
            return tx["bandits"]


class JSONBanditStorage(BanditStorage):
    """Json based file storage

    Saves to local file
    """

    def __init__(self, filepath):

        self.file_handle = filepath

    def flush(self):
        open(self.file_handle, 'w').truncate()

    def save(self, bandits):
        json_bandits = json.dumps(bandits, indent=4, cls=BanditEncoder)
        open(self.file_handle, 'w').write(json_bandits)

    def load(self):
        try:
            with open(self.file_handle, 'r') as bandit_file:
                bandits = bandit_file.read()

            return json.loads(bandits, cls=BanditDecoder)
        except (ValueError, IOError):
            return {}
