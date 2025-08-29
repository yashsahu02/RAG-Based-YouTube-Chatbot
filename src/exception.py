import sys 

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() ## This exc_info() returns and gives us all the info like in which line exception has occured why it occured etc. It returns 3 things starting 2 are not important 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number =  exc_tb.tb_lineno
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        line_number,
        str(error)
    )
    return error_message
    
class CustomException(Exception): ## Inheriting from the Exception Class 
    def __init__(self, error_message, error_detail:sys): ## error_detail will be of sys type 
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self): ## changing __str__ dundant method according to out ease of use
        return self.error_message