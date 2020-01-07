def open_page(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    if response.status_code != 200:
        print(f"requests get {url} failed! {response.status_code}")
        return ''
    return response.text
