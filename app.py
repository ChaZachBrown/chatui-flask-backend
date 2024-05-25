from flask import Flask, request, jsonify
from celery_app import app, celery  # Import app and celery from celery_app
from tasks import long_running_task  # Import the task from the tasks module

@app.route('/generate/start', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    task = long_running_task.apply_async(args=[prompt])
    return jsonify({"task_id": task.id})

@app.route('/generate/result/<task_id>', methods=['GET'])
def get_result(task_id):
    task = long_running_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': task.state, 'status': 'Pending...'}
    elif task.state == 'FAILURE':
        response = {'state': task.state, 'status': str(task.info)}
    else:
        response = {'state': task.state, 'status': 'Task completed', 'result': task.result}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
