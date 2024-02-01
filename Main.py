number=input("Enter a valid phone number with country code: ")
import phonenumbers

from phonenumbers import geocoder, timezone, carrier

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_prov = carrier.name_for_number(pepnumber, "en")
print(service_prov)

time = timezone.time_zones_for_number(pepnumber)
print(time)
