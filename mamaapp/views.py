from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail



# Create your views here.

def index(request):
    swiper_contents = SwiperContent.objects.all()
    mamamia_content = MamamiaContent.objects.first()
    mamamia_section = MamamiaSection.objects.first()
    mamamia_items  =  MamamiaItem.objects.all()
    services = mamamiaService.objects.all()
    sections = AboutSection.objects.first()
    locations = Location_section.objects.first()
    associates = AssociateImage.objects.all()
    hiring_info = HiringInfo.objects.first()
    testimonials = Testimonial.objects.all()
    team_members  = TeamMember.objects.all()
    return render(request,'index.html',{
        'swiper_contents':swiper_contents,
        'mamamia_content':mamamia_content,
        'mamamia_section':mamamia_section,
        'mamamia_items':mamamia_items,
        'services':services,
        'sections':sections,
        'locations':locations,
        'associates':associates,
        'hiring_info':hiring_info,
        'testimonials':testimonials,
        'team_members':team_members,})


def about_us(request):
    content = Aboutus.objects.first()
    people = Aboutus_people.objects.first()
    assoc = Aboutus_associates.objects.first()
    return render(request,'about_us_page.html',{'content':content,'people':people,'assoc':assoc})


def services(request):
    egg_donor = MamamiaServices_egg_donor.objects.first()
    sperm_donor = MamamiaServices_sperm_donor.objects.first()
    surogacy = MamamiaServices_surrogacyr.objects.first()
    return render (request,'services.html',{'egg_donor':egg_donor,'sperm_donor':sperm_donor,'surogacy':surogacy})


def contact_us(request):
    return render(request,'contact_us.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request,'gallery.html',{'images':images})

def why_mamamia(request):
    whym = why.objects.first()
    return render(request,'why_mamamia.html',{'whym':whym})

def egg_donor(request):
    egg_opening = Egg_Donor_opening.objects.first()
    egg_elig = egg_eligibility.objects.all()
    egg_step = egg_steps.objects.all()
    egg_help = egg_donors_helpful.objects.all()
    egg_image = egg_donor_image.objects.first()
    return render(request,'egg_donor.html',{'egg_opening':egg_opening,'egg_elig':egg_elig,'egg_step':egg_step,'egg_help':egg_help,'egg_image':egg_image})

def sperm_donor(request):
    sperm = sperm_donor_opening_content.objects.first()
    sperm_eligible = SpermEligibility.objects.all()
    sperm_contents = Sperm_eligible_Section.objects.first()
    faqs = FAQs.objects.first()
    sperm_guide = sperm_guidlines.objects.all()
    sperm_section = sperm_guidlines_opening_content.objects.first()
    sperm_finals = Sperm_donor_Final.objects.first()
    return render(request,'sperm_donor.html',{'sperm':sperm,'sperm_eligible':sperm_eligible,'sperm_contents':sperm_contents,'faqs':faqs,'sperm_guide':sperm_guide,'sperm_section':sperm_section,'sperm_finals':sperm_finals})

def surrogacy_program(request):
    surogacy = surrogacy_opening_content.objects.first()
    requirements = SurrogateRequirement.objects.all()
    section = SurrogateSection.objects.first()
    criteria = EligibilityCriterion.objects.all()
    guide = Guidlines.objects.all()
    eligy_guide = eligiblity_guildnes_Section.objects.first()
    qa_section = Question_anser.objects.first()
    return render(request,'surrogacy.html',{'surogacy':surogacy,'requirements':requirements,'section':section,'criteria':criteria,'guide':guide,'eligy_guide':eligy_guide,'qa_section':qa_section})

def our_team(request):
    team_members  = TeamMember.objects.all()
    return render(request,'our_team.html',{'team_members':team_members})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request,'blog.html',{'blog_posts':blog_posts})


def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_post_detail.html', {'post': post})


def contact_page_submit(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Save the contact form data to the database
        contact = Contact_US.objects.create(
            name=name,
            email=email,
            phone_no=phone,
            message=message
        )
        contact.save()

        # Send email to the admin
        subject = f"Messages From The Website"
        message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        sender_email = 'mamamialifesolutions@gmail.com'  # Update with a valid sender email address
        admin_email = 'amald416@gmail.com'  # Admin email address

        send_mail(
            subject,
            message_body,
            sender_email,
            [admin_email],
            fail_silently=False,
        )

        messages.info(request, 'We will get back to you soon')
        return redirect('contact_us')

    

def contact_page_submit_index(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact_US.objects.create(
            name=name,
            email=email,
            phone_no=phone,
            message=message
        )
        contact.save()
        messages.info(request,'We will get you soon')
        return redirect('index')

@login_required(login_url='signin')
def admin_page(request):
    return render(request,'admin.html')


def login_page(request):
    return render(request,'login.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_page')
        else:
            messages.error(request, 'Invalid credentials or you do not have admin access.')
            return redirect('login_page')

    return redirect('login_page')


def our_associates(request):
    images = AssociateImage.objects.all()
    return render(request,'our_associates.html',{'images':images})


def setnewpassword(request):

    if request.method=='POST':
        email_or_username = request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:

            c = User.objects.filter(Q(username = email_or_username)|Q(email = email_or_username)).first()
            c.set_password(password)
            c.save()

        return redirect('login_page' )
    return render(request,'setpassword.html')


def logout(request):
	auth.logout(request)
	return redirect('index')


def contact_page_submit_why(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact_US.objects.create(
            name=name,
            email=email,
            phone_no=phone,
            message=message

        )
        contact.save()
        messages.info(request,'We will get you soon')
        return redirect('why_mamamia')
    
def home_page_contents(request):
    return render(request,'home_page_contents.html')

def swiper_view(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        
        

        # Save the data to the database
        swiper_content = SwiperContent.objects.create(
            image=image,
            heading=heading,
            paragraph=paragraph
            
        )
        swiper_content.save()

        # Redirect or do other actions after saving
        return redirect('swiper_view')  # Replace 'success_page' with your actual success page URL

    swiper_contents = SwiperContent.objects.all()
    return render(request, 'add_slider_contents.html', {'swiper_contents': swiper_contents})


def delete_portfolio_content(request, portfolio_id):
    content = get_object_or_404(SwiperContent, id=portfolio_id)
    content.delete()
    return redirect('swiper_view')


def edit_swiper_contents(request, content_id):
    content = get_object_or_404(SwiperContent, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
       
        
        content.save()

        return redirect('swiper_view')  # Redirect to the Swiper view after editing

    return render(request, 'edit_swiper_content.html', {'content': content})


def opening_view(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph_1 = request.POST['paragraph_1']
        paragraph_2 = request.POST['paragraph_2']
        link = request.POST['link']
        url= request.POST['url']
        
        
        

        # Save the data to the database
        opening_content = MamamiaContent.objects.create(
            image=image,
            heading=heading,
            paragraph1=paragraph_1,
            paragraph2=paragraph_2,
            link_text=link,
            link_url=url
            
        )
        opening_content.save()

        # Redirect or do other actions after saving
        return redirect('opening_view')  # Replace 'success_page' with your actual success page URL

    opening_contents = MamamiaContent.objects.all()
    return render(request, 'add_opening_section.html', {'opening_contents': opening_contents})


def delete_opening_content(request, opening_id):
    content = get_object_or_404(MamamiaContent, id=opening_id)
    content.delete()
    return redirect('opening_view')


def edit_opening_contents(request, content_id):
    content = get_object_or_404(MamamiaContent, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph_1 = request.POST.get('paragraph_1',content.paragraph1)
        paragraph_2 = request.POST.get('paragraph_2',content.paragraph2)
        link_text = request.POST.get('link_text',content.link_text)
        link_url = request.POST.get('link_url',content.link_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph1 = paragraph_1
        content.paragraph2 = paragraph_2
        content.link_text = link_text
        content.link_url = link_url
       
        
        content.save()

        return redirect('opening_view')  # Redirect to the Swiper view after editing

    return render(request, 'edit_opening_content.html', {'content': content})


def mamamia_view(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        
# Save the data to the database
        opening_content = MamamiaSection.objects.create(
            image=image,
            heading=heading,
            paragraph=paragraph,
            button_text=button_text,
            button_url=button_url
            
            
        )
        opening_content.save()

        # Redirect or do other actions after saving
        return redirect('mamamia_view')  # Replace 'success_page' with your actual success page URL

    mamamia_contents = MamamiaSection.objects.all()
    return render(request, 'add_mamamia_section.html', {'mamamia_contents': mamamia_contents})


def delete_mamamia_content(request, opening_id):
    content = get_object_or_404(MamamiaSection, id=opening_id)
    content.delete()
    return redirect('mamamia_view')



def edit_mamamia_contents(request, content_id):
    content = get_object_or_404(MamamiaSection, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('mamamia_view')  # Redirect to the Swiper view after editing

    return render(request, 'edit_mamamia_content.html', {'content': content})


def mamamia_item(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
       
        title = request.POST['title']
        content = request.POST['content']

        
        
# Save the data to the database
        item_content = MamamiaItem.objects.create(
            title=title,
            content=content,

            
            
        )
        item_content.save()

        # Redirect or do other actions after saving
        return redirect('mamamia_item')  # Replace 'success_page' with your actual success page URL

    mamamia_items = MamamiaItem.objects.all()
    return render(request, 'add_mamamia_item.html', {'mamamia_items': mamamia_items})


def delete_mamamia_items(request, opening_id):
    content = get_object_or_404(MamamiaItem, id=opening_id)
    content.delete()
    return redirect('mamamia_item')



def edit_mamamia_items(request, content_id):
    contents = get_object_or_404(MamamiaItem, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        
        title = request.POST.get('title',contents.title)
        content = request.POST.get('content',contents.content)
        
        
        
       

        # Update the SwiperContent instance with the new data
        
        contents.title = title
        contents.content = content
        

       
        
        contents.save()

        return redirect('mamamia_item')  # Redirect to the Swiper view after editing

    return render(request, 'edit_mamamia_item.html', {'contents': contents})



def mamamia_services(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = mamamiaService.objects.create(
            title=title,
            description=description,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_services')  # Replace 'success_page' with your actual success page URL

    mamamia_services = mamamiaService.objects.all()
    return render(request, 'add_mamamia_services.html', {'mamamia_services': mamamia_services})




def delete_mamamia_services(request, opening_id):
    content = get_object_or_404(mamamiaService, id=opening_id)
    content.delete()
    return redirect('mamamia_services')



def edit_mamamia_service(request, service_id):
    
    service = get_object_or_404(mamamiaService, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

       
        service.title = title
        service.description = description
        if image:
            service.image = image

        
        service.save()

        return redirect('mamamia_services')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_mamamia_service.html', {'service': service})
    

def mamamia_aboutus(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = AboutSection.objects.create(
            title=title,
            description=description,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_aboutus')  # Replace 'success_page' with your actual success page URL

    mamamia_aboutus = AboutSection.objects.all()
    return render(request, 'add_mamamia_aboutus.html', {'mamamia_aboutus': mamamia_aboutus})


def delete_mamamia_aboout_us(request, opening_id):
    content = get_object_or_404(AboutSection, id=opening_id)
    content.delete()
    return redirect('mamamia_aboutus')


def edit_mamamia_aboutus(request, service_id):
    
    service = get_object_or_404(AboutSection, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

       
        service.title = title
        service.description = description
        if image:
            service.image = image

        
        service.save()

        return redirect('mamamia_aboutus')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_mamamia_aboutus.html', {'service': service})
    

def mamamia_locations(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = Location_section.objects.create(
            title=title,
            description=description,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_locations')  # Replace 'success_page' with your actual success page URL

    mamamia_locations = Location_section.objects.all()
    return render(request, 'add_mamamia_locations.html', {'mamamia_locations': mamamia_locations})


def delete_mamamia_locations(request, opening_id):
    content = get_object_or_404(Location_section, id=opening_id)
    content.delete()
    return redirect('mamamia_locations')



def edit_mamamia_locations(request, service_id):
    
    service = get_object_or_404(Location_section, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

       
        service.title = title
        service.description = description
        if image:
            service.image = image

        
        service.save()

        return redirect('mamamia_locations')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_mamamia_locations.html', {'service': service})



def add_associates(request):
    if request.method == 'POST':

        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = AssociateImage.objects.create(

            image=image
        )
        # Redirect or do other actions after saving
        return redirect('add_associates')  # Replace 'success_page' with your actual success page URL

    associates_images = AssociateImage.objects.all()
    return render(request, 'add_associates.html', {'associates_images': associates_images})




def delete_associate_image(request, opening_id):
    content = get_object_or_404(AssociateImage, id=opening_id)
    content.delete()
    return redirect('add_associates')




def edit_associates_image(request, service_id):
    
    service = get_object_or_404(AssociateImage, pk=service_id)

    if request.method == 'POST':
        

        image = request.FILES.get('image')  

       

        if image:
            service.image = image

        
        service.save()

        return redirect('add_associates')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_associates.html', {'service': service})
    


def mamamia_jumbotron(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = HiringInfo.objects.create(
            title=title,
            description=description,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_jumbotron')  # Replace 'success_page' with your actual success page URL

    mamamia_jumbo = HiringInfo.objects.all()
    return render(request, 'add_mamamia_jumbotron.html', {'mamamia_jumbo': mamamia_jumbo})



def delete_associate_jumpo(request, opening_id):
    content = get_object_or_404(HiringInfo, id=opening_id)
    content.delete()
    return redirect('mamamia_jumbotron')


def edit_mamamia_jumbo(request, service_id):
    
    service = get_object_or_404(HiringInfo, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

       
        service.title = title
        service.description = description
        if image:
            service.image = image

        
        service.save()

        return redirect('mamamia_jumbotron')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_mamamia_jumpo.html', {'service': service})
    

def mamamia_testimonials(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        

        
        # Save the data to the database
        service_content = Testimonial.objects.create(
            content=description,
            author=title,
            
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_testimonials')  # Replace 'success_page' with your actual success page URL

    mamamia_testimonials = Testimonial.objects.all()
    return render(request, 'add_mamamia_testimonials.html', {'mamamia_testimonials': mamamia_testimonials})



def delete_testimonials(request, opening_id):
    content = get_object_or_404(Testimonial, id=opening_id)
    content.delete()
    return redirect('mamamia_testimonials')



def edit_testimonials(request, service_id):
    
    service = get_object_or_404(Testimonial, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        

       
        service.author = title
        service.content = description


        
        service.save()

        return redirect('mamamia_testimonials')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_testimonials.html', {'service': service})



def mamamia_teams(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('title')
        positions = request.POST.get('description')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = TeamMember.objects.create(
            name=name,
            position=positions,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('mamamia_teams')  # Replace 'success_page' with your actual success page URL

    mamamia_team = TeamMember.objects.all()
    return render(request, 'add_mamamia_teams.html', {'mamamia_team': mamamia_team})



def delete_teams(request, opening_id):
    content = get_object_or_404(TeamMember, id=opening_id)
    content.delete()
    return redirect('mamamia_teams')



def edit_teams(request, service_id):
    
    service = get_object_or_404(TeamMember, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  
        

       
        service.name = title
        service.position = description
        if image:
           service.image = image


        
        service.save()

        return redirect('mamamia_teams')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_teams.html', {'service': service})


def admin_contacts(request):
    contact_details = Contact_US.objects.all()
    reversed_order = reversed(list(contact_details))
    return render(request,'admin_contacts.html',{'contact_details':reversed_order})


def delete_contacts(request, opening_id):
    content = get_object_or_404(Contact_US, id=opening_id)
    content.delete()
    return redirect('admin_contacts')


def mamamia_blogs(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = BlogPost.objects.create(
            heading=title,
            
            image=image,
            content=description,
            author=author

        )
        # Redirect or do other actions after saving
        return redirect('mamamia_blogs')  # Replace 'success_page' with your actual success page URL

    mamamia_blog = BlogPost.objects.all()
    return render(request, 'add_mamamia_blogs.html', {'mamamia_blogs': mamamia_blog})


def delete_blogs(request, opening_id):
    content = get_object_or_404(BlogPost, id=opening_id)
    content.delete()
    return redirect('mamamia_blogs')


def edit_blogs(request, service_id):
    
    service = get_object_or_404(BlogPost, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        image = request.FILES.get('image')  
        

       
        service.heading = title
        service.content = description
        service.author = author
        if image:
           service.image = image


        
        service.save()

        return redirect('mamamia_blogs')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_blogs.html', {'service': service})



def add_images(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = GalleryImage.objects.create(

            image=image,
            name=name
        )
        # Redirect or do other actions after saving
        return redirect('add_images')  # Replace 'success_page' with your actual success page URL

    add_images = GalleryImage.objects.all()
    return render(request, 'add_gallery_img.html', {'add_images': add_images})




def delete_gallery_image(request, opening_id):
    content = get_object_or_404(GalleryImage, id=opening_id)
    content.delete()
    return redirect('add_images')


def service_page_contents(request):
    return render(request,'service_page_contents.html')


def mamamia_egg_donor(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        
# Save the data to the database
        opening_content = MamamiaServices_egg_donor.objects.create(
            image=image,
            heading=heading,
            paragraph=paragraph,
            button_text=button_text,
            button_url=button_url
            
            
        )
        opening_content.save()

        # Redirect or do other actions after saving
        return redirect('mamamia_egg_donor')  # Replace 'success_page' with your actual success page URL

    mamamia_egg_donor = MamamiaServices_egg_donor.objects.all()
    return render(request, 'add_eggdonor_section.html', {'mamamia_egg_donor': mamamia_egg_donor})


def delete_egg_donor_section(request, opening_id):
    content = get_object_or_404(MamamiaServices_egg_donor, id=opening_id)
    content.delete()
    return redirect('mamamia_egg_donor')


def edit_eggdonor_contents(request, content_id):
    content = get_object_or_404(MamamiaServices_egg_donor, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('mamamia_egg_donor')  # Redirect to the Swiper view after editing

    return render(request, 'edit_eggdonor_sections.html', {'content': content})


def mamamia_sperm_donor(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        
# Save the data to the database
        opening_content = MamamiaServices_sperm_donor.objects.create(
            image=image,
            heading=heading,
            paragraph=paragraph,
            button_text=button_text,
            button_url=button_url
            
            
        )
        opening_content.save()

        # Redirect or do other actions after saving
        return redirect('mamamia_sperm_donor')  # Replace 'success_page' with your actual success page URL

    mamamia_sperm_donor = MamamiaServices_sperm_donor.objects.all()
    return render(request, 'add_spermdonor_section.html', {'mamamia_sperm_donor': mamamia_sperm_donor})



def delete_sperm_donor_section(request, opening_id):
    content = get_object_or_404(MamamiaServices_sperm_donor, id=opening_id)
    content.delete()
    return redirect('mamamia_sperm_donor')



def edit_spermdonor_contents(request, content_id):
    content = get_object_or_404(MamamiaServices_sperm_donor, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('mamamia_sperm_donor')  # Redirect to the Swiper view after editing

    return render(request, 'edit_sperm_sections.html', {'content': content})



def mamamia_surrogacy_section(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        
# Save the data to the database
        opening_content = MamamiaServices_surrogacyr.objects.create(
            image=image,
            heading=heading,
            paragraph=paragraph,
            button_text=button_text,
            button_url=button_url
            
            
        )
        opening_content.save()

        # Redirect or do other actions after saving
        return redirect('mamamia_surrogacy_section')  # Replace 'success_page' with your actual success page URL

    mamamia_surrogacy = MamamiaServices_surrogacyr.objects.all()
    return render(request, 'add_surrogacy_section.html', {'mamamia_surrogacy': mamamia_surrogacy})


def delete_surrogacy_section(request, opening_id):
    content = get_object_or_404(MamamiaServices_surrogacyr, id=opening_id)
    content.delete()
    return redirect('mamamia_surrogacy_section')


def edit_surrogacy_contents(request, content_id):
    content = get_object_or_404(MamamiaServices_surrogacyr, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('mamamia_surrogacy_section')  # Redirect to the Swiper view after editing

    return render(request, 'edit_surrogacy_sections.html', {'content': content})



def surrogacy_pge(request):
    return render(request,'surrogacy_service_contents.html')


def surrogacy_opening_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = surrogacy_opening_content.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('surrogacy_opening_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_surrogacy = surrogacy_opening_content.objects.all()
    return render(request, 'add_surrogacy_services.html', {'mamamia_surrogacy': mamamia_surrogacy})


def delete_surrogacy_services(request, opening_id):
    content = get_object_or_404(surrogacy_opening_content, id=opening_id)
    content.delete()
    return redirect('surrogacy_opening_contents')


def edit_surrogcy_services(request, service_id):
    
    service = get_object_or_404(surrogacy_opening_content, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')  
        

       
        service.heading = heading
        service.paragraph = paragraph
        if image:
           service.image = image


        
        service.save()

        return redirect('surrogacy_opening_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_surrogcy_services.html', {'service': service})


def add_requirment_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = SurrogateRequirement.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_requirment_list')
    requremnet_contents = SurrogateRequirement.objects.all()
    return render(request,'add_requirment_list.html',{'requremnet_contents':requremnet_contents})


def delete_requirment_list(request, opening_id):
    content = get_object_or_404(SurrogateRequirement, id=opening_id)
    content.delete()
    return redirect('add_requirment_list')


def edit_requirments_lists(request, service_id):
    
    service = get_object_or_404(SurrogateRequirement, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_requirment_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_requirments_lists.html', {'service': service})




def add_requirements_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        other_content = request.POST.get('contents')
        
        # Check if image is provided

        
        # Save the data to the database
        service_content = SurrogateSection.objects.create(
            heading=heading,
            paragraph=paragraph,
            other_content=other_content
        )
        # Redirect or do other actions after saving
        return redirect('add_requirements_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_requirements = SurrogateSection.objects.all()
    return render(request, 'add_requirements_contents.html', {'mamamia_requirements': mamamia_requirements})



def delete_requirment_contents(request, opening_id):
    content = get_object_or_404(SurrogateSection, id=opening_id)
    content.delete()
    return redirect('add_requirements_contents')


def edit_requirements_contents(request, service_id):
    
    service = get_object_or_404(SurrogateSection, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        other_contents = request.POST.get('contents')
        
        

       
        service.heading = heading
        service.paragraph = paragraph
        service.other_content = other_contents
        


        
        service.save()

        return redirect('add_requirements_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_requirements_contents.html', {'service': service})
    

def add_eligiblity_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = EligibilityCriterion.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_eligiblity_list')
    eligiblity_contents = EligibilityCriterion.objects.all()
    return render(request,'add_eligiblity_list.html',{'eligiblity_contents':eligiblity_contents})


def delete_eligiblity_contents(request, opening_id):
    content = get_object_or_404(EligibilityCriterion, id=opening_id)
    content.delete()
    return redirect('add_eligiblity_list')


def edit_eligibility_lists(request, service_id):
    
    service = get_object_or_404(EligibilityCriterion, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_eligiblity_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_eligibility_lists.html', {'service': service})


def add_guidlines_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = Guidlines.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_guidlines_list')
    guidlines_contents = Guidlines.objects.all()
    return render(request,'add_guidlines_list.html',{'guidlines_contents':guidlines_contents})


def delete_guidelines_contents(request, opening_id):
    content = get_object_or_404(Guidlines, id=opening_id)
    content.delete()
    return redirect('add_guidlines_list')


def edit_guidelines_lists(request, service_id):
    
    service = get_object_or_404(Guidlines, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_guidlines_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_guidelines_lists.html', {'service': service})


def add_eligiblity_guidliness_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph1 = request.POST.get('paragraph1')
        paragraph2 = request.POST.get('paragraph2')
        other_content = request.POST.get('contents')
        
        # Check if image is provided

        
        # Save the data to the database
        service_content = eligiblity_guildnes_Section.objects.create(
            heading=heading,
            paragraph1=paragraph1,
            paragraph2=paragraph2,
            other_content=other_content
        )
        # Redirect or do other actions after saving
        return redirect('add_eligiblity_guidliness_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_eligiblity_guildines = eligiblity_guildnes_Section.objects.all()
    return render(request, 'add_eligiblity_guidliness_contents.html', {'mamamia_eligiblity_guildines': mamamia_eligiblity_guildines})



def delete_eligiblity_guidliness_contents(request, opening_id):
    content = get_object_or_404(eligiblity_guildnes_Section, id=opening_id)
    content.delete()
    return redirect('add_eligiblity_guidliness_contents')


def edit_eligiblity_guidliness_contents(request, service_id):
    
    service = get_object_or_404(eligiblity_guildnes_Section, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph1 = request.POST.get('paragraph1')
        paragraph2 = request.POST.get('paragraph2')
        other_contents = request.POST.get('contents')
        
        

       
        service.heading = heading
        service.paragraph1 = paragraph1
        service.paragraph2 = paragraph2
        service.other_content = other_contents
        


        
        service.save()

        return redirect('add_eligiblity_guidliness_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_eligiblity_guidliness_contents.html', {'service': service})


def add_quetion_answer_contents(request):
    if request.method == 'POST':
        # Get form data
        heading1 = request.POST.get('heading1')
        paragraph1 = request.POST.get('paragraph1')
        heading2 = request.POST.get('heading2')
        paraagraph2 = request.POST.get('paraagraph2')
        
        # Check if image is provided

        
        # Save the data to the database
        service_content = Question_anser.objects.create(
            heading1=heading1,
            heading2=heading2,
            paragraph1=paragraph1,
            paragraph2=paraagraph2
        )
        # Redirect or do other actions after saving
        return redirect('add_quetion_answer_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_quetion_answer = Question_anser.objects.all()
    return render(request, 'add_quetion_answer_contents.html', {'mamamia_quetion_answer': mamamia_quetion_answer})


def delete_quetion_answer_contents(request, opening_id):
    content = get_object_or_404(Question_anser, id=opening_id)
    content.delete()
    return redirect('add_quetion_answer_contents')


def edit_quetion_answer_contents(request, service_id):
    
    service = get_object_or_404(Question_anser, pk=service_id)

    if request.method == 'POST':
        
        heading1 = request.POST.get('heading1')
        paragraph1 = request.POST.get('paragraph1')
        heading2 = request.POST.get('heading2')
        paragraph2 = request.POST.get('paragraph2')
        
        
        

       
        service.heading1 = heading1
        service.paragraph1 = paragraph1
        service.paragraph2 = paragraph2
        service.heading2 = heading2
        


        
        service.save()

        return redirect('add_quetion_answer_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_quetion_answer_contents.html', {'service': service})



def sper_donor_service_page(request):
    return render(request,'sperm_donor_service.html')


def sperm_donor_opening_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = sperm_donor_opening_content.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('sperm_donor_opening_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_sperm = sperm_donor_opening_content.objects.all()
    return render(request, 'add_sperm_donor_services.html', {'mamamia_sperm': mamamia_sperm})


def delete_sperm_donor_contents(request, opening_id):
    content = get_object_or_404(sperm_donor_opening_content, id=opening_id)
    content.delete()
    return redirect('sperm_donor_opening_contents')


def edit_sperm_donor_services(request, service_id):
    
    service = get_object_or_404(sperm_donor_opening_content, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')  
        

       
        service.heading = heading
        service.paragraph = paragraph
        if image:
           service.image = image


        
        service.save()

        return redirect('sperm_donor_opening_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_donor_services.html', {'service': service})



def add_sperm_eligiblity_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = SpermEligibility.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_sperm_eligiblity_list')
    sperm_eligiblity_contents = SpermEligibility.objects.all()
    return render(request,'add_sperm_eligiblity_list.html',{'sperm_eligiblity_contents':sperm_eligiblity_contents})


def delete_sperm_eligiblity_lists(request, opening_id):
    content = get_object_or_404(SpermEligibility, id=opening_id)
    content.delete()
    return redirect('add_sperm_eligiblity_list')


def edit_sperm_eligiblity_lists(request, service_id):
    
    service = get_object_or_404(SpermEligibility, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_sperm_eligiblity_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_eligiblity_lists.html', {'service': service})


def add_sperm_eligible_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        other_content = request.POST.get('contents')
        
        # Check if image is provided

        
        # Save the data to the database
        service_content = Sperm_eligible_Section.objects.create(
            heading=heading,
            paragraph=paragraph,
            other_content=other_content
        )
        # Redirect or do other actions after saving
        return redirect('add_sperm_eligible_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_sperm_requirements = Sperm_eligible_Section.objects.all()
    return render(request, 'add_sperm_eligible_contents.html', {'mamamia_sperm_requirements': mamamia_sperm_requirements})



def delete_sperm_eligiblity_contents(request, opening_id):
    content = get_object_or_404(Sperm_eligible_Section, id=opening_id)
    content.delete()
    return redirect('add_sperm_eligible_contents')



def edit_sperm_eligiblity_contents(request, service_id):
    
    service = get_object_or_404(Sperm_eligible_Section, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        other_contents = request.POST.get('contents')
        
        

       
        service.heading = heading
        service.paragraph = paragraph
        service.other_content = other_contents
        


        
        service.save()

        return redirect('add_sperm_eligible_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_eligiblity_contents.html', {'service': service})
    
def add_sperm_faqs(request):
    if request.method == 'POST':
        # Get form data
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        image = request.FILES.get('image') 

        
        # Save the data to the database
        service_content = FAQs.objects.create(
            # question=title,
            # answer=description,
            image=image
            
        )
        # Redirect or do other actions after saving
        return redirect('add_sperm_faqs')  # Replace 'success_page' with your actual success page URL

    sperm_faq = FAQs.objects.all()
    return render(request, 'add_sperm_faqs.html', {'sperm_faq': sperm_faq})



def delete_sperm_faqs(request, opening_id):
    content = get_object_or_404(FAQs, id=opening_id)
    content.delete()
    return redirect('add_sperm_faqs')


def edit_sperm_faqs(request, service_id):
    
    service = get_object_or_404(FAQs, pk=service_id)

    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        

       
        service.question = title
        service.answer = description


        
        service.save()

        return redirect('add_sperm_faqs')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_faqs.html', {'service': service})




def add_sperm_guidlines_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = sperm_guidlines.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_sperm_guidlines_list')
    sperm_guidlines_contents = sperm_guidlines.objects.all()
    return render(request,'add_sperm_guidlines_list.html',{'sperm_guidlines_contents':sperm_guidlines_contents})



def delete_sperm_guidlines_lists(request, opening_id):
    content = get_object_or_404(sperm_guidlines, id=opening_id)
    content.delete()
    return redirect('add_sperm_guidlines_list')



def edit_sperm_guidlines_lists(request, service_id):
    
    service = get_object_or_404(sperm_guidlines, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_sperm_guidlines_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_guidlines_lists.html', {'service': service})


def sperm_donor_guidlines_contents(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = sperm_guidlines_opening_content.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('sperm_donor_guidlines_contents')  # Replace 'success_page' with your actual success page URL

    mamamia_guidliness = sperm_guidlines_opening_content.objects.all()
    return render(request, 'add_sperm_guidlines_contents.html', {'mamamia_guidliness': mamamia_guidliness})



def delete_sperm_guidlines_contents(request, opening_id):
    content = get_object_or_404(sperm_guidlines_opening_content, id=opening_id)
    content.delete()
    return redirect('sperm_donor_guidlines_contents')


def edit_sperm_guidlines_contents(request, service_id):
    
    service = get_object_or_404(sperm_guidlines_opening_content, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')  
        

       
        service.heading = heading
        service.paragraph = paragraph
        if image:
           service.image = image


        
        service.save()

        return redirect('sperm_donor_guidlines_contents')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_guidlines_contents.html', {'service': service})
    


def add_sperm_final(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        

        
        # Save the data to the database
        service_content = Sperm_donor_Final.objects.create(
            heading=heading,
            paragraph=paragraph,
            
        )
        # Redirect or do other actions after saving
        return redirect('add_sperm_final')  # Replace 'success_page' with your actual success page URL

    sperm_final = Sperm_donor_Final.objects.all()
    return render(request, 'add_sperm_final.html', {'sperm_final': sperm_final})


def delete_sperm_final(request, opening_id):
    content = get_object_or_404(Sperm_donor_Final, id=opening_id)
    content.delete()
    return redirect('add_sperm_final')


def edit_sperm_final(request, service_id):
    
    service = get_object_or_404(Sperm_donor_Final, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        

       
        service.heading = heading
        service.paragraph = paragraph


        
        service.save()

        return redirect('add_sperm_final')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_sperm_final.html', {'service': service})


def egg_donor_service(request):
    return render(request,'egg_donor_service.html')



def add_eggdonor_opening(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = Egg_Donor_opening.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image
        )
        # Redirect or do other actions after saving
        return redirect('add_eggdonor_opening')  # Replace 'success_page' with your actual success page URL

    mamamia_opening = Egg_Donor_opening.objects.all()
    return render(request, 'add_eggdonor_opening.html', {'mamamia_opening': mamamia_opening})



def delete_eggdonor_opening(request, opening_id):
    content = get_object_or_404(Egg_Donor_opening, id=opening_id)
    content.delete()
    return redirect('add_eggdonor_opening')



def edit_eggdonor_opening(request, service_id):
    
    service = get_object_or_404(Egg_Donor_opening, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')  
        

       
        service.heading = heading
        service.paragraph = paragraph
        if image:
           service.image = image


        
        service.save()

        return redirect('add_eggdonor_opening')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_eggdonor_opening.html', {'service': service})
    

def add_egg_eligibility_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = egg_eligibility.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_egg_eligibility_list')
    egg_eligibility_lists = egg_eligibility.objects.all()
    return render(request,'add_egg_eligibility_list.html',{'egg_eligibility_lists':egg_eligibility_lists})


def delete_egg_eligibility(request, opening_id):
    content = get_object_or_404(egg_eligibility, id=opening_id)
    content.delete()
    return redirect('add_egg_eligibility_list')


def edit_egg_eligibility_lists(request, service_id):
    
    service = get_object_or_404(egg_eligibility, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_egg_eligibility_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_egg_eligibility_lists.html', {'service': service})


def add_eggdonor_steps(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        # Check if image is provided

        
        # Save the data to the database
        service_content = egg_steps.objects.create(
            heading=heading,
            paragraph=paragraph,
            
        )
        # Redirect or do other actions after saving
        return redirect('add_eggdonor_steps')  # Replace 'success_page' with your actual success page URL

    mamamia_steps = egg_steps.objects.all()
    return render(request, 'add_eggdonor_steps.html', {'mamamia_steps': mamamia_steps})


def delete_egg_steps(request, opening_id):
    content = get_object_or_404(egg_steps, id=opening_id)
    content.delete()
    return redirect('add_eggdonor_steps')



def edit_eggdonor_steps(request, service_id):
    
    service = get_object_or_404(egg_steps, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        
        

       
        service.heading = heading
        service.paragraph = paragraph



        
        service.save()

        return redirect('add_eggdonor_steps')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_eggdonor_steps.html', {'service': service})


def add_egg_helpful_list(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')

        requremnet_content = egg_donors_helpful.objects.create(
            description=heading
        )
        requremnet_content.save()
        return redirect('add_egg_helpful_list')
    egg_helpful_lists = egg_donors_helpful.objects.all()
    return render(request,'add_egg_helpful_list.html',{'egg_helpful_lists':egg_helpful_lists})


def delete_egg_helpful_list(request, opening_id):
    content = get_object_or_404(egg_donors_helpful, id=opening_id)
    content.delete()
    return redirect('add_egg_helpful_list')


def edit_egg_helpful_list(request, service_id):
    
    service = get_object_or_404(egg_donors_helpful, pk=service_id)

    if request.method == 'POST':
        
        heading = request.POST.get('heading')
   
        

       
        service.description = heading


        
        service.save()

        return redirect('add_egg_helpful_list')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_egg_helpful_list.html', {'service': service})
    

def add_egg_donor_image(request):
    if request.method == 'POST':

        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = egg_donor_image.objects.create(

            image=image
        )
        # Redirect or do other actions after saving
        return redirect('add_egg_donor_image')  # Replace 'success_page' with your actual success page URL

    egg_images = egg_donor_image.objects.all()
    return render(request, 'add_egg_donor_image.html', {'egg_images': egg_images})


def delete_egg_images(request, opening_id):
    content = get_object_or_404(egg_donor_image, id=opening_id)
    content.delete()
    return redirect('add_egg_donor_image')


def edit_eggdonor_images(request, service_id):
    
    service = get_object_or_404(egg_donor_image, pk=service_id)

    if request.method == 'POST':
        

        image = request.FILES.get('image')  
        

       

        if image:
           service.image = image


        
        service.save()

        return redirect('add_egg_donor_image')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_eggdonor_images.html', {'service': service})


def aboutus_page_contents(request):
    return render(request,'aboutus_page_control.html')



def add_about(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = Aboutus.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image,
            button_text=button_text,
            button_url=button_url
        )
        # Redirect or do other actions after saving
        return redirect('add_about')  # Replace 'success_page' with your actual success page URL

    add_about = Aboutus.objects.all()
    return render(request, 'add_about.html', {'add_about': add_about})


def edit_mission(request, content_id):
    content = get_object_or_404(Aboutus, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('add_about')  # Redirect to the Swiper view after editing

    return render(request, 'edit_mission.html', {'content': content})



def delete_about(request, opening_id):
    content = get_object_or_404(Aboutus, id=opening_id)
    content.delete()
    return redirect('add_about')



def add_about_people(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = Aboutus_people.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image,
            button_text=button_text,
            button_url=button_url
        )
        # Redirect or do other actions after saving
        return redirect('add_about_people')  # Replace 'success_page' with your actual success page URL

    add_about_people = Aboutus_people.objects.all()
    return render(request, 'add_about_people.html', {'add_about_people': add_about_people})


def edit_about_people(request, content_id):
    content = get_object_or_404(Aboutus_people, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('add_about_people')  # Redirect to the Swiper view after editing

    return render(request, 'edit_about_people.html', {'content': content})


def delete_about_people(request, opening_id):
    content = get_object_or_404(Aboutus_people, id=opening_id)
    content.delete()
    return redirect('add_about_people')



def add_about_assoc(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = Aboutus_associates.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image,
            button_text=button_text,
            button_url=button_url
        )
        # Redirect or do other actions after saving
        return redirect('add_about_assoc')  # Replace 'success_page' with your actual success page URL

    add_about_assoc = Aboutus_associates.objects.all()
    return render(request, 'add_about_associates.html', {'add_about_assoc': add_about_assoc})

def edit_about_assoc(request, content_id):
    content = get_object_or_404(Aboutus_associates, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('add_about_assoc')  # Redirect to the Swiper view after editing

    return render(request, 'edit_about_assoc.html', {'content': content})



def delete_about_assoc(request, opening_id):
    content = get_object_or_404(Aboutus_associates, id=opening_id)
    content.delete()
    return redirect('add_about_assoc')



def add_why(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        heading1 = request.POST.get('heading1')
        paragraph1 = request.POST.get('paragraph1')
        heading2 = request.POST.get('heading2')
        paragraph2 = request.POST.get('paragraph2')
        heading3 = request.POST.get('heading3')
        paragraph3 = request.POST.get('paragraph3')
        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = why.objects.create(
            heading=heading,
            paragraph=paragraph,
            heading1=heading1,
            paragraph1=paragraph1,
            heading2=heading2,
            paragraph2=paragraph2,
            heading3=heading3,
            paragraph3=paragraph3,
            image=image,
            button_text=button_text,
            button_url=button_url
        )
        # Redirect or do other actions after saving
        return redirect('add_why')  # Replace 'success_page' with your actual success page URL

    add_why = why.objects.all()
    return render(request, 'add_why.html', {'add_why': add_why})

def edit_why(request, content_id):
    content = get_object_or_404(why, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        heading1 = request.POST.get('heading1',content.heading1)
        paragraph1 = request.POST.get('paragraph1',content.paragraph1)
        heading2 = request.POST.get('heading2',content.heading2)
        paragraph2 = request.POST.get('paragraph2',content.paragraph2)
        heading3 = request.POST.get('heading3',content.heading3)
        paragraph3 = request.POST.get('paragraph3',content.paragraph3)
       

        # Update the SwiperContent instance with the new data
        content.image = image
        content.heading = heading
        content.paragraph = paragraph
        content.button_text = button_text
        content.button_url = button_url
        content.heading1 = heading1
        content.paragraph1 = paragraph1
        content.heading2 = heading2
        content.paragraph2 = paragraph2
        content.heading3 = heading3
        content.paragraph3 = paragraph3
        content.save()

        return redirect('add_why')  # Redirect to the Swiper view after editing

    return render(request, 'edit_why.html', {'content': content})





def delete_why(request, opening_id):
    content = get_object_or_404(why, id=opening_id)
    content.delete()
    return redirect('add_why')

