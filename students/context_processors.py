import os

def branch_context(request):
    return {
        'BRANCH_NAME': os.environ.get('BRANCH_NAME', '')
    }
