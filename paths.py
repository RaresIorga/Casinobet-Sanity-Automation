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

# country
country_select_xpath = "//div[text() = 'Select your country']"
country_search_xpath = "//input[@type = 'text']"
country_option_select_xpath = "//ul[@class = 'country-list']/li"
country_submit_xpath = "//span[text()='Submit']/.."

# Profile pop-up
profile_settings = "//button[text()='Settings']"

# Settings
settings_verification = "//span[text()='Verification']/.."

# Verification
verification_code = "//input[@name = 'pin-field']"
verification_send = "//span[text()= 'Send']/.."

# Gmail Access
gmail_is_signed = "//span[text()='Sign in']"
# google_reject_cookies = "//div[text() = 'Reject all']//parent::*"
# google_signin = "//a[@aria-label = 'Sign in']"
gmail_email_textbox = "//input[@type = 'email']"
gmail_password_textbox = "//input[@type= 'password']"
gmail_next_btn = "//span[text() = 'Next']"
gmail_nu_acum = "//span[text() = 'Nu acum']"
gmail_casinobet_verification = "//div[contains(text(), 'CasinoBet')]"