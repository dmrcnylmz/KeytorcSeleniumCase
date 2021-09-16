from getgauge.python import step, DataStoreFactory
from step_impl.step_def.page_factory import PageFactory


@step('Do control added product text is contains at the likes product')
def controlProductText():
    PageFactory.favorite_page.controlProductText()


@step('Delete favorite product on the list and do control')
def deleteFavoriteProductAndDoControl():
    PageFactory.favorite_page.deleteFavoriteProduct()
