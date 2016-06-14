#Download the twilio python library
from twilio.rest import TwilioRestClient

account_sid = 'AC3c6b071fc84ace9f10e405405d36a237'
auth_token = '4c19d9255be4f793e1ad8422a5dd3d53'

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17203751359", from_="+16172022866", body="sup")
