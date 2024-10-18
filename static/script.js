// Плавная прокрутка к разделам
function smoothScroll(target) {
    document.querySelector(target).scrollIntoView({
        behavior: 'smooth'
    });
}

// Пример: Добавляем обработчик на кнопки с прокруткой
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');
    buttons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const target = event.target.getAttribute('data-target');
            if (target) smoothScroll(target);
        });
    });
});

// Обработка отправки формы с сообщением пользователю
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const responseMessage = document.createElement('p'); // Сообщение после отправки
    form.appendChild(responseMessage);

    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Предотвращаем перезагрузку страницы

        const name = form.elements['name'].value;
        const email = form.elements['email'].value;
        const message = form.elements['message'].value;

        if (name && email && message) {
            responseMessage.textContent = `Спасибо, ${name}! Мы скоро свяжемся с вами.`;
            responseMessage.style.color = 'green';
            form.reset(); // Очистка формы после отправки
        } else {
            responseMessage.textContent = 'Пожалуйста, заполните все поля.';
            responseMessage.style.color = 'red';
        }
    });
});
