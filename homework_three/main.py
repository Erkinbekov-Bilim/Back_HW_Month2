from Geeks_M2.homework_three.roomTypes.familyRoomClass import FamilyRoom
from Geeks_M2.homework_three.roomTypes.luxuryRoomClass import LuxuryRoom
from Geeks_M2.homework_three.roomTypes.standardRoomClass import StandardRoom

standard_room = StandardRoom([], 100)
family_room = FamilyRoom([], 200)
luxury_room = LuxuryRoom([], 300)


print("Standard Room:")
print("Цена:", standard_room.get_price())
print("Удобства:", standard_room.get_features())

print("\nFamily Room:")
print("Цена:", family_room.get_price())
print("Удобства:", family_room.get_features())

print("\nLuxury Room:")
print("Цена:", luxury_room.get_price())
print("Удобства:", luxury_room.get_features())