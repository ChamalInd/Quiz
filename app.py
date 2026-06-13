from flask import Flask, render_template, redirect, request, session, flash
from helper import create_database
import sqlite3


# configuring app
app = Flask(__name__)
# secret key for flask flash notifications 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# linking the database
create_database()
con = sqlite3.connect('quiz.db', check_same_thread=False)
cur = con.cursor()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        quiz = int(request.form.get('quiz'))
        session['quiz_id'] = quiz
        return redirect('/quiz')
    data = cur.execute('SELECT id, title FROM quiz').fetchall()
    return render_template('index.html', data=data)

@app.route('/quiz')
def quiz():
    quiz_name = cur.execute('SELECT title FROM quiz WHERE id = ?', (session['quiz_id'], )).fetchall()[0][0]
    no_of_ques = cur.execute('SELECT nos FROM quiz WHERE id = ?', (session['quiz_id'], )).fetchall()[0][0]
    quiz_data = []
    for i in range(no_of_ques):
        data = cur.execute('SELECT ques.question, ques.answer FROM qanda qa JOIN quiz q ON qa.quiz_id = q.id JOIN question ques ON qa.ques_id = ques.id WHERE q.id = ?', (session['quiz_id'], )).fetchall()[i]
        answers = cur.execute('SELECT a.ans_1, a.ans_2, a.ans_3, a.ans_4 FROM qanda qa JOIN quiz q ON qa.quiz_id = q.id JOIN answers a ON qa.ans_id = a.id WHERE q.id = ?', (session['quiz_id'], )).fetchall()[i]
        quiz_data.append([data[0], data[1], answers])
    print(quiz_data)
    return render_template('quiz.html', quiz_name=quiz_name, quiz_data=quiz_data, total=no_of_ques)

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    if request.method == 'POST' and request.form.get('page') == 'one':
        session['quiz-data'] = []
        title = request.form.get('title')
        ques = request.form.get('ques')

        if title != '' and ques != '' and int(ques) > 0:
            session['quiz-data'].append(title)
            session['quiz-data'].append(int(ques))
            session['question'] = 1

            cur.execute('INSERT INTO quiz (title, nos) VALUES(?, ?)', (session['quiz-data'][0], session['quiz-data'][1], ))
            con.commit()
            session['quiz-data'].append(cur.lastrowid)
            return render_template('generate-pg-2.html', question=session['question'])
        else:
            flash('Incorrect input.')

    if request.method == 'POST' and request.form.get('page') == 'two':
        ques = request.form.get('question')
        ans_1 = request.form.get('ans-01')
        ans_2 = request.form.get('ans-02')
        ans_3 = request.form.get('ans-03')
        ans_4 = request.form.get('ans-04')
        ans = request.form.get('correct')

        if ques != '' and ans_1 != '' and ans_2 != '' and ans_3 != '' and ans_4 != '' and ans != '' and int(ans) > 0 and int(ans) < 5:
            session['question'] += 1

            cur.execute('INSERT INTO question (question, answer) VALUES(?, ?)', (ques, ans, ))
            ques_id = cur.lastrowid
            cur.execute('INSERT INTO answers (ans_1, ans_2, ans_3, ans_4) VALUES(?, ?, ?, ?)', (ans_1, ans_2, ans_3, ans_4, ))
            ans_id = cur.lastrowid
            cur.execute('INSERT INTO qanda (quiz_id, ques_id, ans_id) VALUES(?, ?, ?)', (session['quiz-data'][2], ques_id, ans_id, ))
            con.commit()

            if session['quiz-data'][1] >= session['question']:
                return render_template('generate-pg-2.html', question=session['question'])
            else:
                return redirect('/')
        else:
            flash("Fields cannot be empty.")
            return render_template('generate-pg-2.html', question=session['question'])
    
    return render_template('generate-pg-1.html')

@app.route('/history')
def history():
    return render_template('history.html')