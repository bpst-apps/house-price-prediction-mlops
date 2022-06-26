# Importing required packages
import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_message: Exception, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = HousingException.get_error_message(
            error_message=error_message,
            error_detail=error_detail
        )
        
        
    def get_error_message(error_message: Exception, error_detail: sys) -> str:
        
        # Get error message details
        _, _, exec_tb = error_detail.exc_info()
        
        # Get exception block line number
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        
        # Get try block line number
        try_block_line_number = exec_tb.tb_lineno
        
        # Get filename where exception occured
        filename = exec_tb.tb_frame.f_code.co_filename
        
        # Define error message
        error_message = f"""
        Error occured in script: 
        [ {filename} ] at 
        try block line number: [{try_block_line_number}] and 
        exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        
        return error_message
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()