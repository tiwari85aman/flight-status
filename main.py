from handler.indigo import Indigo
from handler.spice_jet import SpiceJet


class Airlines(object):
    def __init__(self, aviation):
        self.mapping = {
            "indigo": Indigo,
            "spice_jet": SpiceJet
        }
        self.aviation = self.mapping[aviation]()

    def get_pnr_status(self, parameters):
        return self.aviation.get_pnr_status(parameters)


# TESTING
from env.variables import indigo_config, spice_jet_config

indigo = Airlines(aviation="indigo")
print(indigo.get_pnr_status(parameters=indigo_config))

spice_jet = Airlines(aviation="spice_jet")
print(spice_jet.get_pnr_status(parameters=spice_jet_config))
