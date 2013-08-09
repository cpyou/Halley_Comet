from bit.models import Url

def disp_data():
    user_data = Url.objects.all().order_by('-visit_time')
    if len(user_data) >= 10:
        user_data = user_data[:10]
    return user_data




   
