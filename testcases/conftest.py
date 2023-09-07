import os
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# from webdriver_manager.core import driver


###### only for chrome browser #############
@pytest.fixture(autouse=True, scope='function')
# @pytest.fixture(scope="class")
def setup(request):
    ##head less run
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = False
    ##inialize webdriver
    global driver
    driver = webdriver.Chrome(options=options)
    ## driver.get() to get in to mentioned urll
    driver.get(
        "https://www.ryanair.com/ie/en")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.ryanair.com/ie/en"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.sleep() *1000)))+".png"
            file_name = report.nodeid.replace(": :", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Ryanair report$"





