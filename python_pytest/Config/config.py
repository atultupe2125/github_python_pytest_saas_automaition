class TestData:
    #Below are some Class Variable initialise
    CHROME_EXECUTABLE_PATH="/usr/local/bin/chromedriver"
    FIREFOX_EXECUTABLE_PATH="/usr/local/bin/geckodriver"
    Tealeaf_URL="https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs"
    #Tealeaf_URL="https://tealeaf-staging.goacoustic.com/webapp/login"
    #OPENCART_URL="https://qa-pages.tealeaf-aws.com/opencart/sdk-n/qa/index.php"
    OPENCART_URL = "http://10.235.137.37/opencart/upload/"
    #OPENCART_URL = "https://qa-pages.tealeaf-aws.com/opencart/sdk-n/staging/index.php"
    ADMIN_USER_NAME="massweather1980@zoho.eu"
    ADMIN_USER_PASSWORD="VWyjMkYnDI243019!"
    NORMAl_USER_NAME="kevin.mssgs@zoho.eu"
    NORMAL_USER_PASSSWORD="YhEJnhpbD121416$"
    EMAIl="atul.tupe@gmail.com"
    PASSWORD_OC="Kiran#2125"
    INPUT_QUANTITY="1"
    INPUT_NAME="Atul"

    # Below method is use to return the TLSaaS URL base on the informaiton in log file
    def dnc_cust_select_env(self):
        with open(r"/Users/atultupe/Documents/Tealeaf/TLSaaS/dns_cut_files/TLSaaSFeeder_20221011.log", 'r') as fp:
            for l_no, line in enumerate(fp):
                # search string
                # env is Staging = Staging

                if 'http://collector-tealeaf-staging.goacoustic.com/collector/collectorPost' in line:
                    self.url = "https://tealeaf-staging.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is QA = QA
                if 'http://collector-eaoc.qa.goacoustic.com/collector/collectorPost' in line:
                    # print('Env is QA')
                    self.url = "https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs"
                    return self.url
                    break
                # env is US-1 = #DAL
                if 'http://lib-us-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is WDC')
                    self.url = "https://tealeaf-us-1.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is US-2 = #WDC
                if 'http://lib-us-2.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is Dal')
                    self.url = "https://tealeaf-us-2.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is AP-1= #Sydney
                if 'http://lib-ap-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is Sydney')
                    self.url = "https://tealeaf-ap-1.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is AP-1= #Sydney
                if 'http://lib-eu-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is France')
                    self.url = "https://tealeaf-eu-1.goacoustic.com/webapp/login"
                    return self.url
                    break





