# -*- coding: utf-8 -*-
"""
Created on 2021-08-11 22:04:04
---------
@summary:
---------
@author: lanba
"""

from feapder import Item


class EtsyProdcutDetailItem(Item):
    """
    This class was generated by feapder.
    command: feapder create -i etsy_prodcut_detail.
    """

    def __init__(self, *args, **kwargs):
        self.batch_date = None
        self.category = None
        self.favorites = None
        self.id = None
        self.price = None
        self.rating = None
        self.review = None
        self.sales = None
        self.shop = None
        self.tags = None
        self.title = None
        self.description=None
