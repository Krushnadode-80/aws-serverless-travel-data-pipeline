from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

routes = [
("Pune","Mumbai","3h 15m","4.5/5","AC Seater"),
("Mumbai","Pune","3h 30m","4.2/5","Volvo AC"),
("Kolhapur","Pune","4h 45m","4.0/5","AC Sleeper"),
("SambhajiNagar","Nashik","4h 15m","3.8/5","Non-AC"),
("Nashik","Pune","5h 00m","4.3/5","AC Sleeper"),
("Solapur","Mumbai","8h 30m","4.1/5","Luxury AC"),
("Nagpur","Mumbai","14h 00m","4.4/5","Multi-Axle"),
("Dhule","Mumbai","7h 45m","3.9/5","Non-AC")
]

@app.route("/traveldata")
def travel():

    data=[]

    for d in range(60):

        date=datetime.now()-timedelta(days=d)

        for r in routes:

            lowest=random.randint(1500,3000)
            highest=lowest+random.randint(300,600)

            row={
                "Source":r[0],
                "Destination":r[1],
                "Date":date.strftime("%d-%m-%Y"),
                "Time":date.strftime("%I:%M %p"),
                "Contact_Number":"+91 9000000000",
                "Duration":r[2],
                "Rating":r[3],
                "Seat_Type":r[4],
                "Status":"Available",
                "Lowest":lowest,
                "Highest":highest,
                "Average":int((lowest+highest)/2)
            }

            data.append(row)

    return jsonify(data)

if __name__ == "__main__":
    app.run()