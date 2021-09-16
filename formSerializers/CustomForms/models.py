from django.db import models


class CustomForm(models.Model):
    STATUS_CHOICES = (
        ('admin', 'Creating form'),
        ('fill', 'Filling form'),
        ('result', 'Form results')
    )
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)


class Section(models.Model):
    form = models.ForeignKey(CustomForm, related_name='sections', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)


class Subsection(models.Model):
    section = models.ForeignKey(Section, related_name='subsections', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)


class Widget(models.Model):
    WIDGET_TYPES = (
        ('text', "Text Widget"),
        ('number', "Number Widget"),
        ('email', "Email Widget"),
        ('password', "Password Widget"),
        ('checkbox', "Checkbox Widget"),
    )

    subsection = models.ForeignKey(Subsection, related_name="fields", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    label = models.CharField(max_length=40)
    widget_type = models.CharField(max_length=10, choices=WIDGET_TYPES)
    input = models.CharField(max_length=300, blank=True, null=True)
    required = models.BooleanField()
    visible = models.BooleanField()
    validators = models.JSONField(blank=True, null=True)
    props_css = models.CharField(max_length=300, blank=True, null=True)


class Action(models.Model):
    condition = models.JSONField(blank=True, null=True)
    actions = models.JSONField(blank=True, null=True)
    fixed_widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    conditional_widget = models.ForeignKey(Widget, on_delete=models.CASCADE, related_name="variable_widgets")