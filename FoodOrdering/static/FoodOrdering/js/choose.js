$(document).ready(function(){
    $("#seeAnotherField").change(function() {
  if ($(this).val() == "Átvétel") {
    $('#hazhozDiv').hide();
    $('#hazhoz').removeAttr('required');
    $('#hazhoz').removeAttr('data-error');

  } else {
    $('#hazhozDiv').show();
    $('#hazhoz').attr('required', '');
    $('#hazhoz').attr('data-error', 'This field is required.');
  }
});
$("#seeAnotherField").trigger("change");




});
