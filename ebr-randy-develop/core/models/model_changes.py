from django.db import models
# from . import Review

class ModelYear(models.Model):
    year = models.PositiveIntegerField(null=True, blank=True)
    
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.year)
# field_name = models.Field(verbose_name = "name")

    class Meta:
            db_table = "model_year_changes"
            verbose_name = "ModelYear"
            verbose_name_plural = "ModelYear"
            indexes = [
                models.Index(fields=['id']),
                models.Index(fields=['year'])
            ]
    def get_absolute_url(self):
        return f'/category/{self.year}/'
        

class BikeClass(models.Model):
    bike_class = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bike_class)

    class Meta:
            db_table = "bike_class_changes"
            verbose_name = "BikeClass"
            verbose_name_plural = "BikeClass"
            indexes = [
                models.Index(fields=['id']),
                models.Index(fields=['bike_class'])
            ]
    def get_absolute_url(self):
        return f'/category/{self.bike_class}/'


class FrameType(models.Model):
    frame_type = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.frame_type)

    # class Meta:
	#     db_table = "frame_type_changes"
    class Meta:
            db_table = "frame_type_changes"
            verbose_name = "FrameType"
            verbose_name_plural = "FrameType"
            indexes = [
                models.Index(fields=['id']),
                models.Index(fields=['frame_type'])
            ]
    def get_absolute_url(self):
        return f'/category/{self.frame_type}/'

class WheelSize(models.Model):
    wheel_size = models.FloatField(null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.wheel_size)

    # class Meta:
	#     db_table = "wheel_size_changes"
    class Meta:
            db_table = "wheel_size_changes"
            verbose_name = "WheelSize"
            verbose_name_plural = "WheelSize"
            indexes = [
                models.Index(fields=['id']),
                models.Index(fields=['wheel_size'])
            ]
    def get_absolute_url(self):
        return f'/category/{self.wheel_size}/'


class BreakType(models.Model):
    break_type = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.break_type)

    # class Meta:
	#     db_table = "break_type_changes"
    class Meta:
            db_table = "break_type_changes"
            verbose_name = "BreakType"
            verbose_name_plural = "BreakType"
            indexes = [
                models.Index(fields=['id']),
                models.Index(fields=['break_type'])
            ]
    def get_absolute_url(self):
        return f'/category/{self.break_type}/'