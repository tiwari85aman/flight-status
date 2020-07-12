from handler.indigo import Indigo
# from handler.spice_jet import SpiceJet


class Airlines(object):
    def __init__(self, aviation):
        self.mapping = {
            "indigo": Indigo,
            # "spice_jet": SpiceJet
        }
        self.aviation = self.mapping[aviation]()
        self.aviation.get_pnr_status()


print(Airlines(aviation="indigo"))
