from rest_framework import serializers

from CustomForms.models import CustomForm, Section, Subsection, Widget, Action


#Filtrar que no sean fixed_widget
#Resolver el problema recursivo
class ActionSerializer(serializers.ModelSerializer):
    conditional_widget = serializers.SerializerMethodField()

    def get_conditional_widget(self, widget):

        if widget is not None:
            return WidgetSerializer(widget.conditional_widget).data

    class Meta:
        model = Action
        fields = ('id', 'condition', 'actions', 'conditional_widget')


class WidgetSerializer(serializers.ModelSerializer):
    variable_widgets = ActionSerializer(many=True)

    class Meta:
        model = Widget
        fields = ['id', 'name', 'widget_type', 'input', 'required', 'visible', 'validators', 'props_css', 'variable_widgets']


class SubsectionSerializer(serializers.ModelSerializer):
    fields = WidgetSerializer(many=True)

    class Meta:
        model = Subsection
        fields = ('id', 'section', 'name', 'fields')


class SectionSerializer(serializers.ModelSerializer):
    subsections = SubsectionSerializer(many=True)

    class Meta:
        model = Section
        fields = ('id', 'form', 'name', 'subsections')


class CustomFormSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = CustomForm
        fields = ('id', 'name', 'status', 'sections')