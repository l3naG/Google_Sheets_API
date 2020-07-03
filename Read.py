import csv

# final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

test_time_data = []
diff_time_chart = [["Test Name", "Diff from AVG"]]
current_runtime_data = [["Test Name", "Current Runtime"]]

with open('TestTimingData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        test_time_data.append(row)

for row in test_time_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_runtime = float(row[1])
    avg_runtime = float(row[2])
    diff_from_avg = avg_runtime - current_runtime
    diff_time_chart.append([test_name, diff_from_avg])
    current_runtime_data.append([test_name, current_runtime])

# print(diff_time_chart)
# print(current_runtime_data)

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

html_data_str = ''
for row in diff_time_chart[1:]:
    html_data_str += '%s,\n' % row
completed_html = html_string.substitute(labels=diff_time_chart[0], data=html_data_str)

with open('column_test_data_chart.html', 'w') as f:
    f.write(completed_html)
