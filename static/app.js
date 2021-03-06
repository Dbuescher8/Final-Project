function buildPlot(id,bardivid,scatterdivid) {
    d3.json("/api/v1.0/" + id).then((importedData) => {
        var data = importedData;

        data.sort(function(a, b) {
        return parseFloat(b.hp) - parseFloat(a.hp);
        });
    
        var trace1 = {
        y: data.map(row => row.hp),
        x: data.map(row => row.name),
        text: data.map(row => row.name),
        name: "Health",
        type: "bar",
        orientation: "v"
        };
    
        var chartData = [trace1];
    
        var layout = {
        title: "HP",
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 100
        },
        height: 600,
        width: 1200
        };
    
        Plotly.newPlot(bardivid, chartData, layout);

        var data2 = importedData;
        data2.sort(function(a, b) {
            return parseFloat(b.attack) - parseFloat(a.attack);
        });
        var trace2 = {
            x: data2.map(row=>row.name),
            y:data2.map(row=>row.attack),
            text: data2.map(row=>row.name),
            name: "Attack",
            type: 'scatter',
            mode: 'lines+markers'
        };
        var chartData2 = [trace2];
        var layout2 = {
            title: "Attack",
            margin: {
                l: 100,
                r: 100,
                t: 100,
                b: 100
            },
            height: 600,
            width: 1200
        };
        Plotly.newPlot(scatterdivid,chartData2,layout2);
  });
}

function plotInfo(id,divmetadata) {
    d3.json("/api/v1.0/" + id).then((importedData)=> {
        var data = importedData;
        data.sort(function(a, b) {
            return parseFloat(b.name) - parseFloat(a.name);
            });

        var pokeSet = d3.select(`#${divmetadata}`);
        pokeSet.html("");
        
        Object.entries(data).forEach(function(Pokemon) {
            console.log(Pokemon);
            pokeSet.append("h5").text(Pokemon[1]["name"].toUpperCase() + "\n");
            pokeSet.append("img").attr("src", `static/images/${id}.png`)
            
        });
    });
}

function init() {
    var dropdownMenu = d3.select("#selDataset");
    d3.json("/api/v1.0/pokemon").then((data)=>{
        var pokeList = []
        data.forEach(function(name) {
            if (pokeList.indexOf(name.name)<0) {
                pokeList.push(name.name)
            }
        });
        dropdownMenu.append("option").text("-select-").property("value");
        pokeList.forEach(function(name) {
            dropdownMenu.append("option").text(name).property("value");
        });
        dropdownMenu.on("change",function(){
            console.log(this.value)
            buildPlot(this.value,"bar","scatter")
            plotInfo(this.value,"sample-metadata")
        });
    var dropdownMenu2 = d3.select("#selDataset2");
        var pokeList2 = []
        data.forEach(function(name) {
            if (pokeList2.indexOf(name.name)<0) {
                pokeList2.push(name.name)
            }
        });
        dropdownMenu2.append("option").text("-select-").property("value");
        pokeList2.forEach(function(name) {
            dropdownMenu2.append("option").text(name).property("value");
        });
        // Binding event
        dropdownMenu2.on("change",function(){
            console.log(this.value)
            buildPlot(this.value,"bar2","scatter2")
            plotInfo(this.value,"sample-metadata2")
        });
    });
    var fightButton = d3.select("#battle");
    fightButton.on("click",function() {
        var pokemon1 = d3.select("#dropdownMenu").value;
        var pokemon2 = d3.select("#dropdownMenu2").value;
        d3.json("/api/v1.0/battle/" + pokemon1 + "/" + pokemon2).then((data)=>{
            console.log(data) 
        var ult = d3.select("Win/Loss append");
        ult.html("");
            console.log(Pokemon);
            ult.append("h3").text(pokemon1);
            ult.append("h5").text(data);
        });
    });
}

// Insert table for selected pokemon stats upon dropdown selection
// Format charts to show selected pokemon on same chart for each stat



init();

let animation = anime({
    targets: '.letter',
    opacity: 1,
    translateY: 50, 
    rotate: {
      value: 360,
      duration: 2000,
      easing: 'easeInExpo'
    }, 
    scale: anime.stagger([0.7, 1], {from: 'center'}), 
    delay: anime.stagger(100, {start: 1000}), 
    translateX: [-10, 30]
  });                