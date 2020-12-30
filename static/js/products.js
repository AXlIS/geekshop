window.addEventListener('DOMContentLoaded', () => {
    let pagination = document.querySelector('.pagination'),
        items = document.querySelectorAll('.tab')

    let number = 0

    function active(n = 0) {
        items.forEach((item, i) => {
            item.classList.remove('disabled');
            items[n].classList.add('disabled');
        })
    }

    pagination.addEventListener('click', (e) => {
        const target = e.target
        items.forEach((item, i) => {
            if (target === item || target.parentNode === item) {
                console.log(i)
                number = i;
                active(number);
            }
        })
    })
})