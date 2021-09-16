from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
from step_impl.pages.home_page import HomePage


class FavoritePageLocators:
    """ This is the class for home page locators. All home page locators should come here """

    FAVORITE_PRODUCT_TEXT2 = (By.XPATH, "(//h3[@data-test-id='product-card-name'])")
    PRODUCT_DETAIL_BUTTON = (By.XPATH, "(//div[@data-test-id='product-image-right-bar-container'])[1]")
    DELETE_PRODUCT_BUTTON = (By.XPATH, "(//div[@data-test-id='product-image-right-bar-container'])[1]")


class FavoritePage(BasePage):
    """ Home page actions """

    def controlProductText(self):
        FavoriteProduct2 = self.get(FavoritePageLocators.FAVORITE_PRODUCT_TEXT2)
        print("Favori listesindeki ürün adı:" + FavoriteProduct2)
        assert self.assertEqual(HomePage.getProductName(), FavoriteProduct2), "Eklenen ürün ile listedeki ürün " \
                                                                              "eşleşmiyor. "
        print("Eklenen ürün listede bulundu")

    def deleteFavoriteProduct(self):
        self.click(FavoritePageLocators.DELETE_PRODUCT_BUTTON)
        assert self.is_not_displayed(FavoritePageLocators.FAVORITE_PRODUCT_TEXT2), "Delete process fail"
        print("Favori listesi boş durumda.")
