from celery_app import celery

@celery.task(name='app.long_running_task')
def long_running_task(prompt):
    import time
    # time.sleep(1)  # Simulate a long-running task
    return {"generated_text": ["this", "is", "a", "test", "response"], "details": None}
