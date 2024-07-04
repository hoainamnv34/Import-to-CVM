import json
import string
import requests
import sys
import argparse
import os


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    elif v.lower() in ('none', 'null', ""):
        return None
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def uploadToCVM(
        host, 
        project_id, 
        run_id, 
        run_url, 
        commit_hash, 
        branch_name, 
        tool_name, 
        test_title, 
        server_url,
        api_key,
        service_key, 
        file_path,
        ):

    params = {
        'project_id': project_id,
        'run_id': run_id,
        'tool_name': tool_name,
        'test_title': test_title,
    }
    
    if run_url:
        params['run_url'] = run_url
    if commit_hash:
        params['commit_hash'] = commit_hash
    if branch_name:
        params['branch_name'] = branch_name
    if server_url:
        params['url'] = server_url
    if api_key:
        params['api_key'] = api_key
    if service_key:
        params['service_key'] = service_key

    files = {}
    if file_path:
        files = {'file': open(file_path, 'rb')}
    # print(files['file'][1].read())
    

    endpoint = f"{host}/api/import"

    print(endpoint)
    # headers = {
    #     "accept": "application/json",
    #     "Content-Type": "multipart/form-data"
    # }
    r = requests.post(endpoint, params=params, files=files)
    if r.status_code != 200:
        sys.exit(f'Post failed: {r.text}')
    print(r.text)

def fetchArguments():
    parse = argparse.ArgumentParser(description='Import scan results to CVM')
    parse.add_argument('--host', dest='host')
    parse.add_argument('--project_id', dest='project_id')
    parse.add_argument('--run_id', dest='run_id')
    parse.add_argument('--run_url', dest='run_url')
    parse.add_argument('--commit_hash', dest='commit_hash')
    parse.add_argument('--branch_name', dest='branch_name')
    parse.add_argument('--tool_type', dest='tool_type')
    parse.add_argument('--test_title', dest='test_title')
    parse.add_argument('--server_url', dest='server_url')
    parse.add_argument('--api_key', dest='api_key')
    parse.add_argument('--service_key', dest='service_key')
    parse.add_argument('--report', dest='report')

    return parse.parse_args()   


if __name__ == "__main__":
    args = fetchArguments()
    print(args)

    uploadToCVM(
        args.host, 
        args.project_id, 
        args.run_id, 
        args.run_url, 
        args.commit_hash, 
        args.branch_name, 
        args.tool_type, 
        args.test_title, 
        args.server_url,
        args.api_key,
        args.service_key, 
        args.report
    )