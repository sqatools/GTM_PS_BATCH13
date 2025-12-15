Types of Xpath:
1.  Absolute XPath: These xpath follows complete DOM structure the find the element.
     e.g. /html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input


2.  Relative XPath: These xpath find the element with help of element attributes.
     e.g.   //tagname[@attribute='value']
         -> //input[@placeholder='Username']
         -> //input[@name='password']
         -> //button[@type='submit']
         -> //button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']

     e.g.   //*[@attribute='value']
        ->  //*[@placeholder='Username']



# XPath Methods:
1. Text Method :
       e.g. //taganame[text()='value']
       -> //button[text()='Log in']
       -> //button[text()='Log in']
       -> //a[text()='Forgotten password?']
       -> //a[text()='Create new account']
       -> //a[text()='Create a Page']


2. contains method: contains method help to indetify element with the help of partial value of text or attribute.
       i) contains with attribute : //tagname[contains(@attribute, 'partial value')]
                                   -> //input[contains(@data-testid,"email")]
                                   -> //input[contains(@data-testid,"pass")]
                                   -> //input[contains(@data-testid,"royal-e")]
                                   -> //button[contains(@data-testid, "login-button")]

       ii) contains with text : //tagname[contains(text(), 'partial value')]
                                -> //h2[contains(text(), 'Facebook helps')]
                                -> //button[contains(text(), 'Log')]
                                -> //a[contains(text(), 'Forgotten')]


3. starts-with:  //tagname[starts-with(@attribute, 'start-value')]
                 -> //input[starts-with(@placeholder, 'Email address')]
                 -> //input[starts-with(@placeholder, 'Pass')]
                 -> //a[starts-with(@data-testid, 'open-registration')]

4. and\or condition:
                  # AND Condition
                  e.g. //tagname[@attribute='value1' and @attrinute2='value2']
                  ->   //input[@id='email' and @data-testid='royal-email']
                  ->  //a[@data-testid='open-registration-form-button' and text()='Create new account']


                  # or Condition
                  e.g. //tagname[@attribute='value1' and @attrinute2='value2']
                  ->   //a[@data-testid='open-registration-form-button' or text()='Create new account1']
                  ->   //input[contains(@data-testid,'royal') or @name='pass1']

 5.  Deal with multiple matching element
    i). Indexing in the xpath :   e.g. (//tagname[@attribute='value'])[1]
                                 -> (//*[contains(text(), 'Car')])[1]

    ii). Family help :  //parent_element//tagname[@attribute='value']
                      -> //div/*[contains(text(), 'Car')]
                      -> //a/span/div/span[contains(text(), 'Car rental')]
                      -->//a/span/div/span[contains(text(), 'Car r')]


 6.  Normalize space: This method ignore any trailing spaces from text value or attribute value.
     -> //button[normalize-space()='Log in']
     -> //button[normalize-space()='Create new account']
     -> //button[normalize-space(@id)='create-account']



####### Advance XPath : ##########
1.  Parent:  identify the parent element with the help of child reference.
             e.g. //ref_tagname[@attribute='value']//parent:tar_tagname[@attribute='value']
             -> //span[text()='Flights']//parent::div

2.  Ancestor:  identify the grand parent element with the help of grand child reference.
              e.g. //ref_tagname[@attribute='value']//ancestor:tar_tagname[@attribute='value']
             -> //span[text()='Flights']//ancestor::a[@id="flights"]
             -> //span[text()='Flights']//ancestor::li

3.  Following: Any element on web page is available below to the reference element is a following element
               e.g. //ref_tagname[@attribute='value']//following:tar_tagname[@attribute='value']
               -> //input[@id='billing_name']//following::td[text()='Delhi']
               -> //input[@id='billing_name']//following::input[@id='street_address1']

4.  Following-sibling: Any sibling is available below side reference sibling element, then it is called
                      following sibling.
                e.g. //ref_tagname[@attribute='value']//following-sibling:tar_tagname[@attribute='value']
                -> //td[text()='6001']//following-sibling::td[text()='1033']
                -> //td[text()='Equity']//following-sibling::td[4]

5.  Preceding: Any element on web page is available above to the reference element is a preceding element.
               e.g. //ref_tagname[@attribute='value']//preceding:tar_tagname[@attribute='value']
               -> //input[@id='firstname']//preceding::input[@value='radio_678']
               -> //input[@id='firstname']//preceding::h1[@align="center"]

6.  Preceding-sibling: Any sibling is available above side reference sibling element, then it is called
                 -> e.g. //ref_tagname[@attribute='value']//preceding-sibling:tar_tagname[@attribute='value']
                 -> //td[text()='Kolkata']//preceding-sibling::td/input




