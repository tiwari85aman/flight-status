from flight_status.handler.web_controller import WebController
from flight_status.handler.air_asia.scraper import Scraper


class AirAsia(object):
    def __init__(self, config):
        self.url = {
            "home": "",
            "pnr_status": "https://www.airasia.com/member/search?culture=en-GB"
        }
        self.user_config = config

    def get_pnr_status(self, parameters):
        web = WebController(self.user_config)
        web.open_page(url=self.url["pnr_status"])
        web.input_text(tag_type="id", name="input-depCity", value=parameters["departure_city"])
        web.input_text(tag_type="id", name="input-pnr", value=parameters["booking_reference"])
        web.input_text(tag_type="id", name="input-lastName", value=parameters["email_lastname"])
        web.click_element(tag_type="class", name="aasbw-button")

        status = web.wait_till_load(tag_type="class", name="icon-container")
        if status:

            scraper_controller = Scraper()
            web.click_element(tag_type="class", name="icon-container")
            html_page = web.get_attribute(tag_type="class", name= "booking-page", attribute="innerHTML")
            web.exit_driver()
            response = scraper_controller.get_pnr_status(html_page)
            return response
        else:
            # TODO: Handle incorrect details and server error differently
            return {"error": "Please check the input details / Server Error"}
