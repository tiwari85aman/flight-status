from handler import BeautifulSoup


class Scraper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_pnr_status(page_source):

        soup = BeautifulSoup(page_source, features="html.parser")
        summary = soup.find(name="div", attrs={"class": "conf-summary"})
        details = summary.find("div", {"class": "trip-summary-id"})

        ticket_status = soup.find("div", {"class": "cnf-summary-status"})

        destinations = []
        for item in details.find_all("p"):
            destinations.append(item.find("span").text)

        flight_details = []
        for each in details.find("ul", {"class": "conf-flight-details"}).find_all("li"):
            flight_details.append(each.text.strip())

        passengers = []
        passenger_table = soup.find("table", {"id": "view-itinerary-hbo"})
        for tr in passenger_table.find("tbody").find_all('tr'):
            passengers.append({
                'Name': tr.find_all('td')[0].text.strip(),
                'seat': tr.find_all('td')[1].text.strip()
            })
        response = {
            "flight_details": {
                "from_airport": destinations[0],
                "to_airport": destinations[1],
                "direction": flight_details[0],
                "date_of_journey": flight_details[1],
                "num_of_travellers": flight_details[2]
            },
            "passenger_details": passengers,
            "status": ticket_status.text
        }

        return response
