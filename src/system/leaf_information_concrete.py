
""" System Leaf Information """

import platform
import psutil

from .leaf_information_abc import LeafInformationAbc

class LeafInformationConcrete(LeafInformationAbc):

    def __init__(self) -> None:
        system_information = self._get_system_information()
        self._system = self._get_system(system_information)
        self._node = self._get_node(system_information)
        self._release = self._get_release(system_information)
        self._version = self._get_version(system_information)
        self._machine = self._get_machine(system_information)
        self._cpu_count = self._get_cpu_count()
        self._total_ram = self._get_total_ram()
        del system_information

    def _get_system_information(self) -> dict:
        info = platform.uname()._asdict()
        return info

    def _get_system(self, system_information:dict) -> str:
        system = system_information.get("system")
        return system

    def _get_node(self, system_information:dict) -> str:
        node = system_information.get("node")
        return node

    def _get_release(self, system_information:dict) -> str:
        release = system_information.get("release")
        return release

    def _get_version(self, system_information:dict) -> str:
        version = system_information.get("version")
        return version

    def _get_machine(self, system_information:dict) -> str:
        machine = system_information.get("machine")
        return machine

    def _get_cpu_count(self):
        logical = psutil.cpu_count(logical=True)
        return str(logical)

    def _get_total_ram(self):
        total_ram = round(psutil.virtual_memory().total/1000000000, 2)
        return str(total_ram)

    def get_system(self):
        return self._system

    def get_node(self):
        return self._node

    def get_release(self):
        return self._release

    def get_version(self):
        return self._version

    def get_machine(self):
        return self._machine

    def get_cpu_count(self):
        return self._cpu_count

    def get_total_ram(self):
        return self._total_ram

