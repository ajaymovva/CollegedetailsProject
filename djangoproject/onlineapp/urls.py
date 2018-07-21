from django.urls import path, re_path
from onlineapp.views.auth import *
from onlineapp.apiviews import *
from onlineapp.views.college import *
from onlineapp.views.student import *
from rest_framework_jwt.views import *

app_name = "onlineapp"

urlpatterns = [
    # path('myapp/', views.current_datetime),
    # path('student/', views.studentinfo),
    # path('students/<id>', views.dynamicrender),
    # path('button/', views.studentinfoonclick),
    # path('college/<acronym>', views.collegebyorder),
    # path('session/', views.login),
    # path("colleges/", CollegeView.as_view(), name="firstclass.html"),
    path("colleges/", CollegeListView.as_view(), name="colleges"),
    # path("colleges/<acronym>", CollegeDetailsView.as_view(), name="detailviewcollege"),
    path("colleges/<int:id>/", CollegeDetailsView.as_view(), name="college_details"),
    path("colleges/add/", CreateCollegeView.as_view(), name="Add_college"),
    path("colleges/<int:id>/student/add/", CreateStudentView.as_view(), name="Add_student"),
    path("colleges/<int:pk>/edit/", EditCollegeView.as_view(), name="Edit_college"),
    path("colleges/<int:pk>/delete/", DeleteCollegeView.as_view(), name="Delete_college"),
    path("colleges/<int:college_id>/student/<int:pk>/edit/", UpdateStudentView.as_view(), name="Edit_student"),
    path("colleges/<int:college_id>/student/<int:pk>/delete/", DeleteStudentView.as_view(), name="Delete_college"),
    path("signup/", Signupclass.as_view(), name="signup"),
    path("apicolleges/", dislay),
    path("apicollegesmodify/<int:pk>", modification_detail),
    path('apicollegesmodify/<int:pk>/student/', studentlistview.as_view(), name="student_info_api"),
    path('apicollegesmodify/<int:pk>/studentadd/', studentlistview.as_view(), name="student_create_api"),
    path('apicollegesmodify/<int:college_id>/student/<int:pk>/options/', studentdetailview.as_view(),
         name="student_update_api"),
    path("login/", LoginClass.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    # path('api/api-auth-token/', obtain_jwt_token)
]
