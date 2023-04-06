from django.contrib import admin

from training.models import TrainingDefinition, Training

# Register your models here.
@admin.register(TrainingDefinition)
class TrainingDefinitionAdmin(admin.ModelAdmin):
    list_display = ("trainingName","preparedTraining","preparationDate",)    
    search_fields = ("trainingName","preparedTraining")

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):       
    search_fields = ("projectName","trainingName")
    list_display = ("projectName","trainingName","providingTraining","trainingStatus","trainingStartDate","trainingEndDate")
    