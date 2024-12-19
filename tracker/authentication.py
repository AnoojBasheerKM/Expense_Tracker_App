from django.contrib.auth.backends import BaseBackend

from tracker.models import User

class EmailBackend(BaseBackend):
    
    def authenticate(self,request,username=None,password=None):
        
        try:
            
            user_object = User.objects.get(email=username)
            
            if user_object.check_password(password):
                
                return user_object
             
            else:
                
                return None
        except:
            
            return None
    
    def get_user(self, user_id):
        
        return User.objects.get(id=user_id)
    
class PhoneBackend(BaseBackend):
    
    def authenticate(self,request,username=None,password=None):
        
        try:
            
            user_object = User.objects.get(phone=username)
            
            if user_object.check_password(password):
                
                return user_object
            
            else:
                
                return None
        except:
            
            return None
        
    def get_user(self, user_id):
        
        return User.objects.get(id=user_id)