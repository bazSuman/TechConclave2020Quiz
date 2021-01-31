const burger = document.querySelector(".burger");
const aside = document.querySelector(".aside");

burger.addEventListener("click", () => {
  aside.classList.toggle("nav_active");
  burger.classList.toggle("open");
});

const mainItem1 = document.querySelector(".main-item1 a");
const subItem1 = document.querySelector(".sub1");

mainItem1.addEventListener("click", () => {
  subItem1.classList.toggle("show");
});



let count=20;
var myInterval;
const time=0;
const counter = document.querySelector(".timer h2");
function timer(){
clearInterval(myInterval);
count= 21;
myInterval = setInterval(function(){
  if(count>time){
    document.getElementById('q_text').style.color = '#000000';
    count--;
    counter.innerHTML=count;
  }else{
    clearInterval(myInterval)
    counter.innerHTML="20"
    count=21;
    document.getElementById('questionbox').style.background = 'red'
    document.getElementById('q_text').style.color = 'white'
  }
},1000)
}


// let count = 20;
// const time = 0;
// const counter = document.querySelector(".timer h2");
// function updateCounter() {
//   if (count > time) {
//     document.getElementById('q_text').style.color = '#000000';
//     count--;
//     counter.innerHTML = count;
//   }
//   else {
//     clearInterval(TIMER);
//     counter.innerHTML = "20";
//     count = 20;
//     document.getElementById('questionbox').style.background = 'red'
//     document.getElementById('q_text').style.color = 'white'
//   }
// }

var buttons = document.querySelector("div.optionlist");
console.log(buttons)
buttons.addEventListener("click", getQuestion, true);

function getQuestion(e) {
  if (e.target != e.currentTarget) {
    var id = e.target.id;
    document.getElementById(id).style.backgroundColor = "red";
    document.getElementById(id).style.color = "white";
    document.getElementById(id).setAttribute("disabled", "");
    document.getElementById('waiting-screen').style.display = "none";
    document.getElementById('questionbox').style.background = '#dddddd'


    for (let i = 1; i <= 100; i++) {
      var questionNumber = document.getElementById('question'+i);
      var answerbutton = document.getElementById('answerbutton'+i);
      var answer = document.getElementById('answer'+i);
      if (questionNumber.id.length == 9) {
        if (id == questionNumber.id.charAt(questionNumber.id.length - 1)) {
          questionNumber.style.display = 'block';
          // TIMER = setInterval(updateCounter, 1000);
          timer();
          answerbutton.style.display = 'block';
          answerbutton.addEventListener("click",()=>
          {
            document.getElementById('answer'+i).style.display = "block";
          })
        }
        else {
          questionNumber.style.display = 'none';
          answerbutton.style.display = 'none';
          document.getElementById('answer'+i).style.display = "none";
        }
      }
      else {
        if (id == (questionNumber.id.charAt(questionNumber.id.length - 2)+questionNumber.id.charAt(questionNumber.id.length - 1))) {
          questionNumber.style.display = 'block';
          // TIMER = setInterval(updateCounter, 1000);
          timer();
          answerbutton.style.display = 'block';
          answerbutton.addEventListener("click",()=>
          {
            document.getElementById('answer'+i).style.display = "block";
          })
        }
        else {
          questionNumber.style.display = 'none';
          answerbutton.style.display = 'none';
          document.getElementById('answer'+i).style.display = "none";
        }
      }
    }

    document.getElementById('waiting-screen').style.display = "flex";

  }
  e.stopPropagation();
}


function answer(i){
  var answer = document.getElementById('answer'+i);
  answer.style.display = 'flex';
}

var rows = document.querySelector("tr");
rows.addEventListener("click", () => {
  rows.style.backgroundColor = "none";
});

/*================================*/
/*-------Categories---------------*/
/*================================*/

const filterContainer = document.querySelector(".row"),
  filterBtns = filterContainer.children,
  totalFilterBtns = filterBtns.length,
  categoryItems = document.querySelectorAll(".option"),
  totalCategoryItems = categoryItems.length;

for (let i = 0; i < totalFilterBtns; i++) {
  filterBtns[i].addEventListener("click", function () {
    filterContainer
      .querySelector(".activesection")
      .classList.remove("activesection");
  this.classList.add("activesection");

    const filterValue = this.getAttribute("data-filter");
    for (let k = 0; k < totalCategoryItems; k++) {
      if (filterValue === categoryItems[k].getAttribute("data-category")) {
        categoryItems[k].classList.remove("hide");
        categoryItems[k].classList.add("show");
      } else {
        categoryItems[k].classList.remove("show");
        categoryItems[k].classList.add("hide");
      }
    }
  });
}