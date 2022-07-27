;(function(){
    const modal = new bootstrap.Modal(document.getElementById("modal"))

htmx.on("htmx:afterSwap", (e) => {
  // Response targeting #dialog => show the modal
  if (e.detail.target.id == "dialog") {
    modal.show()

    let birthYearWrapper = document.getElementById('id_birth_year').parentNode.parentNode;

    // if birth year unknown, hide the birth year box
    document.getElementById('id_birth_year_unknown').onchange = function() {
      birthYearWrapper.style.display = this.checked ? 'none' : 'flex';
    };

    // calculate age based on day / month / year filled in
    document.getElementById('id_birth_year').onchange = event => {
      let birthMonth = document.getElementById('id_birth_month').value;
      let birthDay = document.getElementById('id_birth_day').value;
      let birthYear = document.getElementById('id_birth_year').value;

      let ageEndpoint = `/calculate_age/${birthYear}/${birthMonth}/${birthDay}`;
      fetch(ageEndpoint).then(function (response) {
        return response.json();
      }).then(function (data) {
        console.log(data);
        document.getElementById('id_age').value = data.age;
      }).catch(function (err) {
        console.warn('Something went wrong.', err);
      });
    }
  }
})

htmx.on("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
      modal.hide()
      e.detail.shouldSwap = false
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("dialog").innerHTML = ""
  })
})()
