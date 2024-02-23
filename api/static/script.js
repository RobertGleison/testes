// Confere the existe ou não um termo para a pesquisa e aciona o endpoint /search

function submitForm() {
  var searchTerm = document.forms["form-input"].elements["id"].value.trim();
  if (searchTerm === "") {
    window.open("/search", "_self");
  } else {
    window.open("/search/" + searchTerm, "_self");
  }
  return false;
}
