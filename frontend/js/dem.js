$(document).ready(function(){
   $("#kitchen_color").change(function(){
     $("img[name=mapp]").attr("src",$(this).val());

   });

});

//
// function showimage() {
//     if (!document.images) return
//     document.images.map.src = document.picture.options[document.picture.selectedIndex].value
// }


//
// function changeImage(a) {
//        document.getElementById("img").src=a;
//    }
//
// var pictureList = [
//     "http://lorempixel.com/400/200/sports/1",
//     "http://lorempixel.com/400/200/sports/2",
//     "http://lorempixel.com/400/200/sports/3",
//     "http://lorempixel.com/400/200/sports/4",
//     "http://lorempixel.com/400/200/sports/5", ];
//
// $('#dropdownMenu1').change(function () {
//     var val = parseInt($('#dropdownMenu1').val());
// document.getElementById("img").src=pictureList[val];
//     // $('map').attr("src",pictureList[val]);
// });
