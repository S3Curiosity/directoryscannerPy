import requests

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        return None

def main():
    target_url = input('[*] Enter Target URL (e.g., http://example.com): ')
    if not target_url.startswith(("http://", "https://")):
        target_url = "http://" + target_url

    file_name = input('[*] Enter Name Of The File Containing Directories: ')

    try:
        with open(file_name, 'r') as file:
            for line in file:
                directory = line.strip()
                full_url = f'{target_url}/{directory}'
                response = request(full_url)
                if response:
                    print(f'[*] Discovered Directory At This Path: {full_url}')
    except FileNotFoundError:
        print(f"[*] File '{file_name}' not found.")

if __name__ == "__main__":
    main()
