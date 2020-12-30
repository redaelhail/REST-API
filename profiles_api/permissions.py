from rest_framework import permissions




class updateOwnProfile(permissions.BasePermission):
	 """Allow users to edit their own profile"""
	 def has_object_permission(self, request, view, obj):
		 """Check user's trying to edit their own profile"""
		 if request.method in permissions.SAFE_METHODS:
			 return True
		 return obj.id == request.user.id