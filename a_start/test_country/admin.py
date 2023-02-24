from django.contrib import admin

from .models import For_teacher


class For_teacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'course', 'college', 'subject', 'delivery_time', 'count')
    list_display_links = ('id', 'name', 'surname')
    search_fields = ('id', 'name')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'count')
#     list_display_links = ('id', 'name',)
#     search_fields = ('id',) # всегда остовлять запятую если один обьект так как это картеж


admin.site.register(For_teacher, For_teacherAdmin)
# admin.site.register(Category, CategoryAdmin)
