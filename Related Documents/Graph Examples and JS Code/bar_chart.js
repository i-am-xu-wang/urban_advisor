//config................................................................
const stackedBarChart = {
    type: 'bar',
    data: data,
    options: {
        indexAxis: 'y', // convert to horizontal bar chart
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true
            }
            // y: {beginAtZero: true} // convert to non-stacked bar chart
        }
    },
};
//setup................................................................
const data = {
    labels: [
        'Cost of Living to Income Ratio',
        'Housing Expense to Income Ratio',
        'Health Care Index',
        'Crime Index',
        'Safety Index',
        'Food Option Index',
        'Overall Quality Index'
    ],
    datasets: [{
        label: 'Roanoke',
        data: [65, 59, 80, 81, 56, 55, 40],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 99, 132, 0.2)'
        ],
        borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)',
            'rgb(255, 99, 132)'
        ],
        borderWidth: 1
    }, {
        label: 'Washington D.C.',
        data: [40, 55, 56, 88, 90, 59, 65],
        backgroundColor: [
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(54, 162, 235, 0.2)'
        ],
        borderColor: [
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)',
            'rgb(54, 162, 235)'
        ],
        borderWidth: 1
    }, {
        label: 'Philadelphia',
        data: [88, 56, 59, 90, 65, 40, 56],
        backgroundColor: [
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(75, 192, 192, 0.2)'
        ],
        borderColor: [
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)',
            'rgb(75, 192, 192)'
        ],
        borderWidth: 1
    }]
};