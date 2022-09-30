function mobileFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

function testLog() {
  let amount = document.getElementsByTagName('input')[0].value
  let price = document.getElementsByClassName('itemPrice')[0].innerHTML
  console.log("Amount: " + amount)
  console.log("Price: " + price)
  console.log(amount * price)
}