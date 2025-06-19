from django.db import models


class WordInput(models.Model):
    user_text = models.CharField(max_length=200)
    req_date = models.DateTimeField("date requested")

    def __str__(self):
        return self.user_text


class WordOutput(models.Model):
    input = models.ForeignKey(WordInput, on_delete=models.CASCADE)
    return_text = models.CharField(max_length=200)

    def __str__(self):
        return self.return_text
