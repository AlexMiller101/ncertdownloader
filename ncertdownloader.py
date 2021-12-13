import wget

#basic url structure to get the pdf book of ncert

base_url = 'https://ncert.nic.in/textbook/pdf/'

# writing classes and their alphabets accordingly

class_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# ask the class you want

book_class = int(input('Enter the Class: '))
book_class = book_class - 1

#changing class to class num

class_num = class_list[book_class]
print(class_num)

# ask the part of book

book_part = 1
book_part = int(input('Enter the Part of the Book: '))

# ask the total chapter to download

num_of_chapters = int(input('Enter the number of chapters: '))

# asking the subject

subjects_list = {
        'maths': 'mh',
        'physics': 'ph',
        'chemistry': 'ch',
        'biology': 'bo',
        'psychology': 'py',
        'accountancy': 'ac',
        'economics': 'ec',
        'sociology': 'sy',
        'geography': 'gy',
        'politics': 'ps',
        'business': 'bs',
        'computer': 'cs'
    }

for s in subjects_list:
    print(s)

subject_name = input('Enter the Subject: ')

#changing the subject to subject num

subject = subjects_list[subject_name]
print(subject)

# creating the url

if num_of_chapters > 9:
    filename = '{}e{}{}{}.pdf'.format(class_num, subject, book_part, 0)
    url_for_use = base_url + '{}e{}{}{}.pdf'.format(class_num, subject, book_part, '{}')
else:
    filename = '{}e{}{}0{}.pdf'.format(class_num, subject, book_part, 0)
    url_for_use = base_url + '{}e{}{}{}.pdf'.format(class_num, subject, book_part, '{}')
    
#print(filename)    
url = base_url + filename
#print(url)
#print(url_for_use)

# creating the loop

for i in range(1, num_of_chapters + 1):

    url = url.replace(url, url_for_use.format('0'+ str(i)))
    print(url)

    # downloading using wget
    file = '{}e{}{}{}.pdf'.format(class_num, subject, book_part, '0'+str(i))
    wget.download(url, file)
    

