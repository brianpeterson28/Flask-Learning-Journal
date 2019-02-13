import datetime

from peewee import *

DATABASE = SqliteDatabase('entry.db')

class Entry(Model):
    title = TextField()
    date = DateTimeField(formats='%m/%d/%Y')
    time_spent = IntegerField()
    entry_text = TextField()
    resources_text = TextField()

    class Meta:
        database = DATABASE
        order_by = ('date')


    @classmethod
    def create_entry(cls, title, date, time_spent, entry_text, resources_text):
        try:
            with DATABASE.transaction():
                cls.create(title=title,
                           date=date,
                           time_spent=time_spent,
                           entry_text=entry_text,
                           resources_text=resources_text)
        except IntegrityError:
            pass


def initialize():

    '''
    For some reason, 4 entries are getting created instead of two. 
    Need to fix. Why? -- May need to add @app.before_request and @app.after
    to open and close database. May be duplicating things weirdly because of
    request response cycle. 
    '''
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()

