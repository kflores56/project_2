
// -----------------------------------
// Male v Female Bar Chart
// -----------------------------------
var dataUrl = "/api/demographics"
d3.json(dataUrl).then((data) => {
  console.log(data)
})

// // Create function
// function build_mfChart() {
  
  var dataUrl = "http://127.0.0.1:5000/api/demographics";
  // d3.json(dataUrl).then(function(data){
  //   console.log(data)
  // })
//   // var dataUrl = "/Resources/demographics.csv"

//   // var userInfo;
  d3.json(dataUrl).then((data) => {
    console.log(data)
    var mf_year = data.map(info => info.year);
    var m_total = data.map(info => info.m_total);
    var f_total = data.map(info => info.f_total);
    var country = data.map(info => info.host_country);
    // var gender = [m_total, f_total];

    // Build Bar Chart
    var barData = [
      {
        x: m_total,f_total,
        y: country,
        //text: " ",
        type: "bar",
        orientation: "h",
      }
    ];

    var barLayout = {
      title: "Total Assylum Seekers by Year",
      margin: { t: 30, l: 150 }
    };

    Plotly.newPlot("mf_bar", barData, barLayout);
  });

// // -----------------------------------
// // Male vs Female Bubble Chart
// // -----------------------------------

// function buildCharts(sample) {
  
  var dataUrl = "http://127.0.0.1:5000/api/demographics";

  d3.json(dataUrl).then((data) => {

    // var resultArray = data.results;
    // userInfo = data.user;

    // var mf_year = data.map(info => info.year);
    var m_total = data.map(info => info.m_total);
    var f_total = data.map(info => info.f_total);
    var country = data.map(info => info.host_country);

    // Build a Bubble Chart
    var bubbleLayout = {
      title: "Male vs Female",
      margin: { t: 0 },
      hovermode: "closest",
      xaxis: { title: "Country" },
      yaxis: { title: "Number of People"},
      margin: { t: 30}
    };
    var bubbleData = [
      {
        x: m_total, f_total,
        y: country,
        text: country,
        mode: "markers",
        marker: {
          size: (m_total/1,000),
          // color: m_total,
          colorscale: "Earth"
        }
      }
    ];

    Plotly.newPlot("bubble", bubbleData, bubbleLayout);
  })


// // -----------------------------------
// // Top 25 Chart Countries Bar Graph
// // -----------------------------------

// Create Function 
// function build_topChart(sample) {

  var dataUrl = "http://127.0.0.1:5000//api/timeseries";

  d3.json(dataUrl).then((data) => {

    // var top_year = data.map(info => info.year);
    var host = data.map(info => info.host_country);
    var value = data.map(info => info.value);

    // Build Bar Chart
    var barData = [
      {
        y: value,
        x: host.slice(0, 25),
        text: host.slice(0, 25),
        type: "bar",
        // orientation: "h",
      }
    ];

    var barLayout = {
      title: "Top 25 Host Countries for Past 5 Years",
      margin: { t: 30, l: 150 }
    };

    Plotly.newPlot("top_bar", barData, barLayout);
  });


// // Dropdown function 
// function init() {
//   // Grab a reference to the dropdown select element
//   var selector = d3.select("#selDataset");

//   // Use the list of sample names to populate the select options
//   d3.json("/api/v1.0/ids").then((data) => {
//     var sampleNames = data;

//     // Use the first sample from the list to build the initial plots
//     var firstSample = sampleNames[0];
//     var userData = buildCharts(firstSample);

//   });
// }

// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected
//   console.log(`change ${{newSample}}`)
//   buildCharts(newSample);

// }

// // Initialize the dashboard
// init():
