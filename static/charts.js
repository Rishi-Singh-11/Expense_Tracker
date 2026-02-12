async function loadCategoryChart() {
    const response = await fetch('/api/category-data');
    const data = await response.json();
    
    const ctx = document.getElementById('categoryChart');
    if (!ctx || data.categories.length === 0) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.categories,
            datasets: [{
                data: data.amounts,
                backgroundColor: ['#6366f1', '#10b981', '#f59e0b', '#3b82f6', '#ef4444', '#8b5cf6'],
                borderWidth: 0,
                hoverOffset: 10
            }]
        },
        options: {
            cutout: '70%',
            plugins: {
                legend: { position: 'bottom', labels: { padding: 20, usePointStyle: true } }
            }
        }
    });
}

function confirmDelete(id) {
    if (confirm("Delete this transaction?")) {
        window.location.href = "/delete/" + id;
    }
}

document.addEventListener('DOMContentLoaded', loadCategoryChart);