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
        pipeline_run_id, 
        pipeline_run_url, 
        commit_hash, 
        branch_name, 
        tool_name, 
        test_title, 
        service_key, 
        file_path,
        # token
        ):

    # multipart_form_data = {
    #     'project_id': (None, project_id),
    #     'pipeline_run_id': (None, pipeline_run_id),
    #     'pipeline_run_url': (None, pipeline_run_url),
    #     'commit_hash': (None,commit_hash),
    #     'branch_name': (None, branch_name),
    #     'tool_name': (None, tool_name),
    #     'test_title': (None, test_title),
    #     'service_key': (None, service_key),
    # }

    params = {
        'project_id': project_id,
        'pipeline_run_id': pipeline_run_id,
        'tool_name': tool_name,
        'test_title': test_title,
    }
    
    if pipeline_run_url:
        params['pipeline_run_url'] = pipeline_run_url
    if commit_hash:
        params['commit_hash'] = commit_hash
    if branch_name:
        params['branch_name'] = branch_name
    if service_key:
        params['service_key'] = service_key

    # files = {}
    # if file_path:
    #     files['file']=(file_path, open(file_path, 'rb'))

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
    parse.add_argument('--pipeline_run_id', dest='pipeline_run_id')
    parse.add_argument('--pipeline_run_url', dest='pipeline_run_url')
    parse.add_argument('--commit_hash', dest='commit_hash')
    parse.add_argument('--branch_name', dest='branch_name')
    # parse.add_argument('--token', dest='token')

    parse.add_argument('--tool_type', dest='tool_type')
    parse.add_argument('--test_title', dest='test_title')
    parse.add_argument('--service_key', dest='service_key')
    parse.add_argument('--report', dest='report')

    return parse.parse_args()   


if __name__ == "__main__":
    args = fetchArguments()
    print(args)

    uploadToCVM(
        args.host, 
        args.project_id, 
        args.pipeline_run_id, 
        args.pipeline_run_url, 
        args.commit_hash, 
        args.branch_name, 
        args.tool_type, 
        args.test_title, 
        args.service_key, 
        args.report
    )