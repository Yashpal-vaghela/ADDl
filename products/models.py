from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Author(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    insta = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="SEO", null=True)

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete= models.CASCADE)
    h1 = models.CharField(blank=True, null=True, max_length=100)
    meta_title = models.CharField(max_length=160)
    meta_description = models.TextField()
    slug = models.SlugField(unique=True)
    canonical = models.CharField(max_length=180, default="https://acedigitaldentallaboratory.com/product/")

    main_heading = models.CharField(max_length=255)
    intro_descrption = models.TextField()

    product_video_link = models.URLField(blank=True, null=True, help_text="add video link here")
    cta_video = models.FileField(blank=True, null=True, upload_to="videos") 
    product_image = models.ImageField(blank=True, null=True, upload_to="product")
    product_image_alt = models.CharField(blank=True, null=True)

    why_heading = models.CharField(max_length=255, blank=True, null=True)
    why_description = models.TextField(blank=True, null=True)

    commitment_heading = models.CharField(max_length=255, blank=True, null=True)
    commitment_description = models.TextField(blank=True, null=True)
    
    sub_product_title = models.CharField(max_length=255, blank=True, null=True)
    sub_product_description = models.TextField(blank=True, null=True)

    cta_heading = models.CharField(max_length=255, blank=True, null=True)
    cta_description = models.TextField(blank=True, null=True)
    cta_btn_name = models.CharField(max_length=180,blank=True,null=True)
    schema = models.TextField( blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product_image_alt and self.why_heading:
            self.product_image_alt = self.why_heading
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} – {self.meta_title}"
    
class SubProduct(models.Model):
    product = models.ForeignKey(Product, related_name="subproducts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="sub-product-image")

    def __str__(self):
        return f"{self.title} ({self.product.category.name})"
    
class Advantage(models.Model):
    product = models.ForeignKey(Product, related_name="Advantage", on_delete=models.CASCADE)
    title = models.CharField(blank=True, null=True, max_length=160)
    point = models.TextField(help_text="Add Benefite")
    
    def __str__(self):
        return f"Why: {self.point[:50]}... ({self.product.category.name})"
    
class CommitmentPoint(models.Model):
    product = models.ForeignKey(Product, related_name="commitment_points", on_delete=models.CASCADE)
    point = models.TextField(help_text="Add commiments")
    point_image = models.FileField(blank=True, null=True, upload_to="commitment", help_text="upload your image here")

    def __str__(self):
        return f"Commitment: {self.point[:50]}... ({self.product.category.name})"

class Blogs(models.Model):
    H1 = models.CharField(blank=True, null=True, max_length=100)
    meta_title = models.CharField(blank=True, null=True, max_length=180)
    slug = models.SlugField()
    meta_description = models.TextField(unique=True)
    canonical = models.CharField(max_length=180, default="https://acedigitaldentallaboratory.com/blog/")
    category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog-image")
    alt = models.CharField(blank=True, null=True, max_length=180)
    content = RichTextUploadingField()
    schema = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="blogs")

    def save(self, *args, **kwargs):
    # Auto fill alt with meta_title only
        if not self.alt and self.meta_title:
            self.alt = self.meta_title
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.H1 if self.H1 else self.meta_title

class BlogCategory(models.Model):
    H1 = models.CharField(blank=True, null=True, max_length=100)
    meta_title = models.CharField(blank=True, null=True, max_length=180)
    meta_description = models.TextField()
    breadcrumb = models.CharField(blank=True, null=True, max_length=100)
    canonical = models.CharField(max_length=180, default="https://acedigitaldentallaboratory.com/category/")
    name = models.CharField(blank=True, null=True, max_length=100)
    slug = models.SlugField()
    image = models.ImageField(blank=True, null=True, upload_to="SEO")
    alt = models.CharField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto fill alt with name if empty
        if not self.alt and self.name:
            self.alt = self.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.slug

class Review(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.name
    

        