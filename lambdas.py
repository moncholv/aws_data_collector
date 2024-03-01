""" Lambdas utility script """
import argparse
import os
from pathlib import Path
import boto3
from common_utils import get_environment_name, write_to_csv

directory = os.path.dirname(os.path.abspath("__file__"))
FOLDER_NAME = "Lambdas"
FUNCTIONS_DETAILS_FILENAME = "lambdas_functions_details"

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/list_functions.html

def append_dataset_data(item: dict) -> str:
    """_summary_"""
    dataset_list = []
    dataset_list.append(item["FunctionName"])
    dataset_list.append(item["Description"])
    last_modified = str(item["LastModified"])
    dataset_list.append(f"{last_modified[:10]} {last_modified[11:16]}")
    dataset_list.append(item["Role"])
    dataset_list.append(str(item["MemorySize"]))
    dataset_list.append(str(item["Timeout"]))

    return ','.join(dataset_list)


parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--functions",
    help="Generates files with details for all options",
    action="store_true",
)

args = parser.parse_args()
functions = args.functions

folder_path = f"{directory}/files/{FOLDER_NAME}"
Path(folder_path).mkdir(parents=True, exist_ok=True)
client = boto3.client("lambda")
line_list = []

if not functions:
    print("Please add at least one argument when executing script")
elif functions:
    total_num_functions = 0
    aws_environment = get_environment_name()
    response_list_functions = client.list_functions()

    if response_list_functions["ResponseMetadata"]["HTTPStatusCode"] == 200:
        line_list.append("FunctionName,Description,LastModified,Role,MemorySize,Timeout")

        functions_list = response_list_functions["Functions"]
        total_num_functions += len(functions_list)
        for function in functions_list:
            line_list.append(append_dataset_data(function))

        while "NextMarker" in response_list_functions:
            response_list_functions = client.list_functions(
                Marker=response_list_functions["NextMarker"]
            )
            functions_list = response_list_functions["Functions"]
            total_num_functions += len(functions_list)
            for function in functions_list:
                line_list.append(append_dataset_data(function))

        print('-------------------------------')
        print(f"Functions: {total_num_functions}")
        write_to_csv(folder_path=folder_path,
                     file_name=FUNCTIONS_DETAILS_FILENAME,
                     content_list=line_list,
                     aws_environment=aws_environment)
    else:
        print(response_list_functions["ResponseMetadata"])
