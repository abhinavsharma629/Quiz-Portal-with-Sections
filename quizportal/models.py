from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField

#Questions
class Section1(models.Model):
	ANSWER_CHOICES=(
		("A", ("A")),
		("B", ("B")),
		("C", ("C")),
		("D", ("D")),
		)
	id_no=models.CharField(max_length=1000,primary_key=True)
	question=models.TextField()
	image=models.ImageField(upload_to='pictures', blank=True)
	optionA=models.TextField()
	optionB=models.TextField()
	optionC=models.TextField()
	optionD=models.TextField()
	correct_choice=models.CharField(choices=ANSWER_CHOICES, max_length=10, null=False)

#Questions
class Section2(models.Model):
	ANSWER_CHOICES=(
		("A", ("A")),
		("B", ("B")),
		("C", ("C")),
		("D", ("D")),
		)
	id_no=models.CharField(max_length=1000,primary_key=True)
	question=models.TextField()
	image=models.ImageField(upload_to='pictures', blank=True)
	optionA=models.TextField()
	optionB=models.TextField()
	optionC=models.TextField()
	optionD=models.TextField()
	correct_choice=models.CharField(choices=ANSWER_CHOICES, max_length=10, null=False)

#Questions
class Section3(models.Model):
	ANSWER_CHOICES=(
		("A", ("A")),
		("B", ("B")),
		("C", ("C")),
		("D", ("D")),
		)
	id_no=models.CharField(max_length=1000,primary_key=True)
	question=models.TextField()
	image=models.ImageField(upload_to='pictures', blank=True)
	optionA=models.TextField()
	optionB=models.TextField()
	optionC=models.TextField()
	optionD=models.TextField()
	correct_choice=models.CharField(choices=ANSWER_CHOICES, max_length=10, null=False)


#Time Interval Of Quiz
class Time1(models.Model):
	id_no=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	start_time = models.DateTimeField(max_length=100, blank=False, default=now)
	end_time = models.DateTimeField(max_length=100, blank=False, default=now)

	def __str__(self):
		return str(self.end_time)

#Time Interval Of Quiz
class Time2(models.Model):
	id_no=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	start_time = models.DateTimeField(max_length=100, blank=False, default=now)
	end_time = models.DateTimeField(max_length=100, blank=False, default=now)

	def __str__(self):
		return str(self.end_time)

#Time Interval Of Quiz
class Time3(models.Model):
	id_no=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	start_time = models.DateTimeField(max_length=100, blank=False, default=now)
	end_time = models.DateTimeField(max_length=100, blank=False, default=now)

	def __str__(self):
		return str(self.end_time)

		
'''#Scored Card + Solved
class SolvedQ1(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_idsol=ArrayField(models.IntegerField(), default=list)
	q_idunsol=ArrayField(models.IntegerField(), default=list)

#Scored Card + Solved
class SolvedQ2(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_idsol=ArrayField(models.IntegerField(), default=list)
	q_idunsol=ArrayField(models.IntegerField(), default=list)

#Scored Card + Solved
class SolvedQ3(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_idsol=ArrayField(models.IntegerField(), default=list)
	q_idunsol=ArrayField(models.IntegerField(), default=list)'''


class SolvedQ1(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_id=models.ForeignKey(Section1, on_delete=models.CASCADE)
	check=models.BooleanField(default=False)
	
class SolvedQ2(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_id=models.ForeignKey(Section2, on_delete=models.CASCADE)
	check=models.BooleanField(default=False)
	
class SolvedQ3(models.Model):
	id_no=models.ForeignKey(User, on_delete=models.CASCADE)
	q_id=models.ForeignKey(Section3, on_delete=models.CASCADE)
	check=models.BooleanField(default=False)

class Time(models.Model):
	s_no=models.PositiveIntegerField()
	time=models.TimeField()
	