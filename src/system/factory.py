
from .composite_concrete import Composite
from .leaf_information_concrete import LeafInformationConcrete
from .leaf_database_concrete import LeafDatabaseConcrete

class Factory:
   
    @staticmethod
    def create_system(
            p_database_name:str,
            p_table_name:str) -> Composite:

        sys_info = LeafInformationConcrete()
        sys_db = LeafDatabaseConcrete(p_database_name, p_table_name)
        sys_comp = Composite(sys_info, sys_db)

        return sys_comp

