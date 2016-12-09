$(document).ready(function(){
  /////////////////////
  // Global variables
  var viz, workbook, activeSheet
  // console.log('Here');
  // console.log("{{viz}}")

  // Reload the viz
  $('#resetViz').click(function(){
    console.log('here')
    initViz()
  });
  // Initiate the viz
  initViz();
  // function called by viz on marks being selected in the workbook
  function onMarksSelection(marksEvent) {
    $('#dataTarget').html('');
    return marksEvent.getMarksAsync().then(reportSelectedMarks);
  }
  function reportSelectedMarks(marks) {
      var html = "";
      for (var markIndex = 0; markIndex < marks.length; markIndex++) {
          var pairs = marks[markIndex].getPairs();
          for (var pairIndex = 0; pairIndex < pairs.length; pairIndex++) {
              var pair = pairs[pairIndex];
              if (pairIndex==0) {
                var count = markIndex + 1
                var end = marks.length
                html += pair.fieldName + " " + count + " of " + end + ": ";

              }
              else {
                html += pair.fieldName + " "  +  ": ";
              }
              html += "<b>" + pair.formattedValue + "</b><br/>";
              if (pairIndex+1==pairs.length){html += "<br/>"}
          }
      }
      console.log(html)
      $('#dataTarget').append(html);
      $('#dataTarget').show();
  }

  function initViz(){
       var placeholderDiv = document.getElementById("tableauViz");
       var url = "https://public.tableau.com/views/IHC" + chart + "?:embed=y&:display_count=yes";
       var options = {
            hideTabs: true,
            hideToolbar: true,
            onFirstInteractive: function () {
                  workbook = viz.getWorkbook();
                  activeSheet = workbook.getActiveSheet();
            }
       };
       viz = new tableauSoftware.Viz(placeholderDiv, url, options);
      // Add event listener
      viz.addEventListener(tableauSoftware.TableauEventName.MARKS_SELECTION, onMarksSelection);
  };
});
