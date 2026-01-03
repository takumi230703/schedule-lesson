
const now = new Date();
let month = now.getMonth() + 1;
let year = now.getFullYear();
let startWeekday = now.getDay();

const month_label = document.getElementById("monthLabel");
month_label.textContent = `${month} ${year}`;

const last_month_label = document.getElementById("last_month");
const next_month_label = document.getElementById("next_month");


if(month == 12){
    last_month_label.textContent = month - 1;
    next_month_label.textContent = 1;
}else if(month == 1){
    last_month_label.textContent = 12;
    next_month_label.textContent = month + 1;
}else{
    last_month_label.textContent = month - 1;
    next_month_label.textContent = month + 1;
}


function changeMonth(difference){
    month += difference;

    if (month === 13) {
    month = 1;
    year++;
    } else if (month === 0) {
    month = 12;
    year--;
    }

    updateCalendar();
}

function updateCalendar(){
    updateMonthLabel();
    renderCalendar(year, month);

}

function updateMonthLabel() {
    last_month_label.textContent =
        month === 1 ? 12 : month - 1;
    month_label.textContent = `${month} ${year}`;



    next_month_label.textContent =
        month === 12 ? 1 : month + 1;
    month_label.textContent = `${month} ${year}`;

}

last_month_label.addEventListener("click", () => {
    changeMonth(-1);
});
next_month_label.addEventListener("click", () => {
    changeMonth(1);
})

function renderCalendar(year, month) {
  const calendar = document.getElementById("calendar-container");
  calendar.innerHTML = ""; 

  const firstDay = new Date(year, month - 1, 1).getDay();
  const daysInMonth = new Date(year, month, 0).getDate();

  for (let i = 0; i < firstDay; i++) {
    const blank = document.createElement("div");
    blank.className = "day empty";
    calendar.appendChild(blank);
  }

  for (let date = 1; date <= daysInMonth; date++) {
    const day = document.createElement("div");
    day.className = "day";
    day.textContent = date;
    day.style.cursor = "pointer";
    calendar.appendChild(day);
  }
}

renderCalendar(year, month);


