;(function(){
    const modal = new bootstrap.Modal(document.getElementById("modal"))

htmx.on("htmx:afterSwap", (e) => {
  // Response targeting #dialog => show the modal
  if (e.detail.target.id == "dialog") {
    modal.show()

    let birthYearWrapper = $('#id_birth_year').parent().parent();
    birthYearWrapper.hide();

    $("#id_birth_year_unknown").click(function() {
      if($(this).is(":checked")) {
          birthYearWrapper.show();
      } else {
          birthYearWrapper.hide();
      }
    });
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
