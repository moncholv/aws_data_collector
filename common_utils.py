""" Common utility functions """
import time


def get_environment_name() -> str:
    """_summary_"""
    print()
    return input(" >> AWS Environment: ")


def write_to_csv(
        folder_path: str = "",
        file_name: str = "",
        content_list: list = None,
        aws_environment: str = ""):
    """_summary_

    Args:
        aws_environment (str): _description_
        folder_path (str): _description_
        file_name (str): _description_
        content_list (list): _description_
    """
    if aws_environment != "":
        aws_environment += "_"
    final_file_name = f"{aws_environment}{time.strftime('%Y%m%d')}_{file_name}.csv"
    with open(f"{folder_path}/{final_file_name}", "w", encoding="utf-8") as f:
        f.write('\n'.join(content_list) + '\n')
    print(f"File {final_file_name} created")
