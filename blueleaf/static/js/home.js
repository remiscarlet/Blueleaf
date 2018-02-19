var plot_dom, plot, redrawPlot;
$(document).ready(function () {
	console.log("HALLOOOO");
	TESTER = document.getElementById('tester');
	plot_dom = $('#plot-usage-tracker');
	var layout = {
	  autosize: true,
	  //width: plot_dom.width(),
	  //height: plot_dom.height(),
	  margin: {
	  },
	  paper_bgcolor: 'rgba(0,0,0,0)',
	  plot_bgcolor: '#355ad9'
	};

	setTimeout(function () {
	plot = Plotly.plot( plot_dom.get(0), [{
	x: [1, 2, 3, 4, 5],
	y: [1, 2, 4, 8, 16] }], layout );
	}, 2000);

	redrawPlot = function () {
		console.log("A");
		var params = {
			width: plot_dom.width(),
			height: plot_dom.height(),
		}
		Plotly.relayout(plot_dom.get(0), params)
	}
	$(window).resize(redrawPlot);
});
