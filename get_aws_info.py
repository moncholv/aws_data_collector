""" _summary_ """
import copy
import os
import sys
from common_utils import get_environment_name, write_to_csv
from configs import CONFIG_DETAILS

directory = os.path.dirname(os.path.abspath("__file__"))


# Functions -----------------
def _display_options(options: dict = None):
    """_summary_

    Args:
        options (dict, optional): _description_. Defaults to None.
    """
    print()
    print("Script options:")
    print("----------------------------------------------")
    for key, value in options.items():
        print(f"{key}. {value.capitalize()}")
    print()
    print("0. Help")


def _get_user_choice(options: dict = None):
    """Get user's choice from the displayed options"""
    _display_options(options)
    choice = int(input("Enter the number of your choice: "))
    if choice not in range(0, len(options) + 1):
        print("ERROR >> Please select a valid option.")
        sys.exit(1)
    if choice == 0:
        print("HELP")
        sys.exit(0)
    return int(choice)


def _get_dict_by_key(key, array, id_value):
    """_summary_

    Args:
        key (_type_): _description_
        array (_type_): _description_
        id_value (_type_): _description_

    Returns:
        _type_: _description_
    """
    for d in array:
        if d.get(key) == id_value:
            return d
    return None  # Return None if ID is not found


config = copy.deepcopy(CONFIG_DETAILS)
options_dict = {value["ID"]: key for key, value in config.items()}
service = options_dict[_get_user_choice(options_dict)]
element_config = config[service]
options_dict = {item["ID"]: item["TYPE"] for item in element_config["TYPES"]}
option = _get_user_choice(options_dict)
option_selected = _get_dict_by_key("ID", element_config["TYPES"], option)

aws_environment = get_environment_name()

print(service)
print(option_selected)

if service == "Glue":
    print("1")
    from glue import get_glue_elements
    elements = get_glue_elements(option_selected)
elif service == "AppConfig":
    print("2")
    from app_config import get_appconfig_elements
    elements = get_appconfig_elements(option_selected)
elif service == "Databrew":
    print("3")
    from databrew import get_databrew_elements
    elements = get_databrew_elements(option_selected)

csv_data = [option_selected["CSV_HEADER"]]
csv_data.extend(elements)
print('-------------------------------')
print(f"{service} {option_selected['TYPE']}: {len(elements)}")
write_to_csv(folder_path=f"files/{service}",
             file_name=f"{option_selected['TYPE'].capitalize()}_details",
             content_list=csv_data,
             aws_environment=aws_environment)
