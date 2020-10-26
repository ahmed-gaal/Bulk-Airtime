from __future__ import print_function
import os
import flask
from flask import Flask, request, render_template
import africastalking

app = Flask(__name__)
username = os.environ.get('NAME')
api_key = os.environ.get('KEY')

africastalking.initialize(username, api_key)
airtime = africastalking.Airtime



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        airtime_amount = request.form["airtimeAmount"]
        phone_number = request.form["phoneNumber"]
        country_code = "KES"
        
        recipients = [{
			"phoneNumber": phone_number,
			"amount": airtime_amount,
			"currency_code": "KES"  
		}]
        
        response = airtime.send(recipients = recipients)
        print(response)
    
    return render_template('index.html')

class AIRTIME:
    def __init__(self):
		# Set your app credentials
        self.username = username
        self.api_key = api_key

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the airtime service
        self.airtime = africastalking.Airtime

    def send(self):
        # Set phone_number in international format
        phone_number = 'MyPhoneNumber'

        # Set The 3-Letter ISO currency code and the amount
        amount = "908"
        currency_code = "KES"

        try:
			# That's it hit send and we'll take care of the rest
            responses = self.airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
            print (responses)
        except Exception as e:
            print ("Encountered an error while sending airtime:%s" %str(e))

if __name__ == '__main__':
    AIRTIME().send()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 3030, debug=True)