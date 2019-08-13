# coding = utf-8

from haystack import indexes
from .models import GoodsInfo



class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    #索引字段  use_template=True ；根据指定表中的那些字段建立索引文件 放在一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo
    #建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
