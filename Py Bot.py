
import requests
from datetime import datetime


class ScoreGet:
    def __init__(self):
        self.url_get_all_Matches = "https://cricapi.com/api/matches"
        self.get_Score = "https://cricapi.com/api/cricketScore"
        self.apikey = "Your api key here"
        self.unique_id = ""

    def get_unique_id(self):
        url_params = {"apikey": self.apikey}
        response = requests.get(self.url_get_all_Matches, params=url_params)
        response_dict = response.json()
        uid_found = -1

        for i in response_dict["matches"]:
            if (i["team-2"] == "Baroda" or i["team-1"] == "India" and i["matchStarted"]):
                todays_date = datetime.today().strftime("%Y-%m-%d")
                todays_date = "2019-01-28"
                if todays_date == "2019-01-28":
                    self.unique_id = i["unique_id"]
                    uid_found = 1
                    break
        if not uid_found:
            self.unique_id = -1

        send_data = self.get_score_current(self.unique_id)
        print(send_data)

    def get_score_current(self, unique_id):
        data = ""
        if unique_id == -1:
            data = "No match today"
        else:
            uri_params = {"apikey": self.apikey, "unique_id": unique_id}
            response = requests.get(self.get_Score, params=uri_params)
            data_json = response.json()
            try:
                data = "Here's the score : \n" + \
                    data_json["stat"] + "\n" + data_json["score"]
            except KeyError as e:
                print(e)
        return data


if __name__ == "__main__":
    o1 = ScoreGet()
    o1.get_unique_id()
