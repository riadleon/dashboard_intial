from django.db import models

class ParsedOutput(models.Model):
    url = models.TextField()
    title = models.TextField()
    favicon = models.TextField()
    locale = models.TextField()
    type = models.TextField()
    names = models.TextField()  
    emails = models.TextField()  # Similar to names
    phone_numbers = models.TextField()  # Similar to names
    ip_address = models.TextField()
    location = models.TextField()
    keywords = models.TextField()

    class Meta:
        db_table = "parsed_output_table"

class DirtySEOMetadata(models.Model):
    dirty_seo_metadata = models.TextField()
    language = models.TextField()

    class Meta:
        db_table = "dirty_seo_metadata"

class CleanList(models.Model):
    keyword = models.TextField(unique=True)
    language = models.TextField()

    class Meta:
        db_table = "cleanlist"