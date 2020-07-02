$(document).on("click", ".open-AddBookDialog", function () {
     var myBookId = $(this).data('id');
     $(".modal-body #bookId").val( myBookId );
});

function changeBg(color,id){
  document.getElementById(id).style.backgroundColor = color;
  var elements = document.getElementsByTagName("a");
  for (i = 0; i < elements.length; i++){
  if (elements[i].id == id) {
    console.log(elements[i].id)
    elements[i].style.backgroundColor = color;
   }
  else{
    elements[i].style.backgroundColor = "transparent";
  }
  }
}
$(document).ready(function(){

    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');

        if(value == "all")
        {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        }
        else
        {
//            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
//            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.'+value).hide('3000');
            $('.filter').filter('.'+value).show('3000');

        }
    });

    if ($(".filter-button").removeClass("active")) {
$(this).removeClass("active");
}
$(this).addClass("active");

});
