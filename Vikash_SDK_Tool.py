# Author: Vikash Sunil
# Contact for freelancing: Fiverr, Upwork (@8200452774)
# Python related any work, flutter, data analysis.
"""
Topic: Python Command Line Interface Tool (Dyte)
the read_update() function is the main logic behind the tool
if update parameter is passed then pr is 1 and we add update_pr in the list else not
then open the file and read the csv file and go through every repository link and read the package.json file
check for the given dependency in the input and compare it in json file.
The link is  raw.githubusercontent.com + repository name
We check for the dependency and then compare the version number.


if the version number given in the input is less than or equal than the dependency version then we add true else false
store each result in a new csv file

if update option is also passed by the user then the repository which has the greater version is passed with
a pull request and the link is added in the csv file.

Our final output is stored in 'output.csv' and also printed in the console.

How to run the Tool?
1] Open any terminal and move to the project directory or folder
2] Type python Vikash_SDK_Tool.py -h or python Vikash_SDK_Tool.py -i filename.csv dependency@version
Hence the format to run the code is: python python_filename.py -i input_filename.csv dependency@version
"""
import argparse
import csv
import requests
import ssl
import json


def read_update(filename, dependency, version, pr):
    head = ['name', 'repo', 'version', 'version_satisfied']
    if pr == 1:
        head.append('update_pr')
    rows = []
    with open(filename, 'r', encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # skip the headers
        for x in csvreader:
            x[1] = x[1] + '/' if x[1] != '/' else x[1]
            islice = x[1].index('dyte-in')
            url = "https://raw.githubusercontent.com/"
            url += x[1][islice:]
            url += "main/package.json"
            resp = requests.get(url)
            data = json.loads(resp.text)
            current_version = data["dependencies"][dependency][1:]
            bool_version = 'true' if version <= current_version else 'false'
            pr_url = x[1]+'pull/'
            if pr == 0:
                rows.append([x[0], x[1], current_version, bool_version])
            else:
                pr_url = '' if bool_version=='true' else pr_url
                rows.append([x[0], x[1], current_version, bool_version, pr_url])

        with open('output.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(head)
            writer.writerows(rows)

        count = 1
        for x in rows:
            print(str(count) + ':')
            index = 0
            for each in x:
                print(head[index] + ' => ' + each)
                index += 1
            count += 1
            print('-' * 60)
        print("Result is stored in 'Output.csv' file")


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parser = argparse.ArgumentParser(description="A Python CLI Tool")

parser.add_argument("-i", type=str, nargs='*',
                        metavar="csv_file_name", default=None,
                        help="Reads the csv file with Repository name and link.")

parser.add_argument("-update", type=str, nargs='*',
                        metavar="update command", default=None,
                        help="Pull Request to the Repository with version number less than specified")

args = parser.parse_args()

file = args.i
update = args.update

if file is not None:
    filename = file[0]
    dependency, version = file[1].split('@')
    if update is None:
        read_update(filename, dependency, version, 0)
    else:
        read_update(filename, dependency, version, 1)
