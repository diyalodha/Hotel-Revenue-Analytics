import csv
import random
from datetime import datetime, timedelta

# ------------------ CONFIGURATIONS ------------------
num_customers = 2000     # Change between 2000–5000 as per your need
num_bookings = num_customers * 2   # Example: if 2000 customers → 4000 bookings

# ------------------ STATIC DATA ------------------
room_types = [
    {"RoomTypeID": "RT1", "RoomType": "Single", "Price": 2500, "MaxOccupancy": 1, "Amenities": "WiFi,TV", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT2", "RoomType": "Double", "Price": 4000, "MaxOccupancy": 2, "Amenities": "WiFi,TV,MiniBar", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT3", "RoomType": "Suite", "Price": 7000, "MaxOccupancy": 4, "Amenities": "WiFi,TV,MiniBar,Jacuzzi", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT4", "RoomType": "Deluxe", "Price": 5500, "MaxOccupancy": 3, "Amenities": "WiFi,TV,Balcony", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT5", "RoomType": "Executive", "Price": 6000, "MaxOccupancy": 2, "Amenities": "WiFi,TV,MiniBar,LoungeAccess", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT6", "RoomType": "Family Suite", "Price": 8000, "MaxOccupancy": 5, "Amenities": "WiFi,TV,MiniBar,Kitchenette", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT7", "RoomType": "Luxury Villa", "Price": 12000, "MaxOccupancy": 6, "Amenities": "WiFi,PrivatePool,TV,Jacuzzi", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT8", "RoomType": "Economy", "Price": 1800, "MaxOccupancy": 1, "Amenities": "WiFi", "IsAC": False, "IsSeaFacing": False},
    {"RoomTypeID": "RT9", "RoomType": "Studio", "Price": 3500, "MaxOccupancy": 2, "Amenities": "WiFi,Kitchenette", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT10", "RoomType": "Dormitory", "Price": 1200, "MaxOccupancy": 6, "Amenities": "WiFi,SharedBathroom", "IsAC": False, "IsSeaFacing": False},
    {"RoomTypeID": "RT11", "RoomType": "Penthouse", "Price": 15000, "MaxOccupancy": 4, "Amenities": "WiFi,Jacuzzi,MiniBar,Balcony", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT12", "RoomType": "Cottage", "Price": 5000, "MaxOccupancy": 3, "Amenities": "WiFi,Fireplace", "IsAC": False, "IsSeaFacing": False},
    {"RoomTypeID": "RT13", "RoomType": "Garden View", "Price": 4800, "MaxOccupancy": 2, "Amenities": "WiFi,TV,Balcony", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT14", "RoomType": "Mountain View", "Price": 5300, "MaxOccupancy": 2, "Amenities": "WiFi,TV,Balcony", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT15", "RoomType": "Sea View Deluxe", "Price": 6500, "MaxOccupancy": 2, "Amenities": "WiFi,TV,Balcony,MiniBar", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT16", "RoomType": "Honeymoon Suite", "Price": 9000, "MaxOccupancy": 2, "Amenities": "WiFi,Jacuzzi,Balcony", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT17", "RoomType": "Presidential Suite", "Price": 20000, "MaxOccupancy": 6, "Amenities": "WiFi,Jacuzzi,PrivateButler", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT18", "RoomType": "Business Room", "Price": 6000, "MaxOccupancy": 2, "Amenities": "WiFi,Desk,MiniBar", "IsAC": True, "IsSeaFacing": False},
    {"RoomTypeID": "RT19", "RoomType": "Cabana", "Price": 7500, "MaxOccupancy": 3, "Amenities": "WiFi,TV,PrivatePool", "IsAC": True, "IsSeaFacing": True},
    {"RoomTypeID": "RT20", "RoomType": "Royal Villa", "Price": 25000, "MaxOccupancy": 8, "Amenities": "WiFi,PrivatePool,Jacuzzi,MiniBar,Kitchen", "IsAC": True, "IsSeaFacing": True}
]


branches = [
    {"BranchID": "B1", "BranchName": "HotelRev Theni", "City": "Theni", "State": "Tamil Nadu", "ManagerName": "Mr. Rajan", "Phone": "9876543210", "StarRating": 4, "RoomCount": 40, "RevenueScore": 78.5, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B2", "BranchName": "HotelRev Coimbatore", "City": "Coimbatore", "State": "Tamil Nadu", "ManagerName": "Ms. Priya", "Phone": "9988776655", "StarRating": 5, "RoomCount": 60, "RevenueScore": 85.2, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B3", "BranchName": "HotelRev Chennai", "City": "Chennai", "State": "Tamil Nadu", "ManagerName": "Mr. Santhosh", "Phone": "9090909090", "StarRating": 5, "RoomCount": 80, "RevenueScore": 92.3, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B4", "BranchName": "HotelRev Madurai", "City": "Madurai", "State": "Tamil Nadu", "ManagerName": "Ms. Keerthi", "Phone": "9812312312", "StarRating": 4, "RoomCount": 45, "RevenueScore": 75.6, "HasPool": False, "HasConferenceRoom": True},
    {"BranchID": "B5", "BranchName": "HotelRev Hyderabad", "City": "Hyderabad", "State": "Telangana", "ManagerName": "Mr. Aravind", "Phone": "9123456789", "StarRating": 5, "RoomCount": 90, "RevenueScore": 89.4, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B6", "BranchName": "HotelRev Mumbai", "City": "Mumbai", "State": "Maharashtra", "ManagerName": "Mr. Ajay", "Phone": "9001122334", "StarRating": 5, "RoomCount": 100, "RevenueScore": 94.8, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B7", "BranchName": "HotelRev Pune", "City": "Pune", "State": "Maharashtra", "ManagerName": "Ms. Rina", "Phone": "9022334455", "StarRating": 4, "RoomCount": 60, "RevenueScore": 82.7, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B8", "BranchName": "HotelRev Kochi", "City": "Kochi", "State": "Kerala", "ManagerName": "Mr. Ravi", "Phone": "9876501234", "StarRating": 5, "RoomCount": 70, "RevenueScore": 90.1, "HasPool": True, "HasConferenceRoom": False},
    {"BranchID": "B9", "BranchName": "HotelRev Bengaluru", "City": "Bengaluru", "State": "Karnataka", "ManagerName": "Mr. Manoj", "Phone": "9812345678", "StarRating": 5, "RoomCount": 95, "RevenueScore": 91.5, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B10", "BranchName": "HotelRev Mysore", "City": "Mysore", "State": "Karnataka", "ManagerName": "Ms. Nisha", "Phone": "9765432190", "StarRating": 4, "RoomCount": 50, "RevenueScore": 79.8, "HasPool": True, "HasConferenceRoom": False},
    {"BranchID": "B11", "BranchName": "HotelRev Goa", "City": "Goa", "State": "Goa", "ManagerName": "Mr. Arjun", "Phone": "9888776655", "StarRating": 5, "RoomCount": 80, "RevenueScore": 95.0, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B12", "BranchName": "HotelRev Delhi", "City": "Delhi", "State": "Delhi", "ManagerName": "Ms. Radhika", "Phone": "9898989898", "StarRating": 5, "RoomCount": 110, "RevenueScore": 93.4, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B13", "BranchName": "HotelRev Gurgaon", "City": "Gurgaon", "State": "Haryana", "ManagerName": "Mr. Rohit", "Phone": "9777665544", "StarRating": 4, "RoomCount": 75, "RevenueScore": 87.1, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B14", "BranchName": "HotelRev Noida", "City": "Noida", "State": "Uttar Pradesh", "ManagerName": "Ms. Sneha", "Phone": "9123344556", "StarRating": 4, "RoomCount": 70, "RevenueScore": 85.6, "HasPool": False, "HasConferenceRoom": True},
    {"BranchID": "B15", "BranchName": "HotelRev Jaipur", "City": "Jaipur", "State": "Rajasthan", "ManagerName": "Mr. Deepak", "Phone": "9988774411", "StarRating": 5, "RoomCount": 80, "RevenueScore": 88.9, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B16", "BranchName": "HotelRev Kolkata", "City": "Kolkata", "State": "West Bengal", "ManagerName": "Mr. Rajesh", "Phone": "9678341250", "StarRating": 4, "RoomCount": 60, "RevenueScore": 82.4, "HasPool": True, "HasConferenceRoom": False},
    {"BranchID": "B17", "BranchName": "HotelRev Ahmedabad", "City": "Ahmedabad", "State": "Gujarat", "ManagerName": "Ms. Pooja", "Phone": "9767895432", "StarRating": 4, "RoomCount": 55, "RevenueScore": 80.1, "HasPool": False, "HasConferenceRoom": True},
    {"BranchID": "B18", "BranchName": "HotelRev Chandigarh", "City": "Chandigarh", "State": "Punjab", "ManagerName": "Mr. Varun", "Phone": "9123456700", "StarRating": 5, "RoomCount": 75, "RevenueScore": 86.7, "HasPool": True, "HasConferenceRoom": True},
    {"BranchID": "B19", "BranchName": "HotelRev Bhopal", "City": "Bhopal", "State": "Madhya Pradesh", "ManagerName": "Ms. Kavita", "Phone": "9797979797", "StarRating": 4, "RoomCount": 50, "RevenueScore": 79.2, "HasPool": False, "HasConferenceRoom": True},
    {"BranchID": "B20", "BranchName": "HotelRev Lucknow", "City": "Lucknow", "State": "Uttar Pradesh", "ManagerName": "Mr. Suresh", "Phone": "9876543100", "StarRating": 5, "RoomCount": 90, "RevenueScore": 88.3, "HasPool": True, "HasConferenceRoom": True}
]


customer_names = [
    "Aarav Sharma", "Kavya Mehta", "Rohan Kapoor", "Simran Singh", "Ishaan Verma",
    "Tanya Bhatia", "Aditya Malhotra", "Neha Chauhan", "Rajat Sethi", "Sanya Gupta",
    "Karan Patel", "Ananya Iyer", "Vikram Joshi", "Priya Deshmukh", "Rahul Nair"
]

# ------------------ ATTRIBUTES ------------------
nationalities = ['Indian']
loyalty_tiers = ['Bronze', 'Silver', 'Gold', 'Platinum']
age_groups = ['18-25', '26-35', '36-50', '51+']
genders = ['Male', 'Female', 'Other']
booking_statuses = ['Cancelled', 'Checked-in', 'No-show']
cancellation_reasons = ['Price', 'Change of plans', 'Weather', 'Other']
payment_methods = ['Credit Card', 'UPI', 'Cash', 'Corporate Account']
booking_channels = ['Website', 'Mobile App', 'Travel Agent', 'Call Center']
purpose_booking = ['Business', 'Vacation', 'Conference', 'Holiday']

# ------------------ GENERATE CUSTOMERS ------------------
def generate_customers():
    customers = []
    for i in range(num_customers):
        cid = f"C{i+1:04d}"
        name = random.choice(customer_names)
        email = f"{name.lower().replace(' ', '')}{i}@example.com"
        phone = f"9{random.randint(100000000, 999999999)}"
        nationality = random.choice(nationalities)
        tier = random.choice(loyalty_tiers)
        age = random.choice(age_groups)
        gender = random.choice(genders)
        customers.append([cid, name, email, phone, nationality, tier, age, gender])
    return customers

# ------------------ GENERATE BOOKINGS ------------------
def generate_bookings(customers):
    bookings = []
    for i in range(num_bookings):
        bid = f"BK{i+1000}"
        customer = random.choice(customers)
        room = random.choice(room_types)
        branch = random.choice(branches)
        check_in = datetime.today() - timedelta(days=random.randint(0, 900))
        duration = random.randint(1, 7)
        check_out = check_in + timedelta(days=duration)
        revenue = room['Price'] * duration
        status = random.choice(booking_statuses)
        cancel_reason = random.choice(cancellation_reasons) if status == 'Cancelled' else ''
        lead_time = random.randint(0, 60)
        payment = random.choice(payment_methods)
        discount = random.choice([0, 5, 10, 15, 20])
        channel = random.choice(booking_channels)
        purpose = random.choice(purpose_booking)
        bookings.append([
            bid, customer[0], room['RoomTypeID'], branch['BranchID'],
            check_in.strftime('%Y-%m-%d'),
            check_out.strftime('%Y-%m-%d'),
            duration, revenue, status, cancel_reason,
            lead_time, payment, discount, channel, purpose
        ])
    return bookings

# ------------------ WRITE CSV FUNCTION ------------------
def write_csv(filename, header, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# ------------------ EXECUTION ------------------
customers = generate_customers()
bookings = generate_bookings(customers)

write_csv('Customer.csv',
          ['CustomerID', 'Name', 'Email', 'Phone', 'Nationality', 'LoyaltyTier', 'AgeGroup', 'Gender'],
          customers)

write_csv('RoomType.csv',
          ['RoomTypeID', 'RoomType', 'Price', 'MaxOccupancy', 'Amenities', 'IsAC', 'IsSeaFacing'],
          [list(r.values()) for r in room_types])

write_csv('Branch.csv',
          ['BranchID', 'BranchName', 'City', 'State', 'ManagerName', 'Phone', 'StarRating', 'RoomCount', 'RevenueScore', 'HasPool', 'HasConferenceRoom'],
          [list(b.values()) for b in branches])

write_csv('Booking.csv',
          ['BookingID', 'CustomerID', 'RoomTypeID', 'BranchID', 'CheckInDate', 'CheckOutDate', 'Duration', 'Revenue',
           'BookingStatus', 'CancellationReason', 'LeadTime', 'PaymentMethod', 'DiscountApplied', 'BookingChannel', 'Purpose'],
          bookings)

print("✅ CSVs generated successfully: Customer.csv, Booking.csv, RoomType.csv, Branch.csv") 