from django.db import models

# Create your models here.

class Temp_category(models.Model):
    temp_name = models.CharField(max_length=200)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()

    def __str__(self):
        return self.temp_name
# 의류
class Cloth(models.Model):
    photo = models.ImageField(null=True)        # 사진
    name = models.CharField(max_length=50)      # 옷이름
    brand = models.CharField(max_length=30)     # 브랜드이름
    price = models.CharField(max_length=15)     # 가격
    color = models.CharField(max_length=15)     # 색상
    size = models.CharField(max_length=15)      # 사이즈
    gender = models.CharField(max_length = 15)  # 성별
    sort = models.CharField(max_length=15)      # 상의인지 하의인지
    temp = models.ForeignKey(Temp_category, on_delete=models.CASCADE, db_column='temp_name')   # 온도 연결

    def __str__(self):
        return self.name
