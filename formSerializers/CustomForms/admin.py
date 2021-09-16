from django.contrib import admin

from CustomForms.models import CustomForm, Section, Subsection, Widget, Action


class ActionInLineAdmin(admin.StackedInline):
    model = Action
    fk_name = 'fixed_widget'
    fields = ('condition','actions', 'conditional_widget')


class WidgetAdmin(admin.ModelAdmin):
    inlines = [
        ActionInLineAdmin,
    ]


class WidgetInLineAdmin(admin.StackedInline):
    model = Widget


class SubsectionAdmin(admin.ModelAdmin):
    inlines = [
        WidgetInLineAdmin,
    ]

class SubsectionLineAdmin(admin.StackedInline):
    model = Subsection


class SectionAdmin(admin.ModelAdmin):
    inlines = [
        SubsectionLineAdmin,
    ]

class SectionInLineAdmin(admin.StackedInline):
    model = Section


class FormAdmin(admin.ModelAdmin):
    inlines = [
        SectionInLineAdmin,
    ]

class SectionInLineAdmin(admin.StackedInline):
    model = Section


class FormAdmin(admin.ModelAdmin):
    inlines = [
        SectionInLineAdmin,
    ]


admin.site.register(CustomForm, FormAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Widget, WidgetAdmin)