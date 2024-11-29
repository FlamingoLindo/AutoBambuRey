import base64  
import os  
import pytest  
import pytest_html  
from pytest_metadata.plugin import metadata_key

# Lojista
# from Lojista.App.test_bank_account import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Lojista.App.test_create_product_lojista import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Lojista.App.test_add_cupom import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Lojista.App.test_add_voucher import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Lojista.App.test_approve_promotor_products import (TEST_TITLE, QA, BACK, MOBILE, TYPE)

# Promotor
# from Promotor.App.test_create_product_promotor import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Promotor.App.test_create_feed_post import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Promotor.App.test_delete_all_pending_products import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Promotor.App.test_add_store_promotor import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
from Promotor.App.test_add_bank_account import (TEST_TITLE, QA, BACK, MOBILE, TYPE)

# Cliente
# from Client.test_add_addres import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Client.test_change_password import (TEST_TITLE, QA, BACK, MOBILE, TYPE)
# from Client.test_add_card import (TEST_TITLE, QA, BACK, MOBILE, TYPE)

@pytest.hookimpl(hookwrapper=True)  
def pytest_runtest_makereport(item):  
    outcome = yield  
    report = outcome.get_result()  
    extra = getattr(report, "extra", [])  
    if report.when == "call":  
        # Assuming your screenshot is saved correctly at the specified path  
        screenshot_path = os.path.join(os.getcwd(), 'Images', 'Screenshots', 'screenshot.png')
        if os.path.exists(screenshot_path):
            try:
                with open(screenshot_path, "rb") as image_file:  
                    encoded_string = base64.b64encode(  
                        image_file.read()  
                    ).decode()  # https://github.com/pytest-dev/pytest-html/issues/265  
                extra.append(pytest_html.extras.png(encoded_string))  
                report.extra = extra
            except PermissionError:
                print(f"Permission denied: '{screenshot_path}'")
        else:
            print(f"File not found: '{screenshot_path}'")

def pytest_html_report_title(report):  
    report.title = TEST_TITLE
  
def pytest_configure(config):
    config.option.htmlpath = 'Reports/report.html'
  
    config.stash[metadata_key]["Projeto"] = f"Bamburey {TYPE}"  
    config.stash[metadata_key]["QA"] = f"{QA}" 
    config.stash[metadata_key]["Back"] = f"{BACK}"
    config.stash[metadata_key]["Mobile"] = f"{MOBILE}" 
    
    config.stash[metadata_key]["Ambiente"] = "Produção"
    config.stash[metadata_key]["Versão"] = "1.0.0"
    config.stash[metadata_key]["Build"] = "12345"