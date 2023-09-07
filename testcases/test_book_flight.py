import pytest
import softest
from pages.homepage_pom import homepage
from ddt import ddt, data, file_data ,unpack
from utilities.utils import Utils




@pytest.mark.usefixtures("setup")
@ddt    #### use decorator at class level so that all methodscan use
class Test_book_plane(softest.TestCase):

    @pytest.fixture(autouse=True)
    def objects_setup(self):
        self.homepage_1 = homepage(self.driver)

    # @data(("Italy","Alghero"), ("Ireland","Kerry"))
    # @unpack              ###Looks like the unpack decorator should be used when there are more than one arguments
    # def test_1(self, item,number):
    #     self.homepage_1.open_search_box(item,number)
    #     self.homepage_1.click_on_country()

    @data(*Utils.read_data_from_excel("D:\\Ma$ter\\pythonProject\\pythonProject\\ryanair_final\\testdata\\departure_arival.xlsx", "page_1"))
    @unpack
    def test_2(self, country_from, city_from, country_to, city_to,departure_date, arrival_date, adults, teens, children):
        self.homepage_1.locator_generoator(country_from,city_from, country_to, city_to, departure_date, arrival_date, adults,teens, children)
        self.homepage_1.country_city_select()
