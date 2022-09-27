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
                # models.Index(fields=['slug']),
            ]
    def get_absolute_url(self):
        return f'/category/{self.year}/'




# class ReviewCategory(models.Model):
# 	name = models.CharField(max_length=255)
# 	slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
# 	meta_title = models.CharField(max_length=255, null=True, blank=True)
# 	description = models.TextField()
# 	short_description = models.TextField()
# 	category_image_full = models.ImageField(upload_to='category-images/', null=True, blank=True)
# 	category_image_web = models.ImageField(upload_to='category-web-images/', null=True, blank=True)
# 	category_image_mobile = models.ImageField(upload_to='category-mobile-images/', null=True, blank=True)
# 	icon_image = models.ImageField(upload_to='category-icon-images/', null=True, blank=True)
# 	parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
# 	status = models.CharField(max_length=50, choices=PUBLISH_STATUS, default='Draft')
# 	featured_review = models.CharField(max_length=100, null=True, blank=True)
# 	create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# 	create_at = models.DateTimeField(auto_now_add=True)
# 	update_at = models.DateTimeField(auto_now=True)

# 	def __str__(self):
# 		return str(self.name)

# 	def save(self, *args, **kwargs):
# 		if self.category_image_full:
# 			self.category_image_mobile = resize_image(self.category_image_full, (97, 52))
# 			self.category_image_web = resize_image(self.category_image_full, (432, 239))
# 		super().save(*args, *kwargs)

# 	def get_absolute_url(self):
# 		return f'/category/{self.slug}/'


# 	class Meta:
# 		db_table = "review_category"
# 		verbose_name = "Review category"
# 		verbose_name_plural = "Review categories"
# 		indexes = [
# 			models.Index(fields=['id']),
# 			models.Index(fields=['name']),
# 			models.Index(fields=['slug']),
# 		]





        

class BikeClass(models.Model):
    bike_class = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bike_class)

    class Meta:
	    db_table = "bike_class_changes"

class FrameType(models.Model):
    frame_type = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.frame_type)

    class Meta:
	    db_table = "frame_type_changes"


class WheelSize(models.Model):
    wheel_size = models.FloatField(null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.wheel_size)

    class Meta:
	    db_table = "wheel_size_changes"


class BreakType(models.Model):
    break_type = models.CharField(max_length=255, null=True, blank=True)

    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.break_type)

    class Meta:
	    db_table = "break_type_changes"