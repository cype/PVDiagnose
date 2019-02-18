//load csv data file and generate elements to bind for visualization
d3.csv("data.csv",function(csvFile){
    
    //map csv data rows to JS Objects
    var data = csvFile.map(function(d){
        var dataItem = {};

        dataItem.FoodType = d.FoodType;   

        for(var i= 1974; i < 2015; i++){
          var year = "" + i;
          dataItem[year] = +d[year];
          //dataItem.disabled = true; //disable all selections as default
        }

        return dataItem;
    })

    
    //update chart values to match data for year selected
    d3.selectAll("input").on("change", updateChart);
    
    //redraw chart with new values for the year
    function updateChart(){
        var value = this.value;

        var chart;
        nv.addGraph(function() {
            //define attributes of chart to draw
            var chart = nv.models.pieChart()
                .title(value)
                .id("donut")
                .x(function(d) { return d.FoodType })
                .y(function(d) { return d[value] })
                .showLegend(true)
                .legendPosition("right")
                .showLabels(true)     
                .labelThreshold(.01)  //minimum slice size for showing label (based on type)
                .labelType("percent") //type of data for label (Can be "key", "value" or "percent")
                .donut(true)          //turn pie chart to donut chart
                .donutRatio(0.35)     //size of donut hole
                .margin({"left":5,"right":5,"top":10,"bottom":10})
                ;
          
            //draw chart with data on selected svg, and transition if previously drawn
            d3.select("#chart")
                .datum(data)
                .transition().duration(400)
                .call(chart);

            d3.selectAll(".nv-pieWrap").attr("transform", "translate(-50,0)");
            //d3.select(".nv-legendWrap").attr("transform", "translate(500,50)");
            return chart;
        });    

    }
    

});