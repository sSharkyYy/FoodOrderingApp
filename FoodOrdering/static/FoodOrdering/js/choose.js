$(document).ready(function () {
  $("#id_shipping").change(function () {
    console.log($(this).val());
    if ($(this).val() == 2) {
      $('#div_id_address').hide();
      $('#div_id_address').removeAttr('required');
      $('#div_id_address').removeAttr('data-error');
      console.log($('#div_id_address'))
    } else {
      $('#div_id_address').show();
      $('#div_id_address').attr('required', '');
      $('#div_id_address').attr('data-error', 'This field is required.');
    }
  });
  $("#id_shipping").trigger("change");


});
