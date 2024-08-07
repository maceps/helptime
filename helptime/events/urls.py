# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("eventupdate/<int:pk>", views.eventupdate, name="eventupdate"),  
    path("taskupdate/<int:pk>", views.taskupdate, name="taskupdate"),  
    path("tasklist/<int:pk>", views.tasklist, name="tasklist"),  
    path("eventdelete/<int:pk>", views.eventdelete, name="eventdelete"),
    path("volunteer/<int:pk>", views.volunteer, name="volunteer")
]
