# header
register_button_xpath = "//div[@id='account']/div/button[2]"
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
register_button_popup_xpath = "//span[text() = 'Register']/parent::*"

# Gmail Access
# gmail_button = "//a[contains(text(), 'Gmail')]"
stackoverflow_email = "//input[@id = 'email']"
stackoverflow_password = "//input[@id = 'password']"
stackoverflow_submit = "//button[@id = 'submit-button']"
stackoverflow_signin_google = "//button[@data-provider = 'google']"
google_reject_cookies = "//div[text() = 'Reject all']//parent::*"
google_signin = "//a[@aria-label = 'Sign in']"
gmail_email_textbox = "//input[@type = 'email']"
gmail_password_textbox = "//input[@type= 'password']"
gmail_next_btn = "//span[text() = 'Next']"
gmail_nu_acum = "//span[text() = 'Nu acum']"
