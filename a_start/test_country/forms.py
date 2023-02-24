from .models import *
from django.forms import ModelForm, TextInput, RadioSelect
from django.forms import ModelForm, TextInput, RadioSelect, CheckboxInput
from django.forms import *


class For_teacherForm(ModelForm):
    class Meta:
        model = For_teacher
        fields = ['name',
                  'surname',
                  'course',
                  'college',
                  'subject',
                  'question_1',
                  'question_2',
                  'question_3',
                  'question_4',
                  'question_5',

                  ]
        widgets = {
            'name': TextInput(attrs={'class': 'rounded mt-3 container form-control', 'placeholder': 'введите имя'}),
            'surname': TextInput(attrs={'class': 'rounded mt-3 container form-control', 'placeholder': 'введите фамилию'}),
            'course': TextInput(attrs={'class': 'rounded mt-3 container form-control', 'placeholder': 'введите курс'}),
            'college': TextInput(attrs={'class': 'rounded mt-3 container form-control', 'placeholder': 'введите колледж'}),
            'subject': TextInput(attrs={'class': 'rounded mt-3 container form-control', 'placeholder': 'введите предмет', 'value': 'France'}),
            'question_1': RadioSelect(choices=[(True, ' «Свобода, Равенство, Братство»'), (False, '«Свобода, Единство, Величие»'), (False, '«Свобода, Возможности, Счастье»')]),
            'question_2': RadioSelect(choices=[(False, ' Клёна и вишни'), (True, 'Дуба и оливы'), (False, 'Ивы и вьюна')]),
            'question_3': RadioSelect(choices=[(False, ' Нор — Па-де-Кале'), (True, ' Иль-де-Франс'), (False, 'Пеи-де-ла-Луар')]),
            'question_4': RadioSelect(choices=[(False, ' Произошло от слова «францизм»'), (False, ' Название страны произошло от немецкого имени Франц, которое означало «свободный, смелый»'), (True, ' Название страны произошло от сочетания «земля франков»')]),
            'question_5': RadioSelect(choices=[(True, ' Галльский петух'), (False, ' Ястребиный орёл'), (False, ' Сокол-сапсан')]),
        }
