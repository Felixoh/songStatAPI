import http
from rest_framework import permissions
from users.models import Membership, NewUser,UserMembership
from django.core.exceptions import ObjectDoesNotExist

class IsCreateorAdminReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj):
        # check if its a safe method such as ((GET,HEAD,OPTIONS)) allow 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_staff and request.method not in self.edit_methods:
            return True 
        
        if request.user.is_superuser:
            return True

        if request.user == obj:
            return True

class ISAdminOnly(permissions.BasePermission):
    
    def has_permission(self,request,view):
        if request.user.is_authenticated:
            return True 
        if request.user.is_superuser:
            return True
        if request.user.is_staff and request.method not in self.edit_methods:
            return True

# this permission class will allow this customer to create a new subscription
class IsFreePlan(permissions.BasePermission):
    # check if object has objectified permissions to setup the appropriate plan :
    def has_permission(self,request,view):
        try:
            get_membership = Membership.objects.get(membership_type='Free')
            user_membership = UserMembership.objects.get(user=request.user,membership=get_membership)
            if not user_membership:
                return False
            if request.user.is_active:
                return True
                
        except ObjectDoesNotExist as DoesNotExist:
            # create and use a custom Error to identify missing object when not found in database.
            pass
