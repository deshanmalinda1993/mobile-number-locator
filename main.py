import (self, *args, **kwargs):
    return super().(*args, **kwargs)


from +94758658826 import carrier, geocoder, timezone

mobileNo=input("+94759736359:") 
mobileNo=phonenumbers.parse(+94758658826)

print("Is number valid:",phonenumbers.is_valid_number(mobileNo))
print("Time Zone:", timezone.time_zones_for_number(+9459796359))
print("Carrier Name:",carrier.name_for_number(+94759736359,"en"))
print("Location:",geocoder.description_for_number(+94759736359,"en"))