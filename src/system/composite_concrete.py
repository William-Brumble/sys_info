
from .composite_abc import CompositeAbstract
from .leaf_information_abc import LeafInformationAbc
from .leaf_database_abc import LeafDatabaseAbc

class Composite(CompositeAbstract):
    """
    Gathers System Information

    methods:
        get_system()
        get_node()
        get_release()
        get_version()
        get_machine()
        get_cpu_count()
        get_total_ram()
        save_information()
    """

    def __init__(self,
            p_leaf_information:LeafInformationAbc,
            p_leaf_database:LeafDatabaseAbc) -> None:
        self._information_leaf = p_leaf_information
        self._database_leaf = p_leaf_database

    def __repr__(self) -> str:
        representation = ("SystemInformation(" +
            "{},".format(self._information_leaf.get_system()) +
            "{},".format(self._information_leaf.get_node()) +
            "{},".format(self._information_leaf.get_release()) +
            "{},".format(self._information_leaf.get_version()) +
            "{})".format(self._information_leaf.get_machine()()) +
            "{})".format(self._information_leaf.get_total_ram()()) +
            "{})".format(self._information_leaf.get_cpu_count()()))
        return representation

    def __str__(self) -> str:
        string = ("(system={},".format(self._information_leaf.get_system()) +
            "node={},".format(self._information_leaf.get_node()) +
            "release={},".format(self._information_leaf.get_release()) +
            "version={},".format(self._information_leaf.get_version()) +
            "machine={})".format(self._information_leaf.get_machine()) +
            "total_ram={})".format(self._information_leaf.get_total_ram()) +
            "cpu_count={})".format(self._information_leaf.get_cpu_count()))
        return string

    def get_system(self):
        system = self._information_leaf.get_system()
        return system

    def get_node(self):
        node = self._information_leaf.get_node()
        return node

    def get_release(self):
        release = self._information_leaf.get_release()
        return release

    def get_version(self):
        version = self._information_leaf.get_version()
        return version

    def get_machine(self):
        machine = self._information_leaf.get_machine()
        return machine

    def get_total_ram(self):
        total_ram = self._information_leaf.get_total_ram()
        return total_ram

    def get_cpu_count(self):
        cpu_count = self._information_leaf.get_cpu_count()
        return cpu_count

    def save_information(self):
        self._database_leaf.save_information(
                self.get_system(),
                self.get_node(),
                self.get_release(),
                self.get_version(),
                self.get_machine(),
                self.get_total_ram(),
                self.get_cpu_count())

