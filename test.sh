#!/bin/bash
python3 import_to_cvm.py --host "http://localhost:3001" --project_id 2 --pipeline_run_id "222" --pipeline_run_url "pipeline_run_url"  --commit_hash="commit_hash" --branch_name="branch_name" --tool_type="Gitleaks" --test_title="Secret Scan" --report "./report/gitleak-report/report.json" 
