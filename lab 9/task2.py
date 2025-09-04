class SRUStudent:
    # Constructor to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                  # Student's name
        self.roll_no = roll_no            # Student's roll number
        self.hostel_status = hostel_status  # Hostel status: 'Hosteler' or 'Day Scholar'
        self.fee_paid = False             # Default: fee not paid

    # Method to update the student's fee status
    def fee_update(self, status):
        self.fee_paid = status            # Set fee_paid to True or False based on status

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")                       # Print student name
        print(f"Roll No: {self.roll_no}")                 # Print roll number
        print(f"Hostel Status: {self.hostel_status}")     # Print hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Print fee payment status


# ✅ Create an object of SRUStudent
student1 = SRUStudent("ramu", "SRU1234", "Hosteler")

# ✅ Update fee status to True (paid)
student1.fee_update(True)

# ✅ Display student details
student1.display_details()
