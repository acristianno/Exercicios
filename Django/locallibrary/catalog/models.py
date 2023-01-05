from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Genre(models.Model):
    """Modelo representando o genero do livro"""
    name = models.CharField(max_length=100, help_text="Insira o genero do livro (Ex: Ação)")

    def __str__(self):
        # String para representar o Objeto
        return self.name


class Language(models.Model):
    """Modelo representando a Linguagem (Ex. Inglês, Portugues, Espanhol)"""
    name = models.CharField(max_length=30, help_text="Insira a linguagem do livro.")


class Book(models.Model):
    # Modelo representando um livro (mas não uma copia especifica)
    title = models.CharField(max_length=200)

    # Usado Foreign Key porque o livro tem um author, mas o author tem muitos livros.
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Insira um resumo do livro")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org'
                            '/content/what-isbn">ISBN number</a>')

    # ManyToManyField usado, porque um genero pode ser usado em muitos livros, e um livro pode ter muitos generos
    genre = models.ManyToManyField(Genre, help_text="Selecione o genero desse livro.")

    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absoluted_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Modelo representando uma copia especifica de um livro"""
    id = models.URLField(primary_key=True, default=uuid.uuid4, help_text="Id unico desse exemplar")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Disponibilidade do livro'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """modelo representando o author"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'