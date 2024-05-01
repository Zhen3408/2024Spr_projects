# 2024Spr_projects
## Environment Setup

To replicate the Conda environment, follow these steps:

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) if you haven't already.
2. Clone the repository or download the project files, including the `environment.yml` file.
3. Open your terminal and navigate to the project directory.
4. Create the Conda environment by running:

   ```bash
   conda env create -f environment.yml
5. Activate the environment:

   ```bash
   conda activate env-name
6. You are now ready to run the project file.



# Reference:
https://data.bls.gov/PDQWeb/ln
https://ec.europa.eu/eurostat/databrowser/view/tepsr_wc170__custom_11059624/default/table?lang=en
https://www.ethnicity-facts-figures.service.gov.uk/work-pay-and-benefits/unemployment-and-economic-inactivity/unemployment/latest/#data-sources
https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/timeseries/mgsx/lms
https://stats.oecd.org/viewhtml.aspx?datasetcode=EAG_NEAC&lang=en#
National Bureau of Statistics of China
https://www.stats.gov.cn/sj/





---

## Unit Tests for the `DownloadTable` Function in Scraper

The unit tests designed for the `DownloadTable` function cover various scenarios to ensure the function behaves as expected under different conditions:

1. **File Already Exists Test**:
   - This test verifies the behavior of the `DownloadTable` function when the target file already exists in the specified directory. The expected behavior is that the function should return immediately without performing any download actions. The `os.path.exists` function is mocked to return `True` to simulate the scenario where the file already exists.

2. **Successful Download Test**:
   - This test checks if the function correctly handles file downloads when all parameters are correct, and the network request succeeds. `requests.get` is mocked to return a successful response (HTTP status code 200), and the test checks if the function executes correctly without returning any errors. File writing operations are simulated using `mock_open`.

3. **Retry Logic Test**:
   - This test assesses whether the function properly retries the download attempt when it fails (due to network issues or server errors, for example). In this scenario, `requests.get` is set with a `side_effect` to return several failed responses (HTTP status code 404) consecutively, and the test verifies if the function retries the specified number of times. This test ensures that the retry mechanism works correctly in response to download failures.

These tests are intended to guarantee that the `DownloadTable` function operates reliably across different scenarios, helping to prevent issues during practical usage.

--- 
