
from django.contrib import admin
from django.urls import path

from app.views import near_100
from app.views import splice
from app.views import animal
from app.views import add
urlpatterns = [
    path('warmup-1/near-100/<int:n>',near_100),
    path('warmup-2/string-splosion/<str:given>',splice),
    path('string-2/cat-dog/<thing>',animal),
    path('logic-2/lone-sum/<int:a>/<int:b>/<int:c>',add),
    path("admin/", admin.site.urls),
]
