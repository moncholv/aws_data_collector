""" Glue utility script """
import time
import boto3

client = boto3.client('databrew')


def _get_response(element_type: str, next_token: str) -> dict:
    """_summary_

    Args:
        element (str): _description_

    Returns:
        dict: _description_
    """
    if element_type == "datasets":
        if next_token:
            response = client.list_datasets(NextToken=next_token)
        else:
            response = client.list_datasets()

    return response


def get_databrew_elements(config_value: dict):
    """_summary_

    Args:
        element_type (str): _description_
        config_value (dict): _description_

    Returns:
        _type_: _description_
    """
    all_elements = []
    next_token = ""

    while True:
        response = _get_response(
            element_type=config_value["TYPE"],
            next_token=next_token
        )
        if "KEY_NAME" in config_value:
            for data in response[config_value["LIST_NAME"]]:
                all_elements.extend(data[config_value["KEY_NAME"]])
        else:
            all_elements.extend(response[config_value["LIST_NAME"]])
        time.sleep(0.5)  # To avoid error
        next_token = response.get('NextToken')
        if not next_token:
            break

    return all_elements
