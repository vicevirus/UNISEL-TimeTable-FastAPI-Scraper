import os
import requests
import ujson as json
import time

#Verify false, only for local environment, turning off warning
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Function to get the latest semester code for a given campus
def get_latest_semester_code(campus):
    url = "https://127.0.0.1:8000/latest_semester_codes"
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        raise Exception("Failed to get latest semester code")
    latest_semester_codes = response.json()
    latest_semester_code = latest_semester_codes[campus][0]
    return latest_semester_code

# Function to update timetable for the latest semester code for a given campus
def update_timetable(campus, semester_code):
    url = f"https://127.0.0.1:8000/timetable_data/{campus}/{semester_code}"
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        raise Exception("Failed to update timetable")
    timetable_data = response.json()
    with open(f"/root/UNISEL-TimeTable-REST-Scraper/timetable_data_{semester_code}_{campus}.json", "w") as f:
        json.dump(timetable_data, f)
    print(f"Timetable updated for semester code {semester_code} ({campus})")

# Main function
def main():
    campuses = ["SA", "BJ", "F"]
    for campus in campuses:
        semester_code = get_latest_semester_code(campus)
        update_timetable(campus, semester_code)

if __name__ == "__main__":
    main()