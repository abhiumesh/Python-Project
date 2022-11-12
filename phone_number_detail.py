import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter the Number:- ")

phoneNumber = phonenumbers.parse(number)    # String to phonenumber format
timeZone = timezone.time_zones_for_number(phoneNumber)  # Get Timezone

Carrier = carrier.name_for_number(phoneNumber, 'en')    # Carrier and Region of a Phone Number
Region = geocoder.description_for_number(phoneNumber, 'en')    

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)