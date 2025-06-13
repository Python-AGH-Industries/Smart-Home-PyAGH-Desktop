from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import requests
from urllib.request import urlopen



class PublicSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.publicDataLayout = QVBoxLayout(self)
        self.publicDataLayout.setContentsMargins(10, 10, 10, 10)
        self.publicDataLayout.setSpacing(5)
        
        # Title
        label = QLabel("Weather", self)
        label.setObjectName("title")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.publicDataLayout.addWidget(label)

        self.send_weather_request()

    def send_weather_request(self):
        try:
            api_key = "b9e1a613f23a49eeb4a105025252305"
            city = "Cracow"
            aqi = "no"
            base_url = "http://api.weatherapi.com/v1/current.json"
            params = {
                "key": api_key,
                "q": city,
                "aqi": aqi
            }
            response = requests.get(base_url, params=params)


            if response.status_code == 200:
                # generate weather info
                print(response.json())
                self.json_data = response.json
                self.weather = response.json()["current"]["condition"]
                self.temp = response.json()["current"]["temp_c"]
                self.cloud = response.json()["current"]["cloud"]
                self.pressure = response.json()["current"]["pressure_mb"]
                self.humidity = response.json()["current"]["humidity"]
                self.wind = response.json()["current"]["wind_mph"]

                weather_layout = QHBoxLayout()
                weather_layout.setSpacing(10)
                weather_layout.setContentsMargins(0, 0, 0, 0)

                self.temp_label = QLabel(self.weather["text"], self)
                self.temp_label.setObjectName("weatherCondition")
                self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                weather_layout.addWidget(self.temp_label)

                icon_url = "https:" + self.weather["icon"]
                image_data = urlopen(icon_url).read()
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)

                self.icon_label = QLabel(self)
                self.icon_label.setObjectName("weatherIcon")
                self.icon_label.setPixmap(pixmap.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                weather_layout.addWidget(self.icon_label)

                self.publicDataLayout.addLayout(weather_layout)
                self.cloud_label = QLabel("Temperature: "+str(self.temp), self)
                self.cloud_label.setObjectName("weatherInfo")
                self.cloud_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.publicDataLayout.addWidget(self.cloud_label)

                self.cloud_label = QLabel("Clouds: "+str(self.cloud)+"%", self)
                self.cloud_label.setObjectName("weatherInfo")
                self.cloud_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.publicDataLayout.addWidget(self.cloud_label)

                self.pressure_label = QLabel("Pressure: "+str(self.pressure), self)
                self.pressure_label.setObjectName("weatherInfo")
                self.pressure_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.publicDataLayout.addWidget(self.pressure_label)

                self.humidity_label = QLabel("Humidity: "+str(self.humidity), self)
                self.humidity_label.setObjectName("weatherInfo")
                self.humidity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.publicDataLayout.addWidget(self.humidity_label)

                self.wind_label = QLabel("Wind speed: "+str(self.wind), self)
                self.wind_label.setObjectName("weatherInfo")
                self.wind_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.publicDataLayout.addWidget(self.wind_label)
        except:
            pass
        else:
            print(f"Request failed with status code {response.status_code}")
