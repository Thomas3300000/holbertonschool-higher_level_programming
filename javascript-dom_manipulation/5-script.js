document.addEventListener('DOMContentLoaded', function() {

  const header = document.querySelector('header');

  document.getElementById('update_header').addEventListener('click', function() {
    header.textContent = 'New Header!!!';
  });
})
