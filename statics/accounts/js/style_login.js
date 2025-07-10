document.addEventListener('DOMContentLoaded', function() {
    // Adiciona efeito de glow ao título se existir
    const brandName = document.querySelector('.brand-name');
    if (brandName) {
        brandName.classList.add('forge-effect');
    }

    // Validação básica do formulário
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const email = form.querySelector('input[type="email"]');
            const password = form.querySelector('input[type="password"]');
            
            if (email && email.value.trim() === '') {
                e.preventDefault();
                alert('Please enter your email');
                email.focus();
                return false;
            }
            
            if (password && password.value.trim() === '') {
                e.preventDefault();
                alert('Please enter your password');
                password.focus();
                return false;
            }
        });
    }

    // Efeito hover personalizado para botões
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