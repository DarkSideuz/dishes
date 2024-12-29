from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Dish
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(post_save, sender=Dish)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Dish Added'
        message = f'A new dish "{instance.name}" has been added.'
        

        users = User.objects.all()
        email_list = [user.email for user in users if user.email]
        
        if email_list:
            send_mail(
                subject,
                message,
                'admin@gmail.com',
                email_list,
                fail_silently=False,
            )