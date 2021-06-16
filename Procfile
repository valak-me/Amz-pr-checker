web: waitress-serve --port=$PORT amz_pr_checker.wsgi:application
worker: celery -A amz_pr_checker.celery worker -B --loglevel=info

