$(document).ready(function () {
  $('.add-to-card').on('click', function (ev) {
    var $target = $(ev.target);
    var id = $target.data('cartid');
    console.log(id)
    $.ajax({
      url: '/add-to-cart/' + id + '/',
      data: {
        dish_id: id
      },
      success: function () {
        alert('Termék a kosáraba került')
      }
    })
  })
});
