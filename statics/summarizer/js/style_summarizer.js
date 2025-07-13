document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const progressBar = document.getElementById('progresso');
  const fileInput = document.querySelector('input[type="file"]');
  const urlInput = document.getElementById('input_or_file');
  const promptInput = document.getElementById('ia_prompt');
  const fileNameInput = document.getElementById('file_name_tag');

  // Adiciona feedback visual ao input de arquivo
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      const label = document.createElement('p');
      label.textContent = `Arquivo selecionado: ${fileInput.files[0].name}`;
      label.style.color = '#0d47a1';
      label.style.fontWeight = 'bold';
      fileInput.parentNode.appendChild(label);
    }
  });

  // Validação e animação de progresso
  form.addEventListener('submit', (e) => {
    let valid = true;
    clearErrors();

    if (!urlInput.value && fileInput.files.length === 0) {
      showError(urlInput, 'Você deve informar uma URL ou enviar um arquivo.');
      valid = false;
    }

    if (!promptInput.value.trim()) {
      showError(promptInput, 'Digite um prompt para a IA.');
      valid = false;
    }

    if (!fileNameInput.value.trim()) {
      showError(fileNameInput, 'Informe um nome para o arquivo de saída.');
      valid = false;
    }

    if (!valid) {
      e.preventDefault();
      return;
    }

    // Simula progresso
    let progress = 0;
    const interval = setInterval(() => {
      progress += 2;
      progressBar.value = progress;
      progressBar.innerText = `${progress}%`;

      if (progress >= 100) {
        clearInterval(interval);
      }
    }, 100); // 2% a cada 100ms = ~5s
  });

  function showError(input, message) {
    input.style.borderColor = 'red';
    const error = document.createElement('div');
    error.className = 'error-message';
    error.textContent = message;
    error.style.color = 'red';
    error.style.marginTop = '5px';
    error.style.fontSize = '0.9em';
    input.parentNode.appendChild(error);
  }

  function clearErrors() {
    document.querySelectorAll('.error-message').forEach(el => el.remove());
    document.querySelectorAll('input, textarea').forEach(el => {
      el.style.borderColor = '#ccc';
    });
  }
});
