

var navbarForm = document.getElementById('navbarForm');

var showOpenBtn = document.getElementById('showOpenBtn');
var showAcceptBtn = document.getElementById('showAcceptBtn');
var showRejectBtn = document.getElementById('showRejectBtn');
var navBarStatusInput = document.getElementById('navBarStatusInput');


showOpenBtn.addEventListener('click', () => {
  navBarStatusInput.value = "0";
  navbarForm.submit();
});

showAcceptBtn.addEventListener('click', () => {
  navBarStatusInput.value = "1";
  navbarForm.submit();

});
showRejectBtn.addEventListener('click', () => {
  navBarStatusInput.value = "2";
  navbarForm.submit();
});
