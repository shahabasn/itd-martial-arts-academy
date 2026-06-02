from django.contrib import admin

from .models import (
    Batch,
    FeePackage,
    Student,
    Staff
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
    )

    search_fields = (
        'name',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'parent_name',
        'phone',
        'batch',
        'belt',
        'fee_package',
        'fee_start_date',
        'fee_end_date',
    )

    list_filter = (
        'batch',
        'belt',
        'fee_package',
    )

    search_fields = (
        'name',
        'phone',
    )