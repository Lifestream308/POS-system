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
  let total = 0
  let amountField = document.getElementsByTagName('input')
  let priceField = document.getElementsByClassName('itemPrice')
  let totalField = document.getElementById("total")
  for (let i = 0; i < amountField.length; i++) {
    total += amountField[i].value * priceField[i].innerHTML
  }
  console.log(total)
  totalField.innerHTML = "Total: $" + total
}