from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BoardModel, ReadMember

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    #fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('customClm',)}),)
    #list_display = ['username', 'email', 'age']

class BoardModelAdmin(admin.ModelAdmin):
    model = BoardModel
"""
    list_display = ('title', 'content', 'author', 'images', 'good', 'read', 'readMember_name')

    def readMember_name(self, obj):
        return obj.readMember.name

    readMember_name.short_description = '既読者'
    readMember_name.admin_order_field = 'readMember__name'
"""

class ReadMemberAdmin(admin.ModelAdmin):
    model = ReadMember
    list_display = ('name', 'boardModel_title', 'boardModel_content', 'boardModel_author', 'boardModel_images', 'boardModel_good', 'boardModel_read')

    def boardModel_title(self, obj):
        return obj.boardModel.title

    def boardModel_content(self, obj):
        return obj.boardModel.content

    def boardModel_author(self, obj):
        return obj.boardModel.author

    def boardModel_images(self, obj):
        return obj.boardModel.images

    def boardModel_good(self, obj):
        return obj.boardModel.good

    def boardModel_read(self, obj):
        return obj.boardModel.read

    boardModel_title.short_description = 'タイトル'
    boardModel_title.admin_order_field = 'boardModel__title'
    boardModel_content.short_description = '本文'
    boardModel_content.admin_order_field = 'boardModel__content'
    boardModel_author.short_description = '作成者'
    boardModel_author.admin_order_field = 'boardModel__author'
    boardModel_images.short_description = '画像'
    boardModel_images.admin_order_field = 'boardModel__images'
    boardModel_good.short_description = 'いいね'
    boardModel_good.admin_order_field = 'boardModel__good'
    boardModel_read.short_description = '既読'
    boardModel_read.admin_order_field = 'boardModel__read'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BoardModel, BoardModelAdmin)
admin.site.register(ReadMember, ReadMemberAdmin)