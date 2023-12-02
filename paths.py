register_button_xpath = "//div[@id='account']/div/button[2]"
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
