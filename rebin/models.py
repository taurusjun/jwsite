# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Actopic(models.Model):
    acid = models.BigAutoField(primary_key=True)
    topic = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actopic'


class Accomment(models.Model):
    cid = models.BigAutoField(primary_key=True)
    acid = models.ForeignKey(Actopic, models.DO_NOTHING, db_column='acid', blank=True, null=True)
    quoteid = models.BigIntegerField(db_column='quoteId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    postdate = models.DateTimeField(db_column='postDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    userimg = models.CharField(db_column='userImg', max_length=300, blank=True, null=True)  # Field name made lowercase.
    localimgpath = models.CharField(db_column='localImgPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    deep = models.IntegerField(blank=True, null=True)
    refcount = models.IntegerField(db_column='refCount', blank=True, null=True)  # Field name made lowercase.
    ups = models.IntegerField(blank=True, null=True)
    downs = models.IntegerField(blank=True, null=True)
    namered = models.IntegerField(db_column='nameRed', blank=True, null=True)  # Field name made lowercase.
    avatarframe = models.IntegerField(db_column='avatarFrame', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    isupdelete = models.IntegerField(db_column='isUpDelete', blank=True, null=True)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='nameType', blank=True, null=True)  # Field name made lowercase.
    verified = models.IntegerField(blank=True, null=True)
    verifiedtext = models.TextField(db_column='verifiedText', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    issignedupcollege = models.IntegerField(db_column='isSignedUpCollege', blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        return  {'username': self.username,
                  'cid': self.cid,
                  'quoteid': self.quoteid,
                  'postdate': self.postdate,
                  'content': self.content,
                  'count': self.count,
                 }

    class Meta:
        managed = False
        db_table = 'accomment'


class Accommentimg(models.Model):
    cid = models.BigAutoField(primary_key=True)
    acid = models.BigIntegerField(blank=True, null=True)
    quoteid = models.BigIntegerField(db_column='quoteId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    postdate = models.DateTimeField(db_column='postDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    userimg = models.CharField(db_column='userImg', max_length=120, blank=True, null=True)  # Field name made lowercase.
    localimgpath = models.CharField(db_column='localImgPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    deep = models.IntegerField(blank=True, null=True)
    refcount = models.IntegerField(db_column='refCount', blank=True, null=True)  # Field name made lowercase.
    ups = models.IntegerField(blank=True, null=True)
    downs = models.IntegerField(blank=True, null=True)
    namered = models.IntegerField(db_column='nameRed', blank=True, null=True)  # Field name made lowercase.
    avatarframe = models.IntegerField(db_column='avatarFrame', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    isupdelete = models.IntegerField(db_column='isUpDelete', blank=True, null=True)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='nameType', blank=True, null=True)  # Field name made lowercase.
    verified = models.IntegerField(blank=True, null=True)
    issignedupcollege = models.IntegerField(db_column='isSignedUpCollege', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accommentImg'


class Accommentcache(models.Model):
    cid = models.BigAutoField(primary_key=True)
    acid = models.BigIntegerField(blank=True, null=True)
    quoteid = models.BigIntegerField(db_column='quoteId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    postdate = models.DateTimeField(db_column='postDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    userimg = models.CharField(db_column='userImg', max_length=300, blank=True, null=True)  # Field name made lowercase.
    localimgpath = models.CharField(db_column='localImgPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    deep = models.IntegerField(blank=True, null=True)
    refcount = models.IntegerField(db_column='refCount', blank=True, null=True)  # Field name made lowercase.
    ups = models.IntegerField(blank=True, null=True)
    downs = models.IntegerField(blank=True, null=True)
    namered = models.IntegerField(db_column='nameRed', blank=True, null=True)  # Field name made lowercase.
    avatarframe = models.IntegerField(db_column='avatarFrame', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    isupdelete = models.IntegerField(db_column='isUpDelete', blank=True, null=True)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='nameType', blank=True, null=True)  # Field name made lowercase.
    verified = models.IntegerField(blank=True, null=True)
    verifiedtext = models.TextField(db_column='verifiedText', blank=True, null=True)  # Field name made lowercase.
    issignedupcollege = models.IntegerField(db_column='isSignedUpCollege', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accommentcache'