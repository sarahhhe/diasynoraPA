function openSearch() {
  document.getElementById("myOverlay").style.display = "block";
}

function closeSearch() {
  document.getElementById("myOverlay").style.display = "none";
}
$(document).ready(function(){
  $(".open-event-modal").click(function(){
    console.log("open event modal")
    document.getElementById("event-modal-label").append($(this).attr('data-id'));
    document.getElementById("event-modal-body").append($(this).attr('id'));
    console.log($(this).attr('data-id'));
    console.log($(this).attr('id'));
  });
  $(".close-event-modal").click(function(){
    console.log("close event modal")
    document.getElementById("event-modal-label").innerHTML = "";
    document.getElementById("event-modal-body").innerHTML = "";
  });
});

$(document).ready(function(){
  $(".open-campaign-modal").click(function(){
    console.log("open campaign modal")
    document.getElementById("campaign-modal-label").append($(this).attr('data-id'));
    document.getElementById("campaign-modal-body").append($(this).attr('id'));
    console.log($(this).attr('data-id'));
    console.log($(this).attr('id'));
  });
  $(".close-campaign-modal").click(function(){
    console.log("close campaign modal")
    document.getElementById("campaign-modal-label").innerHTML = "";
    document.getElementById("campaign-modal-body").innerHTML = "";
  });
});

function changeBg(color,id){
  document.getElementById(id).style.backgroundColor = color;
  var elements = document.getElementsByTagName("a");
  for (i = 0; i < elements.length; i++){
  if (elements[i].id == id) {
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
