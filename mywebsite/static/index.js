// create Bar chart from csv file, using default options
new roughViz.Bar({
    element: '#viz0', // container selection
    data: 'https://raw.githubusercontent.com/jwilber/random_data/master/flavors.csv',
    labels: 'flavor',
    values: 'price',
    margin: { top: 20, right: 20, bottom: 45, left: 25 },
    color: 'pink',
    roughness: 3
});

// create Donut chart using defined data & customize plot options
new roughViz.Donut(
    {
      element: '#viz1',
      data: {
        labels: ['North', 'South', 'East', 'West'],
        values: [10, 5, 8, 3]
      },
      title: "Regions",
      roughness: 8,
      colors: ['pink', 'orange', 'blue', 'skyblue'],
      stroke: 'black',
      strokeWidth: 3,
      fillStyle: 'cross-hatch',
      fillWeight: 2,
    }
  ); 

console.log("Hello World stocks visualization!");