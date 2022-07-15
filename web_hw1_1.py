from abc import ABCMeta, abstractmethod, ABC
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    def __init__(self, data, f_name):
        self.data = data
        self.__f_name = None
        self.f_name = f_name

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class SerializeJ(SerializationInterface):
    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        parse = f_name.split('.')
        if parse[1] == 'json':
            self.__f_name = f_name
        else:
            raise ValueError("File must be JSON format")

    def serialize(self):
        with open(self.__f_name, 'w') as file:
            json.dump(self.data, file)

    def deserialize(self):
        with open(self.__f_name, 'r') as file:
            unpacked = json.load(file)
            print(unpacked)


class SerializeB(SerializationInterface):
    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        parse = f_name.split('.')
        if parse[1] == 'bin':
            self.__f_name = f_name
        else:
            raise ValueError("File must be BIN format")

    def serialize(self, ):
        with open(self.__f_name, 'wb') as file:
            pickle.dump(self.data, file)

    def deserialize(self):
        with open(self.__f_name, 'rb') as file:
            unpacked = pickle.load(file)
            print(unpacked)


my_dict = {
    "kwarg1": "value_1",
    "kwarg2": "value_2",
    "kwarg3": "value_3",
    "additional": ["value_4", "value_5", "value_6"]}


json_test = SerializeJ(my_dict, 'My dict.json')
json_test.serialize()
json_test.deserialize()


bin_test = SerializeB(my_dict, 'My dict.bin')
bin_test.serialize()
bin_test.deserialize()
