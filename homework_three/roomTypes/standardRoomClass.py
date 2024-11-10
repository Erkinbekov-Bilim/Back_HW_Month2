from Geeks_M2.homework_three.roomTypes.roomAbstractClass import Room


class StandardRoom(Room):

    def get_features(self):
        return self._features

    def get_price(self):
        return self._Room__price
