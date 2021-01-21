"""onlineQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Quiz.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('company/',Company,name='company'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('studentlogin/', Studentlogin, name='studentlogin'),
    path('tutorlogin/', Tutorlogin, name='tutorlogin'),
    path('userdashboard/', Userdashboard, name='userdashboard'),
    path('addtopic/', addTopic, name='addtopic'),
    path('addcourse/', addCourse, name='addcourse'),
    path('addquestion/', addQuestion, name='addquestion'),
    path('adduser/', addUser, name='adduser'),
    path('tutorreport/', TutorReport, name='tutorreport'),
    path('studentreport/', StudentReport, name='studentreport'),
    path('topicreport/', TopicDetail, name='topicreport'),
    path('coursereport/', CourseReport, name='coursereport'),
    path('questionreport/', QuestionReport, name='questionreport'),
    path('changepassword/(?P<pid>[0-9]+)', ChangePassword, name='changepassword'),
    path('changepassword2/(?P<pid>[0-9]+)', ChangePassword2, name='changepassword2'),
    path('logout/', Logout, name='logout'),
    path('courselist/', CourseList, name='courselist'),
    path('myresult/(?P<pid>[0-9]+)', MyResult, name='myresult'),
    path('viewtopic/(?P<pid>[0-9]+)', ViewTopic, name='viewtopic'),
    path('studentdashboard/', StudentDashboard, name='studentdashboard'),
    path('startquiz/(?P<pid>[0-9]+)', StartQuiz, name='startquiz'),
    path('signuptutor/', Signup_Tutor, name='signuptutor'),
    path('signupstudent/', Signup_Student, name='signupstudent'),
    path('myaccount/(?P<pid>[0-9]+)',MyAccount, name='myaccount'),
    path('deletetutor/(?P<pid>[0-9]+)',DeleteTutor, name='deletetutor'),
    path('deletecourse/(?P<pid>[0-9]+)',DeleteCourse, name='deletecourse'),
    path('deletequestion/(?P<pid>[0-9]+)',DeleteQuestion, name='deletequestion'),
    path('deletestudent/(?P<pid>[0-9]+)',DeleteStudent, name='deletestudent'),
    path('deletetopic/(?P<pid>[0-9]+)',DeleteTopic, name='deletetopic'),
    path('edittopic/(?P<pid>[0-9]+)',EditTopic, name='edittopic'),
    path('editcourse/(?P<pid>[0-9]+)',EditCourse, name='editcourse'),
    path('editstudent/(?P<pid>[0-9]+)',EditStudent, name='editstudent'),
    path('edittutor/(?P<pid>[0-9]+)',EditTutor, name='edittutor'),
    path('editquestion/(?P<pid>[0-9]+)',EditQuestion, name='editquestion'),
    path('viewresult/(?P<pid>[0-9]+)',View_Result, name='viewresult'),
    path('myaccountstudent/(?P<pid>[0-9]+)',MyAccountStudent, name='myaccountstudent'),
    path('resultreport/',ResultReport, name='resultreport'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
