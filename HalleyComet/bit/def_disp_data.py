from bit.models import Url

def disp_five_data():
    user_data = Url.objects.all().order_by('-visit_time')[:4]
    return user_data




   
