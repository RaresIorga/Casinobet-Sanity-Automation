# header
register_button_xpath = "//div[@id='account']/div/button[2]"
avatar_xpath = "//div[@id='account']/div/button"

# registration pop-up
register_popup_login_xpath = ('//div[@class="modal-content custom-modal  "]//div[@class="modal-body"]//button[text('
                              ')="Login"]')
is_login_popup_xpath = "//div[@role='dialog']//div[contains(@class, 'login')]"
login_popup_register_xpath = "//button[contains(text(), 'Register')]"
is_register_popup_xpath = "//div[contains(@class, 'register')]"
register_username = "//input[@placeholder = 'Username']"
register_email = "//input[@placeholder = 'Email address']"
register_password = "//input[@placeholder = 'Password']"
register_checkbox = "//div[contains(@class, 'CheckBox')]//label"
register_button_popup_xpath = "//form/button/span[contains(text(), 'Register')]/.."
x_button = "//button[@class='auth-exit']"

# login
login_button = "//span[text()='Login']/.."
login_username = "//input[@name='username']"
login_password = "//input[@name='password']"
login_submit = "//button[@type='submit']"

# logout
logout_button = "//button[text() = 'Logout']"
got_it = "//span[text()='Got it']"


# country
country_select_xpath = "//div[text() = 'Select your country']"
country_search_xpath = "//input[@type = 'text']"
country_option_select_xpath = "//ul[@class = 'country-list']/li"
country_submit_xpath = "//span[text()='Submit']/.."

# Profile pop-up
profile_settings = "//button[text()='Settings']"

# Settings
settings_verification = "//span[text()='Verification']/.."
settings_x_button = ("//button[@class='p-2 fill-icon1 hover:fill-icon-active1 inline-flex']/*[local-name()='svg' and "
            "namespace-uri()='http://www.w3.org/2000/svg']")

# Verification
verification_code = "//input[@name = 'pin-field']"
verification_send = "//span[text()= 'Send']/.."
verification_request_another_code = "//span[text()= 'request another code']"
verification_specify_another_email = "//span[text()= 'specify another email']"
verification_another_email_input = "//input[@type = 'email']"
back_button = "//button[contains(@class, 'back-btn')]"

# Gmail Access
gmail_is_signed = "//span[text()='Sign in']"
gmail_email_textbox = "//input[@type = 'email']"
gmail_password_textbox = "//input[@type= 'password']"
gmail_next_btn = "//span[text() = 'Next']"
gmail_nu_acum = "//span[text() = 'Nu acum']"
gmail_casinobet_verification = "//span[text() = 'Verify your email address']/../../.."
gmail_casinobet_verification_code = "//table//p[contains(., 'Verification code:')]//b"
gmail_request_change_email = "//span[text() = 'Request to change your email address']"

# Paths for verifying if it's the correct account
gmail_account_button = "//a[contains(@aria-label, 'Google Account')]"
gmail_account_iframe = "//iframe[@name = 'account']"
gmail_add_another_acount = "//div[contains(text(), 'Add account')]"


def get_path_gmail_account(email):
    return f"//a[contains(@aria-label, '{email}')]"