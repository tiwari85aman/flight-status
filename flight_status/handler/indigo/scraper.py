from flight_status.handler import BeautifulSoup


class Scraper(object):
    def __init__(self):
        self.error_message = "Error: Not able to fetch details"

    def get_pnr_status(self, page_source):

        soup = BeautifulSoup(page_source, features="html.parser")
        summary = soup.find(name="div", attrs={"class": "conf-summary"})
        details = summary.find("div", {"class": "trip-summary-id"})

        try:
            ticket_status = soup.find("div", {"class": "cnf-summary-status"}).text
        except Exception as err:
            ticket_status = self.error_message

        destinations = []
        try:
            for item in details.find_all("p"):
                destinations.append(item.find("span").text)
        except Exception as err:
            destinations = None

        flight_summary = []
        try:
            for each in details.find("ul", {"class": "conf-flight-details"}).find_all("li"):
                flight_summary.append(each.text.strip())
        except Exception as err:
            flight_summary = None

        passengers = []
        try:
            passenger_table = soup.find("table", {"id": "view-itinerary-hbo"})
            for tr in passenger_table.find("tbody").find_all('tr'):
                passengers.append({
                    'Name': tr.find_all('td')[0].text.strip(),
                    'seat': tr.find_all('td')[1].text.strip()
                })
        except Exception as err:
            passengers = []

        try:
            flight_details = {
                "from_airport": destinations[0],
                "to_airport": destinations[1],
                "direction": flight_summary[0],
                "date_of_journey": flight_summary[1],
                "num_of_travellers": len(passengers)
            }
        except Exception as err:
            flight_details = self.error_message

        response = {
            "flight_details": flight_details,
            "passenger_details": passengers,
            "status": ticket_status
        }

        return response
