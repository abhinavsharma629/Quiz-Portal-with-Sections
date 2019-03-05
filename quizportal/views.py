from django.shortcuts import render,redirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone


# #Registration
# def register(request):
# 	if(request.method=="POST"):
# 		form=RegistrationForm(request.POST)
# 		if(form.is_valid()):
# 			form.save()
# 			return HttpResponseRedirect('/')  #Back To Login Form
# 	else:
# 		form=RegistrationForm()
# 	return render(request,'quizportal/register.html',{'form':form})


#Questions rendering
@login_required(login_url='login')
def detail(request, section_no, id_no):
	print(section_no, id_no, request)
	#Check if logged in user is Admin
	if(request.user.username=='admin'):
		return HttpResponseRedirect('/adminmain')

	else:
		
		#Setting time to user given time in minutes from the login to that section , time

		if(section_no =='1' and len(Time1.objects.filter(Q(id_no=request.user)))==0 and id_no=='1' and len(Section1.objects.all())>0):
			start=timezone.now()
			timeobj=Time.objects.filter(Q(s_no=1))
			for timeob in timeobj:
				end=timeob.time
				break
			end=str(end).split(":")
			end=end[1]

			obj,notif=Time1.objects.get_or_create(id_no=request.user, start_time=start, end_time=start+timedelta(minutes=(int)(end)))
			if notif is True:
				obj.save()

		elif(section_no=='2' and len(Time2.objects.filter(Q(id_no=request.user)))==0 and id_no=='1' and len(Section2.objects.all())>0):
			time=Time1.objects.filter(Q(id_no=request.user))
			if(len(time)>0):
				for i in time:
					endtime=i.end_time
					break
			if(endtime<timezone.now()):
				start=timezone.now()
				timeobj=Time.objects.filter(Q(s_no=2))
				for timeob in timeobj:
					end=timeob.time
					break
				end=str(end).split(":")
				end=end[1]

				obj,notif=Time2.objects.get_or_create(id_no=request.user,start_time=start, end_time=start+timedelta(minutes=(int)(end)))
				if notif is True:
					obj.save()

		elif(section_no=='3' and len(Time3.objects.filter(Q(id_no=request.user)))==0 and id_no=='1' and len(Section3.objects.all())>0):
			#print("3")
			time=Time1.objects.filter(Q(id_no=request.user))
			time1=Time2.objects.filter(Q(id_no=request.user))
			if(len(time)>0):
				for i in time:
					endtime=i.end_time
					break
			if(len(time1)>0):
				for i in time1:
					endtime1=i.end_time
					break
			if(endtime<timezone.now() and endtime1<timezone.now()):
				start=timezone.now()
				timeobj=Time.objects.filter(Q(s_no=3))
				for timeob in timeobj:
					end=timeob.time
					break
				end=str(end).split(":")
				end=end[1]
				obj,notif=Time3.objects.get_or_create(id_no=request.user,start_time=start, end_time=start+timedelta(minutes=(int)(end)))
				if notif is True:
					obj.save()
		#Quiz Ended
		if(section_no=='1'):
			time=Time1.objects.filter(Q(id_no=request.user))
		elif(section_no=='2'):
			time=Time2.objects.filter(Q(id_no=request.user))
		else:
			time=Time3.objects.filter(Q(id_no=request.user))
		#print(time)

		if(len(time)>0):
			for i in time:
				endtime=i.end_time
				break
			#Time Conversion according to 24hrs clock
			f=(endtime)
			f=str(f).split(" ")
			time=f[1]
			time=str(time).split(":")
			h=str(((int)(time[0])))
			m=str(((int)(time[1])))

		else:
			endtime=""

		if(len(time)<0 and endtime < timezone.now()):
			return HttpResponseRedirect('/ended')


		#Trying to access Section 2 before time
		if(section_no=='2'):
			time2=Time1.objects.filter(Q(id_no=request.user))
			if(len(time2)>0):
				for i in time2:
					endtime=i.end_time
					break
			#print(endtime, timezone.now())
			if(endtime > timezone.now()):
				return HttpResponseRedirect('/detail/Section/1/1')

		#Trying to access Section 3 before time
		elif(section_no=='3'):
			time3=Time1.objects.filter(Q(id_no=request.user))
			if(len(time3)>0):
				for i in time3:
					endtime=i.end_time
					break
			#print(endtime, timezone.now())
			if(endtime > timezone.now()):
				return HttpResponseRedirect('/detail/Section/1/1')

			time2=Time2.objects.filter(Q(id_no=request.user))
			if(len(time2)>0):
				for i in time2:
					endtime=i.end_time
					break
			if(endtime > timezone.now()):
				if(len(Section2.objects.all())>0):
					return HttpResponseRedirect('/detail/Section/2/1')


		
		#POST request
		if(request.method=='POST'):
			id1=(int)(id_no)
			id1=id1-1
			
			if(section_no=='1'):
				question=Section1.objects.filter(id_no=str(id_no))
				question1=Section1.objects.filter(id_no=str(id1))
				p1=SolvedQ1.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user), Q(check=False))
			
			elif(section_no=='2'):
				question=Section2.objects.filter(id_no=str(id_no))
				question1=Section2.objects.filter(id_no=str(id1))
				p1=SolvedQ2.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user), Q(check=False))
			
			elif(section_no=='3'):
				question=Section3.objects.filter(id_no=str(id_no))
				question1=Section3.objects.filter(id_no=str(id1))
				p1=SolvedQ3.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user), Q(check=False))


			#Choices
			for i in question1:
				correct_choice1=i.correct_choice
				if(len(p1)==0 and correct_choice1==request.POST.get('choice')):
					if(section_no=='1'):
						obj,notif=SolvedQ1.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=True)
					elif(section_no=='2'):
						obj,notif=SolvedQ2.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=True)
					elif(section_no=='3'):
						obj,notif=SolvedQ3.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=True)
						
					if notif is True:
						obj.save()

				else:
					if(len(p1)==0 and correct_choice1!=request.POST.get('choice')):
						if(section_no=='1'):
							obj,notif=SolvedQ1.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=False)
						elif(section_no=='2'):
							obj,notif=SolvedQ2.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=False)
						else:
							obj,notif=SolvedQ3.objects.get_or_create(id_no=request.user, q_id=question1.get(id_no=id1), check=False)
								
						if notif is True:
							obj.save()

			if(len(question)>0):
				args={}
				for i in question:
					if(i.image):
						#Image.open('http://127.0.0.1:8000/media/'+str(i.image))
						args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0], 'image1':"image"}
					else:
						args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0]}
					break
				return render(request, 'quizportal/questions.html', args)

			else:
				if(len(SolvedQ1.objects.filter(Q(id_no=request.user))) < len(Section1.objects.all())):
					return HttpResponseRedirect('/detail/Section/1/'+str(int(id_no)+1))
				elif(len(SolvedQ2.objects.filter(Q(id_no=request.user)))< len(Section2.objects.all()) and section_no=='1'):
					markSection1End(request)
					return HttpResponseRedirect('/detail/Section/2/1')
				elif(len(SolvedQ2.objects.filter(Q(id_no=request.user)))< len(Section2.objects.all()) and section_no=='2'):
					return HttpResponseRedirect('/detail/Section/2/'+str(int(id_no)+1))
				elif(len(SolvedQ3.objects.filter(Q(id_no=request.user)))< len(Section3.objects.all()) and section_no=='2'):
					markSection2End(request)
					return HttpResponseRedirect('/detail/Section/3/1')
				elif(len(SolvedQ3.objects.filter(Q(id_no=request.user)))< len(Section3.objects.all()) and section_no=='3'):
					return HttpResponseRedirect('/detail/Section/2/'+str(int(id_no)+1))
				else:
					return HttpResponseRedirect('/ended')


		#GET request
		else:
			
			#Check if its the last Question for Section 1
			if(section_no=='1'):
				question=Section1.objects.all()
				if(len(question)==0):
					markSection1End(request)
					if(len(Section2.objects.all())>0):
						return HttpResponseRedirect('/detail/Section/2/1')
					else:
						return HttpResponseRedirect('/ended')
			
			#Check if its the last Question for Section 2
			elif(section_no=='2'):
				question=Section2.objects.all()
				if(len(question)==0):
					markSection2End(request)
					if(len(Section3.objects.all())>0):
						return HttpResponseRedirect('/detail/Section/3/1')
					else:
						return HttpResponseRedirect('/ended')
			
			#Check if its the last Question for Section 3
			elif(section_no=='3'):
				question=Section3.objects.all()
				if(len(question)==0):
					markSection3End(request)
					return HttpResponseRedirect('/ended')



			#If its the last Question for the particular Section
			id1=(int)(id_no)

			#Section 1
			if(section_no=='1'):
				question1=Section1.objects.filter(id_no=str(id1))
				if(len(question1)==0):
					#print("yes")
					markSection1End(request)
					return HttpResponseRedirect('/detail/Section/2/1')
				else:
					#Attempted Questions
					if(len(SolvedQ1.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user)))>0):
						score=SolvedQ1.objects.filter(Q(id_no=request.user))
						return render(request, 'quizportal/attempted.html', {'section_no':section_no, 'id_no':id1})
					else:
						#Unattempted
						question=Section1.objects.filter(Q(id_no__exact=str(id_no)))
						args={}
						for i in question:
							if(i.image):
								#Image.open('http://127.0.0.1:8000/media/'+str(i.image))
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0], 'image1':"image"}
							else:
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0]}
							break
						return render(request, 'quizportal/questions.html', args)

			#Section 2
			elif(section_no=='2'):
				question1=Section2.objects.filter(id_no=str(id1))
				if(len(question1)==0):
					markSection2End(request)
					return HttpResponseRedirect('/detail/Section/3/1')
				else:
					#Attempted Questions
					if(len(SolvedQ2.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user)))>0):
						score=SolvedQ2.objects.filter(Q(id_no=request.user))
						return render(request, 'quizportal/attempted.html', {'section_no':section_no, 'id_no':id1})
					else:
						#Unattempted
						question=Section2.objects.filter(Q(id_no__exact=str(id_no)))
						args={}
						for i in question:
							if(i.image):
								#Image.open('http://127.0.0.1:8000/media/'+str(i.image))
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0], 'image1':"image"}
							else:
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0]}
							break
						return render(request, 'quizportal/questions.html', args)

			#Section 3
			elif(section_no=='3'):
				question1=Section3.objects.filter(id_no=str(id1))
				if(len(question1)==0):
					return HttpResponseRedirect('/ended')
				else:
					#Attempted Questions
					if(len(SolvedQ3.objects.filter(Q(q_id=question1.get(id_no=id1)) ,Q(id_no=request.user)))>0):
						score=SolvedQ3.objects.filter(Q(id_no=request.user))
						return render(request, 'quizportal/attempted.html', {'section_no':section_no, 'id_no':id1})
					else:
						#Unattempted
						question=Section3.objects.filter(Q(id_no__exact=str(id_no)))
						args={}
						for i in question:
							if(i.image):
								#Image.open('http://127.0.0.1:8000/media/'+str(i.image))
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0], 'image1':"image"}
							else:
								args={'question':question, 'section_no':section_no, 'timer':h+":"+m+":"+time[2].split("+")[0]}
							break
						return render(request, 'quizportal/questions.html', args)


#Scorecard
@login_required(login_url='login')
def score(request, section_no, id_no):
	if(section_no=='1'):
		score=SolvedQ1.objects.filter(Q(id_no=request.user), Q(check=True))
	elif(section_no=='2'):
		score=SolvedQ2.objects.filter(Q(id_no=request.user), Q(check=True))
	elif(section_no=='3'):
		score=SolvedQ3.objects.filter(Q(id_no=request.user), Q(check=True))
	id1=User.objects.filter(Q(username=request.user)).values('username')
	return render(request, 'quizportal/score.html', {'score':len(score), 'id':id1, 'section_no':section_no, 'id_no':id_no})


#Actual function for ending Section 1
def markSection1End(request):
	question=Section1.objects.all()
	for i in question:
		if(SolvedQ1.objects.filter(Q(id_no=request.user), Q(q_id=question.get(id_no=i.id_no)))):
			continue
		else:
			obj,notif=SolvedQ1.objects.get_or_create(id_no=request.user, q_id=question.get(id_no=i.id_no), check=False)
			if notif is True:
				obj.save()
	times=Time1.objects.filter(Q(id_no=request.user))
	for time1 in times:
		time1.end_time=timezone.now()
		time1.save()
		break


#Actual function for ending Section 2
def markSection2End(request):
	question=Section2.objects.all()
	for i in question:
		if(SolvedQ2.objects.filter(Q(id_no=request.user), Q(q_id=question.get(id_no=i.id_no)))):
			continue
		else:
			obj,notif=SolvedQ2.objects.get_or_create(id_no=request.user, q_id=question.get(id_no=i.id_no), check=False)
			if notif is True:
				obj.save()
	times=Time2.objects.filter(Q(id_no=request.user))
	for time1 in times:
		time1.end_time=timezone.now()
		time1.save()
		break


#Actual function for ending Section 3
def markSection3End(request):
	question=Section3.objects.all()
	for i in question:
		if(SolvedQ3.objects.filter(Q(id_no=request.user), Q(q_id=question.get(id_no=i.id_no)))):
			continue
		else:
			obj,notif=SolvedQ3.objects.get_or_create(id_no=request.user, q_id=question.get(id_no=i.id_no), check=False)
			if notif is True:
				obj.save()
	times=Time3.objects.filter(Q(id_no=request.user))
	for time1 in times:
		time1.end_time=timezone.now()
		time1.save()
		break


#Ended Quiz
@login_required(login_url='login')
def ended(request):

	#Marking All Questions as Attempted
	markSection1End(request)
	markSection2End(request)
	markSection3End(request)

	#Scores Of All Sections
	score1=SolvedQ1.objects.filter(Q(id_no=request.user), Q(check=True))
	score2=SolvedQ2.objects.filter(Q(id_no=request.user), Q(check=True))
	score3=SolvedQ3.objects.filter(Q(id_no=request.user), Q(check=True))
	id1=User.objects.filter(Q(username=request.user)).values('username')
	scores=[]
	scores.append(len(score1))
	scores.append(len(score2))
	scores.append(len(score3))
	return render(request, 'quizportal/ended.html', {'scores':scores, 'id':id1})


#Ended
@login_required(login_url='login')
def endSection(request, section_no):

	#Marking All Questions as Attempted According to the Sections

	#Section 1
	if(section_no=='1'):
		markSection1End(request)
		if(len(Section2.objects.all())>0):
			return HttpResponseRedirect('/detail/Section/2/1')
		else:
			return HttpResponseRedirect('/ended')

	#Section 2
	elif(section_no=='2'):
		markSection2End(request)
		if(len(Section3.objects.all())>0):
			return HttpResponseRedirect('/detail/Section/3/1')
		else:
			return HttpResponseRedirect('/ended')

	#Section 3
	elif(section_no=='3'):
		return HttpResponseRedirect('/ended')




#ADMIN ACCESS ONLY

def check_admin(user):
	return user.is_superuser


#Admin Main
@user_passes_test(check_admin)
def adminmain(request):
	return render(request, 'quizportal/adminmain.html')


#All Users' Details
@user_passes_test(check_admin)
def adminall(request):

	#Score of all Users
	admindict={}
	userscore=[]
	users=User.objects.all()

	for j in users:
		if(j.username =='admin'):
			continue
		else:
			
			name=User.objects.filter(Q(username=j))
			for i in name:
				name=i.first_name
				break
			userscore.append(name)
			l1=len(SolvedQ1.objects.filter(Q(id_no=j), Q(check=True)))
			l2=len(SolvedQ2.objects.filter(Q(id_no=j), Q(check=True)))
			l3=len(SolvedQ3.objects.filter(Q(id_no=j), Q(check=True)))
			userscore.append('Ab.' if(l1==0) else l1)
			userscore.append('Ab.' if(l2==0) else l2)
			userscore.append('Ab.' if(l3==0) else l3)

			admindict[j.username]=userscore
			userscore=[]

	return render(request, 'quizportal/adminall.html', {'allusers':admindict})

    
#CSV File Upload
@user_passes_test(check_admin)
def DownloadUserData(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="QuizData.csv"'

	writer = csv.writer(response)
	writer.writerow(['S.No', 'Enrollment Number', 'Name', 'Section1 Score', 'Section2 Score', 'Section3 Score'])

	users=User.objects.all()
	usertuple=[]
	userscore=[]

	count=1

	for j in users:
		if(j.username =='admin'):
			continue
		else:
			name=User.objects.filter(Q(username=j))
			for i in name:
				name=i.first_name
				break
			userscore.append(name)
			l1=len(SolvedQ1.objects.filter(Q(id_no=j), Q(check=True)))
			l2=len(SolvedQ2.objects.filter(Q(id_no=j), Q(check=True)))
			l3=len(SolvedQ3.objects.filter(Q(id_no=j), Q(check=True)))
			userscore.append('Ab.' if(l1==0) else l1)
			userscore.append('Ab.' if(l2==0) else l2)
			userscore.append('Ab.' if(l3==0) else l3)

			usertuple=[]
			usertuple.append(count)
			usertuple.append(j.username)
			usertuple.append(name)
			usertuple.append(userscore[1])
			usertuple.append(userscore[2])
			usertuple.append(userscore[3])

			writer.writerow(tuple(usertuple))

			usertuple=[]
			userscore=[]
			count=count+1

	return response


#CSV File Upload
@user_passes_test(check_admin)
def csvupload(request, section_no):
	if request.method == "POST":
		try:
			if(section_no == '1'):
				form = DataInput1(request.POST, request.FILES)
			elif(section_no == '2'):
				form = DataInput2(request.POST, request.FILES)
			else:
				form = DataInput3(request.POST, request.FILES)

			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/adminmain')
		except Exception as e:
			#print(e)
			section='/admincsvupload/'+str(section_no)
			return HttpResponseRedirect(section)
	else:
		if(section_no == '1'):
			form = DataInput1()
		elif(section_no == '2'):
			form = DataInput2()
		else:
			form = DataInput3()
		args = {"form": form, 'section_no':section_no}
		return render(request, 'quizportal/csvupload.html', args)
		

#Time Upload
@user_passes_test(check_admin)
def timeupload(request, section_no):
	if request.method == "POST":
		try:
			if(section_no == '1'):
				form = TimeInput1(request.POST)
			elif(section_no == '2'):
				form = TimeInput2(request.POST)
			else:
				form = TimeInput3(request.POST)

			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/adminmain')
		except Exception as e:
			print(e)
			section='/admintimeupload/'+str(section_no)
			return HttpResponseRedirect(section)
	else:
		if(section_no == '1'):
			form =TimeInput1()
		elif(section_no == '2'):
			form = TimeInput2()
		else:
			form = TimeInput3()
	args = {"form": form, 'section_no':section_no}
	return render(request, 'quizportal/timeupload.html', args)
		


@user_passes_test(check_admin)
def admindelete(request, nu):
	#Delete enteries

	if(nu=='1' and len(User.objects.all())>1):
		for user in User.objects.all():
			if(user=='admin'):
				continue
			else:
				user.delete()

	if(nu=='2' and len(Section1.objects.all())>0):
		Section1.objects.all().delete()
	elif(nu=='3' and len(Section2.objects.all())>0):
		Section2.objects.all().delete()
	elif(nu=='4' and len(Section3.objects.all())>0):
		Section3.objects.all().delete()


	elif(nu=='5' and len(Time1.objects.all())>0):
		Time1.objects.all().delete()
	elif(nu=='6' and len(Time2.objects.all())>0):
		Time2.objects.all().delete()
	elif(nu=='7' and len(Time3.objects.all())>0):
		Time3.objects.all().delete()

	elif(nu=='8' and len(Time.objects.all())>0):
		Time.objects.all().delete()

	elif(nu=='9' and len(SolvedQ1.objects.all())>0):
		SolvedQ1.objects.all().delete()
	elif(nu=='10' and len(SolvedQ2.objects.all())>0):
		SolvedQ2.objects.all().delete()
	elif(nu=='11' and len(SolvedQ3.objects.all())>0):
		SolvedQ3.objects.all().delete()

	args = {'message':nu}
	return render(request, 'quizportal/adminmain.html', args)

#Registering Users Manually
@user_passes_test(check_admin)
def regis(request):
	if request.method == "POST":
		try:
			form=RegistrationForm(request.POST, request.FILES)
			print(form)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/adminmain')
		except Exception as e:
			section='/regis'
			return HttpResponseRedirect(section)
	else:
		form=RegistrationForm()
	args = {"form": form}
	return render(request, 'quizportal/regis.html', args)