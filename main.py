from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep, asctime


def change_show_value():
    ele = driver.find_element(By.XPATH, '//*[@id="example_length"]/label/select/option[2]')
    driver.execute_script("arguments[0].setAttribute('value','10000')", ele)
    a = Select(driver.find_element(By.XPATH, '//*[@id="example_length"]/label/select'))
    a.select_by_value('10000')
    sleep(1)


def write_into_csv(details, college, course):
    with open('resultslist.txt', 'a') as fp:
        for i, k in enumerate(details):
            x = f"{k.text}," if i % 9 else f"{k.text},{college},{course}\n" if i != 0 else ''
            fp.write(x)
        fp.write(f"{college},{course}\n")


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get('https://eapcet-sche.aptonline.in/EAPCET/collegeWiseAllotedReport.do')

colleges = ['SRKR-S R K R ENGINEERING COLLEGE', 'ABRK-ABR COLLEGE OF ENGG AND TECHNOLOGY',
            'ADTP-ADITYA ENGINEERING COLLEGE', 'AMRN-A.M.REDDY MEMORIAL COLL. OF ENGINEERING',
            'CABP-COLLEGE OF AGRICULTURAL ENGINEERING', 'CAMS-COLLEGE OF AGRICULTURAL ENGINEERING',
            'ESWR-ESWAR COLLEGE OF ENGINEERING', 'ISTS-INTERNATIONAL SCHOOL OF TECH AND SCI FOR WOMEN',
            'KISR-KAKINADA INSTITUTE OF TECHNOLOGY SCIENCES', 'KTSP-KAKINADA INSTITUTE OF TECHNOLOGY AND SCIENCE',
            'NOVA-NOVA COLLEGE OF ENGG. AND TECHNOLOGY', 'NVAV-NOVA COLLEGE OF ENGINEERING AND TECHNOLOGY',
            'PYDE-PYDAH COLL OF ENGINEERING', 'VCTN-VIKAS COLLEGE OF ENGINEERING AND TECHNOLOGY',
            'VGTN-VIKAS GROUP OF INSTITUTIONS', 'QISE-QIS COLLEGE OF ENGG. AND TECHNOLOGY',
            'RUCESF-RAYALASEEMA UNIVERSITY COLLEGE OF ENGG-SELF FINANCE',
            'BITS-BHASKAR INSTITUTE OF TECHNOLOGY & SCIENCE', 'BESTPU-BHARATIYA ENGG, SCI. &TECH INNOVATION UNIVERSITY',
            'CEVP-CHAITANYA ENGINEERING COLLEGE', 'AITT-ANNAMACHARYA INST OF TECHNOLOGYAND SCIENCES',
            'AITK-ANNAMACHARYA INST OF TECH AND SCI', 'AITS-ANNAMACHARYA INST OF TECHNOLOGY AND SCIENCES',
            'ACEM-ADITYA COLLEGE OF ENGINEERING', 'KIEK-KAKINADA INSTITUTE OF ENGG. AND TECHNOLOGY',
            'KIET-KAKINADA INSTITUTE OF ENGG. AND TECHNOLOGY', 'GVRS-G V R AND S COLLEGE OF ENGG. AND TECHNOLOGY',
            'GDLV-SESHADRI RAO GUDLAVALLERU ENGINEERING COLLEGE', 'ELRU-ELURU COLLEGE OF ENGG AND TECHNOLOGY',
            'GLIM-A1 GLOBAL INST OF ENGG TECHNOLOGY', 'CHKN-CHAITANYA INST. OF SCI. AND TECHNOLOGY',
            'DNRE-DNR COLLEGE OF ENGG AND TECH', 'NBKR-NBKR INSTITUTE OF SCI. AND TECHNOLOGY',
            'MVRS-M.V.R.COLL OF ENGINEERING AND TECHNOLOGY', 'PACE-PACE INSTITUTE OF TECHNOLOGY AND SCIENCES',
            'PIIT-PRIYADARSHINI INST OF TECH AND MGMT', 'PITT-PRIYADARSHINI INST. OF TECHNOLOGY AND SCIENCES',
            'LBCE-LAKIREDDY BALIREDDY COLLEGE OF ENGINEERING', 'LIMT-LINGAYAS INST OF MGMT AND TECHNOLOGY',
            'KIEW-KAKINADA INST OF ENGG AND TECHNOLOGY FOR WOMEN',
            'KLMW-KANDULA LAKSHUMMA MEMORIAL COLLEGE OF ENGG FOR WOMEN',
            'KORM-KANDULA OBUL REDDY MEMORIAL COLL. OF ENGG.', 'MICT-DVR AND DR.HS MIC COLLEGE OF TECHNOLOGY',
            'MLEW-MALINENI LAKSHMAIAH WOMENS ENGG. COLLEGE', 'MRCL-MIRACLE EDNL SOC GROUP OF INSTNS',
            'MTIE-MOTHER THERESA INST OF ENGG AND TECH', 'RSRN-RAMIREDDY SUBBA RAMIREDDY ENGG COLLEGE',
            'SANK-AUDHISANKARA COLLEGE OF ENGG. AND TECHNOLOGY', 'RCEE-RAMACHANDRA COLLEGE OF ENGINEERING',
            'SGVP-SATYA INST OF TECHNOLOGY AND MGMT', 'SIEN-SRI SARATHI INSTITUTE OF ENGG. AND TECHNOLOGY',
            'SMGG-ST.MARYS GROUP OF INSTITUTIONS GUNTUR FOR WOMEN', 'SRET-SREE RAMA ENGINEERING COLLEGE',
            'VISM-VISWAM ENGINEERING COLLEGE', 'URCE-USHA RAMA COLL OF ENGG AND TECHNOLOGY',
            'SWRN-SWARNANDHRA COLL. OF ENGG AND TECHNOLOGY', 'STMW-ST.MARYS WOMENS ENGINEERING COLLEGE',
            'SVCN-SREE VENKATESWARA COLL OF ENGG', 'VIVP-VIGNANS INSTITUTE OF INFORMATION TECHNOLOGY',
            'VRIT-VARAPRASAD REDDY INST OF TECHNOLOGY', 'VRSE-V R SIDDHARTHA ENGINEERING COLLEGE',
            'VVGV-VKR VNB AND AGK ENGINEERING COLLEGE', 'VVIT-VASIREDDY VENKATADRI INST. OF TECHNOLOGY',
            'WISE-WEST GODAVARI INSTT OF SCIENCE AND ENGINEERING', 'VSVT-SRI VASAVI ENGINEERING COLLEGE',
            'VITW-VIJAYA INST. OF TECHNOLOGY FOR WOMEN', 'VLIT-VIGNANS LARA INST. OF TECHNOLOGY AND SCI',
            'VITK-P B R VISVODAYA INSTITUTE OF TECHNOLOGY AND SCI.', 'SVHE-D M S S V H COLLEGE OF ENGINEERING',
            'UNIV-UNIVERSAL COLLEGE OF ENGG AND TECHNOLOGY', 'VHNI-SREE VAHINI INSTT OF SCIENCE AND TECHNOLOGY',
            'VETS-SR VENKATESWARA COLL OF ENGINEERING', 'SRIN-SRINIVASA INST OF ENGG AND TECHNOLOGY',
            'SRTS-SRINIVASA INST OF TECHNOLOGY AND SCIENCE', 'SSCE-SRI SIVANI COLLEGE OF ENGINEERING',
            'SGIT-DR SAMUEL GEORGE INSTITUTE OF ENGG. AND TECHNOLOGY',
            'SASI-SASI INSTITUTE OF TECHNOLOGY AND ENGINEERING', 'RKCE-R.K.COLLEGE OF ENGINEERING',
            'KSRM-K S R M COLLEGE OF ENGINEERING', 'NSPE-NARSARAOPETA ENGINEERING COLLEGE',
            'NRIA-NRI INSTITUTE OF TECHNOLOGY', 'NRIT-NRI INSTT OF TECHNOLOGY',
            'CVRT-SIR C.V RAMAN INST OF TECHNOLOGY SCIENCES', 'CITY-CHALAPATHI INST OF TECHNOLOGY',
            'KCIT-KRISHNA CHAITANYA INST OF TECHNOLOGY AND SCIENCES',
            'HIND-HINDU COLLEGE OF ENGINEERING AND TECHNOLOGY', 'AECN-ANDHRA ENGINEERING COLLEGE',
            'ANCUSF-DR.YSR COLLEGE OF ENGINEERING & TECHNOLOGY-SELF FINANCE', 'BWEC-BAPATLA WOMENS ENGG COLLEGE',
            'BVCE-B V CHALAMAIAH ENGINEERING COLLEGE', 'BVTS-BONAM VENKATA CHALAMAIAH INST. OF TECH AND SCI.',
            'GIER-GODAVARI INSTITUTE OF ENGG. AND TECHNOLOGY', 'VSPT-VISAKHA INST OF ENGG AND TECHNOLOGY',
            'CVST-SVVU COLLEGE OF DAIRY TECHNOLOGY', 'CDTK-COLLEGE OF DAIRY TECHNOLOGY',
            'AUCE-A U COLLEGE OF ENGG. VISAKHAPATNAM', 'APUCPU-APOLLO UNIVERSITY',
            'CRRE-SIR C R R COLLEGE OF ENGINEERING', 'KHIT-KALLAM HARANADH REDDY INST OF TECH',
            'GMRI-G M R INSTITUTE OF TECHNOLOGY', 'SDTN-SIDDHARTH INSTITUTE OF ENGG. AND TECHNOLOGY',
            'SIST-SIDDHARTHA INST OF SCI AND TECHNOLOGY', 'VISW-SHRI VISHNU ENGG. COLLEGE FOR WOMEN',
            'VITB-VISHNU GRP OF INSTNS - VISHNU INST OF TECHNOLOGY', 'VEMU-VEMU INSTITUTE OF TECHNOLOGY',
            'VIEW-VIGNANS INSTT OF ENGINEERING FOR WOMEN', 'SVEN-SREE VENKATESWARA ENGINEERING COLLEGE',
            'SVPP-SRI VENKATESA PERUMAL COLLEGE OF ENGG. AND TECH',
            'SVUCSS-S V U COLLEGE OF ENGG. -SELF SUPPORTING-TIRUPATHI',
            'SVCT-SRI VENKATESWARA COLLEGE OF ENGG. AND TECHNOLOGY', 'SEAT-SIDDARTHA EDNL ACADEMY GRP OF INSTNS',
            'SSCC-SRINIVASA INSTITUTE OF TECHNOLOGY AND MANG STUDIES',
            'PSCV-POTTI SRIRAMULU COLLEGE OF ENGG AND TECHNOLOGY', 'PKSK-PRAKASAM ENGINEERING COLLEGE',
            'PRAG-PRAGATI ENGINEERING COLLEGE', 'KITS-KKR AND KSR INST OF TECHNOLOGY AND SCI',
            'KMMT-KMM INST OF TECHNOLOGY AND SCIENCE', 'MITS-MADANAPALLY INSTITUTE OF TECHNOLOGY AND SCI',
            'MPLG-SRI MITTAPALLI COLLEGE OF ENGINEERING', 'MJRT-MJR COLLEGE OF ENGG AND TECHNOLOGY',
            'NARN-NARAYANA ENGINEERING COLLEGE', 'PCEK-G.PULLAIAH COLL. OF ENGG. AND TECHNOLOGY',
            'IITM-INDIRA INST OF TECHNOLOGY SCI', 'JONY-ST. JOHNS COLLEGE OF ENGG. AND TECHNOLOGY',
            'CHDL-CHADALAWADA RAMANAMMA ENGG. COLLEGE', 'CIET-CHALAPATHI INST OF ENGG AND TECHNOLOGY',
            'DSIT-DAMISETTY BALA SURESH INST OF TECHNOLOGY', 'GATE-GATES INSTITUTE OF TECHNOLOGY',
            'GGIB-GOKUL GROUP OF INSTITUTIONS', 'CBIT-CHAITANYA BHARATHI INSTITUTE OF TECHNOLOGY',
            'ASVR-SVR ENGINEERING COLLEGE', "ASKW-ASHOKA WOMEN'S ENGINEERING COLLEGE",
            'ASIP-AMRITA SAI INST. OF SCIENCE AND TECHNOLOGY', 'RVJC-R V R AND J C COLLEGE OF ENGINEERING',
            'MVRG-M V G R COLLEGE OF ENGINEERNG', 'ANIL-ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY AND SCI',
            'JNTA-JNTUA COLLEGE OF ENGG. ANANTAPURAMU', 'JNTKSF-JNTUK COLLEGE OF ENGG. KAKINADA-SELF FINANCE',
            'GVPE-GAYATHRI VIDYA PARISHAD COLL. OF ENGINEERING', 'SVUC-S V U COLLEGE OF ENGG. TIRUPATHI',
            'CCVY-VRS AND YRN COLLEGE OF ENGG. AND TECHNOLOGY',
            'CENUPU-CENTURION UNIVERSITY OF TECHNOLOGY & MANAGEMENT', 'LIET-LENDI INST OF ENGG AND TECHNOLOGY',
            'SAVE-SANKETHIKA VIDYA PARISHAD ENGINEERING COLLEGE',
            'SKUASF-SRI KRISHNADEVARAYA UNIV.COLL.OF ENG.- SELF FINANCE', 'SRKI-S R K INST. OF TECHNOLOGY',
            'SRIP-SAI RAJESWARI INSTITUTE OF TECHNOLOGY', 'SSSE-SANSKRITHI SCHOOL OF ENGINEERING',
            'SRIT-SRINIVASA RAMANUJAN INST OF TECHNOLOGY', 'SRMUPU-S R M UNIVERSITY AP',
            'RAGU-RAGHU ENGINEERING COLLEGE', 'PVKK-P.V.K.K. INSTITUTE OF TECHNOLOGY',
            'PREC-DR PAUL RAJS ENGINEERING COLLEGE', 'PRIK-PRIYADARSHINI COLL OF ENGG. AND TECHNOLOGY',
            'PPSV-PRASAD V POTLURI SIDDHARTHA INSTT OF TECHNOLOGY',
            'RPRA-RISE KRISHNA SAI PRAKASAM GROUP OF INSTITUTIONS',
            'RGIT-RAJIV GANDHI MEMORIAL COLLEGE OF ENGG. AND TECH.', 'KVSR-DR.K.V.SUBBA REDDY INST. OF TECHNOLOGY',
            'LENO-LENORA COLLEGE OF ENGINEERING', 'KUPM-KUPPAM ENGINEERING COLLEGE',
            'MIET-MANDAVA INSTITUTE OF ENGG AND TECHNOLOGY', 'MBUTPU1-MOHAN BABU UNIVERSITY',
            'LOYL-LOYOLA INSTITUTE OF TECHNOLOGY AND MGMT', 'NEWS-NEWTONS INST OF SCI AND TECH',
            'PINN-PRIYADARSHINI INST OF TECHNOLOGY', 'NSRT-NADIMPALLI SATYANARAYANA RAJU INSTITUTE OF TECHNOLOGY',
            'NRNG-NARAYANA ENGINEERING COLLEGE', 'CRIT-CHIRANJIVI REDDY INST OF ENGG AND TECHNOLOGY',
            'DJRC-SRI CHAITANYA -DJR COLL OF ENGG AND TECH', 'DLBC-DR L BULLAYYA COLL EGE OF ENGINEERING',
            'DHAN-DHANEKULA INST OF ENGG TECHNOLOGY', 'DIET-DADI INSTT. OF ENGINEERING AND TECHNOLOGY',
            'GITS-GONNA INST OF INFO TECHNOLOGY SCIENCES', 'GKCS-GOKULA KRISHNA COLLEGE OF ENGINEERING',
            'GVPT-G V P COLLEGE FOR DEGREE AND PG COURSES', 'HITE-HELAPURI INST OF TECH AND SCIENCE',
            'GPRE-G P R ENGINEERING. COLLEGE', 'GTNN-GEETHANJALI INST OF SCIENCE AND TECHNOLOGY',
            'JNTN-JNTUK COLLEGE OF ENGINEERING NARSARAOPETA', 'JNTC-JNTUA COLLEGE OF ENGINEERING. KALIKIRI',
            'JNTK-JNTUK COLLEGE OF ENGG. KAKINADA', 'JNTP-JNTUA COLLEGE OF ENGG PULIVENDULA',
            'JNTV-JNTUK COLLEGE OF ENGINEERING VIZIANAGARAM',
            'BRAUSF-COLLEGE OF ENGINEERING BR AMBEDKAR UNIV SELF FINANCE', 'BVSR-BVSR ENGINEERING COLLEGE',
            'BEMA-BHEEMA INST OF TECHNOLOGY AND SCI', 'BECB-BAPATLA ENGINEERING COLLEGE',
            'AUEWSF-A U COLLEGE OF ENGG FOR WOMEN-SELF FINANCE', 'BABA-BABA INST OF TECH AND SCIENCES',
            'ALIT-ANDHRA LOYOLA INSTT OF ENGG AND TECHNOLOGY', 'ALTS-ANANTHA LAKSHMI INST OF TECHNOLOGY AND SCI',
            'ANURSF-ADI KAVI NANNAYA UNIVERSITY COLLEGE OF ENGG.-SELF FINANCE',
            'ANSN-ST. ANNS COLLEGE OF ENGG. AND TECHNOLOGY', 'ACEE-ADARSH COLLEGE OF ENGINEERING',
            'ACES-ADITYA COLLEGE OF ENGINEERING', 'ACET-ADITYA COLLEGE OF ENGINEERING AND TECHNOLOGY',
            'ADIT-ADITYA INSTITUTE OF TECHNOLOGY AND MGMT', 'TECH-TADIPATRI ENGG COLLEGE',
            'SVIT-SRI VENKATESWARA INST OF TECHNOLOGY', 'SVET-SRI VASAVI INSTT OF ENGINEERING AND TECHNOLOGY',
            'SVIK-SRI VENKATESWARA INST. OF SCIENCE AND TECHNOLOGY',
            'SUNL-SRI SUNFLOWER COLLEGE OF ENGG AND TECHNOLOGY', 'SVCE-SRI VENKATESWARA COLL OF ENGINEERING',
            'VSUESS-VIKRAMA SIMHAPURI UNIVERSITY-SELF SUPPORTING', 'WSTM-WELLFARE INST OF SCIENCE TECH AND MGMT',
            'YGVU-YGVU YSR ENGINEERING COLLEGE', 'VSMR-V.S.M COLLEGE OF ENGINEERING',
            'IDEL-IDEAL INSTITUTE OF TECHNOLOGY', 'VITAPU-VIT-AP UNIVERSITY',
            'ARTB-AVANTHIS RESEARCH AND TECHNOLOGICAL ACADEMY', 'MBUTPU2-MOHAN BABU UNIVERSITY',
            'VNRC-VELAGA NAGESWARA RAO COLL OF ENGINEERING', 'VNIW-VIGNANS NIRULA INST OF TECH. AND SCI FOR WOMEN',
            'MPLW-SRI MITTAPALLI INST OF TECHNOLOGY FOR WOMEN', 'NVRT-N.V.R.COLLEGE OF ENGG TECHNOLOGY',
            'NMRE-NIMRA COLLEGE OF ENGG AND TECHNOLOGY', 'PPDV-PALADUGU PARVATHI DEVI COLLEGE OF ENGG AND TECH',
            'RIET-RAJAMAHENDRI INST OF ENGG AND TECHNOLOGY', 'RVIT-R V INSTITUTE OF TECHNOLOGY',
            'SREC-SANTHIRAM ENGINEERING COLLEGE', 'RGAN-RISE KRISHNA SAI GANDHI GROUP OF INSTITUTIONS',
            'SATS-SRI ANNAMACHARYA INSTITUTE OF TECHNOLOGY AND SCIENCE', 'GECG-GUNTUR ENGINEERING COLLEGE',
            'AVEV-AVANTHI INST. OF ENGINEERING AND TECHNOLOGY', 'AVEN-AVANTHI INSTITUTE OF ENGG. AND TECHNOLOGY',
            'CECC-CHIRALA ENGINEERING COLLEGE', 'BVCR-BVC COLLEGE OF ENGINEERING',
            'BRNK-BRINDAVAN INST OF TECHNOLOGY AND SCI', 'BVRM-BHIMAVARAM INST. OF ENGG. AND TECHNOLOGY',
            'ASTC-AVANTHIS ST THERESSA INSTITUTE OF ENGG AND TECHNOLOGY', 'ANMB-ACHARYA COLLEGE OF ENGINEERING',
            'GIET-GIET ENGINEERING COLLEGE', 'GTMW-GOUTHAMI INST OF TECHNOLOGY MGMT FOR WOMEN',
            'GVIC-GOLDEN VALLEY INTEGRATED CAMPUS', 'GVPW-GAYATHRI VIDYA PARISHAD COLL OF ENGG FOR WOMEN',
            'SGEC-SAI GANAPATHI ENGINEERING COLLEGE', 'SIMH-SIMHADRI EDNL SOC GRP OF INSTNS',
            'SPMUSF-SCHOOL OF ENGG. TECH. SPMVV - SELF FINANCE', 'SRSR-SRI SAI INSTITUTE OF TECHNOLOGY. AND SCI.',
            'QUBA-QUBA COLL OF ENGG AND TECHNOLOGY', 'PITW-PRIYADARSHINI INST. OF TECH AND SCIENCES FOR WOMEN',
            'RAVW-RAVINDRA COLLEGE OF ENGG FOR WOMEN', 'NEWT-NEWTON INSTITUTE OF ENGINEERING',
            'MSEW-MALINENI SUSEELAMMA WOMENS ENGG COLLEGE', 'NIST-NARAYANADRI INST OF SCI TECHNOLOGY',
            'NSRE-N S RAJU INSTITUTE OF ENGG AND TECHNOLOGY', 'KECW-KRISHNAVENI ENGG COLLEGE FOR WOMEN',
            'KRUESF-KRISHNA UNIVERSITY COLLEGE OF ENGG AND TECHNOLOGY-SLEF FINANCE',
            'STEN-SAI TIRUMALA N V R ENGINEERING COLLEGE', 'SVCK-SRI VENKATESWARA COLLEGE OF ENGINEERING',
            'SVCS-SREE VENKATESWARA COLLEGE OF SCIENCE AND TECHNOLOGY', 'TMLN-TIRUMALA ENGINEERING COLLEGE',
            'VITAPUMT-VIT-AP UNIVERSITY-5 YEAR INTEGRATED MTECH', 'VITS-VAAGDEVI INSTITUTE OF TECHNOLOGY. AND SCI.',
            'JNTKSS-JNTUK COLLEGE OF ENGG. KAKINADA-SELF SUPPORTING',
            'YSRA-DR.YSR ARCHITECTURE AND FINE ARTS UNIVERSITY',
            'ANCUSS-DR.YSR COLLEGE OF ENGINEERING & TECHNOLOGY-SELF SUPPORTING',
            'JNKFSF-SCHOOL OF FOOD TECHNOLOGY JNTUK KAKINADA-SELF FINANCE',
            'CFSB-COLLEGE OF FOOD SCIENCE AND TECHNOLOGY', 'CFSP-COLLEGE OF FOOD SCIENCE AND TECHNOLOGY',
            'AUCESF-A U COLLEGE OF ENGG-SELF FINANCE VISAKHAPATNAM']

for college in colleges:
    present_college = Select(driver.find_element(By.XPATH, '//*[@id="programmeId"]'))
    present_college.select_by_visible_text(college)
    sleep(2)
    try:
        courses = [x.text for x in Select(driver.find_element(By.XPATH, '//*[@id="collegeId"]')).options[1:]]
    except:
        courses = []
        with open('problems.txt', 'a') as fp:
            fp.write(f"{college},ALL COURSES,{asctime()}\n")
        print(college, 'options problem')
    for course in courses:
        try:
            Select(driver.find_element(By.XPATH, '//*[@id="collegeId"]')).select_by_visible_text(course)
            driver.find_element(By.ID, 'SUBMIT').click()
            change_show_value()
            html = driver.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr/td')
            write_into_csv(html, college, course)
            with open('completed.txt', 'a') as fp:
                fp.write(f'{college},{course},{asctime()}\n')
        except:
            with open('problems.txt', 'a') as fp:
                fp.write(f"{college},{course},{asctime()}\n")

driver.close()
