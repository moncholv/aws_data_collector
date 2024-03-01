"""_summary_"""
from typing import Dict

CONFIG_DETAILS: Dict[str, Dict[str, str]] = {
    "Glue": {
        "ID": 1,
        "CLIENT": "glue",
        "FOLDER_NAME": "Glue",
        "TYPES": [
            {
                "ID": 1,
                "TYPE": "jobs",
                "LIST_NAME": "JobNames",
                "CSV_HEADER": "JobName",
            },
            {
                "ID": 2,
                "TYPE": "crawlers",
                "LIST_NAME": "CrawlerNames",
                "CSV_HEADER": "CrawlerName",
            },
            {
                "ID": 3,
                "TYPE": "tables",
                "LIST_NAME": "TableNames",
                "CSV_HEADER": "Database,TableName",
            }
        ]
    },
    "Lambdas": {
        "ID": 2,
        "CLIENT": "lambda",
        "FOLDER_NAME": "Lambdas",
        "TYPES": [
            {
                "ID": "functions",
                "LIST_NAME": "Functions",
                "CSV_HEADER": "FunctionName,Description,LastModified,Role,MemorySize,Timeout",
            }
        ]
    },
    "Databrew": {
        "ID": 3,
        "CLIENT": "databrew",
        "FOLDER_NAME": "Databrew",
        "TYPES": [
            {
                "ID": 1,
                "TYPE": "datasets",
                "LIST_NAME": "Datasets",
                "KEY_NAME": "Name",
                "CSV_HEADER": "DatasetName",
            }
        ]
    },
    "AppConfig": {
        "ID": 4,
        "CLIENT": "appconfig",
        "FOLDER_NAME": "AppConfig",
        "TYPES": [
            {
                "ID": 1,
                "TYPE": "jobs",
                "LIST_NAME": "JobNames",
                "CSV_HEADER": "JobName",
            }
        ]
    }
}
