from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Announcement, Course, Tutorial, Notes, Quiz, Question, Answer, Learner, Instructor, TakenQuiz, LearnerAnswer
from django.utils.html import format_html

# Register your models here.


admin.site.register(User)
admin.site.register(Profile)

admin.site.register(Announcement)
admin.site.register(Course)

admin.site.register(Tutorial)
admin.site.register(Notes)

admin.site.register(Quiz)
admin.site.register(Question)

admin.site.register(Answer)
admin.site.register(Learner)


admin.site.register(Instructor)
admin.site.register(TakenQuiz)


admin.site.register(LearnerAnswer)


'''

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)



'''
