import django_tables2 as tables
from .models import Person
from django_tables2.utils import A


class PersonTable(tables.Table):

    #name = tables.Column(accessor="full_name") #добавляет колонну со значением столбца Person.full_name
    #population = tables.Column(footer="hello") #вставляет вниз столбца указанный текст
    #selection = tables.CheckBoxColumn(accessor="pk", orderable=False) #создает колонну чекбоксов
    buttons = tables.TemplateColumn("""<div style="text-align: center">
                        <button hx-get="edit/{{person.object.id}}" hx-target="#dialog" class="btn btn-sm btn-white btn-svg" type="button" data-bs-toggle="modal" data-bs-target="#user-form-modal">Edit</button>
                        <button hx-get="delete/{{model.object.id}}" hx-target="#dialog" class="btn btn-sm btn-white btn-svg" type="button"><svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"></path><path d="M8 9h8v10H8z" opacity=".3"></path><path d="M15.5 4l-1-1h-5l-1 1H5v2h14V4zM6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9z"></path></svg></button>
                    </div>""")

    #def render_id_provider(self, **kwargs):
        #return kwargs['value'].id

    class Meta:
        attrs = {"class": "table table-striped table-bordered text-nowrap", "a" : { "class": "btn btn-secondary"}}#задать стиль CSS
        model = Person
        #template_name = "django_tables2/bootstrap.html"
        sequence = ("id", "full_name", "phone_number", "comment", "phone_type") #последовательность столбцов
        fields = ("id", "full_name", "phone_number", "comment", "phone_type") #какие поля показывать


#<a href="/schedule/update_schedule/{{ record.id }}">Update</a> / Cancel / Event /
#<a href="/schedule/delete_schedule/{{ record.id }}"
#onclick="return confirm('Are you sure you want to delete this?')">Delete</a>