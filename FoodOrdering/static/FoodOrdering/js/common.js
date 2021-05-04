$(document).ready(function () {
  $('.add-to-cart').on('click', function (ev) {
    var $target = $(ev.target);
    var id = $target.data('cartid');
    var quantity = $('.quantity-' + id)?.val();
    if (!quantity || quantity == 0) {
      quantity = 1
    }
    console.log(quantity)
    $.ajax({
      url: '/add-to-cart/' + id + '/',
      method: 'get',
      data: {
        'quantity': quantity
      },
      success: function () {
        alert('Termék a kosáraba került')
      }
    })
  })
});
