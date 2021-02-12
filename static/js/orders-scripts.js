window.addEventListener('DOMContentLoaded', () => {

    const TOTAL_FORMS = parseInt(document.querySelector('input[name=orderitems-TOTAL_FORMS]').value);
    let quantity_arr = [],
        price_arr = [],
        delta_quantity,
        order_total_quantity = parseInt(document.querySelector('.order_total_quantity').textContent),
        order_total_price = parseFloat(document.querySelector('.order_total_cost').textContent.replace(',', '.')) || 0;

    for (let i = 0; i < TOTAL_FORMS; i++) {
        let quantity = parseInt(document.querySelector(`input[name=orderitems-${i}-quantity]`).value),
            price = parseFloat(document.querySelector(`.orderitems-${i}-price`).textContent.replace(',', '.')) || 0;

        quantity_arr[i] = quantity
        if (price) {
            price_arr[i] = price / quantity_arr[i]
        } else {
            price_arr[i] = 0
        }
        console.log(1)
    }

    function orderSummeryUpdate(orderitem_price, delta_quantity) {
        let delta_cost = orderitem_price * delta_quantity;
        order_total_price = Number((order_total_price + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;

        document.querySelector('.order_total_quantity').innerHTML = order_total_quantity.toString();
        document.querySelector('.order_total_cost').innerHTML = order_total_price.toString();
    }

    document.querySelector('.order_form').addEventListener('click', (event) => {
        if (event.target.type === 'number') {
            let target = event.target
            let orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''))
            if (price_arr[orderitem_num]) {
                let orderitem_quantity = parseInt(target.value),
                    delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
                quantity_arr[orderitem_num] = orderitem_quantity
                orderSummeryUpdate(price_arr[orderitem_num], delta_quantity)
                document.querySelector(`.orderitems-${orderitem_num}-price`).innerHTML =
                    price_arr[orderitem_num] * quantity_arr[orderitem_num] + ',00'
            }
        }

        if (event.target.type === 'checkbox') {
            let target = event.target;
            let orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
            if (target.checked) {
                delta_quantity = -quantity_arr[orderitem_num]
            } else {
                delta_quantity = quantity_arr[orderitem_num]
            }
            orderSummeryUpdate(price_arr[orderitem_num], delta_quantity)
        }
    })

})