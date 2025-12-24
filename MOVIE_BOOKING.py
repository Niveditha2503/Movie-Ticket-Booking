class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.show_list = []
        self.seats = {}  

    def add_show(self, show_id, movie_name, time):
        self.show_list.append((show_id, movie_name, time))
        seat_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_matrix

    def view_shows(self):
        print("\n Today's Shows ")
        for show in self.show_list:
            print(f"Show ID: {show[0]} | Movie: {show[1]} | Time: {show[2]}")
        print("\n")

    def view_seats(self, show_id):
        if show_id not in self.seats:
            print("Invalid Show ID!")
            return
        print("\nSeat Layout (0 = Available, 1 = Booked):")
        for row in self.seats[show_id]:
            print(" ".join(str(seat) for seat in row))
        print()

    def book_ticket(self, show_id, seats_to_book):
        if show_id not in self.seats:
            print("Invalid Show ID!")
            return

        for seat in seats_to_book:
            row, col = seat
            if row >= self.rows or col >= self.cols:
                print(f"Seat {seat} is out of range!")
                continue
            if self.seats[show_id][row][col] == 0:
                self.seats[show_id][row][col] = 1
                print(f"Seat {seat} booked successfully!")
            else:
                print(f"Seat {seat} already booked!")

class Cinema:
    def __init__(self):
        self.halls = []

    def add_hall(self, hall):
        self.halls.append(hall)

cinema = Cinema()
hall1 = Hall(5, 5, 1)
cinema.add_hall(hall1)

hall1.add_show(111, "OG", "10:00 AM")
hall1.add_show(222, "Kantara (Chapter 1)", "2:00 PM")
hall1.add_show(333, "Mirai", "6:00 PM")

def main():
    while True:
        print("\n1. View All Shows")
        print("2. View Available Seats")
        print("3. Book Ticket")
        print("4. Exit")
        choice = input("Enter option: ")
        if choice == "1":
            hall1.view_shows()
        elif choice == "2":
            show_id = int(input("Enter Show ID: "))
            hall1.view_seats(show_id)
        elif choice == "3":
            show_id = int(input("Enter Show ID: "))
            n = int(input("How many seats you want to book? "))
            seats = []
            for i in range(n):
                row = int(input(f"Seat {i+1} - Enter Row: "))
                col = int(input(f"Seat {i+1} - Enter Column: "))
                seats.append((row, col))
            hall1.book_ticket(show_id, seats)
        elif choice == "4":
            print("Thank you for visiting! ")
            break
        else:
            print("Invalid option! Try again.")

main()
