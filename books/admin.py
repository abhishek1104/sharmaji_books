from django.contrib import admin

# Register your models here.

from .models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email',) #It is always fine to have a (,) following last entry entry of tuple
    search_fields=('first_name','last_name',) #searching among these fields.

class BookAdmin(admin.ModelAdmin):
    list_display=('title','publisher','publication_date',) #Fields while showing the Books list page
    list_filter=('publication_date',) # For being a tuple entry we need to place (,) in case of single entry to avoid error!
    date_hierarchy = 'publication_date' # date_hierarchy takes a string, not a tuple (Only 1 date field)
    ordering = ('-publication_date',) #Result set default ordering
    filter_horizontal=('authors',) #filter_vertical will put the both boxed one below another!
    fields=('title','authors','publisher','publication_date') #Fields while creating new Book entry from admin panel(visible)
    raw_id_fields = ('publisher',) #Foreign key as simple text box display rather than select box.
    readonly_fields = ('publication_date',) #Readonly,can't be updated


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
