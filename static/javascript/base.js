$(document).ready(() => {
    setTimeout(() => {
        $('#alert-message').css('display', 'none');
    }, 3000);
    
    function clearRadioButtons() {
        $("input[type=radio]").prop('checked', false);
    }
    
    let isSubmitClicked = false;
    let selectedOption = null;
    let select_option = [];
    let allquestions;
    
    function countscores(questionslist, selectedlist) {
        const length = questionslist.length;
        let score = 0;
    
        for (let i = 0; i < length; i++) {
            if (questionslist[i].correct_answer === selectedlist[i])
                score++;
        }
    
        return score;
    }
    
    function ques(data, no) {
        $('.qs').css('display', 'inherit');
    
        $('#question').text(`Q${no}. ${data.question}`);
    
        $('#op_1').text(data.option_1);
        $('#op_2').text(data.option_2);
        $('#op_3').text(data.option_3);
        $('#op_4').text(data.option_4);

        $('#answer1').css('background-color', '#F2F4F4');
        $('#answer2').css('background-color', '#F2F4F4');
        $('#answer3').css('background-color', '#F2F4F4');
        $('#answer4').css('background-color', '#F2F4F4');
    
        const option1 = $('#option1');
        const option2 = $('#option2');
        const option3 = $('#option3');
        const option4 = $('#option4');
        const correct = $('#correct_answer');    
    
        option1.val(data.option_1);
        option2.val(data.option_2);
        option3.val(data.option_3);
        option4.val(data.option_4);
        correct.val(data.correct_answer);
    
        option1.on('input', function (e) {
            selectedOption = option1.val();
        });
    
        option2.on('input', function (e) {
            selectedOption = option2.val();
        });
    
        option3.on('input', function (e) {
            selectedOption = option3.val();
        });
    
        option4.on('input', function (e) {
            selectedOption = option4.val();
        });
    }
    
    let i = 0;
    async function quizpage() {
        const questions = $('.qs');
        questions.css('display', 'initial');
    
        const pathname = window.location.pathname;
        const id = pathname.charAt(pathname.length - 2);
        const url = `/api/subtopics/questions/${id}/`;
    
        const resp = await fetch(url)
        const data = await resp.json()
        if (i == 0)
            ques(data[i], i + 1);

        $('.next').on('click', function () {
            i++;
            console.log(selectedOption);
            select_option.push(selectedOption);
            console.log(select_option);
            selectedOption = null;

            if (i == data.length) {
                const score = countscores(data, select_option);
                $('#scores').val(score);
                console.log(select_option);
                $('#total-questions').val(i);

                questions.css('display', 'none');
                $('.viewscore').css('display', 'inherit');
            }
            else if (i < data.length) {
                clearRadioButtons();
                ques(data[i], i + 1);
            }
        });
    }
    
    quizpage();
})