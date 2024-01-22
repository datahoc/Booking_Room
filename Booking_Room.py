class BookingRoom:
    def __init__(self):
        self.booking = []
    def addBooking(self, name, check_in, check_out):
        booking = { 'name': name, 'check_in': check_in, 'check_out': check_out}
        self.booking.append(booking)

request = BookingRoom()
request.addBooking(name= "Alex", check_in="2024-01-01 07:00", check_out="2024-01-02 08:00")
request.addBooking(name= "Marry", check_in="2024-01-01 08:00", check_out="2024-01-02 09:00")

for danhsach in request.booking:
    print(f"Name: {danhsach['name']}, Check-in: {danhsach['check_in']}, Check-out: {danhsach['check_out']}")