
// -----------------------------------
// Male v Female Bar Chart
// -----------------------------------

// Create function

function build_mfChart(sample) {
  
  var dataUrl = `https://asylumseekersapp.herokuapp.com/api/demographics`;
  // var dataUrl = "/Resources/demographics.csv"

  // var userInfo;
  d3.json(dataUrl).then((data) => {
    console.log(data)
    var mf_year = data.map(info => info.Year);
    var m_total = data.map(info => info.Male_total);
    var f_total = data.map(info => info.Female_total);
    var gender = [m_total, f_total];

    // Build Bar Chart
    var barData = [
      {
        y: mf_year,
        x: gender,
        text: "",
        type: "bar",
        orientation: "h",
      }
    ];

    var barLayout = {
      title: "Male vs Female",
      margin: { t: 30, l: 150 }
    };

    Plotly.newPlot("mf_bar", barData, barLayout);
    
  }
)}
// // -----------------------------------
// // Age Breakdown Bar Chart
// // -----------------------------------

//     var 


// // -----------------------------------
// // Top 25 Chart Countries Bar Graph
// // -----------------------------------

// // Create Function 
// function build_topChart(sample) {

//   var dataUrl = "/api/timeseries";

//   d3.json(dataUrl).then((data) => {

//     var top_year = data.map(info => info.year);
//     var host = data.map(info => info.host);
//     var value = data.map(info => info.value);

//     // Build Bar Chart
//     var barData = [
//       {
//         y: top_year,
//         x: value.slice(0, 25).reverse(),
//         text: host.slice(0, 25).reverse(),
//         type: "bar",
//         // orientation: "h",
//       }
//     ];

//     var barLayout = {
//       title: "Top 25 Host Countries",
//       margin: { t: 30, l: 150 }
//     };

//     Plotly.newPlot("bar", barData, barLayout);


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
  