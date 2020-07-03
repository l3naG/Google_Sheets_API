import csv

# final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

test_timing_data = []
charts = [["Test Name", "Diff from AVG"]]
spreadsheets = [["Test Name", "Current Runtime"]]

with open('TestTimingData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        test_timing_data.append(row)

for row in test_timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_runtime = float(row[1])
    average_runtime = float(row[2])
    diff_from_average = average_runtime - current_runtime
    charts.append([test_name, diff_from_average])
    spreadsheets.append([test_name, current_runtime])

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
<div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

chart_data_str = ''
for row in charts[1:]:
    chart_data_str += '%s\n' % row

completed_html = html_string.substitute(labels=charts[0], data=chart_data_str)

with open('test_data_chart.html', 'w') as f:
    f.write(completed_html)

