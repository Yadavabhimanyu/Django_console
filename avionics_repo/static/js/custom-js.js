/*---------------- Customised JS ------------------*/

/* ---- Data tables starts ---- */
$(document).ready(function() {
    $('table.display').DataTable({
        "bDestroy": true,
        "ordering": false
    });
});
/* ---- Data tables ends ---- */


/* ---- MultiSelect starts ---- */
$(document).ready(function() {
    $('#multiple-checkboxes').multiselect({
      nonSelectedText: 'Select Roles', 
      includeSelectAllOption: true,
    });
});
/* ---- MultiSelect ends ---- */


/* ---- Add class starts ---- */
$(document).ready(function() {
    $('#multiple-checkboxes').next().addClass("multiDropDown");
});
/* ---- Add class ends ---- */


/* ---- Modal animation starts ---- */
$('.modal').on('show.bs.modal', function (e) {
    $(this).removeClass("zoomOut animated").addClass("zoomIn animated");
})

$('.modal').on('hide.bs.modal', function (e) {
    $(this).removeClass("zoomIn animated").addClass("zoomOut animated");
})
/* ---- Modal animation ends ---- */


/* ---- Export button and class change starts ---- */
$(document).ready(function($){
    $('#tabsProcess #dataTable_filter').append('<button class="export-button btn-sm btn-primary ml-2">Export</button>');
    $('#tabsProcess #dataTable_wrapper .row:first-child div[class^="col-"]:first-child').removeClass('col-sm-12 col-md-6').addClass('col-sm-12 col-md-4');
    $('#tabsProcess #dataTable_wrapper .row:first-child div[class^="col-"]:last-child').removeClass('col-sm-12 col-md-6').addClass('col-sm-12 col-md-8');
});
/* ---- Export button and class change ends ---- */


/* ---- Time picker starts ---- */
$(document).ready(function(){
    $('#input.timepicker').timepicker({});  
});

$('.timepicker').timepicker({
    timeFormat: 'h:mm p',
    interval: 30,
    minTime: '10',
    dynamic: false,
    dropdown: true,
    scrollbar: true 
});
/* ---- Time picker ends ---- */


/* ---- Date picker starts ---- */
$(document).ready(function(){
  $("#datepicker").datepicker({
    dateFormat: "yy-mm-dd"
  });

  $("#datepicker2").datepicker({
    dateFormat: "yy-mm-dd"
  });
});
/* ---- Date picker ends ---- */

/* ---- Add or Remove Forms starts ---- */
$(document).ready(function() {
    $(".add").click(function() {
        $("#original").clone()
            .removeAttr("id")
            .append( $('<a class="delete" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms");
    });

    $("body").on('click',".delete", function() {
        $(this).closest(".input").remove();
    });
});
/* ---- Add or Remove Forms ends ---- */

 
/* ---- Add or Remove Forms 2 starts ---- */
$(document).ready(function() {
    $(".add2").click(function() {
        $("#original2").clone()
            .removeAttr("id")
            .append( $('<a class="delete2" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms2");
    });

    $("body").on('click',".delete2", function() {
        $(this).closest(".input2").remove();
    });
});
/* ---- Add or Remove Forms 2 ends ---- */


/* ---- Add or Remove Forms 3 starts ---- */
$(document).ready(function() {
    $(".add3").click(function() {
        $("#original3").clone()
            .removeAttr("id")
            .append( $('<a class="delete3" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms3");
    });

    $("body").on('click',".delete3", function() {
        $(this).closest(".input3").remove();
    });
});
/* ---- Add or Remove Forms 3 ends ---- */


/* ---- Add or Remove Forms 4 starts ---- */
$(document).ready(function() {
    $(".add4").click(function() {
        $("#original4").clone()
            .removeAttr("id")
            .append( $('<a class="delete4" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms4");
    });

    $("body").on('click',".delete4", function() {
        $(this).closest(".input4").remove();
    });
});
/* ---- Add or Remove Forms 4 ends ---- */


/* ---- Add or Remove Forms 5 starts ---- */
$(document).ready(function() {
    $(".add5").click(function() {
        $("#original5").clone()
            .removeAttr("id")
            .append( $('<a class="delete5" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms5");
    });

    $("body").on('click',".delete5", function() {
        $(this).closest(".input5").remove();
    });
});
/* ---- Add or Remove Forms 5 ends ---- */


/* ---- Add or Remove Forms 6 starts ---- */
$(document).ready(function() {
    $(".add6").click(function() {
        $("#original6").clone()
            .removeAttr("id")
            .append( $('<a class="delete6" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms6");
    });

    $("body").on('click',".delete6", function() {
        $(this).closest(".input6").remove();
    });
});
/* ---- Add or Remove Forms 6 ends ---- */


/* ---- Add or Remove Forms 7 starts ---- */
$(document).ready(function() {
    $(".add7").click(function() {
        $("#original7").clone()
            .removeAttr("id")
            .append( $('<a class="delete7" href="#"><i class="fas fa-fw fa-minus-circle"></i></a>') )
            .appendTo("#additionalForms7");
    });

    $("body").on('click',".delete7", function() {
        $(this).closest(".input7").remove();
    });
});
/* ---- Add or Remove Forms 7 ends ---- */


/* ---- Datatable tabs starts ---- */
$(document).ready(function() {
    $('a[data-toggle="tab"]').on( 'shown.bs.tab', function (e) {
        $.fn.dataTable.tables( {visible: true, api: true} ).columns.adjust();
    });
});
/* ---- Datatable tabs ends ---- */


/* ---- Tabs to Accordion starts ---- */
$(document).ready(function() {
  $(".panel-heading").click(function () {
    $(".show").not(this).removeClass("show").next().slideUp(300);
    $(this).toggleClass("show").next().slideToggle(300);
  });
});
/* ---- Tabs to Accordion ends ---- */


/* ---- Radio Tabs starts ---- */
$('[name=tab]').each(function(i,d){
  var p = $(this).prop('checked');
//   console.log(p);
  if(p){
    $('article').eq(i).addClass('on');
  }    
});  

$('[name=tab]').on('change', function(){
  var p = $(this).prop('checked');
  
  // $(type).index(this) == nth-of-type
  var i = $('[name=tab]').index(this);
  
  $('article').removeClass('on');
  $('article').eq(i).addClass('on');
});
/* ---- Radio Tabs ends ---- */


/* ---- Stacked popup starts ---- */
//set button id on click to hide first modal
$(".newFieldPopUp").on( "click", function() {
    $('#exampleModalSchemaCreation').modal('hide');  
});

//trigger next modal
$(".newFieldPopUp").on( "click", function() {
    $('#exampleModalNewFieldCreation').modal('show');
});
/* ---- Stacked popup starts ---- */


/* ---- Stacked popup starts ---- */
//set button id on click to hide first modal
$(".billsEdit").on( "click", function() {
    $('#exampleModalNewFieldCreation').modal('hide');  
});

//trigger next modal
$(".billsEdit").on( "click", function() {
    $('#exampleModalTemplateConfigViewEdit').modal('show');
});


$(".okEdit").on( "click", function() {
    $('#exampleModalTemplateConfigViewEdit').modal('hide');
    $('.billAreaComment, .add6, .add7').css("display", "block");
    $('#exampleModalTemplateConfigView input, #exampleModalTemplateConfigView select').attr('disabled', false);
});


$(".okEdit").on( "click", function() {
    $('#exampleModalTemplateConfigView').modal('show');
});
/* ---- Stacked popup ends ---- */


/* ---- Tootip starts ---- */
$(function() {
  $('[data-toggle="popover"]').popover({
    trigger: 'hover'
  })
})
/* ---- Tootip ends ---- */


/* ---- div collapse starts ---- */
$(document).ready(function() {
   $(".taskCollapse").click(function(){
    $(this).toggleClass("active");
      $(".taskCollapseDiv").slideToggle("500");
    }); 
});
/* ---- div collapse ends ---- */


/* ---- Redirect to output details tab starts ---- */
$(document).ready(function() {
   $(".directToNextTab").click(function(){
      
      $('a[href$="taskExecuted"]').removeClass("active");
      $('a[href$="outputDetails"]').addClass("active");

      $("#taskExecuted").removeClass("active");
      $("#outputDetails").addClass("active");
      
    }); 
});
/* ---- Redirect to output details tab ends ---- */


/* ---- Custom scrollbar starts ---- */
(function($){
    $(window).on("load",function(){
        $(".modal-body").mCustomScrollbar({
            autoHideScrollbar:true
        });
    });
})(jQuery);
/* ---- Custom scrollbar ends ---- */


/* ------ View template DOM manipulation starts --------*/
$(".editBill").click(function() {
  $(".templateConfigViewModal input").attr('disabled', false);
})

$(".invoiceTemp .rawText").click(function() {
    $(".col").addClass("colCss");
    $(".rawTxt, .originalDoc").css("display", "block");
    $(".tempTest").css("display", "block");  
})

$(".rawTxtClose").click(function() {
  $(".rawTxt").css("display", "none");
})

$(".origDocClose").click(function() {
  $(".originalDoc").css("display", "none");
});

$(".rawText").click(function() {
    $(".tempAttr").removeClass("col-lg-6").addClass("col-lg-12");
    $(".tempFields").removeClass("col-lg-4").addClass("col-lg-6");
});

$(".rawTxtClose, .origDocClose").click(function() {
    $(".tempAttr").removeClass("col-lg-12").addClass("col-lg-6");
    $(".tempFields").removeClass("col-lg-6").addClass("col-lg-4");
    $(".tempFieldsOccr").removeClass("col-lg-6").addClass("col-lg-4");
    $(".tempTest").css("display", "none");
});
/* ------ View template DOM manipulation ends --------*/



$(document).ready(function () {
    $('#t1').on('change', function () {
    var num =$("div#clonedDiv").children().length
    var newNum = new Number (num +1 )
        $('#t1').clone(true, true).attr('name', 'projectfile'+newNum).appendTo('#clonedDiv').val("");

    });
});

$(document).ready(function () {
    $('#dropdown1').on('change', function () {
    var num =$("div#clonedDiv").children().length
    var newNum = new Number (num +1 )
        $('#dropdown1').clone(true, true).attr('name', 'projectfile'+newNum).appendTo('#clonedDiv2').val("");

    });
});

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });
    
    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});


$(document).ready(function() {

    $('#addTask').click(function(){

          var intId = $("#taskArea .w-row").length + 1 || 1;

          var presFields = $('<div class="w-row mb-4"><div class="col-12 taskLabel"><label>Task' + intId + '</label></div><div class="fieldsDiv"><div class="col-4"><label class="mb-0" for="selectFile' + intId + '">Select File <span class="text-color-red">*</span></label><input type="file" id="selectFile' + intId + '" name="selectFile' + intId + '" data-name="selectFile' + intId + '" required="" class="form-control select-field w-select"></div><div class="col-4"><label class="mb-0" for="selectRPA' + intId + '">Select RPA <span class="text-color-red">*</span></label><select id="selectRPA' + intId + '" name="selectRPA' + intId + '" data-name="selectRPA' + intId + '" required="" class="custom-select form-control select-RPA select-field w-select"><option value="">Select</option><option value="10 Days">10 Days</option><option value="20 Days">20 Days</option><option value="50 Days">50 Days</option><option value="0 Days">0 Days</option></select></div><div class="col-4"><label class="mb-0" for="selectPRY' + intId + '">Select Supply <span class="text-color-red">*</span></label><select id="selectPRY' + intId + '" name="selectPRY' + intId + '" data-name="selectPRY' + intId + '" required="" class="custom-select form-control select-PRY select-field w-select"><option value="">Select</option><option value="30 Days">30 Days</option><option value="60 Days">60 Days</option><option value="90 Days">90 Days</option><option value="180 Days">180 Days</option></select></div></div></div>');

        $('#taskArea').append(presFields);
    });

    $('#removeTask').click(function(){
          $("#taskArea .w-row:last").not(':first-child').remove();
    });

});










