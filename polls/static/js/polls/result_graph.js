Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Stacked column chart'
    },
    xAxis: {
        categories: [1,2,3,4,5,6,7,8,9,10]
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Resultados test'
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            }
        }
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true
            }
        }
    },
    series: [{
        name: 'Sintomatología leve',
        data: [1,2,3,4,5,6,7,8,9,10]
    }, {
        name: 'Sintomatología grave',
        data: [0,0,0,4,5,6,7,8,9,10]
    }, {
        name: 'Casos de contacto',
        data: [1,1,1,1,1,1,0,2,0]
    }, {
        name: 'Diagnostico confirmado',
        data: [2,2,2,2,2,2,2,2,2,2]
    },
    ]
});