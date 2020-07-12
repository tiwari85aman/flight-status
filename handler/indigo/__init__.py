from web_controller import WebController
from handler.indigo.scraper import Scraper


class Indigo(object):
    def __init__(self):
        self.url = {
            "home": "https://www.goindigo.in/",
            "pnr_status": "https://www.goindigo.in/member/my-booking.html"
        }

    def get_pnr_status(self, parameters):
        web = WebController()
        web.open_page(url=self.url["pnr_status"])
        web.input_text(tag_type="id", name="booking-reference", value=parameters["booking_reference"])
        web.input_text(tag_type="id", name="email-lastname", value=parameters["email_lastname"])
        web.click_element(tag_type="id", name="mybooking-retrive-button")

        status = web.wait_till_load(tag_type="class", name="pass-det-blck")
        if status:
            html_source = web.get_attribute(tag_type="class", name="viewItinerary", attribute="innerHTML")
            web.exit_driver()
            scraper_controller = Scraper()
            response = scraper_controller.get_pnr_status(html_source)
            return response
        else:
            return False
