// //
// // $( document ).ready(function () {
// //   $(".moreBox").slice(0,9).show();
// //     if ($(".blogBox").length !== 0) {
// //       $("#loadMore").show();
// //     }
// //     $("#loadMore").on('click', function (e) {
// //       e.preventDefault();
// //       $(".moreBox").slice(0, 6).slideDown();
// //       if ($(".moreBox:hidden").length === 0) {
// //         $("#loadMore").fadeOut('slow');
// //       // }
// //     });
// //   });
// function loadData(){
// $( document ).ready(function () {
//   $(".moreBox").slice(0, 12).show();
//     if ($(".blogBox").length !== 0) {
//       $("#loadMore").show();
//     }
//     $("#loadMore").on('click', function (e) {
//       e.preventDefault();
//       $(".moreBox").slice(0, 6).slideDown();
//       // if ($(".moreBox:hidden").length == 0) {
//       //   $("#loadMore").fadeOut('slow');
//       // }
//        });
//   });
// }
// //
// $(function () {
//     $(".moreBox").slice(0, 3).show();
//     $("#loadMore").on('click', function (e) {
//         e.preventDefault();
//         $('.moreBox:hidden').slice(0, 4).slideDown();
//         if ($(".moreBox:hidden").length === 0) {
//             $("#loadmore").fadeOut('slow');
//             $('#loadMore').replaceWith("<p class='see-all-btn'>No More</p>");
//         }
//         $('html,body').animate({
//             scrollTop: $(this).offset().down
//         }, 1500);
//     });
// });


$( document ).ready(function () {
  $(".moreBox").slice(0, 8).show();
    // if ($(".blogBox:hidden").length != 0) {
    if ($(".moreBox:hidden").length !== 0) {
      $("#loadMore").show();
    }
    $("#loadMore").on('click', function (e) {
      e.preventDefault();
      $(".moreBox:hidden").slice(0, 4).slideDown();
      if ($(".moreBox:hidden").length === 0) {
        $("#loadMore").fadeOut('slow');
      }
    });
  });