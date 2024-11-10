from Geeks_M2.homework_three.additionalServices.BreakfastService import BreakfastService
from Geeks_M2.homework_three.additionalServices.wiFiService import WiFiService
from Geeks_M2.homework_three.roomTypes.roomAbstractClass import Room


class LuxuryRoom(Room, WiFiService, BreakfastService):

    def get_features(self):
        self._features.append(self.get_wifi_description())
        self._features.append(self.get_breakfast_description())
        return self._features

    def get_price(self):
        return self._Room__price

