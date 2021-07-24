# import firebase_admin
from firebase_admin import credentials, messaging
import firebase_admin

cred = credentials.Certificate("D:\satrio\Python-SignLangDetection\serviceAccAstro.json")
firebase_admin.initialize_app(cred)

registration_token = 'cRfpYMsMSGSTB5bHpIF2C2:APA91bE6GipnV7bf_EQFTlE6iPl1LoqFucA_a29iUCbSvVZdjFz5RiqzEYHhdiK_PRaL2kIkdm8yhRtVZNRy1qiUk76nujvPUsPHoJfTiNeSMhhSHHtlZiM-T4xZHMMOhArhh9wgi7OB'

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'title': 'Astro',
        'body': 'test',
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
print(message)