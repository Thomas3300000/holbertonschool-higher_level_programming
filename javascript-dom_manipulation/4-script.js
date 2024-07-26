document.addEventListener('DOMContentLoaded', function() {

  const myList = document.querySelector('ul.my_list');

  document.getElementById('add_item').addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });
})
