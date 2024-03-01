# aws-quotas-util


## Description
Project which contains several scripts to get AWS resources details to control different established quotas.

To make use of these scripts first step consists on login to the desired environment:

```
export AWS_PROFILE=devp2
aws sso login --profile ukhsa-devp2
```
And then run the desired script.

## Scripts

#### AppConfig

The script <font size=2 color="blue">app_config.py</font> is coded in Python, intended to be run from a command line, will provide information about the following resources:
- [ ] Configuration Profiles
- [ ] Deployment Strategies

<br />

##### Script Arguments
The script allows the following arguments:

<img src='images/readme/app_config/help.png' />

- **-q --quotas**:
```
python3 app_config.py -q
```
Prints Configuration Profiles and Deplyoment Strategis data

<img src='images/readme/app_config/execution_quotas.png' />

and generates file <font size=2 color="orange">environment_</font><font size=2 color="blue">AppConfig_quotas_data.csv</font> (AWS environment name will be requested) with the following content:
```
app_id,app_name,num_config_profiles
mp9vfh1,ukhsa-devp2-staging-scan,1
1vn3fx4,ukhsa-devp2-source2ingest-sftp-pull,3
m55sdrd,ukhsa-devp2-source2ingest-scrape-pull,2
wxmwii3,ukhsa-devp2-source2ingest-s3-pull,1
gmkv7hp,ukhsa-devp2-source2ingest-azureobjectstorage-pull,3
...
```

- **-a --all**:
```
python3 app_config.py -a
```
<img src='images/readme/app_config/execution_all.png' />

Generates file <font size=2 color="orange">environment_</font><font size=2 color="blue">AppConfig_details.csv</font> (AWS environment name will be requested) with all applications configuration profiles details.
```
app_id,app_name,config_profile
mp9vfh1,ukhsa-devp2-staging-scan,lambda-av-scan
1vn3fx4,ukhsa-devp2-source2ingest-sftp-pull,test-source
1vn3fx4,ukhsa-devp2-source2ingest-sftp-pull,hep-sentinel
1vn3fx4,ukhsa-devp2-source2ingest-sftp-pull,hep-hepatitis-sgss
m55sdrd,ukhsa-devp2-source2ingest-scrape-pull,test-source
m55sdrd,ukhsa-devp2-source2ingest-scrape-pull,dash-covid-deaths
wxmwii3,ukhsa-devp2-source2ingest-s3-pull,test-source
...
```

- **-l --list**:
```
python3 app_config.py -l
```
Provides list of configuration profiles for specific application (also generates corresponding file).
Will prompt the user for specific application id.

<img src='images/readme/app_config/execution_list.png' /><br /><br />

- **-n --no_screen**:

```
python3 app_config.py -l -n
```
Doesn't print on screen configuration profiles list (to be used in conjunction with list argument).

<img src='images/readme/app_config/execution_list_n.png' /><br /><br />

#### Databrew

The script <font size=2 color="blue">databrew.py</font> is coded in Python, intended to be run from a command line, will provide information and actions to perform for the following resources:
- [ ] Datasets

<br />

##### Script Arguments
The script allows the following arguments:

