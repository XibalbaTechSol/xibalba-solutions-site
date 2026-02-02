document.addEventListener('DOMContentLoaded', () => {
    // --- State Management ---
    const STORAGE_KEYS = {
        LOOP: 'xibalba_mind_loop',
        VAULT: 'xibalba_mind_vault'
    };

    const DEFAULTS = {
        LOOP: [
            "I am sovereign over my own mind.",
            "I build infrastructure for the future.",
            "My focus is sharp and unbreakable.",
            "I solve problems with absolute clarity."
        ],
        VAULT: []
    };

    // --- The Loop Logic ---
    const loopDisplay = document.getElementById('affirmation-display');
    const loopProgress = document.getElementById('loop-progress');
    const btnEditLoop = document.getElementById('btn-edit-loop');
    const loopEditor = document.getElementById('loop-editor');
    const loopInput = document.getElementById('loop-input');
    const btnSaveLoop = document.getElementById('btn-save-loop');
    const affirmationContainer = document.getElementById('affirmation-container');

    let loopInterval;
    let currentLoopIndex = 0;

    function getLoop() {
        const stored = localStorage.getItem(STORAGE_KEYS.LOOP);
        return stored ? JSON.parse(stored) : DEFAULTS.LOOP;
    }

    function saveLoop(loopArray) {
        localStorage.setItem(STORAGE_KEYS.LOOP, JSON.stringify(loopArray));
    }

    function startLoop() {
        const loop = getLoop();
        if (loop.length === 0) {
            loopDisplay.textContent = "Add affirmations to start the loop.";
            return;
        }

        clearInterval(loopInterval);
        showAffirmation(loop[currentLoopIndex % loop.length]);

        loopInterval = setInterval(() => {
            currentLoopIndex++;
            showAffirmation(loop[currentLoopIndex % loop.length]);
        }, 5000);
    }

    function showAffirmation(text) {
        // Fade out
        loopDisplay.style.opacity = 0;

        setTimeout(() => {
            loopDisplay.textContent = text;
            loopDisplay.style.opacity = 1;

            // Reset progress animation
            loopProgress.style.transition = 'none';
            loopProgress.style.width = '0%';
            setTimeout(() => {
                loopProgress.style.transition = 'width 5s linear';
                loopProgress.style.width = '100%';
            }, 50);

        }, 500);
    }

    btnEditLoop.addEventListener('click', () => {
        const isHidden = loopEditor.classList.contains('hidden');
        if (isHidden) {
            loopEditor.classList.remove('hidden');
            affirmationContainer.classList.add('hidden');
            loopInput.value = getLoop().join('\n');
            btnEditLoop.textContent = "Cancel";
            clearInterval(loopInterval);
        } else {
            loopEditor.classList.add('hidden');
            affirmationContainer.classList.remove('hidden');
            btnEditLoop.textContent = "Edit";
            startLoop();
        }
    });

    btnSaveLoop.addEventListener('click', () => {
        const lines = loopInput.value.split('\n').filter(line => line.trim() !== '');
        saveLoop(lines);
        loopEditor.classList.add('hidden');
        affirmationContainer.classList.remove('hidden');
        btnEditLoop.textContent = "Edit";
        currentLoopIndex = 0;
        startLoop();
    });


    // --- The Rewrite Logic ---
    const step1 = document.getElementById('rewrite-step-1');
    const step2 = document.getElementById('rewrite-step-2');
    const negativeInput = document.getElementById('negative-thought');
    const positiveInput = document.getElementById('positive-thought');
    const btnBurn = document.getElementById('btn-burn');
    const btnImprint = document.getElementById('btn-imprint');

    btnBurn.addEventListener('click', () => {
        if (!negativeInput.value.trim()) return;

        // Visual burn effect
        negativeInput.style.transition = "all 0.5s ease";
        negativeInput.style.backgroundColor = "#500";
        negativeInput.style.color = "#000";
        negativeInput.style.transform = "scale(0.95)";

        setTimeout(() => {
            step1.classList.add('hidden');
            step2.classList.remove('hidden');
            negativeInput.value = ''; // Clear for next time
            negativeInput.style = ''; // Reset styles
        }, 500);
    });

    btnImprint.addEventListener('click', () => {
        if (!positiveInput.value.trim()) return;

        // Visual imprint effect
        positiveInput.style.transition = "all 0.5s ease";
        positiveInput.style.backgroundColor = "#050";

        setTimeout(() => {
            const newAffirmation = positiveInput.value.trim();
            if (confirm("Add this truth to your Loop?")) {
                const currentLoop = getLoop();
                currentLoop.push(newAffirmation);
                saveLoop(currentLoop);
                // Restart loop if active
                if (!loopEditor.classList.contains('hidden')) {
                     // If editing, update textarea
                     loopInput.value = currentLoop.join('\n');
                } else {
                    startLoop();
                }
            }

            // Reset
            step2.classList.add('hidden');
            step1.classList.remove('hidden');
            positiveInput.value = '';
            positiveInput.style = '';
        }, 500);
    });


    // --- The Vault Logic ---
    const visionBoard = document.getElementById('vision-board');
    const btnAddVision = document.getElementById('btn-add-vision');
    const visionAddPanel = document.getElementById('vision-add-panel');
    const visionUrlInput = document.getElementById('vision-url');
    const btnSaveVision = document.getElementById('btn-save-vision');

    function getVault() {
        const stored = localStorage.getItem(STORAGE_KEYS.VAULT);
        return stored ? JSON.parse(stored) : DEFAULTS.VAULT;
    }

    function saveVault(vaultArray) {
        localStorage.setItem(STORAGE_KEYS.VAULT, JSON.stringify(vaultArray));
    }

    function renderVault() {
        const vault = getVault();
        visionBoard.innerHTML = '';
        vault.forEach((url, index) => {
            const div = document.createElement('div');
            div.className = 'vision-item';

            const img = document.createElement('img');
            img.src = url;
            img.alt = "Vision";
            img.onerror = function() { this.src = 'https://via.placeholder.com/150?text=Error'; };

            div.appendChild(img);

            // Double click to delete
            div.addEventListener('dblclick', () => {
                if(confirm("Remove this image?")) {
                    vault.splice(index, 1);
                    saveVault(vault);
                    renderVault();
                }
            });

            visionBoard.appendChild(div);
        });
    }

    btnAddVision.addEventListener('click', () => {
        visionAddPanel.classList.toggle('hidden');
    });

    btnSaveVision.addEventListener('click', () => {
        const url = visionUrlInput.value.trim();
        if (url) {
            const vault = getVault();
            vault.push(url);
            saveVault(vault);
            renderVault();
            visionUrlInput.value = '';
            visionAddPanel.classList.add('hidden');
        }
    });


    // --- Initialization ---
    startLoop();
    renderVault();
});
