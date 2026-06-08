from datetime import date, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Student, Batch, FeePackage, Staff, FeePayment, PoliceStation

from .forms import (
    StudentForm,
    BatchForm,
    FeePackageForm,
    StaffLoginForm,
    FeePaymentForm,
    PoliceStationForm
)



def staff_login(request):
    if request.session.get('staff_id'):
        return redirect('home')

    form = StaffLoginForm()
    error = ''

    if request.method == 'POST':

        form = StaffLoginForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            pin = form.cleaned_data['pin']

            staff = Staff.objects.filter(
                name=name,
                pin=pin,
                is_active=True
            ).first()

            if staff:
                request.session['staff_id'] = staff.id
                request.session['staff_name'] = staff.name

                return redirect('home')

            else:
                error = 'Invalid name or PIN'

    return render(request, 'students/login.html', {
        'form': form,
        'error': error
    })


def staff_logout(request):

    request.session.flush()

    return redirect('staff_login')


def staff_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.session.get('staff_id'):
            return redirect('staff_login')

        return view_func(request, *args, **kwargs)

    return wrapper


@staff_required
def home(request):
    query = request.GET.get('q')
    students = []

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(parent_name__icontains=query) | Q(roll_number__icontains=query)
        )

    return render(request, 'students/home.html', {
        'students': students
    })


@staff_required
def students_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(parent_name__icontains=query) | Q(roll_number__icontains=query)
        )

    return render(request, 'students/students.html', {
        'students': students
    })


@staff_required
def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'students/add_student.html', {
        'form': form
    })


@staff_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'students/edit_student.html', {
        'form': form
    })


@staff_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('students')


@staff_required
def fee_pending(request):
    today = date.today()
    next_week = today + timedelta(days=7)

    students = Student.objects.filter(fee_end_date__lte=next_week)

    return render(request, 'students/fee_pending.html', {
        'students': students
    })


@staff_required
def batches(request):
    query = request.GET.get('q')
    batches = Batch.objects.all()

    if query:
        batches = batches.filter(name__icontains=query)

    return render(request, 'students/batches.html', {
        'batches': batches
    })


@staff_required
def add_batch(request):
    form = BatchForm()

    if request.method == 'POST':
        form = BatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('batches')

    return render(request, 'students/add_batch.html', {
        'form': form
    })


@staff_required
def edit_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    form = BatchForm(instance=batch)

    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)

        if form.is_valid():
            form.save()
            return redirect('batches')

    return render(request, 'students/edit_batch.html', {
        'form': form
    })


@staff_required
def delete_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    batch.delete()

    return redirect('batches')


@staff_required
def batch_details(request, id):
    batch = get_object_or_404(Batch, id=id)
    students = Student.objects.filter(batch=batch)

    return render(request, 'students/batch_details.html', {
        'batch': batch,
        'students': students
    })


@staff_required
def fee_packages(request):
    packages = FeePackage.objects.all()

    return render(request, 'students/fee_packages.html', {
        'packages': packages
    })


@staff_required
def add_fee_package(request):
    form = FeePackageForm()

    if request.method == 'POST':
        form = FeePackageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('fee_packages')

    return render(request, 'students/add_fee_package.html', {
        'form': form
    })


@staff_required
def edit_fee_package(request, id):
    package = get_object_or_404(FeePackage, id=id)
    form = FeePackageForm(instance=package)

    if request.method == 'POST':
        form = FeePackageForm(request.POST, instance=package)

        if form.is_valid():
            form.save()
            return redirect('fee_packages')

    return render(request, 'students/edit_fee_package.html', {
        'form': form
    })


@staff_required
def delete_fee_package(request, id):
    package = get_object_or_404(FeePackage, id=id)
    package.delete()

    return redirect('fee_packages')


@staff_required
def pay_fee(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            package = form.cleaned_data['package']
            amount = form.cleaned_data['amount']
            paid_date = form.cleaned_data['paid_date']
            fee_start_date = form.cleaned_data['fee_start_date']

            # Explicitly calculate fee_end_date using package validity days
            fee_end_date = fee_start_date + timedelta(days=package.days)

            # Update student profile
            student.fee_package = package
            student.fee_start_date = fee_start_date
            student.fee_end_date = fee_end_date
            student.save()

            # Create FeePayment history record with explicitly calculated dates
            payment = FeePayment.objects.create(
                student=student,
                package=package,
                amount=amount,
                paid_date=paid_date,
                fee_start_date=fee_start_date,
                fee_end_date=fee_end_date
            )

            return redirect('receipt', payment_id=payment.id)
    else:
        # Prefill default values
        initial_data = {}
        if student.fee_package:
            initial_data['package'] = student.fee_package
        initial_data['paid_date'] = date.today()
        if student.fee_end_date:
            initial_data['fee_start_date'] = student.fee_end_date
        else:
            initial_data['fee_start_date'] = date.today()
        form = FeePaymentForm(initial=initial_data)

    return render(request, 'students/pay_fee.html', {
        'student': student,
        'form': form
    })



@staff_required
def payment_history(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    payments = FeePayment.objects.filter(student=student).order_by('-created_at')

    return render(request, 'students/payment_history.html', {
        'student': student,
        'payments': payments
    })


@staff_required
def receipt(request, payment_id):
    payment = get_object_or_404(FeePayment, id=payment_id)

    return render(request, 'students/receipt.html', {
        'payment': payment
    })


@staff_required
def student_details(request, id):
    student = get_object_or_404(Student, id=id)
    payments = FeePayment.objects.filter(student=student).order_by('-created_at')

    if student.is_fee_expired():
        status = 'Expired'
    elif student.is_fee_expiring():
        status = 'Expiring Soon'
    else:
        status = 'Active'

    return render(request, 'students/student_details.html', {
        'student': student,
        'payments': payments,
        'status': status,
    })


@staff_required
def police_stations(request):
    stations = PoliceStation.objects.all()
    return render(request, 'students/police_stations.html', {
        'stations': stations
    })


@staff_required
def add_police_station(request):
    form = PoliceStationForm()

    if request.method == 'POST':
        form = PoliceStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('police_stations')

    return render(request, 'students/add_police_station.html', {
        'form': form
    })


@staff_required
def edit_police_station(request, id):
    station = get_object_or_404(PoliceStation, id=id)
    form = PoliceStationForm(instance=station)

    if request.method == 'POST':
        form = PoliceStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('police_stations')

    return render(request, 'students/edit_police_station.html', {
        'form': form
    })


@staff_required
def delete_police_station(request, id):
    station = get_object_or_404(PoliceStation, id=id)
    station.delete()
    return redirect('police_stations')


@staff_required
def delete_payment(request, payment_id):
    payment = get_object_or_404(FeePayment, id=payment_id)
    student = payment.student
    
    # Delete payment record
    payment.delete()
    
    # Recalculate student fee dates using the latest remaining payment
    remaining_payments = student.payments.all().order_by('-created_at')
    if remaining_payments.exists():
        latest = remaining_payments.first()
        student.fee_package = latest.package
        student.fee_start_date = latest.fee_start_date
        student.fee_end_date = latest.fee_end_date
    else:
        student.fee_package = None
        student.fee_start_date = student.admission_date
        student.fee_end_date = None
    
    student.save()
    
    # Redirect back to referer if appropriate, otherwise to student details
    referer = request.META.get('HTTP_REFERER')
    if referer and ('payment-history' in referer or 'student-details' in referer) and 'receipt' not in referer:
        return redirect(referer)
    return redirect('student_details', id=student.id)