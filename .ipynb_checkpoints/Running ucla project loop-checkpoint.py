import json
import pandas as pd
import requests
import requests
import time
import datetime as dt
import geopandas as gpd
from datetime import datetime

apiKey = "6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9"

# make blank dataframes
df_scooter_data = pd.DataFrame()
df_Stop_data_1 = pd.DataFrame()
df_Stop_data_2 = pd.DataFrame()
current = datetime.now()

date = dt.date.today()
scooter_file_name = f"Scooters {date}".format(date)
Stop_1_file_name = f"Stop 1 {date}".format(date)
Stop_2_file_name = f"Stop 2 {date}".format(date)

while current.hour <= 21 and current.hour >= 7:  # set hours of code looping, make sure the second value is less than the second value on the following if line
        current = datetime.now()
        print('getting ready to start')
        time.sleep(30)

        if current.hour <= 21 and current.hour >= 9:  # set hours of code looping

                Endpoint = f"https://external.transitapp.com/v3/map_layers/placemarks?lat=34.07236868760976&lon=-118.44423503764042&distance=1000&apiKey=6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9"

                headers = {'apiKey': '6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9'}

                response = requests.get(Endpoint, headers=headers)

                placemarks = response.json()["placemarks"]

                endpoint = "https://external.transitapp.com/v3/public/stop_departures?global_stop_id=BBB:5549&apiKey=6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9"

                # Set the headers for the API request
                headers = {'apiKey': '6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9'}

                # Send the API request
                response = requests.get(endpoint, headers=headers)
                # Check if the request was successful
                if response.status_code == 200:
                    # Parse the JSON response
                    departures1 = response.json()["route_departures"]
                    # Print the list of departures
                    #print(departures1)
                else:
                    print("Error:", response.status_code)

                endpoint = "https://external.transitapp.com/v3/public/stop_departures?global_stop_id=MLA:108905&apiKey=6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9"

                # Set the headers for the API request
                headers = {'apiKey': '6bb0ee84e4c5940b3c0dcd4e5c56247fc4907265dc5d5d37cbe74c6ab82952f9'}

                # Send the API request
                response = requests.get(endpoint, headers=headers)
                # Check if the request was successful
                if response.status_code == 200:
                    # Parse the JSON response
                    departures2 = response.json()["route_departures"]
                    # Print the list of departures
                    #print(departures2)
                else:
                    print("Error:", response.status_code)

                df_scooter_data_new = pd.DataFrame(
                    placemarks)  # replace with code for dataframe containing all the information on the
                df_Stop_data_1_new = pd.DataFrame(
                    departures1)
                df_Stop_data_2_new = pd.DataFrame(
                    departures2)

                df_scooter_data_new['time'] = current
                df_Stop_data_1_new['time'] = current
                df_Stop_data_2_new['time'] = current

                df_scooter_data = df_scooter_data.append(df_scooter_data_new)
                df_Stop_data_1 = df_Stop_data_1.append(df_Stop_data_1_new)
                df_Stop_data_2 = df_Stop_data_2.append(df_Stop_data_2_new)

                print(df_scooter_data)
                print(df_Stop_data_1)



                df_scooter_data.to_csv(f"Data/{scooter_file_name}.csv")
                df_Stop_data_1.to_csv(f"Data/{Stop_1_file_name}.csv")
                df_Stop_data_2.to_csv(f"Data/{Stop_2_file_name}.csv")

                time.sleep(600)  # set time to repeat in seconds
        else:
            print('The loop is now done')

