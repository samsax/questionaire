
 $(function () {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.defaults.xsrfCookieName = "csrftoken"
 axios.post(get_results, {})
        .then(function(res) {
            if(res.data.success)
            createHighChart(res.data.categories, res.data.series)
            else
                Swal.fire(
                    res.data.message,
                    '',
                    'error'
                )
        })
        .catch(function(err) {
            Swal.fire(
                res.data.message,
                '',
                'error'
            )
            })
        
});
function createHighChart(categories,series){
    Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Resultados test por día'
    },
    xAxis: {
        categories
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
    series: series
});
}
