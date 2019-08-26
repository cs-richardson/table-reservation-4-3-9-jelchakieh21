"""
This code is used to tell you whether you are on a 
registry list for a restauraunt.
- This code was made by Julian
"""
guestName=input ("Name:")
reservation_name=["Julian","Justin"]
if guestName==reservation_name[0] or guestName==reservation_name[1]:
    print ("Right this way!")
else:
    print ("Sorry, we don't have a reservation under that name.")
