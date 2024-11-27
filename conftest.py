from pytest_metadata.plugin import metadata_key  

from Lojista.App.test_bank_account import (TEST_TITLE, QA, BACK, MOBILE)
from Lojista.App.test_create_product_lojista import (TEST_TITLE, QA, BACK, MOBILE)
from Promotor.App.test_create_product_promotor import (TEST_TITLE, QA, BACK, MOBILE)
from Lojista.App.test_add_cupom import (TEST_TITLE, QA, BACK, MOBILE)
  
  
def pytest_html_report_title(report):  
    report.title = f"{TEST_TITLE}"  
  
def pytest_configure(config):
    config.option.htmlpath = 'Reports/report.html'
  
    config.stash[metadata_key]["Projeto"] = "Bamburey"  
    config.stash[metadata_key]["Qa"] = f"{QA}" 
    config.stash[metadata_key]["Back"] = f"{BACK}"
    config.stash[metadata_key]["Mobile"] = f"{MOBILE}" 
    
    config.stash[metadata_key]["Hambiente"] = "Produção"
    config.stash[metadata_key]["Versão"] = "1.0.0"
    config.stash[metadata_key]["Build"] = "12345"






