# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Battle(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendId')  # Field name made lowercase.
    win = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Battle'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Friend(models.Model):
    friendid = models.IntegerField(db_column='friendId')  # Field name made lowercase.
    friendrelation = models.IntegerField(db_column='friendRelation')  # Field name made lowercase.
    friend_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='friend_userId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friend'


class Saving(models.Model):
    savingid = models.IntegerField(db_column='savingId', primary_key=True)  # Field name made lowercase.
    savingmoney = models.IntegerField(db_column='savingMoney')  # Field name made lowercase.
    savingtime = models.CharField(db_column='savingTime', max_length=12)  # Field name made lowercase.
    savingdate = models.CharField(db_column='savingDate', max_length=12)  # Field name made lowercase.
    saving_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='saving_userId', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saving'
        unique_together = (('savingid', 'saving_userid'),)


class User(models.Model):
    userid = models.IntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=45)  # Field name made lowercase.
    useraddress = models.CharField(db_column='userAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userimg = models.CharField(db_column='userImg', max_length=45, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
