# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 


# String which represents the QR code 
s = "https://smartpracticeschool.github.io/SBSPS-Challenge-1399-Sentiment-Analysis-of-COVID-19-Tweets-Visualization-Dashboard/"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("output/myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('output/myqr.png', scale = 6) 
