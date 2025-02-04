from django.db import models
from django.db.models import Q
from django.conf import settings
from sqlalchemy import create_engine
import pandas as pd
import re
import operator
from functools import reduce

class Meibo(models.Model):
    id = models.AutoField(primary_key=True)
    simei = models.CharField(max_length=50, verbose_name="氏名")
    simei_kana= models.CharField(max_length=50)
    email_addr = models.CharField(max_length=50)
    seibetu = models.CharField(max_length=10)
    tanjo_bi = models.DateField()
    blood_gata = models.CharField(max_length=5)
    chiiki = models.CharField(max_length=50)
    phone_bango = models.CharField(max_length=10)

    def __str__(self):
        return self.simei

    @classmethod
    def get_kensaku(cls, query):
        def kensaku(s):
            return (
                Q(simei__regex = s) |
                Q(simei_kana__regex = s) |
                Q(seibetu__regex = s) |
                Q(blood_gata__regex = s) |
                Q(chiiki__regex = s)
            )

        if not query:
            return Q(simei__regex = "^$")

        tokens = re.split(r'[ 　]+', query)
        q_objects = (kensaku(token) for token in tokens)
        return reduce(operator.and_, q_objects)

    # CSVファイルを読み込んでモデルに挿入
    @classmethod
    def from_csv(cls, filename):
        fields = [f.name for f in cls._meta.fields] # モデルの列名を取得
        fields.remove('id') # id 列を削除
        cls.objects.all().delete()
        db_table = cls.objects.model._meta.db_table
        con = create_engine("sqlite:///" + (settings.DATABASES['default']['NAME']).name)
        df = pd.read_csv(filename, header=None, names=fields, encoding='utf-8-sig', skiprows=1)
        df.tanjo_bi.replace('\/', r'-', regex=True, inplace=True)
        df.to_sql(db_table, con, if_exists='append', index=False)
