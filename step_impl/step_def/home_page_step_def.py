from getgauge.python import step, DataStoreFactory
from step_impl.step_def.page_factory import PageFactory


@step('User navigates to the home page')
def is_home_page_visible():
    PageFactory.home_page.is_home_page_visible()


@step('Search <searchText> and do control to result')
def searchAndControl(searchText):
    PageFactory.home_page.searchAndControl(searchText)


@step('Go to second page and do control is page active')
def goToSecondPageAndControl():
    PageFactory.home_page.goToSecondPageAndControl()


@step('Add favorite third product')
def addFavoriteThirdProduct():
    PageFactory.home_page.addFavoriteThirdProduct()


@step('Go to favorite page')
def goToFavoritePage():
    PageFactory.home_page.goToFavoritePage()
