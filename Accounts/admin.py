# from cProfile import label
from django.contrib import admin
from .models import User
from .forms import UserChangeForm, UserCreationForm
# Register your models here.
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.forms import ModelForm

# class UserCreateForm(UserCreationForm):
#     # username = forms.CharField(label='Username', widget=forms.TextInput)
#     # password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     # # password2 = forms.CharField(
#     # #     label='Password confirmation', widget=forms.PasswordInput)
#     # print(username,password)
#     # class Meta:
#     #     model = User
#     #     fields = ('username', 'password')

#     # # def clean_password2(self):
#     # #     password1 = self.cleaned_data.get("password1")
#     # #     password2 = self.cleaned_data.get("password2")
#     # #     if password1 and password2 and password1 != password2:
#     # #         raise forms.ValidationError("Passwords don't match")
#     # #     return password2

#     # def save(self, commit=True):
#     #     user = super().save(commit=False)
#     #     user.set_password(self.cleaned_data["password1"])
#     #     if commit:
#     #         user.save()
#     #     return user
    
#     # # class Meta:
#     # #     model = User
#     # #     fields = '__all__'
    
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#         ]
#         widgets = {
#             'username': forms.TextInput(),
#             'password':forms.PasswordInput(),
#         }
    
#     def save(self, commit: bool = ...):
#         print(self.data)
#         # return super().save(commit)

class AccountAdmin(UserAdmin):
    form = UserChangeForm
    # add_form = UserCreateForm
    list_display = ["username","email","phone","date_joined"]
    search_fields = ["email","first_name","phone"]
    readonly_fields = ["date_joined","last_login"]
       
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             # 'first_name' , 
    #             #   'last_name', 
    #               'username',
    #             #   'rollno',
    #             #   'email',
    #             #   'phone',
    #             #   'avatar',
    #             #   'address',
    #               'password' ),
    #     }),
    # )
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering =()

admin.site.register(User,AccountAdmin)