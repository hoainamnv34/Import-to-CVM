import requests

# URL của server mà bạn muốn gửi yêu cầu
url = 'http://localhost:3001/api/import'

# Đường dẫn đến tệp mà bạn muốn gửi
file_path = '/home/hoainamnv34/DATN/import-to-CVM/report/gitleak-report/report.json'

# Tạo headers tùy chỉnh
headers = {
    "accept": "application/json",
    "Content-Type": "multipart/form-data"
}

# Mở tệp ở chế độ nhị phân
with open(file_path, 'rb') as f:
    # Tạo một dictionary để chứa dữ liệu form
    files = {'file': (file_path, f)}

    # Thêm các trường dữ liệu khác vào form
    data = {
        'project_id': 1,
        'pipeline_run_id': 1,
        'pipeline_run_url': "pipeline_run_url",
        'commit_hash': "commit_hash",
        'branch_name': "branch_name",
        'tool_name': "Gitleaks",
        'test_title': "test_title",
        'service_key': "service_key",
    }

    # Gửi yêu cầu POST với dữ liệu form và headers tùy chỉnh
    response = requests.post(url, files=files, params=data, headers=headers)

    # Kiểm tra mã trạng thái phản hồi
    if response.status_code == 200:
        print('Upload thành công!')
        print('Phản hồi từ server:', response.text)
    else:
        print(f'Upload thất bại với mã trạng thái: {response.status_code}')
        print('Phản hồi từ server:', response.text)