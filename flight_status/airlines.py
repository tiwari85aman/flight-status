from .handler.indigo import Indigo
from .handler.spice_jet import SpiceJet
from .handler.air_asia import AirAsia


class Airlines(object):
    def __init__(self, aviation, config):
        self.aviation = None
        self.mapping = {
            "indigo": Indigo,
            "spice_jet": SpiceJet,
            "air_asia": AirAsia
        }
        self.setup(aviation, config)

    def setup(self, aviation, config):
        try:
            self.aviation = self.mapping[aviation](config)
        except KeyError as e:
            raise Exception("This aviation company is not yet available, Please refer docs!")

    def get_pnr_status(self, parameters):
        return self.aviation.get_pnr_status(parameters)

