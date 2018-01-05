from django.contrib import admin
from .models import GroupMember


class GroupMemberInline(admin.TabularInline):
    model = GroupMember
