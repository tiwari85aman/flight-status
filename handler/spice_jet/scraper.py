from handler import BeautifulSoup


class Scraper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_pnr_status(page_source):
        soup = BeautifulSoup(page_source, features="html.parser")
        ticket_status = soup.find(name="td", attrs={"class": "width-pnr-status"}).find("strong")

        flight_details = soup.find("table", {"id": "flight-journey-detail"})
        temp = []
        for tr in flight_details.find("tbody").find_all('tr'):
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

        passengers = []
        for tr in soup.find("tbody", {"id": "passengerBody"}).find_all("tr", {"class": 'passenger-info-border'},
                                                                       recursive=False):
            if tr.find("td"):
                passengers.append({
                    'Name': tr.find_all('td')[0].text.strip(),
                    'Pax Type': [each.strip() for each in tr.find_all('td')[1].text.replace("\n", "").split(",")],
                })

        response = {
            "flight_details": {
                "from_airport": temp["From"],
                "to_airport": temp["To"],
                "date_of_journey": temp["doj"],
                "num_of_travellers": len(passengers)
            },
            "passenger_details": passengers,
            "status": ticket_status.text
        }

        return response
