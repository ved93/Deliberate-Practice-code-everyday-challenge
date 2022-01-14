
# Design a parking lot using object-oriented principles
import string


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.spots = [None] * capacity
        self.vehicles = []
        self.spot_numbers = []
        self.spot_letters = []
        self.create_layout()
        
    def create_layout(self):
        for spot_number in range(1, self.capacity + 1):
            self.spot_numbers.append(spot_number)
        for spot_letter in string.ascii_uppercase[:self.capacity]:
            self.spot_letters.append(spot_letter)
        for spot_number, spot_letter in zip(self.spot_numbers, self.spot_letters):
            self.spots.append(Spot(spot_number, spot_letter))
            
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_available:
                spot.park(vehicle)
                self.vehicles.append(vehicle)
                return True
        return False
    
    def leave_parking_lot(self, spot_number):
        spot = self.spots[spot_number - 1]
        spot.leave()
        self.vehicles.remove(spot.vehicle)
        
    def get_available_spots(self):
        available_spots = []
        for spot in self.spots:
            if spot.is_available:
                available_spots.append(spot.spot_number)
        return available_spots
    
    def get_spot_number_from_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                return spot.spot_number
        return None
    
    def get_spot_letter_from_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                return spot.spot_letter
        return None
    
    def get_spot_number_from_spot_letter(self, spot_letter):
        for spot in self.spots:
            if spot.spot_letter == spot_letter:
                return spot.spot_number 

    def get_vehicle_from_spot_number(self, spot_number):
        for spot in self.spots:
            if spot.spot_number == spot_number:
                return spot.vehicle
        return None

    def get_vehicle_from_spot_letter(self, spot_letter):
        for spot in self.spots:
            if spot.spot_letter == spot_letter:
                return spot.vehicle
        return None
    
    def get_vehicle_from_spot(self, spot_number):
        for spot in self.spots:
            if spot.spot_number == spot_number:
                return spot.vehicle
        return None 
    
       

def Spot(spot_number, spot_letter):
    def __init__(self, spot_number, spot_letter):   
        self.spot_number = spot_number
        self.spot_letter = spot_letter
        self.vehicle = None
        self.is_available = True
    
    def park(self, vehicle):
        self.vehicle = vehicle
        self.is_available = False
        
    def leave(self):
        self.vehicle = None
        self.is_available = True


