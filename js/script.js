window.onload = function(){
  noun11 = document.getElementById('noun1-1');
    noun11.onclick = toggle;
  noun12 = document.getElementById('noun1-2');
    noun12.onclick = toggle;
  noun2 = document.getElementById('noun2');
    noun2.onclick = toggle;
  verb1 = document.getElementById('verb1');
    verb1.onclick = toggle;
  adjective1 = document.getElementById('adjective1');
    adjective1.onclick = toggle;
}

function toggle(){
  let activity = event.target.classList.item(0)
  if (activity=='word') {
    event.target.classList.remove('word');
    event.target.classList.add('wordclicked');
  } else {
    event.target.classList.remove('wordclicked');
    event.target.classList.add('word');
  }
}
