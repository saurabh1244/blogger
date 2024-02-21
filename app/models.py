from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class post(models.Model):
    title = models.CharField(max_length=255)
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

    slugx = AutoSlugField(populate_from='title',unique=True,null=True, default=None)

    date = models.DateField(auto_now_add=True)
    data1 = models.CharField(max_length=255)
    data2 = models.CharField(max_length=255)

    urls = models.TextField(blank=True)
    url_context = models.TextField(blank=True)

    view  = models.TextField(blank=True)
    view_context = models.TextField(blank=True)

    setting = models.TextField(blank=True)
    setting_context = models.TextField(blank=True)

    modelx = models.TextField(blank=True)
    modelx_context = models.TextField(blank=True)

    admin = models.TextField(blank=True)
    admin_context = models.TextField(blank=True)

    html_page1 = models.TextField(blank=True)
    html1_context = models.TextField(blank=True)

    html_page2 = models.TextField(blank=True)
    html2_context = models.TextField(blank=True)
    
    html_page3 = models.TextField(blank=True)
    html3_context = models.TextField(blank=True)



class comments(models.Model):
    cum_id = models.ForeignKey(post ,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
   



    # def get_urls_list(self):
    #     """
    #     Returns a list of URLs from the 'urls' field.
    #     Assumes that URLs are separated by newline characters.
    #     """
    #     if self.urls:
    #         return self.urls.split('\n')
    #     else:
    #         return []
        
    
    # def get_urls_list2(self):
    #     """
    #     Returns a list of URLs from the 'urls' field.
    #     Assumes that URLs are separated by newline characters.
    #     """
    #     if self.setting:
    #         return self.setting.split('\n')
    #     else:
    #         return []
        

    # def get_urls_list3(self):
    #     """
    #     Returns a list of URLs from the 'urls' field.
    #     Assumes that URLs are separated by newline characters.
    #     """
    #     if self.view:
    #         return self.view.split('\n')
    #     else:
    #         return []
        

    # def get_urls_list4(self):
    #     """
    #     Returns a list of URLs from the 'urls' field.
    #     Assumes that URLs are separated by newline characters.
    #     """
    #     if self.modelx:
    #         return self.modelx.split('\n')
    #     else:
    #         return []   


    # def get_urls_list5(self):
    #     """
    #     Returns a list of URLs from the 'urls' field.
    #     Assumes that URLs are separated by newline characters.
    #     """
    #     if self.admin:
    #         return self.admin.split('\n')
    #     else:
    #         return []