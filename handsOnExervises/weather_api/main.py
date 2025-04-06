import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.city_label = QLabel('Enter city name:',self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temperature_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Weather App')

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.humidity_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.humidity_label.setObjectName('humidity_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')
        
        self.setStyleSheet("""
            #city_label { font-size: 20px; }
            #city_input { font-size: 40px; font-style: italic; }
            #get_weather_button { font-size: 20px; background-color: lightblue; }
            #temperature_label { font-size: 50px; }
            #humidity_label { font-size: 50px; }
            #emoji_label { font-size: 40px; font-family: Segoe UI emoji; }
            #description_label { font-size: 40px; }
        """) 
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "454064ed567f4c727eee67bbd83c7811"
        city_name = self.city_input.text()
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
        try:
            response = requests.get(complete_url)
            data = response.json()
            if data['cod'] == 200:
                self.display_weather(data)
            else:
                self.display_error("City not found")
        except requests.exceptions.HTTPError as e:
            self.display_error(e.response.text)
        except requests.exceptions.RequestException as e:
            self.display_error("Network error: " + str(e))


    def display_error(self,message):
        self.temperature_label.setText("")
        self.humidity_label.setText("")
        self.emoji_label.setText("")
        self.description_label.setText(message)

    def get_emoji(self, weather_description):
        weather_emojis = {
            'clear sky': '☀️',
            'few clouds': '🌤️',
            'scattered clouds': '🌥️',
            'broken clouds': '☁️',
            'shower rain': '🌧️',
            'rain': '🌧️',
            'thunderstorm': '⛈️',
            'snow': '❄️',
            'mist': '🌫️',
            'overcast clouds': '☁️',
            'light rain': '🌦️',
        }
        return weather_emojis.get(weather_description, '')

    def display_weather(self, data):
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            emoji = self.get_emoji(weather_description)
            
            self.temperature_label.setText(f'Temperature: {temperature}°C')
            self.humidity_label.setText(f'Humidity: {humidity}%')
            self.emoji_label.setText(emoji)
            self.description_label.setText(weather_description.capitalize())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
