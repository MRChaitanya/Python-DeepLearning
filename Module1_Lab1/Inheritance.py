class Person():
    def __init__(self, name, email, phone, age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age

    def getname(self):
        print(" Name:", self.name)

    def getage(self):
        print("Age:", self.age)

    def getnumber(self):
        print("Phoneno: " + self.phone)

    def getemail(self):
        print("Email:", self.email)


class FlightInfo():
    def __init__(self, flight_number, flight_name, seat_number):
        self.flightnumber = flight_number
        self.flightname = flight_name
        self.seatnumber = seat_number

    def getflightname(self):
        print("Airlines:", self.flightname)

    def getflightnumber(self):
        print("FlightNo:", self.flightnumber)

    def getseatnumber(self):
        print("SeatNo:", self.seatnumber)



class Booking(FlightInfo):

    def __init__(self, source, destination, deptdate,flight_number,flight_name,seat_number,seat_place):
        FlightInfo.__init__(self, flight_number, flight_name, seat_number)
        self.source = source
        self.destination = destination
        self.deptdate = deptdate
        self.flightname = flight_name
        self.flightnumber = flight_number
        self.seatnumber = seat_number
        self.seatplace = seat_place

    def getsource(self):
        print("Source :", self.source)

    def getdestination(self):
        print("Destination :", self.destination)

    def getdeptdate(self):
        print("Departure Date:", self.deptdate)

    def getseatnumber(self):
        print("Seat number:", self.seatnumber)
        print("seat Place", self.seatplace)


class Passenger(Person,Booking):

    def __init__(self, name, email, phone, age, flight_number,
                 flight_name, seat_number, deptdate, source, destination,seatplace):

        super().__init__(name, email, phone, age)

        Booking.__init__(self, deptdate, source, destination, flight_number, flight_name, seat_number, seatplace)
     
        FlightInfo.__init__(self, flight_number, flight_name, seat_number)


p = Passenger("Chaitanya", "chaitanya@gmail.com","8166063644", 24, "SPD100", "AirIndia","18", "USA", "India", "10thMarch", "C")
print(" ____________________")
print("|  Passenger Details:")
print(" _____________________")
p.getname()
p.getemail()
p.getage()
p.getnumber()
print(" _________________")
print("  Flight Details ")
print(" __________________")

p.getflightname()
p.getflightnumber()
p.getseatnumber()
print(" ___________________")
print("|  Booking Details:|")
print(" ____________________")
p.getsource()
p.getdestination()
p.getdeptdate()
print("_____________________")
print("")

f = FlightInfo("Air India", "SPD100", 18)
f.getseatnumber()