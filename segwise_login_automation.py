import asyncio
from playwright.async_api import async_playwright

EMAIL = "qa@segwise.ai"
PASSWORD = "segwise_test"
LOGIN_URL = "https://auth.segwise.ai/en/login"
DASHBOARD_URL = "https://app.segwise.ai/dashboard"
CHART_SELECTOR = "canvas"

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            print("Navigating to login page...")
            await page.goto(LOGIN_URL)
            await page.wait_for_load_state("networkidle")
            await page.screenshot(path="debug_login_page.png")
            print("Screenshot saved as debug_login_page.png")

            print("Looking for input fields...")

            email_selectors = [
                'get_by_placeholder("Email address")',
                'get_by_placeholder("email")',
                'get_by_placeholder("Email")',
                'get_by_placeholder("Enter your email")',
                'input[type="email"]',
                'input[name="email"]',
                '#email',
                '.email-input'
            ]

            email_field = None
            for i, selector in enumerate(email_selectors):
                try:
                    if 'get_by_placeholder' in selector:
                        placeholder_text = selector.split('"')[1]
                        email_field = page.get_by_placeholder(placeholder_text)
                        await email_field.wait_for(timeout=2000)
                        print(f"✅ Found email field with placeholder: {placeholder_text}")
                        break
                    else:
                        email_field = page.locator(selector)
                        await email_field.wait_for(timeout=2000)
                        print(f"✅ Found email field with selector: {selector}")
                        break
                except:
                    print(f"❌ Selector {i+1} failed: {selector}")
                    continue

            if not email_field:
                print("❌ Could not find email field with any selector")
                inputs = await page.locator('input').all()
                print(f"Found {len(inputs)} input elements:")
                for i, input_elem in enumerate(inputs):
                    placeholder = await input_elem.get_attribute('placeholder')
                    name = await input_elem.get_attribute('name')
                    input_type = await input_elem.get_attribute('type')
                    print(f"  Input {i+1}: placeholder='{placeholder}', name='{name}', type='{input_type}'")
                return

            await email_field.fill(EMAIL)
            print("✅ Email filled")

            password_selectors = [
                'get_by_placeholder("Password")',
                'get_by_placeholder("password")',
                'get_by_placeholder("Enter your password")',
                'input[type="password"]',
                'input[name="password"]',
                '#password',
                '.password-input'
            ]

            password_field = None
            for i, selector in enumerate(password_selectors):
                try:
                    if 'get_by_placeholder' in selector:
                        placeholder_text = selector.split('"')[1]
                        password_field = page.get_by_placeholder(placeholder_text)
                        await password_field.wait_for(timeout=2000)
                        print(f"✅ Found password field with placeholder: {placeholder_text}")
                        break
                    else:
                        password_field = page.locator(selector)
                        await password_field.wait_for(timeout=2000)
                        print(f"✅ Found password field with selector: {selector}")
                        break
                except:
                    print(f"❌ Password selector {i+1} failed: {selector}")
                    continue

            if not password_field:
                print("❌ Could not find password field")
                return

            await password_field.fill(PASSWORD)
            print("✅ Password filled")

            login_button_selectors = [
                'get_by_role("button", name="Sign in")',
                'button[type="submit"]',
                'input[type="submit"]',
                '.login-button',
                '#login-button',
                'button:has-text("Login")',
                'button:has-text("Sign in")'
            ]

            login_button = None
            for i, selector in enumerate(login_button_selectors):
                try:
                    if 'get_by_role' in selector:
                        login_button = page.get_by_role("button", name="Sign in")
                        await login_button.wait_for(timeout=2000)
                        print("✅ Found login button with role selector")
                        break
                    else:
                        login_button = page.locator(selector)
                        await login_button.wait_for(timeout=2000)
                        print(f"✅ Found login button with selector: {selector}")
                        break
                except:
                    print(f"❌ Login button selector {i+1} failed: {selector}")
                    continue

            if not login_button:
                print("❌ Could not find login button")
                return

            await login_button.click()
            print("✅ Login button clicked")

            await page.wait_for_load_state("networkidle")
            await page.goto(DASHBOARD_URL)

            try:
                await page.wait_for_selector(CHART_SELECTOR, timeout=5000)
                print("✅ Chart or metric found on dashboard.")
            except:
                print("❌ Chart or metric not found.")

        except Exception as e:
            print(f"❌ Error: {e}")
            await page.screenshot(path="error_screenshot.png")

        finally:
            input("Press Enter to close browser...")
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
