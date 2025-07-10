document.addEventListener('DOMContentLoaded', function() {
    // Efeito glow para o nome da marca
    const brandName = document.querySelector('.brand-name');
    if (brandName) {
        brandName.classList.add('forge-effect');
    }

    // Validação do formulário de cadastro
    const signupForm = document.querySelector('.signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            const email = signupForm.querySelector('#id_email');
            const username = signupForm.querySelector('#id_username');
            const password1 = signupForm.querySelector('#id_password1');
            const password2 = signupForm.querySelector('#id_password2');
            
            // Validação básica
            if (email.value.trim() === '') {
                e.preventDefault();
                alert('{% trans "Please enter your email" %}');
                email.focus();
                return false;
            }
            
            if (username.value.trim() === '') {
                e.preventDefault();
                alert('{% trans "Please choose a username" %}');
                username.focus();
                return false;
            }
            
            if (password1.value.trim() === '') {
                e.preventDefault();
                alert('{% trans "Please enter a password" %}');
                password1.focus();
                return false;
            }
            
            if (password1.value !== password2.value) {
                e.preventDefault();
                alert('{% trans "Passwords do not match" %}');
                password2.focus();
                return false;
            }
        });
    }

    // Efeitos hover para botões
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});