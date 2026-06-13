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

    if (answeredCount === totalCount) {
        alert(score);
    }
}