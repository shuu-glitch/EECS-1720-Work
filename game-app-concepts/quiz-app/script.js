const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')

let shuffledQuestions, currentQuestionIndex

startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})

// RUNS WHEN YOU CLICK THE 'START' BUTTON:
function startGame() {
  startButton.classList.add('hide')
  shuffledQuestions = questions.sort(() => Math.random() - .5) // shuffles questions randomly; don't want it to be linear
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  setNextQuestion()
}


// SETS THE NEXT QUESTION:
function setNextQuestion() {
  resetState() // reset everything back to the default state; to clear answers from prev. questions.
  showQuestion(shuffledQuestions[currentQuestionIndex])
}


// SHOWS QUESTIONS:
// counters placed outside the function so they don't reset to 0 every time an answer gets clicked.
countOption1++;
countOption2++;

function showQuestion(question) {
  questionElement.innerText = question.question
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    // checks if button clicked is the correct answer, and sets it only if the answer is actually correct
    if (answer.correct) {
      button.dataset.correct = answer.correct
      countOption1++; // adds a counter to check how many people selected this option.
    } else {
      countOption2++; // adds a counter to check how many people selected the other option.
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  clearStatusClass(document.body) // CLEARS THE COLOR THAT THE BACKGROUND CHANGES TO WHEN YOU GET AN ANSWER RIGHT OR WRONG.
  nextButton.classList.add('hide')
  // a while loop for looping through to remove elements when necessary.
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

// CONFIRMS THE USER'S SELECTED ANSWER FOR THE QUESTION.
function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answerButtonsElement.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  // CHECKS TO SEE IF THERE ARE ENOUGH QUESTIONS IN THE LIST THAT HAVEN'T BEEN GONE THROUGH ALREADY: IF THERE AREN'T, THEN AN OPTION TO RESTART THE GAME IS GIVEN.
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextButton.classList.remove('hide')
  } else {
    startButton.innerText = 'Restart'
    startButton.classList.remove('hide')
  }
}

// CHECKS AN ELEMENT TO SEE IF IT CORRECT, THEN ADDS THE APPROPIATE CLASS DEPENDING ON WHETHER IT IS OR ISN'T.
function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

// REMOVES THE 'CORRECT' AND 'INCORRECT' TAGS THAT WERE ADDED ABOVE.
function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

// QUESTIONS FOR PROGRAM TO CHOOSE FROM:
const questions = [
  {
    question: 'What is 2 + 2?',
    answers: [
      { text: '4', correct: true },
      { text: '22', correct: false }
    ]
  },
  {
    question: 'Who is the best YouTuber?',
    answers: [
      { text: 'Web Dev Simplified', correct: true },
      { text: 'Traversy Media', correct: true },
    ]
  },
  {
    question: 'Is web development fun?',
    answers: [
      { text: 'Kinda', correct: false },
      { text: 'YES!!!', correct: true },
    ]
  },
  {
    question: 'What is 4 * 2?',
    answers: [
      { text: '6', correct: false },
      { text: '8', correct: true }
    ]
  }
]