from __future__ import unicode_literals
from django.db import models
from OASys import settings
from accounts.managers import UserManager
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class MyUser(AbstractBaseUser, PermissionsMixin):
	OPTIONS = (
		("student", "STUDENT"),
		("instructor", "INSTRUCTOR"),
	)
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	role = models.CharField(choices=OPTIONS,max_length=30,default='students')
	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()
	def get_short_name(self):
		return self.first_name
	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)

##########################################################################################################################
# class StudentProfile(models.Model):
# 	user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
# 	course = models.CharField(
# 							max_length=3,
# 							choices=(
# 								('MCS','Masters in Computer Science'),
# 								('MCA', 'Masters in Comuter Applications')
# 							)
# 						)
# 	rollno = models.IntegerField(default=0)
# 	semester = models.CharField(
# 							max_length=10,
# 							choices=(
# 								('Sem-I','Semester One'),
# 								('Sem-II','Semester Two'),
# 								('Sem-III','Semester Three'),
# 								('Sem-IV','Semester Four'),
# 								('Sem-V','Semester Five'),
# 								('Sem-VI','Semester Six'),
# 								)
# 							)

# 	def __str__(self):
# 		return self.user.email

# 	def full_name(self):
# 		return self.user.first_name+' '+self.user.last_name

# # class TeacherProfile(models.Model):

# def create_profile(sender, **kwargs):
# 	if kwargs['created']:
# 		student_profile = StudentProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=MyUser)

