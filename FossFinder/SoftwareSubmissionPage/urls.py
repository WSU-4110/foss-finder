from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.software_submit_detail, name="software_submit_detail"),
    path("", views.software_submit, name="software_submit"),
    path("index/", views.software_index_All, name="index"),
    path("index/MAC/", views.software_index_MAC, name="software_list"),
    path("index/WIN/", views.software_index_WIN, name="software_list"),
    path("index/NIX/", views.software_index_NIX, name="software_list"),
    path("index/WordProcessers", views.software_index_tag_WordProcesser, name="WordProcessers"),
    path("index/SpreadSheets", views.software_index_tag_SpreadSheet, name="SpreadSheets"),
    path("index/GraphicsEditors", views.software_index_tag_GraphicsEditor, name="GraphicsEditors"),
    path("index/AudioEditors", views.software_index_tag_AudioEditor, name="AudioEditors"),
    path("index/Communication", views.software_index_tag_Communication, name="Communication"),
    path("index/Multimedia", views.software_index_tag_Multimedia, name="Multimedia"),
    path("index/AntiVirus", views.software_index_tag_AntiVirus, name="AntiVirus"),
    path("index/CodeEditor", views.software_index_tag_CodeEditor, name="CodeEditor"),
    path("index/DiskBurners", views.software_index_tag_DiskBurner, name="DiskBurners"),
    path("index/FileShare", views.software_index_tag_FileShare, name="FileShare"),
    path("index/OtherSoftware", views.software_index_tag_Other, name="OtherSoftware"),
]