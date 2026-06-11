from flask import Flask, render_template, redirect, request, session

# configuring app
app = Flask(__name__)
# secret key for flask flash notifications 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route('/')
def index():
    print(session['questions'])
    return render_template('index.html')

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    if 'quiz-data' not in session:
        session['quiz-data'] = []

    if request.method == 'POST' and request.form.get('page') == 'one':
        session['quiz-data'].append(request.form.get('title'))
        session['quiz-data'].append(int(request.form.get('ques')))
        session['questions'] = []
        session['question'] = 1
        return render_template('generate-pg-2.html', question=session['question'])

    if request.method == 'POST' and request.form.get('page') == 'two':
        session['question'] += 1
        data = []
        data.append(request.form.get('question'))
        data.append(request.form.get('ans-01'))
        data.append(request.form.get('ans-02'))
        data.append(request.form.get('ans-03'))
        data.append(request.form.get('ans-04'))
        data.append(request.form.get('correct'))
        session['questions'].append(data)

        if session['quiz-data'][1] >= session['question']:
            return render_template('generate-pg-2.html', question=session['question'])
        else:
            return redirect('/')
    
    return render_template('generate-pg-1.html')

@app.route('/history')
def history():
    return render_template('history.html')