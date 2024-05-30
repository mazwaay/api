import requests
import time

base_url = "https://reqres.in"
endpoint = "/api/users/1"  # Replace with a valid endpoint if needed

url = base_url + endpoint

try:
    start_time = time.time()  # Start time measurement
    response = requests.get(url)
    end_time = time.time()  # End time measurement

    # Calculate total request time in milliseconds
    total_time_ms = int((end_time - start_time) * 1000)

    if response.status_code == 200:
        data = response.json()
        print(f"Pengguna ditemukan (200) dalam {total_time_ms} ms")
        print(data)
        # ... (your data processing logic here)
    elif response.status_code == 404:
        print(f"Pengguna tidak ditemukan (404) dalam {total_time_ms} ms")
    else:
        print(f"Permintaan API gagal dengan kode status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Kesalahan terjadi saat membuat permintaan: {e}")
