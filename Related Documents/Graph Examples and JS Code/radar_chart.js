//config................................................................
const radarChart = {
  type: 'radar',
  data: data,
  options: {
    elements: {
      line: {
        borderWidth: 3
      }
    }
  },
};

//setup................................................................
const data = {
    labels: [
      'Cost of Living to Income Ratio', // replace with 'expenses' variable
      'Housing Expense to Income Ratio',
      'Health Care Index',
      'Crime Index',
      'Safety Index',
      'Food Option Index',
      'Overall Quality Index'
    ],
    datasets: [{
      label: 'Roanoke', // replace with selected city 1
      data: [65, 59, 90, 81, 56, 55, 40], // replace with 'id' of matching 'expense' variable
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    }, {
      label: 'Washington D.C.', // replace with selected city 2
      data: [40, 55, 56, 88, 90, 59, 65],
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgb(54, 162, 235)',
      pointBackgroundColor: 'rgb(54, 162, 235)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(54, 162, 235)'
      }, {
      label: 'Philadelphia', // replace with selected city 3
      data: [88, 56, 59, 90, 65, 40, 56],
      fill: true,
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgb(75, 192, 192)',
      pointBackgroundColor: 'rgb(75, 192, 192)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(75, 192, 192)'
      }]
  };
