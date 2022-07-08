from django.db import models

class Genre(models.Model):
    name = models.CharField("Жанр", max_length= 255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class RaitingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default= 0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Anime(models.Model):
    title = models.CharField("Название", max_length= 255)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="pictures/")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    star = models.OneToOneField(RaitingStar, on_delete = models.CASCADE, primary_key = True)
    url = models.SlugField(max_length= 255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"

class Raiting(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="Аниме")

    def __str__(self):
        return f"{self.star} - {self.anime}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length= 10000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name="Родитель", blank=True, null = True
    )
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="Аниме")
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name="Звезда")

    def __str__(self):
        return f"{self.name} - {self.anime}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"