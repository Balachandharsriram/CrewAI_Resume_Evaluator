document.addEventListener('DOMContentLoaded', () => {
    const resumeInput = document.getElementById('resumeInput');
    const evaluateButton = document.getElementById('evaluateButton');
    const loadingDiv = document.getElementById('loading');
    const messageParagraph = document.getElementById('message');

    evaluateButton.addEventListener('click', async () => {
        const resumeText = resumeInput.value.trim();

        if (!resumeText) {
            alert('Please paste a resume to evaluate.');
            return;
        }

        loadingDiv.classList.remove('hidden'); // Show loading message
        messageParagraph.textContent = ''; // Clear previous message

        try {
            const response = await fetch('/evaluate_resume', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ resume_text: resumeText })
            });

            const data = await response.json();

            if (response.ok) {
                messageParagraph.textContent = data.message;
            } else {
                messageParagraph.textContent = `Error: ${data.error || 'Something went wrong.'}`;
                messageParagraph.style.color = 'red';
            }
        } catch (error) {
            messageParagraph.textContent = `Network error: ${error.message}`;
            messageParagraph.style.color = 'red';
            console.error('Fetch error:', error);
        } finally {
            loadingDiv.classList.add('hidden'); // Hide loading message
        }
    });
});