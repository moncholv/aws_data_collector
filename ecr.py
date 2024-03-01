""" Databrew quotas utility script """
import argparse
import os
from pathlib import Path
import boto3
from common_utils import write_to_csv

directory = os.path.dirname(os.path.abspath("__file__"))
FOLDER_NAME = "ECR"
IMAGES_DETAILS_FILENAME = "image_details"


def append_dataset_data(item: dict) -> str:
    """_summary_"""
    dataset_list = []
    dataset_list.append(item["imageTag"])
    dataset_list.append(item["imageDigest"])

    return ','.join(dataset_list)


parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "--all",
    help="Generates files with details for all options",
    action="store_true",
)

args = parser.parse_args()
all_options = args.all

folder_path = f"{directory}/files/{FOLDER_NAME}"
Path(folder_path).mkdir(parents=True, exist_ok=True)
client = boto3.client("ecr")
line_list = []

if not all_options:
    print("Please add at least one argument when executing script")
if all_options:
    total_num_functions = 0
    print("Available Environments:")
    print("----------------------")
    print("1 - devproduct2")
    print("2 - integration")
    print()
    environment_id = input(" >> Please select an option: ")
    aws_environment = ""
    registry_id = ""
    if environment_id == "1":
        aws_environment = "devp2"
        registry_id = "401139785064"
    elif environment_id == "2":
        aws_environment = "int"
        registry_id = ""

    if environment_id in ["1", "2"]:
        response_list_images = client.list_images(
            registryId=registry_id,
            repositoryName=""
        )

        if response_list_images["ResponseMetadata"]["HTTPStatusCode"] == 200:
            line_list.append("FunctionName,Version,Description")

            functions = response_list_images["imageIds"]
            total_num_functions += len(functions)
            for dataset_item in functions:
                line_list.append(append_dataset_data(dataset_item))

            while "nextToken" in response_list_images:
                response_list_images = client.list_functions(
                    registryId=registry_id,
                    repositoryName="",
                    nextToken=response_list_images["nextToken"]
                )
                functions = response_list_images["imageIds"]
                total_num_functions += len(functions)
                for dataset_item in functions:
                    line_list.append(append_dataset_data(dataset_item))

            print('-------------------------------')
            print(f"Functions: {total_num_functions}")
            write_to_csv(folder_path=folder_path,
                         file_name=IMAGES_DETAILS_FILENAME,
                         content_list=line_list,
                         aws_environment=aws_environment)
        else:
            print(response_list_images["ResponseMetadata"])
    else:
        print("Invalid Option!")
