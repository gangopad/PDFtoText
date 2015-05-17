"""
Downloads pdfs from http://www.jmedicalcasereports.com/content and 
then scrapes the pdfs. We then convert the pdfs to text
"""
import urllib2


#gets the cleaned url of the pdf
def getURL(url):
    index = url.find("http");
    url = url[index:];
    url = url[:-1];
    return url;


#returns the list of pdf urls                                                             
def scrapePDFs(html):
    list_htmls = html.split();
    urls = set();

    for items in list_htmls:
        if 'pdf' in items and 'class' not in items:
            res = getURL(items);
            urls.add(res);
            print res;

    return urls;


#downloads the pdf
def downloadPDF(url):
    response = urllib2.urlopen(str(url));
    #print response.info();
    html = response.read();
    response.close()  # best practice to close the file

    url = url.replace("/","_");
    filename = "/Users/UMBC/MedicalJournals/PDFs/" + str(url);


    f = open(filename, 'w');                                                                                             
    f.write(html);                                                                                                                  
    f.close(); 


def scrapePage( i):
    i = str(i);
    scraped_file = 'http://www.jmedicalcasereports.com/content?page='+i+'&itemsPerPage=25&citation=true&summary=false';
    response = urllib2.urlopen(scraped_file);
    #response = urllib2.urlopen('http://www.jmedicalcasereports.com/content?page=1&itemsPerPage=25&citation=true&summary=false');
    #response = urllib2.urlopen('http://www.jmedicalcasereports.com/content/pdf/1752-1947-7-270.pdf')
    #print response.info()
    html = response.read()
    urls = scrapePDFs(html)
    #print html
    # do something
    response.close()  # best practice to close the file

    for url in urls:
        downloadPDF(url);

    """
    f = open('out.pdf', 'w');
    f.write(html);
    f.close();
    """


if __name__ == '__main__':

    n = 3; #n is the number of pages we want to scrape 
    for i in range(1,n+1):
        print "processing page ", i;
        scrapePage(i);
