from django.db import models

class AccountOfUser(models.Model):
    ID_account = models.AutoField(primary_key=True, verbose_name='Идентификатор аккаунта')
    Name = models.CharField(max_length=20, verbose_name='Имя')
    Surname = models.CharField(max_length=20, verbose_name='Фамилия')
    Age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    Body_measures = models.TextField(null=True, blank=True, verbose_name='Размеры тела')
    Preferences_list = models.TextField(null=True, blank=True, verbose_name='Список предпочтений')
    User_s_autoproducts = models.TextField(null=True, blank=True, verbose_name='Автотовары пользователя')
    User_s_sets = models.TextField(null=True, blank=True, verbose_name='Наборы пользователя')

    def __str__(self):
        return f"{self.Name} {self.Surname}"

class Autoproduct(models.Model):
    ID_autoproduct = models.AutoField(primary_key=True, verbose_name='Идентификатор автотовара')
    Autoproduct_photo = models.ImageField(upload_to='autoproduct_photos/', null=True, blank=True, verbose_name='Фото автотовара')
    Autoproduct_type = models.CharField(max_length=50, verbose_name='Тип Автотовара')
    Price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    In_stock_size = models.CharField(max_length=20, verbose_name='Размер в наличии')
    Material = models.CharField(max_length=50, verbose_name='Материал')
    Color = models.CharField(max_length=20, verbose_name='Цвет')
    Weight = models.CharField(max_length=20, verbose_name='Вес')
    Size = models.CharField(max_length=20, verbose_name='Размер')
    ID_store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name='Идентификатор магазина')

    def __str__(self):
        return f"{self.Autoproduct_type} - {self.Color}"


class CatalogAutoproducts(models.Model):
    ID_account = models.ForeignKey(AccountOfUser, on_delete=models.CASCADE, verbose_name='Идентификатор аккаунта')
    ID_autoproduct = models.ForeignKey(Autoproduct, on_delete=models.CASCADE, verbose_name='Идентификатор автотовара')

    def __str__(self):
        return f"{self.ID_account} - {self.ID_autoproduct}"


class CatalogSets(models.Model):
    ID_account = models.ForeignKey(AccountOfUser, on_delete=models.CASCADE, verbose_name='Идентификатор аккаунта')
    ID_set = models.ForeignKey('SetOfItems', on_delete=models.CASCADE, verbose_name='Идентификатор набора')

    def __str__(self):
        return f"{self.ID_account} - {self.ID_set}"


class ListOfErrors(models.Model):
    ID_Log = models.AutoField(primary_key=True, verbose_name='Идентификатор журнала')
    Log_name = models.CharField(max_length=100,verbose_name='Имя журнала')
    Date_of_request = models.DateTimeField(verbose_name='Дата запроса')
    Description_of_error = models.TextField(verbose_name='Описание ошибки')
    ID_account = models.ForeignKey(AccountOfUser, on_delete=models.CASCADE,verbose_name='Идентификатор аккаунта')

    def __str__(self):
        return f"{self.Log_name} - {self.Date_of_request}"


class ListOfFeatures(models.Model):
    ID_list = models.AutoField(primary_key=True, verbose_name='Идентификатор списка')
    Amount_of_in_stock = models.CharField(max_length=20, verbose_name='Количество в наличии')
    Brand = models.CharField(max_length=50, verbose_name='Марка')

    def __str__(self):
        return f"{self.Brand} - {self.Amount_of_in_stock}"


class SetOfItems(models.Model):
    ID_set = models.AutoField(primary_key=True, verbose_name='Идентификатор набора')
    Name_of_set = models.CharField(max_length=50, verbose_name='Имя набора')
    Creation_date = models.DateTimeField(verbose_name='Дата создания')
    Set_style = models.CharField(max_length=50, verbose_name='Категория набора')

    def __str__(self):
        return self.Name_of_set


class Store(models.Model):
    ID_store = models.AutoField(primary_key=True, verbose_name='Идентификатор магазина')
    Store_name = models.CharField(max_length=100, verbose_name='Имя магазина')
    URL = models.URLField(verbose_name='Ссылка')
    Description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.Store_name
