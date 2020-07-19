from flight_status.handler import BeautifulSoup


class Scraper(object):
    def __init__(self):
        self.error_message = "Error: Not able to fetch details"

    def get_pnr_status(self, page_source):
        soup = BeautifulSoup(page_source, features="html.parser")
        try:
            ticket_status = soup.find(name="td", attrs={"class": "width-pnr-status"}).find("strong").text
        except Exception as err:
            ticket_status = self.error_message

        passengers = []
        try:
            for tr in soup.find("tbody", {"id": "passengerBody"}).find_all("tr", {"class": 'passenger-info-border'},
                                                                           recursive=False):
                if tr.find("td"):
                    passengers.append({
                        'Name': tr.find_all('td')[0].text.strip(),
                        'Pax Type': [each.strip() for each in tr.find_all('td')[1].text.replace("\n", "").split(",")],
                    })
        except Exception as err:
            passengers = []

        temp = {}
        try:
            for tr in soup.find("table", {"id": "flight-journey-detail"}).find("tbody").find_all('tr'):
                if tr.find("td"):
                    temp = {
                        'doj': tr.find_all('td')[0].text.strip(),
                        'Flight': tr.find_all('td')[1].text.strip(),
                        'From': tr.find_all('td')[2].text.strip(),
                        'To': tr.find_all('td')[3].text.strip(),
                        'Dept': tr.find_all('td')[4].text.strip(),
                        'Arr': tr.find_all('td')[5].text.strip(),
                        'Current': tr.find_all('td')[6].text.strip(),
                    }
        except Exception as err:
            temp = None
        try:
            flight_details = {
                "from_airport": temp["From"],
                "to_airport": temp["To"],
                "date_of_journey": temp["doj"],
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
