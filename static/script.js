let score = 0;
let answeredCount = 0;
let totalCount = 0;

function checkAnswer(btn, selected) {
    let div = btn.parentElement;
    totalCount = parseInt(div.dataset.total);
    let correct = parseInt(div.dataset.correct);
    
    const buttons = div.querySelectorAll('.option');
    buttons.forEach(b => b.disabled = true);

    if (selected === (correct - 1)) {
        btn.classList.add('correct');
        score++;
    } else {
        btn.classList.add('wrong');
        buttons[correct - 1].classList.add('correct');
    }

    answeredCount++;

    document.querySelector('.score-lbl').innerHTML = score / totalCount * 100 + '%';
    document.querySelector('.answer-lbl').innerHTML = answeredCount;
    updateScore(score, totalCount, 'score-bar');
    updateScore(answeredCount, totalCount, 'answered-bar');

    // if (answeredCount === totalCount) {
    //     alert(score);
    // }
}

function updateScore(current, total, bar) {
    const progressBar = document.getElementById(bar);
    const percent = current / total;
    const offset = 440 - (440 * percent);
    // here 440 is the circumference 2piR

    progressBar.style.strokeDashoffset = offset;
}