
from abc import ABCMeta, abstractmethod

class LeafInformationAbc(metaclass=ABCMeta):

    @abstractmethod
    def get_system(self):
        raise Exception("concrete class must implement get_system")

    @abstractmethod
    def get_node(self):
        raise Exception("concrete class must implement get_node")

    @abstractmethod
    def get_release(self):
        raise Exception("concrete class must implement get_release")

    @abstractmethod
    def get_version(self):
        raise Exception("concrete class must implement get_version")

    @abstractmethod
    def get_machine(self):
        raise Exception("concrete class must implement get_machine")

    @abstractmethod
    def get_cpu_count(self):
        raise Exception("concrete class must implement get_cpu_count")

    @abstractmethod
    def get_total_ram(self):
        raise Exception("concrete class must implement get_cpu_count")

