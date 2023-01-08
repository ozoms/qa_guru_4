def print_name_func(name_func, *arg_func):
    name_func = ' '.join(name_func.__name__.title().split('_'))
    arg_func = ' '.join(list(arg_func))
    return print(name_func, arg_func)


def open_browser(browser_name):
    return print_name_func(open_browser, browser_name)


open_browser('Chrome')


def go_to_companyname_homepage(page_url):
    return print_name_func(go_to_companyname_homepage, page_url)


go_to_companyname_homepage('google.com')


def find_registration_button_on_login_page(page_url, button_text):
    return print_name_func(find_registration_button_on_login_page, page_url, button_text)


find_registration_button_on_login_page('google.com', 'Search')
