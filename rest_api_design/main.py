"""
Airline Booking, API documents:
API search flights
API book a flight
API get history of booking

"""

"""
API search flights

params:
flight_type (str):
- one_way
- round_trip
departure (str)
destination(str)
passenger: Passenger schema
discount_code (Optional[str])
find_cheapest_ticket (Optional[bool])

"""

"""
Response:
{
    flight_id (str)
    flight_duration (str)
    flight_classes (str)
    ticket_price (str)
    availability:
}
"""

data = {
    "data": {
        "departure": "da_nang",
        "destination": "ho_chi_minh",
        "departure_date": "01-01-2024",
        "content": [
            {
                "flight_id": "VJ634",
                "departure_time": "7:30",
                "arrival_time": "9: 30",
                "flight_classes": "economy",
                "ticket_price": 1200000,
                "availability": "full"
            }
        ]
    }
}

"""
{
    "departure" (str)
    "destination" (str)
    "departure_time"
    "arrival_time"
    "ticket_price"
    "payment_status"
    "ticket_price"
    "passenger_info": [{
        "last_name"
        "first_name"
        "email"
        "phone"
        "birthday"
        "nation"
        "meta": {}
    }]
}

"""

data = {
    "flights": [
        {
            "flights_id": "vbz64",
            "type": "outbound",
        },
        {
            "flights_id": "vbz64",
            "type": "inbound",
        }
    ],
    "passenger": [{
        "last_name": "pham",
        "first_name": "tam",
        "email": "tam@gmail.com",
        "phone": "012312312",
        "birthday": "01-01-2024",
        "nation": "Viet Nam",
        "meta": {}
    }],

}

response = {
    "booking_id": "bk123",
    "flights": [
        {
            "flights_id": "vbz64",
            "type": "outbound",
            "departure": "da_nang",
            "destination": "ho_chi_minh",
            "departure_time": "2024-10-02T10:00:00",
            "arrival_time": "2024-10-02T13:00:00",
        },
        {
            "flights_id": "vbz64",
            "type": "inbound",
            "departure": "ho_chi_minh",
            "destination": "da_nang",
            "departure_time": "2024-10-03T10:00:00",
            "arrival_time": "2024-10-04T13:00:00",
        }
    ],
    "passengers": [{
        "last_name": "pham",
        "first_name": "tam",
        "seat_id": "k10",
    }],

    "payment": {
        "status": "completed",
        "total_price": 3000000,
        "discount": 0.0,
    }

}


"""
    user_id: "xbvamksdk"

"""


data = {
    "flights": [
        {
            "booking_id": "bk123",
            "booking_date": "01-01-2024",
            "trip_type": "roundtrip",
            "departure": "da_nang",
            "destination": "ho_chi_minh",
            "departure_time": "2024-10-02T10:00:00",
            "arrival_time": "2024-10-02T13:00:00",
            "number_of_passengers": 1,
            "payment": {
                "status": "completed",
                "total_price": 3000000,
            }
        }
    ]
}
