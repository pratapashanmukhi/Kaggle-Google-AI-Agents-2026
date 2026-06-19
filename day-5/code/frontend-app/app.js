// JavaScript Logic for Expense Agent Codelab Dashboard

document.addEventListener('DOMContentLoaded', () => {
    const expenseForm = document.getElementById('expense-form');
    const amountInput = document.getElementById('amount');
    const merchantInput = document.getElementById('merchant');
    const categoryInput = document.getElementById('category');
    const receiptInput = document.getElementById('receipt');
    const dropzone = document.getElementById('dropzone');
    const fileNameDiv = document.getElementById('file-name');
    
    const budgetBalance = document.getElementById('budget-balance');
    const budgetProgress = document.getElementById('budget-progress');
    const transactionRows = document.getElementById('transaction-rows');
    const traceConsole = document.getElementById('trace-console');
    const btnSubmit = document.getElementById('btn-submit');

    let currentBudget = 454.50; // Starting budget based on Day 1-4 activities
    const maxBudget = 1000.00;

    // File Drag and Drop / Selection handlers
    dropzone.addEventListener('click', () => receiptInput.click());
    
    receiptInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            fileNameDiv.textContent = `Attached: ${e.target.files[0].name}`;
        }
    });

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = '#3b82f6';
        dropzone.style.background = 'rgba(59, 130, 246, 0.05)';
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.style.borderColor = 'rgba(255, 255, 255, 0.15)';
        dropzone.style.background = 'transparent';
    });

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'rgba(255, 255, 255, 0.15)';
        dropzone.style.background = 'transparent';
        if (e.dataTransfer.files.length > 0) {
            receiptInput.files = e.dataTransfer.files;
            fileNameDiv.textContent = `Attached: ${e.dataTransfer.files[0].name}`;
        }
    });

    // Form Submission
    expenseForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const amount = parseFloat(amountInput.value);
        const merchant = merchantInput.value;
        const category = categoryInput.value;
        const filename = receiptInput.files[0] ? receiptInput.files[0].name : "receipt_scan.png";

        // Prevent double submits
        btnSubmit.disabled = true;
        btnSubmit.textContent = "Agent executing...";

        runAgentReasoning(merchant, category, amount, filename);
    });

    // Simulated Agentic Reasoning Trace (Cloud Run Simulation)
    async function runAgentReasoning(merchant, category, amount, filename) {
        traceConsole.innerHTML = ""; // Clear console
        
        const logs = [
            { type: 'thought', text: `[Thought] Received new expense submission. Merchant: '${merchant}', Amount: $${amount.toFixed(2)}, Category: '${category}'. Initiating security check.` },
            { type: 'action', text: `[Act] Calling policy tool: check_input_authenticity(file='${filename}')...` },
            { type: 'observation', text: `[Observe] File hash verified. Zero injection threats detected.` },
            { type: 'thought', text: `[Thought] Receipt structure looks authentic. Now executing Model Context Protocol (MCP) OCR tool to extract receipt text metadata.` },
            { type: 'action', text: `[Act] Calling MCP Tool: extract_receipt_fields(file='${filename}')...` },
            { type: 'observation', text: `[Observe] OCR matched values -> Merchant: '${merchant}', Total Amount: $${amount.toFixed(2)}.` },
            { type: 'thought', text: `[Thought] Receipt validation succeeded. Checking if budget balance covers the requested $${amount.toFixed(2)} for the department.` },
            { type: 'action', text: `[Act] Calling MCP Tool: fetch_remaining_budget()...` },
            { type: 'observation', text: `[Observe] Current department budget balance remaining: $${currentBudget.toFixed(2)}.` }
        ];

        // Output lines sequentially with human-like latency delays
        for (const log of logs) {
            appendConsoleLine(log.type, log.text);
            await sleep(650);
        }

        // Final decision
        await sleep(400);
        if (amount <= currentBudget) {
            currentBudget -= amount;
            
            // Append success logic
            appendConsoleLine('thought', `[Thought] Budget is sufficient ($${amount.toFixed(2)} <= $${(currentBudget + amount).toFixed(2)}). Generating approval manifest.`);
            await sleep(400);
            appendConsoleLine('success', `[Success] Expense approved! Dispatched Cloud Event notification. Budget balance decremented.`);
            
            // Update UI
            updateUI(merchant, category, amount, 'APPROVED');
        } else {
            // Append failure logic
            appendConsoleLine('thought', `[Thought] Amount ($${amount.toFixed(2)}) exceeds current remaining budget balance ($${currentBudget.toFixed(2)}).`);
            await sleep(400);
            appendConsoleLine('error', `[Error] Submission declined: INSUFFICIENT_BUDGET_BALANCE. Triggered notification to Finance Auditor.`);
            
            updateUI(merchant, category, amount, 'DECLINED');
        }

        // Reset submit button
        btnSubmit.disabled = false;
        btnSubmit.textContent = "Submit to Cloud Agent";
        expenseForm.reset();
        fileNameDiv.textContent = "";
    }

    // Helper to print a line in console
    function appendConsoleLine(type, text) {
        const div = document.createElement('div');
        div.className = `console-line ${type}`;
        div.textContent = text;
        traceConsole.appendChild(div);
        traceConsole.scrollTop = traceConsole.scrollHeight;
    }

    // Updates budget and appends rows to processed table
    function updateUI(merchant, category, amount, status) {
        // Update budget text
        budgetBalance.textContent = `$${currentBudget.toFixed(2)}`;
        
        // Update progress bar
        const progressPercentage = (currentBudget / maxBudget) * 100;
        budgetProgress.style.width = `${progressPercentage}%`;

        // Prepend new transaction row
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${merchant}</td>
            <td>${category}</td>
            <td>$${amount.toFixed(2)}</td>
            <td><span class="status ${status}">${status.charAt(0) + status.slice(1).toLowerCase()}</span></td>
        `;
        transactionRows.insertBefore(row, transactionRows.firstChild);
    }

    const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
});
