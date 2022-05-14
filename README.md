
This project logs system information to a SQLite database.

Database name (full path + name) and table name are defined during instantiation as arguments passed into the constructor.

The database will be created if it doesn't exist (file path directories must exist).

The database table will only ever be one row with a primary key ID of 1, no matter how many times it's run, replaces existing.

Example usage:

```Python
# import the modules factory
from system.factory import Factory

# instantiate the class using the factory method
db_path = "/path/to/db/database_name.db"
tbl_name = "table_name"
sys_info = Factory.create_system(db_path, tbl_name)

# grab any of the available system information
print(sys_info.get_machine())
print(sys_info.get_node())
print(sys_info.get_release())
print(sys_info.get_system())
print(sys_info.get_version())
print(sys_info.get_total_ram())
print(sys_info.get_cpu_count())

# save information to the database
sys_info.save_information()
```

Database schema:\
[ id, timestamp, system, node, release, version, machine, total_ram, cpu_count ]

Dependencies:\
psutil==5.9.0

