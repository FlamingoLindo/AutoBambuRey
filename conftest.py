import base64  
import os  
import pytest  
import pytest_html  
from pytest_metadata.plugin import metadata_key  
  
  
def pytest_html_report_title(report):  
    report.title = "Report Cliente Bambu"  
  
  
def pytest_configure(config):  
    config.stash[metadata_key]["Project"] = "Bamburey"  
    config.stash[metadata_key]["QA"] = "Vitor Flamingo Lindo" 
    config.stash[metadata_key]["Back"] = "Lucas Chinize"
    config.stash[metadata_key]["Mobile"] = "Luciano Espojas" 

