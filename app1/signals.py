
# from django.core.mail import send_mail
# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in
# from django.conf import settings
# from app1.models import CustomUser




# @receiver(user_logged_in)
# def send_login_notification(sender, request, user, **kwargs):
#     print("mail sent")
#     subject = 'Login Notification'
#     message = f'Hello {user.username},\n\nYou have successfully logged in to your account.\n\nBest Regards,\nYour Website Team - Social Book -[ Nagesh Kalburgi ] '
#     # print(user.email)
#     user = CustomUser.objects.get(pk=1)  # Replace 1 with the actual primary key
#     email = user.email
#     if (email):
#         print('email sent')
#     else:
#         print("email not sent")
#     send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
#     # send_mail(subject, message, settings.EMAIL_HOST_USER, ['nageshkalburgi9665@gmail.com','nageshbkalburgi111@gmail.com'])
    
