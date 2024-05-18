<center> <h1> SecURL: A Machine Learning Based Web Extension for Malicious URL Detection </h1> </center>

## About the App

SecURL is a web extension that utilizes machine learning to detect malicious URLs. It is non-intrusive such that it automatically fetches and evaluates the URL input by the user in a timely manner before directing them to the site.

### Features

- Automatic detection of malicious and benign URLs through machine learning.
- Personalized blacklisting.
- Customizable level of detection:
    - Faster but less accurate (using URL's lexical features)
    - Slower but more accurate (using URL's lexical and content-based features)
- Adaptive to new and emerging threats through cumulative user input and feedback

### Installation Prerequisites:

1. Must use one of the following supported browsers:
    - Chrome
    - Firefox
    - Edge
    - Opera
    - Safari
2. Must have EEE VPN/UP Wifi access.
    - If you are currently in EEE and connected through eduroam, no need to use VPN.
    - Otherwise, download the [EEEI VPN profile](https://drive.google.com/file/d/1wY9TiykZsIbkV0BWSkmfpHjN_IgaBR3b/view?usp=sharing) and Open VPN for [Windows](https://openvpn.net/downloads/openvpn-connect-v3-windows.msi)/[Mac](https://openvpn.net/downloads/openvpn-connect-v3-macos.dmg) and follow these guides ([Windows](https://drive.google.com/file/d/132MAgs0sM491BnlXBnbxgsnevXGb8aSY/view?usp=sharing), [Mac](https://drive.google.com/file/d/1TdOHaGkw_ENCccQMUHwhbdR457mO9Zui/view?usp=sharing)) access to the EEE network.

### Installation Guide

By installing this extension, you understand and agree to the following [data policies](#data-policies) that govern its usage.

1. Download [ZIP file](https://drive.google.com/drive/folders/1vVljn![](my_video.mov)BPACA_qkXIbEdUBVkXc6avpo91q?usp=sharing) containing the extension program.
2. Extract the contents of the ZIP file to your desired directory.
3. Head to your browser's extension page, click manage extensions, and enable developer mode.
4. Click the “Load unpacked” option.
5. Select the folder that has been extracted from the ZIP file.

And that's it! Enjoy using our extension!

#### Video Tutorial

https://github.com/SupernovaExe/SecURL/assets/63900699/c2ea4703-d5ec-4895-b3a3-4ef3afd6126b

## Usage Guide

### Casual Use

Once you have set-up the extension, it automatically determines the maliciousness of the URL that you visit. For benign sites, a pop-up notification will show up. For malicious sites, the user will be redirected to a warning page and will be given the options to proceed to the site or to go back to the previously visited site.

### Reporting an Incorrect Benign Prediction

Reporting incorrect benign predictions are done through the pop-up page. To report, click the extension icon and click the report button. A pop-up notification will show up to inform the user that a report has been sent. 

### Reporting an Incorrect Malicious Prediction

Reporting incorrect malicious predictions are done through the warning page. To report, click the report button in the warning page. A window will open up to check if you the user wants to proceed with reporting the prediction. A pop-up notification will also show up to inform the user after the report is sent.

### Accessing the Settings Page

To access the settings page, head over to the extensions button in your browser. You should be able to see all the extensions that you are currently using in your browser. Look for the SecURL extension and click the "more options" button beside it, usually it is a three-dot icon, and then click extension options. The settings page should show up. Make sure to click save for any changes that you have added to take effect. 

## Get in Touch

### Contact Details

Eriel John Benavides: eriel.john.benavides@eee.upd.edu.ph \
Conrado Luiz Bencio: conrado.luiz.bencio@eee.upd.edu.ph \
Steven Sison: steven.sison@eee.upd.edu.ph

### We’d Love your feedback!

If you'd like to become part of testing and evaluation team, please answer this [interest form](https://forms.gle/afMVTqoTwGwe9LW69). More details will be sent through email and a qualitative survey will be conducted after the test period.

## Data Policies
The student researchers acknowledge their responsibilities under RA 10173 or the Data Privacy Act of 2012 with regard to the information they request from their respondents.

By signing up to this form, you express your interest to test and provide feedback to our web extension. Pushing through with the installation means that you understand and agree to the following data policies that our extension adheres to:

- The extension will not collect any identifiable information.
- The extension will collect and retain the URLs you use for its detection and retraining services.

All collected personal information will be kept strictly confidential and utilized only for research purposes. In any reports or papers that may arise from this study, all data will certainly be anonymized.

