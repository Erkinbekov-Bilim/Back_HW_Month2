from Geeks_M2.homework_three.additionalServices.wiFiService import WiFiService
from Geeks_M2.homework_three.roomTypes.roomAbstractClass import Room


class FamilyRoom(Room, WiFiService):

    def get_features(self):
        self._features.append(self.get_wifi_description())
        return self._features

    def get_price(self):
        return self._Room__price
