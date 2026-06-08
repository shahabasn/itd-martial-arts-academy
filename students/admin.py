from django.contrib import admin

from .models import (
    Batch,
    FeePackage,
    Student,
    Staff,
    FeePayment,
    PoliceStation
)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'pin',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'timing',
        'class_days',
        'monthly_fee',
        'max_students',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'timing',
    )


@admin.register(FeePackage)
class FeePackageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'days',
        'class_days',
    )

    search_fields = (
        'name',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'roll_number',
        'name',
        'parent_name',
        'parent_whatsapp',
        'phone',
        'aadhaar_number',
        'police_station',
        'batch',
        'belt',
        'fee_package',
        'fee_end_date',
    )

    list_filter = (
        'batch',
        'belt',
        'fee_package',
    )

    search_fields = (
        'name',
        'roll_number',
        'parent_name',
        'parent_whatsapp',
        'phone',
        'aadhaar_number',
        'police_station__name',
    )


@admin.register(PoliceStation)
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'package',
        'amount',
        'paid_date',
        'fee_start_date',
        'fee_end_date',
        'created_at',
    )

    list_filter = (
        'paid_date',
        'package',
    )

    search_fields = (
        'student__name',
    )