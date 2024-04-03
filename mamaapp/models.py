from django.db import models

# Create your models here.
class Contact_US(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    message = models.TextField()


class SwiperContent(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    heading = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=255)

class MamamiaContent(models.Model):
    heading = models.CharField(max_length=255)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    link_text = models.CharField(max_length=255)
    link_url = models.URLField()
    image = models.ImageField(upload_to='mamamia_images/')

class MamamiaSection(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255)
    button_url = models.URLField()
    image = models.ImageField(upload_to='mamamia_images/')


class MamamiaItem(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()


class mamamiaService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/')

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')


class Location_section(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')


class AssociateImage(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')

    def __str__(self):
        return self.image.name


class HiringInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/',default='1')

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mamamia_images/')

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    heading = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.heading


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    name = models.CharField(max_length=255,default='none')

    def _str_(self):
        return self.image.name 


class MamamiaServices_egg_donor(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255)
    button_url = models.URLField()
    image = models.ImageField(upload_to='mamamia_images/')


class MamamiaServices_sperm_donor(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255)
    button_url = models.URLField()
    image = models.ImageField(upload_to='mamamia_images/')


class MamamiaServices_surrogacyr(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255)
    button_url = models.URLField()
    image = models.ImageField(upload_to='mamamia_images/')


class surrogacy_opening_content(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/')

class SurrogateRequirement(models.Model):
    description = models.CharField(max_length=255)

class SurrogateSection(models.Model):
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    other_content = models.TextField(default='1')


class EligibilityCriterion(models.Model):
    description = models.CharField(max_length=255)

class Guidlines(models.Model):
    description = models.CharField(max_length=255)

class eligiblity_guildnes_Section(models.Model):
    heading = models.CharField(max_length=100)
    paragraph1 = models.TextField(default='1')
    paragraph2 = models.TextField(default='1')
    other_content = models.TextField()


class Question_anser(models.Model):
    heading1 = models.CharField(max_length=100)
    paragraph1 = models.TextField(default='1')
    heading2 = models.CharField(max_length=100)
    paragraph2 = models.TextField()


class sperm_donor_opening_content(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/')

class SpermEligibility(models.Model):
    description = models.CharField(max_length=255)


class Sperm_eligible_Section(models.Model):
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    other_content = models.TextField(default='1')


class FAQs(models.Model):
    image = models.ImageField(upload_to='mamamia_images/',default='1')


class sperm_guidlines(models.Model):
      description = models.CharField(max_length=255)


class sperm_guidlines_opening_content(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/')


class Sperm_donor_Final(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()



class Egg_Donor_opening(models.Model):
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='mamamia_images/')


class egg_eligibility(models.Model):
      description = models.CharField(max_length=255)

class egg_steps(models.Model):
      heading = models.CharField(max_length=255)
      paragraph = models.TextField()

    
class egg_donors_helpful(models.Model):
      description = models.CharField(max_length=255)


class egg_donor_image(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')


class Aboutus(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, default='Default Button Text')
    button_url = models.URLField(blank=True, default='https://example.com')
    def __str__(self):
        return self.heading


class Aboutus_people(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, default='Default Button Text')
    button_url = models.URLField(blank=True, default='https://example.com')
    def __str__(self):
        return self.heading

class Aboutus_associates(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, default='Default Button Text')
    button_url = models.URLField(blank=True, default='https://example.com')
    def __str__(self):
        return self.heading
    

class why(models.Model):
    image = models.ImageField(upload_to='mamamia_images/')
    heading = models.CharField(max_length=100)
    heading1 = models.CharField(max_length=100)
    heading2 = models.CharField(max_length=100)
    heading3 = models.CharField(max_length=100)
    paragraph = models.TextField()
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3  = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, default='Default Button Text')
    button_url = models.URLField(blank=True, default='https://example.com')
    def __str__(self):
        return self.heading

