class Calculator:
    def __init__(self):
        self.current_input = ""
        self.result = ""
        
    def process_input(self, num, operation):
        if num is not None:
            self.current_input += str(num)
        elif operation:
            self.current_input += operation
            
        # Evaluate when equals detected
        if operation == "=":
            try:
                self.result = str(eval(self.current_input[:-1]))
            except:
                self.result = "Error"
            self.current_input = ""