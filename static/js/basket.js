window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });

    $('.basket_list').on('click', '.delete_cart_item', function () {
        let t_href = event.target;
        $.ajax({
            url: "/baskets/remove/" + t_href.id + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });
}