from django.urls import path

from . import views


urlpatterns = [

    # LOGIN
    path(
        '',
        views.staff_login,
        name='staff_login'
    ),

    path(
        'logout/',
        views.staff_logout,
        name='staff_logout'
    ),

    # HOME
    path(
        'home/',
        views.home,
        name='home'
    ),

    # STUDENTS
    path(
        'students/',
        views.students_list,
        name='students'
    ),

    path(
        'add-student/',
        views.add_student,
        name='add_student'
    ),

    path(
        'edit-student/<int:id>/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'delete-student/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),

    # FEES
    path(
        'fee-pending/',
        views.fee_pending,
        name='fee_pending'
    ),

    path(
        'fee-packages/',
        views.fee_packages,
        name='fee_packages'
    ),

    path(
        'add-fee-package/',
        views.add_fee_package,
        name='add_fee_package'
    ),

    path(
        'edit-fee-package/<int:id>/',
        views.edit_fee_package,
        name='edit_fee_package'
    ),

    path(
        'delete-fee-package/<int:id>/',
        views.delete_fee_package,
        name='delete_fee_package'
    ),

    # BATCHES
    path(
        'batches/',
        views.batches,
        name='batches'
    ),

    path(
        'add-batch/',
        views.add_batch,
        name='add_batch'
    ),

    path(
        'edit-batch/<int:id>/',
        views.edit_batch,
        name='edit_batch'
    ),

    path(
        'delete-batch/<int:id>/',
        views.delete_batch,
        name='delete_batch'
    ),

    path(
        'batch-details/<int:id>/',
        views.batch_details,
        name='batch_details'
    ),

    # PAYMENTS
    path(
        'pay-fee/<int:student_id>/',
        views.pay_fee,
        name='pay_fee'
    ),
    path(
        'payment-history/<int:student_id>/',
        views.payment_history,
        name='payment_history'
    ),
    path(
        'receipt/<int:payment_id>/',
        views.receipt,
        name='receipt'
    ),

]