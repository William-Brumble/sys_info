
from abc import ABCMeta, abstractmethod

class LeafDatabaseAbc(metaclass=ABCMeta):

    @abstractmethod
    def save_information(self,
            p_system:str,
            p_node:str,
            p_release:str,
            p_version:str,
            p_machine:str,
            p_total_ram:str,
            p_cpu_count:str) -> None:
        raise Exception("concrete class must implement save_information")

