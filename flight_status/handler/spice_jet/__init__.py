from flight_status.handler.web_controller import WebController
from flight_status.handler.spice_jet.scraper import Scraper


class SpiceJet(object):
    def __init__(self, config):
        self.url = {
            "home": "https://book.spicejet.com/",
            "pnr_status": "https://book.spicejet.com/RetrieveBooking.aspx"
        }
        self.user_config = config

    def get_pnr_status(self, parameters):
        pass
        web = WebController(self.user_config)
        web.open_page(url=self.url["pnr_status"])
        web.input_text(tag_type="id",
                       name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_ConfirmationNumber",
                       value=parameters["booking_reference"])
        web.input_text(tag_type="id",
                       name="ControlGroupRetrieveBookingView_ResendItineraryRetrieveBookingView_RecordLocator",
                       value=parameters["booking_reference"])
        web.input_text(tag_type="id",
                       name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_CONTACTEMAIL1",
                       value=parameters["email_lastname"])
        web.click_element(tag_type="id",
                          name="ControlGroupRetrieveBookingView_BookingRetrieveInputRetrieveBookingView_ButtonRetrieve")
        status = web.wait_till_load(tag_type="id", name="bookingDetail")

        if status:
            html_source = web.get_attribute(tag_type="id", name="itineraryBody", attribute="innerHTML")
            web.exit_driver()
            scraper_controller = Scraper()
            response = scraper_controller.get_pnr_status(html_source)
            return response
        else:
            return {"error": "Please check the input details / Server Error"}
