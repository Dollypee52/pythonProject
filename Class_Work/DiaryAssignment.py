# entries = []
#
# def create_entry():
#     date = input('date: ')
#     title = input('title')
#
#     key = ['date', 'title', 'body']
#     value = [date,title, input(f'{date}\n{title}\n\nWelcome to my Diary,\n')]
#     each_entry = dict(zip(key, value))
#     return each_entry
#
# def Diary(password):
#     if password == 'code':
#         to_continue = input("'y' to continue 'n' to stop[y/n]").lower()
#
#         while to_continue == 'y':
#             entries.append(create_entry())
#             to_continue = input("'y' to continue 'n' to stop[y/n").lower()
#         return entries
#
# def find_by_title(title):
#     return [entry for entry in entries if entries['title'] == title]
#
# def delete_entry_of(title):
#     entries.pop(find_by_title().index())
#
# print(Diary)
# find_by_title('ok')
#
