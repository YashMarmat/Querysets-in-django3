from django.db import models

# QuerySets (mostly used in shell)

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)  
    # authors field provides list of authors (can select more than one author in a single entry)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

# Mainly contains these Four topics
"""
1. Creating a Queryset

from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
# Note: if using Blog.objects.create method then no need to use .save()


2. Retrieve a Queryset

Blog.objects.all() # to retrieve every single queryset
Blog.objects.get(id=1,2,3) # to retrieve a blog of specific id
Blog.objects.get(name__iexact="New Smartphone") # to find an object by its name (needs exact name)
# you can also other filter to retrieve an object (see documentation on QuerySets) 


3. Update a Queryset

# Example 1: 
# Updating multiple objects at once

Blog.objects.update(tagline="Updated tagline") # now all the blogs (objects) will have same tagline that is "updated tagline"

# Example 2: 
# Update objects of a particular year. (our Entry model above)

Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
# now the headline of all objects (of year 2007) contains --> 'Everything is the same'

# Example 3: 
# Updating a specific blog (object)

Blog.objects.all()
#output: <QuerySet [<Blog: New Smartphone>, <Blog: Laptops>, <Blog: Beatles Blog>]>

new = Blog.objects.get(id=1) # select the object you want to update (needs id)
new.name     # output: 'New Smartphone'   # accessing the name field of this object

new.name = "Brandnew Smartphone"    # updating or changing the name field
new.save()      # save changes
new.name     # output: 'Brandnew Smartphone'

Blog.objects.all()
# output: <QuerySet [<Blog: Brandnew Smartphone>, <Blog: Laptops>, <Blog: Beatles Blog>]>

4. Delete a Queryset

# Example 1: 
# delete a particular blog (object)

Blog.objects.all()
# output: <QuerySet [<Blog: Brandnew Smartphone>, <Blog: Laptops>, <Blog: Beatles Blog>]>

d = Blog.objects.get(id=3)   # select the object to delete (needs id)
d.name  # output: 'Beatles Blog'
d.delete()  # output: (1, {'blog.Blog': 1})

Blog.objects.all()
# output: <QuerySet [<Blog: Brandnew Smartphone>, <Blog: Brandnew Laptops>]>

# Example 2: 
# delete all the objects from the QuerySet

Blog.objects.all().delete()
# output: (6, {'blog.Entry_authors': 3, 'blog.Entry': 1, 'blog.Blog': 2}) # your's can be different

Blog.objects.all()
# output: <QuerySet []>   # empty QuerySet (means successfully deleted all the objects)


# Example 3: 
# Delete objects of a particular year. (our Entry model above)

Entry.objects.filter(pub_date__year=2005).delete()
# output: (5, {'webapp.Entry': 5})  # your's can be different

"""