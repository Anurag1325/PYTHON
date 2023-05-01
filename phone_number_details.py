import phonenumbers
from phonenumbers import timezone,geocoder,carrier
country_code=input(str("enter your country code:"))
number=input(str("enter your number:"))
new_number=country_code+number
phone=phonenumbers.parse(new_number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print("your phone number: "+new_number)
print("time zone: "+str(time))
print("carrier: "+carr)
print("registration: "+reg)



