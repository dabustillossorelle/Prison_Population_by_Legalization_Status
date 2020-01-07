async function makePlot(){
    const defaultURL = "/population_in_private_prison";
    let data = await d3.json(defaultURL);
    data = [data];
    const layout = { margin: { t: 30, b: 100 } };
    Plotly.plot("bar", data, layout);
}

function updatePlotly(newdata) {
    Plotly.restyle("bar", "x", [newdata.x]);
    Plotly.restyle("bar", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
async function getData(route) {
    console.log(route);
    let data = await d3.json(`/${route}`);
    updatePlotly(data);
}

makePlot();