from django.db import models


class For_teacher(models.Model):
    name = models.CharField('имя', max_length=100)
    surname = models.CharField('фамилия', max_length=200)
    course = models.CharField('курс', max_length=200)
    college = models.CharField('колледж', max_length=500)
    subject = models.CharField('предмет', max_length=1000) # в дальнейшем рассматривается добавление категорий через класс кат
    delivery_time = models.DateTimeField('время сдачи', auto_now_add=True) #, verbose_name='norm time'
    question_1 = models.BooleanField('вопрос_1', default=False)
    question_2 = models.BooleanField('вопрос_2', default=False)
    question_3 = models.BooleanField('вопрос_3', default=False)
    question_4 = models.BooleanField('вопрос_4', default=False)
    question_5 = models.BooleanField('вопрос_5', default=False)
    count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.count = (self.question_1 + self.question_2 + self.question_3 + self.question_4 + self.question_5)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        # ordering = ['id']




