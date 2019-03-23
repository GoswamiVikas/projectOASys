from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth import update_session_hash_keys
from django.contrib.auth.decorators import login_required
from students.models import Teaches, Subjects, Assignment, Submission
from instructors.forms import AddSubjectForm,GiveAssignmentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_subject(request):
	if request.method == 'POST':
		form = AddSubjectForm(request.POST)
		if form.is_valid():
			course = Subjects.objects.get(subj_id=request.POST['cid'])
			teach = Teaches(cid=course, teacher_id=request.user)
			teach.save(force_insert = True)
			return redirect('/accounts/home')
		else:
			return redirect('/instructors/add_subject')
	else:
		form = AddSubjectForm()
		args = {'form': form }
		return render(request, 'instructors/add_subject.html', args)

@login_required
def my_subjects(request):
	teach = Teaches.objects.filter(teacher_id=request.user)
	args = {'teach': teach}
	return render(request, 'instructors/my_subjects.html', args)

@login_required
def give_asmt(request):
	if request.method == 'POST':
		form = GiveAssignmentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
		else:
			return redirect('/instructors/give_asmt')

	else:
		form = GiveAssignmentForm()
		args = {'form':form}
		return render(request, 'instructors/give_asmt.html', args)
@login_required
def view_asmts(request):
	asmts = Assignment.objects.filter(teacher_id=request.user).order_by('announcement_date')
	args = {'asmts':asmts}

	return render(request, 'instructors/view_asmts.html', args)

@login_required
def view_submissions(request, asmt_name=""):
	submissions = Submission.objects.filter(asmt__asmt_name=asmt_name).order_by('student_id__first_name')
	args = {'submissions': submissions}

	return render(request, 'instructors/view_submissions.html', args)
