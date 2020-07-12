from web_controller import WebController
from handler.indigo.scraper import Scraper


class Indigo(object):
    def __init__(self):
        self.url = {
            "home": "https://www.goindigo.in/",
            "pnr_status": "https://www.goindigo.in/member/my-booking.html"
        }

    def get_pnr_status(self, booking_reference, email_lastname):
        x = WebController()
        x.open_page(url="https://www.goindigo.in/member/my-booking.html")
        x.input_text(tag_type="id", name="booking-reference", value=booking_reference)
        x.input_text(tag_type="id", name="email-lastname", value=email_lastname)
        x.click_element(tag_type="id", name="mybooking-retrive-button")

        status = x.wait_till_load(tag_type="class", name="pass-det-blck")
        if status:
            html_source = x.get_attribute(tag_type="class", name="viewItinerary", attribute="innerHTML")
            scraper = Scraper()
            response = scraper.get_pnr_status(html_source)
            return response
        else:
            return False
