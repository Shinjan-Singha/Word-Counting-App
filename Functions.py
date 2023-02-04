LOCAL_FILEPATH = "Data.txt"

def word_count_text(local_user_input):

    """This function takes a parameter i.e the user input. Then it splits every word in a list,
    and then we take the length of the list, and we return the value. 
    """
    local_user_input = local_user_input.strip()
    local_user_input = local_user_input.replace(' \n', ' ')
    local_user_input = local_user_input.replace('\n', ' ')
    listing = local_user_input.split(' ')
    local_result = len(listing)
    return local_result


def word_count_file(local_filepath=LOCAL_FILEPATH):

    """This function takes a parameter i.e the Filepath. Then it splits every word in the file in a list,
    and then we take the length of the list, and we return the value. 
    """

    with open(local_filepath,'r') as file:
        data = file.read()
        data = data.strip()
        data = data.replace(' \n', ' ')
        data = data.replace('\n', ' ')
        data = data.split(' ')
    local_result = len(data)
    return local_result