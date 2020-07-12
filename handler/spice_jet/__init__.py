from web_controller import WebController
from handler.spice_jet.scraper import Scraper


class SpiceJet(object):
    def __init__(self):
        self.url = {
            "home": "",
            "pnr_status": ""
        }

    def get_pnr_status(self, booking_reference, email_lastname):
        pass
        # x = WebController()
        # x.open_page(url="https://book.spicejet.com/RetrieveBooking.aspx")
        # x.input_text(type="id", name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_ConfirmationNumber", value=)
        # x.input_text(type="id", name="ControlGroupRetrieveBookingView_ResendItineraryRetrieveBookingView_RecordLocator", value=)
        # x.input_text(type="id", name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_CONTACTEMAIL1", value=)
        # x.click_element(type="id", name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_ButtonRetrieve")
        # if status:
        #     html_source = x.get_attribute(tag_type="class", name="viewItinerary", attribute="innerHTML")
        #     scraper = Scraper()
        #     response = scraper.get_pnr_status(html_source)
        #     return response
        # else:
        #     return False
