from abc import ABC, abstractmethod


class Room(ABC):

    def __init__(self, features, price):
        self._features = features
        self.__price = price

    @abstractmethod
    def get_features(self):
        return self._features

    @abstractmethod
    def get_price(self):
        return self._Room__price




