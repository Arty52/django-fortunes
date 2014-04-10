from django.db import models

# Create your models here.

"""
CREATE TABLE fortunes (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
filename TEXT,
size INTEGER,
aphorism TEXT);
"""
class Fortune(models.Model):
    filename = models.CharField(max_length=255)
    size = models.IntegerField( )
    aphorism = models.TextField( )
    @property
    def details( self ):
      return repr( dict( filename=self.filename, size=self.size, aphorism=self.aphorism ) )
    def __str__(self):
      return u'{}'.format(self.aphorism)
    def __repr__(self):
      return u'zzz{}'.format(self.aphorism)
    def __unicode__(self):
      return u'xxx{}'.format(self.aphorism)
    class Meta:
      db_table = 'fortunes'