
var XLSX = require('xlsx')
var fs = require('fs')
var circleToPolygon = require('circle-to-polygon')


var workbook = XLSX.readFile('safe_level2_distance.xlsx')
var xlData = XLSX.utils.sheet_to_json(workbook.Sheets["Sheet1"]);
console.log(xlData[0].x);

var data = new Array();

for(var i =0; i < 50; i++) {
    let polygon = circleToPolygon([xlData[i].x,xlData[i].y],xlData[i].radius,32);
    data[i] = {
        type : "Feature",
        geometry : polygon
    }
}
var geojson = {
    type : "FeatureCollection",
    features : data
}

var pleae = JSON.stringify(geojson);
console.log(pleae);
// var createGeoJSONCircle = function(center, radiusInKm, points) {
//     if(!points) points = 64;

//     var coords = {
//         latitude: center[1],
//         longitude: center[0]
//     };

//     var km = radiusInKm;

//     var ret = [];
//     var distanceX = km/(111.320*Math.cos(coords.latitude*Math.PI/180));
//     var distanceY = km/110.574;

//     var theta, x, y;
//     for(var i=0; i<points; i++) {
//         theta = (i/points)*(2*Math.PI);
//         x = distanceX*Math.cos(theta);
//         y = distanceY*Math.sin(theta);

//         ret.push([coords.longitude+x, coords.latitude+y]);
//     }
//     ret.push(ret[0]);

//     return {
//         "type": "geojson",
//         "data": {
//             "type": "FeatureCollection",
//             "features": [{
//                 "type": "Feature",
//                 "geometry": {
//                     "type": "Polygon",
//                     "coordinates": [ret]
//                 }
//             }]
//         }
//     };
// };
// var geojson = new Array();
// var data = new Array();
// for(var i =0; i < 50; i++) {
//     geojson[i] = createGeoJSONCircle([xlData[i].x,xlData[i].y],xlData[i].radius);
//     data[i] = JSON.stringify(geojson[i]);
//     console.log(data[i]);
// }
// //let data = JSON.stringify(geojson[0]);
fs.writeFileSync('level2_distance.geojson',pleae);


