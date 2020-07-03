import csv

data_analysis = []

with open('TestAnalysisData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        data_analysis.append(row)

data_analysis_chart = [data_analysis[0]]

for row in data_analysis[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    number_of_asserts = int(row[1])
    number_of_failed_asserts = int(row[2])
    data_analysis_chart.append([test_name, number_of_asserts, number_of_failed_asserts])

from string import Template

html_string = Template("""<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var data = google.visualization.arrayToDataTable([
    $labels,
    $data
      ],
      false); // 'false' means that the first row contains labels, not data.
     var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  } 
</script>
</head>
<body>
<div id="chart_div" style="width:800; height:1400"></div>
</body>
</html>""")

html_data_str = ''
for row in data_analysis_chart[1:]:
    html_data_str += '%s,\n' % row

completed_html = html_string.substitute(labels=data_analysis_chart[0], data=html_data_str)

with open('analysis_chart.html', 'w') as f:
    f.write(completed_html)
