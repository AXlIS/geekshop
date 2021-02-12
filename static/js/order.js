window.addEventListener('DOMContentLoaded', () => {
    a = document.querySelectorAll('a')
    a.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.textDecoration = 'none'
        })
    })
})