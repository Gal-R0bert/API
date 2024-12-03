const ctx = document.getElementById('kLineChart').getContext('2d');
const kLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // Add your labels here
        datasets: [{
            label: 'K-Line Data',
            data: [], // Add your data here
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'minute'
                }
            }
        }
    }
});

// Fetch data from your API and update the chart
fetch('http://127.0.0.1:5000/api/k-line-data')
    .then(response => response.json())
    .then(data => {
        kLineChart.data.labels = data.labels;
        kLineChart.data.datasets[0].data = data.values;
        kLineChart.update();
    });