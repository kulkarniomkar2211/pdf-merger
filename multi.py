import requests
from PyPDF2 import PdfFileMerger # Used To Interact with PDF file and Write to PDF files
from multiprocessing.pool import ThreadPool
from datetime import datetime # To display date and time 
import os 
import send2trash as st2 # To delete files 


# Print the start time
start_time= datetime.now()
print("starting Pdf fetching at", datetime.now())
 
def download_url(url):
  #print("downloading: ",url)
  # assumes that the last segment after the / represents the file name
  # if url is abc/xyz/file.txt, the file name will be file.txt
  file_name_start_pos = url.rfind("/") + 1
  file_name = url[file_name_start_pos:]
 
  r = requests.get(url, stream=True)
  if r.status_code == requests.codes.ok:
    with open(file_name, 'wb') as f:
      for data in r:
        f.write(data)
  return url
  
urls =["https://btesimages.s3.amazonaws.com/PdfLabelFiles/404-9012833-0137142_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5056321-1155509_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-6599938-0889938_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/404-7625042-4821125_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539129367-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539114325-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-0303287-1511553_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-2326605-6486768_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5395774-3458768_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD507311467562657000-5731146756265700.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-9537812-3735564_shippinglabel.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-6492784-8589133_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-0857298-7415525_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539053587-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD507311505021513000-5731150502151300.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539010985-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538984393-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538958727-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD607311237362051000-6731123736205100.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19805275520-SLP1140421224.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19805014659-SLP1140406657.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19803429605-SLP1140286741.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-7456146-3809129_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538921681-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538853123-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-9284133-0781116_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19801906394-SLP1140178106.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5670213-6464363_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-0998013-5440314_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-3428884-0889148_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-3179019-2162765_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-2892189-3625157_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD107310867834425001-1731086783442500.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5056321-1155509_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-6599938-0889938_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/404-7625042-4821125_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539129367-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539114325-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-0303287-1511553_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-2326605-6486768_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5395774-3458768_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD507311467562657000-5731146756265700.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-9537812-3735564_shippinglabel.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-6492784-8589133_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-0857298-7415525_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539053587-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD507311505021513000-5731150502151300.pdf ",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539010985-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538984393-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538958727-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD607311237362051000-6731123736205100.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19805275520-SLP1140421224.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19805014659-SLP1140406657.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19803429605-SLP1140286741.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-7456146-3809129_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538921681-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2538853123-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-9284133-0781116_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19801906394-SLP1140178106.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5670213-6464363_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-0998013-5440314_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-3428884-0889148_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-3179019-2162765_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-2892189-3625157_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD107310867834425001-1731086783442500.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/171-5056321-1155509_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-5506700-5794751_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-4536622-4767528_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-9149230-0170747_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807895696-SLP1140616899.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/SnapDealLabel_19807845682-SLP1140616862.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-6599938-0889938_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/404-7625042-4821125_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539129367-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/ebayShippinglabel_2539114325-15242.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/402-0303287-1511553_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/403-2326605-6486768_shippinglabel.pdf",
"https://btesimages.s3.amazonaws.com/PdfLabelFiles/flipkartShippingLabel_OD107310867834425001-1731086783442500.pdf"]
        
# Run 5 multiple threads. Each call will take the next element in urls list
results = ThreadPool(10).imap_unordered(download_url, urls)
for r in results:
    continue

#Merge Multiple PDF files into single PDF
merger = PdfFileMerger()
for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)
merger.write("new_pdf.pdf") # Write files into new file named as new-pdf.pdf

merger.close()

end_time= datetime.now() # end the timer.
print("PDF Fetching Complete at", datetime.now()) # Print the end time.
print('Total time taken to fetch', len(urls), 'PDFs:{}'.format(end_time - start_time))
print("Open File new_pdf.pdf")

# Delete the downloaded files after writing to new_pdf.pdf
for j in os.listdir():
    if j =="new_pdf.pdf":
        continue
    elif j.endswith(".pdf"):
        st2.send2trash(j) 
    elif j.endswith(".pdf%20"):
        st2.send2trash(j) 