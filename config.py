# config.py



PRODUCT_URLS = [
    # iPhone 12
    'https://www.amazon.com/Apple-iPhone-12-64GB-Black/dp/B08PNRG1XH/ref=sr_1_7?crid=2302IR6RLO5E1&dib=eyJ2IjoiMSJ9.FzRNNF3VsC6aurENhB2fYopwGObCRd-tYglZktUS2WcAwEFpjzqbRSa8nSDVXsljtOWZ8m8d5NRw1ayRntKsUkcX5eDoUXyxOU0FEbcddoNE58j2kpAn4r7txwsKLQV6G9_b-WFmHNUC8dAOWTyj239Uk-d0WOwqn4slFx6nEhyTzw1ZAIkJYDt7JMTcZ7mlJYBeK5lH53zvfK7Gbd2CH8W4-XLSB4hsIPB-agmKmdg.wCHK89VNmTMvsPp4HDntNlBsTj5_D4EFKM4ml8DFfDc&dib_tag=se&keywords=iphone&qid=1771927705&sprefix=ipho%2Caps%2C346&sr=8-7&th=1',  
    # iphone 13 
    'https://www.amazon.com/Apple-iPhone-13-128GB-Blue/dp/B09LNV4K66/ref=pd_sbs_d_sccl_1_3/131-4902416-6569335?pd_rd_w=3vDzC&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=TCWE4740WM5CPTWBV0ZY&pd_rd_wg=rUZMC&pd_rd_r=93e234c3-649a-4d32-96e1-c7a146c15689&pd_rd_i=B09LNV4K66&th=1',  
    #iphone 14
    'https://www.amazon.com/Apple-iPhone-128GB-Midnight-Renewed/dp/B0BN73VMBR/ref=pd_sbs_d_sccl_1_7/131-4902416-6569335?pd_rd_w=3vDzC&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=TCWE4740WM5CPTWBV0ZY&pd_rd_wg=rUZMC&pd_rd_r=93e234c3-649a-4d32-96e1-c7a146c15689&pd_rd_i=B0BN73VMBR&th=1'
    
    # you can add as many URLs as you want
]

# Headers to simulate a real browser request
# you can get your user-Agent from this website: https://httpbin.org/get 
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
                    "Accept-Encoding":"gzip, deflate", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                    "DNT":"1",
                    "Connection":"close", 
                    "Upgrade-Insecure-Requests":"1"}  
 



CHECK_INTERVAL = 86400  # 24 Hours (86400 seconds)

CSV_FILE_NAME = "Amazon_Product_Dataset.csv"


# Email configuration 
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


