from django.db import models

class Advertisement(models.Model): #абстрактный класс(модель)
    
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    class Meta: 
        db_table = 'advertisements'