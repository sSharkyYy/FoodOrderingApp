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
      complete: function (xhr) {
        if (xhr.status == 200)
          alert('Termék a kosárba került')
        else {
          alert(xhr.responseText)
        }
      }
    })
  })
});
