""" Databrew quotas utility script """
import argparse
import os
from pathlib import Path
import time
import boto3
import pandas as pd

from common_utils import get_environment_name, write_to_csv

directory = os.path.dirname(os.path.abspath("__file__"))
FOLDER_NAME = "EventBridge"
RULES_DETAILS_FILENAME = "rules_details"

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_rules.html


