from flight_status.handler import BeautifulSoup


class Scraper(object):
    def __init__(self):
        self.error_message = "Error: Not able to fetch details"


    def get_pnr_status(self, page_source):

        soup = BeautifulSoup(page_source, features="html.parser")

        try:
            dep_date_details = soup.find("div", {"class": "dates"})
            dep_date = dep_date_details.find("label", {"class": "date"}).text
        except Exception as err:
            dep_date = self.error_message

        try:
            flight_status = soup.find("div", {"class": "booking-status"}).text
        except Exception as err:
            flight_status = self.error_message

        stations = []
        try:
            flight_stations = soup.find("div", {"class": "flight-stations"})
            stations = flight_stations.find_all("label", {"class": "header"})

        except Exception as err:
            stations = None

        booking_details_label = []
        seat_details= []
        try:
            booking_details = soup.find_all("div", {"class": "booking-ssr-details"})
            for detail in booking_details:
                booking_details_label = detail.find_all("label")
                seat = booking_details_label[1].text.strip()
                seat_details.append(seat)
        except Exception as err:
            flight_summary = None


        passengers = []
        passenger_names = []

        try:
            passenger_details = soup.find_all("div", {"class": "passenger-name"})

            count=0
            for passenger in passenger_details:
                passenger_dict={"name":passenger.text,"seat": seat_details[count]}
                count=count+1
                passenger_names.append(passenger_dict)
        except Exception as err:
            passengers = []
            passenger_names=[]

        try:
            flight_details = {
                "from_airport": stations[0].text,
                "to_airport": stations[1].text,
                "date_of_journey": dep_date,
                "num_of_travellers": len(passenger_names)
            }
        except Exception as err:
            flight_details = self.error_message

        response = {
            "flight_details": flight_details,
            "passenger_details": passenger_names,
            "status": flight_status
        }

        return response
