from pathlib import Path
import shutil
import os

from businessLogic.hotelManager import HotelManager

working_db = Path("./database/working.db")

os.environ["DB_FILE"] = str(working_db)

hm = HotelManager()

hotels = hm.search_hotels("Luzern")
for hotel in hotels:
    print(hotel.name)


city = "Zürich"
street = "Belllariastr. 12"
zip = "8002"

hotel_name = "Bären"
stars = 1
