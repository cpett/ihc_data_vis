$(document).ready(function(){
  /////////////////////
  // Global variables
  var viz, workbook, activeSheet

  // Reload the viz
  $('#resetViz').click(function(){
    console.log('here')
    initViz()
  });
  // Initiate the viz
  initViz();

  function initViz(){
       var placeholderDiv = document.getElementById("tableauViz");
       var url = "https://public.tableau.com/views/Savings_2/ProjectswithCostSavings?:embed=y&:display_count=yes";
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
      // viz.addEventListener(tableauSoftware.TableauEventName.MARKS_SELECTION, onMarksSelection);
  };
});
