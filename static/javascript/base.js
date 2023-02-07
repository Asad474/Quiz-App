function flashmessgaes(){
    let message = document.getElementById('alert-message')

    setTimeout(() => {
        message.style.display = 'none'
    } , 3000)
}


function clearRadioButtons(){
    let ele = document.querySelectorAll("input[type=radio]");
    ele.forEach(input => input.checked = false)
}  


let isSubmitClicked = false 
let selectedOption = null
let select_option = []
let allquestions;


function countscores(questionslist, selectedlist){
    const length = questionslist.length
    let score = 0

    for (let i = 0; i < length; i++){
        if (questionslist[i].correct_answer === selectedlist[i])
           score++
    }

    return score
}


function showanswers(questionslist, selectedlist){ 
    console.log('Hello')
    const displayanswers = document.querySelector('.showanswers')
    displayanswers.innerHTML = ''
    const size = questionslist.length
    displayanswers.style.display = 'inherit'

    for (let i = 0; i < size; i++){
        let a = ` 
            <div class="answerslist">
                <div>
                    <span>Q${i+1}. ${questionslist[i].question}</span>
                </div>

                <div class="d-grid">
                    <button id="ans-1">${questionslist[i].option_1}</button> 
                </div>

                <div class="d-grid">
                    <button id="ans-2">${questionslist[i].option_2}</button> 
                </div>

                <div class="d-grid">
                    <button id="ans-3">${questionslist[i].option_3}</button> 
                </div>

                <div class="d-grid">
                    <button id="ans-4">${questionslist[i].option_4}</button> 
                </div>
                <br><hr>
            </div>
        `

        displayanswers.innerHTML += a
    }
}


function ques(data, no){
    let div = document.querySelector('.qs')
    div.style.display = 'inherit'
    
    const ques = document.querySelector('#question')

    const op1 = document.querySelector('#op_1')
    const op2 = document.querySelector('#op_2')
    const op3 = document.querySelector('#op_3')
    const op4 = document.querySelector('#op_4')

    const option1 = document.querySelector('#option1')
    const option2 = document.querySelector('#option2')
    const option3 = document.querySelector('#option3')
    const option4 = document.querySelector('#option4')
    const correct = document.querySelector('#correct_answer')

    const answer1 = document.querySelector('#answer1')
    const answer2 = document.querySelector('#answer2')
    const answer3 = document.querySelector('#answer3')
    const answer4 = document.querySelector('#answer4')

    ques.innerText = `Q${no}. ${data.question}`
    op1.innerText = data.option_1
    op2.innerText = data.option_2
    op3.innerText = data.option_3
    op4.innerText = data.option_4

    option1.value = data.option_1
    option2.value = data.option_2
    option3.value = data.option_3
    option4.value = data.option_4
    correct.value = data.correct_answer

    answer1.style.backgroundColor = 'black'
    answer2.style.backgroundColor = 'black'
    answer3.style.backgroundColor = 'black'
    answer4.style.backgroundColor = 'black'

    option1.addEventListener('input', (e) => {
        selectedOption = option1.value;
    });

    option2.addEventListener('input', (e) => {
        selectedOption = option2.value;
    });

    option3.addEventListener('input', (e) => {
        selectedOption = option3.value;
    });

    option4.addEventListener('input', (e) => {
        selectedOption = option4.value;
    });

    // next.style.display = 'inherit'
}

let i = 0 
function quizpage(){
    const questions = document.querySelector('.qs')
    questions.style.display = 'initial'

    const pathname = window.location.pathname
    const id = pathname.charAt(pathname.length-2)
    let url = ''
    url = `http://127.0.0.1:8000/api/subtopics/questions/${id}/`
    
    fetch(url)
    .then(resp => resp.json())
    .then((data) => { 
        if (i == 0)
            ques(data[i], i+1)
        
        const next = document.getElementsByClassName('next')[0]
        const result = document.querySelector('.viewscore')
        const scores = document.querySelector('#scores')
        let total_questions = document.querySelector('#total-questions')

        next.addEventListener('click', () => {
            i++               
            console.log(selectedOption)
            select_option.push(selectedOption)
            console.log(select_option)
            selectedOption = null

            if ( i == data.length){
                const score = countscores(data, select_option)
                scores.value = score
                console.log(score)
                console.log(select_option)
                total_questions.value = i

                questions.style.display = 'none'
                result.style.display = 'inherit'
            //     result.addEventListener('submit', () => { 
            //         d = {
            //             arr1 : data,
            //             arr2 : select_option
            //         } 
    
            //         fetch(`http://127.0.0.1:8000/socre/${id}/`, {
            //             method: 'POST',
            //             headers: {
            //               'Content-Type': 'application/json'
            //             },
            //             body: JSON.stringify(d)
            //         })
            //         .then(response => response.json())
            //         .then(data => {
            //             console.log(data);
            //         });
            //     })
            }

            else if (i < data.length){
                clearRadioButtons()
                ques(data[i], i+1)
            }
        })

        // view.addEventListener('click', showanswers(data, select_option))
    })
}

quizpage()
flashmessgaes()