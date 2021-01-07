// window.onload = function () {
//     $('.basket_list').on('click', 'input[type="number"]', function () {
//         let elem = event.target;
//         $.ajax({
//             url: "/baskets/edit/" + elem.name + "/" + elem.value + "/",
//             success: function (data) {
//                 console.log(data)
//                 $('.basket_list').html(data.result);
//             }
//         })
//     });
//     event.preventDefault();
// }

window.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.col-lg-5').addEventListener('click', (e) => {
        let elem = e.target;
        if (elem.type == 'number') {
            basket_list = document.querySelector('.basket_list')
            fetch("/baskets/edit/" + elem.name + "/" + elem.value + "/", {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                },
            })
                .then(data => {
                    return data.json()
                })
                .then(data => {
                    document.querySelector('.col-lg-5').removeChild(basket_list);
                    document.querySelector('.col-lg-5').innerHTML = data.result;
                })
        }
    });
    document.querySelector('.col-lg-5').addEventListener('click', (e) => {
        let elem = e.target
        if (elem.getAttribute('class') == 'fas fa-trash') {
            basket_list = document.querySelector('.basket_list')
            console.log(elem.id)
            fetch("/baskets/remove/" + elem.id + "/", {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                },
            })
                .then(data => {
                    return data.json()
                })
                .then(data => {
                    document.querySelector('.col-lg-5').removeChild(basket_list);
                    document.querySelector('.col-lg-5').innerHTML = data.result;
                })
        }
    });
    event.preventDefault();
})