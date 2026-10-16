
booking = {
    "price": 12000,
    "room_type": "Deluxe",
    "refundable": True,
}

supplier_rate = {
    "price": 9500,
    "room_type": "Deluxe",
    "refundable": True,
}


def compare_bookings(booking, supplier_rate):
    same_room = (
        booking["room_type"] == supplier_rate["room_type"]
    )

    same_cancellation = (
        booking["refundable"] == supplier_rate["refundable"]
    )

    cheaper = supplier_rate["price"] < booking["price"]

    if same_room and same_cancellation and cheaper:
        savings = booking["price"] - supplier_rate["price"]

        return {
            "qualified": True,
            "savings": savings,
        }

    return {
        "qualified": False,
        "savings": 0,
    }


result = compare_bookings(booking, supplier_rate)
print(result)
