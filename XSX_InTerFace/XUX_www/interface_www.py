# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''www域接口'''
        self.PromotionNums_url='http://www.xiaoshuxiong.com/api/order/getPromotionNums'
        self.updateRemindMsg_url='http://www.xiaoshuxiong.com/api/order/updateRemindMsg'
        self.OrderByProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'
        self.updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
        self.RemindMsg_url='http://www.xiaoshuxiong.com/api/order/getRemindMsg'
        self.createOrderTour_url='http://www.xiaoshuxiong.com/api/order/createOrderTour'
        self.OutOrderSn_url='http://www.xiaoshuxiong.com/api/order/setOutOrderSn'
        self.ChildOrderTour_url='http://www.xiaoshuxiong.com/api/order/getChildOrderTour'
        self.shipWithoutCoupon_url='http://www.xiaoshuxiong.com/api/ocoupon/shipWithoutCoupon'
        self.query_url='http://www.xiaoshuxiong.com/api/delivery/query'
        self.ByCouponCode_url='http://www.xiaoshuxiong.com/api/ocoupon/getByCouponCode'
        self.UserOrderNums_url='http://www.xiaoshuxiong.com/api/order/getUserOrderNums'
        self.de_AllStatus_url='http://www.xiaoshuxiong.com/api/delivery/getAllStatus'
        self.AllStatus_url='http://www.xiaoshuxiong.com/api/order/getAllStatus'
        self.OrderPromotionList_url='http://order.api.xiaoshuxiong.com/order/getOrderPromotionList'
        self.G_dingdan_url='http://www.xiaoshuxiong.com/api/source/get'
        self.ProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'
        self.add_XUJ_url='http://www.xiaoshuxiong.com/api/ocoupon/add'
        self.verify_url='http://www.xiaoshuxiong.com/api/ocoupon/verify'
        self.ship_url='http://www.xiaoshuxiong.com/api/ocoupon/ship'
        self.getStocks_url='http://open.xiaoshuxiong.com/openapi/external/ppg/goods/getStock'
        self.InventoryBatchSn_url='http://www.xiaoshuxiong.com/api/goods/decreaseInventoryBatchSn'
        self.createOrderXsx_url='http://order.api.xiaoshuxiong.com/Order/createOrderXsx'
<<<<<<< HEAD
        self.KJ_Url='http://open.xiaoshuxiong.com/openapi/openapi/orderStatus?'
=======
        self.InfoByGoodsIdUrl='http://www.xiaoshuxiong.com/api/goods/getInfoByGoodsId'
        self.InfoByGoodsIdsUrl='http://www.xiaoshuxiong.com/api/goods/getInfoByGoodsIds'
        self.GoodsSkuByGoodsIdUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsSkuByGoodsId'
        self.GoodsSkuByGoodsIdsUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsSkuByGoodsIds'
        self.GoodsSkuByProductsIdUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsSkuByProductsId'
        self.GoodsSkuByProductsIdsUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsSkuByProductsIds'
        self.pageBatchUrl='http://www.xiaoshuxiong.com/api/PurchasePrice/pageBatch'
        self.batchInsertUrl='http://www.xiaoshuxiong.com/api/PurchasePrice/batchInsert'
        self.PurchasePrice_pageUrl='http://www.xiaoshuxiong.com/api/PurchasePrice/page'
        self.batchUpdateUrl='http://www.xiaoshuxiong.com/api/PurchasePrice/batchUpdate'
        self.ReferInfoUrl='http://www.xiaoshuxiong.com/api/supplier/getReferInfo'
        self.BrandBySupplierIdUrl='http://www.xiaoshuxiong.com/api/supplier/getBrandBySupplierId'
        self.GoodsIdsbySnbcUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsIdsbySnbc'
        self.BrandListUrl='http://www.xiaoshuxiong.com/api/brand/getBrandList'
        self.CatListTreeUrl='http://www.xiaoshuxiong.com/api/category/getCatListTree'
        self.GoodsNbcUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsNbc'
        self.GoodsBySupplierIdUrl='http://www.xiaoshuxiong.com/api/supplier/getGoodsBySupplierId'
        self.SkuListBySupplierIdUrl='http://www.xiaoshuxiong.com/api/supplier/getSkuListBySupplierId'
        self.GoodsListBySupplierIdUrl='http://www.xiaoshuxiong.com/api/supplier/getGoodsListBySupplierId'
        self.CatBySupplierIdUrl='http://www.xiaoshuxiong.com/api/supplier/getCatBySupplierId'
        self.hygjListUrl='http://www.xiaoshuxiong.com/api/goods/hygjList'
        self.SkuByPidsTourUrl='http://www.xiaoshuxiong.com/api/goods/getSkuByPidsTour'
        self.CommonGoodsByGidsTourUrl='http://www.xiaoshuxiong.com/api/goods/getCommonGoodsByGidsTour'
        self.GroupGoodsByGidsTourUrl='http://www.xiaoshuxiong.com/api/goods/getGroupGoodsByGidsTour'
        self.CatAttrByCatIdTourUrl='http://www.xiaoshuxiong.com/api/goods/getCatAttrByCatIdTour'
        self.CatTourUrl='http://www.xiaoshuxiong.com/api/goods/getCatTour'

>>>>>>> d9b1926d63bdfe279356feaa6bfa926bd4ddf105






















    def tearDown(self):
        pass
        #print(self.code,self.msgs)
