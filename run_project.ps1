Write-Host "Step 1: Cleaning data..."
python .\python\clean_data.py

Write-Host "`nStep 2: Running analysis..."
python .\python\analysis.py

Write-Host "`nDone. Check the data and outputs folders."
