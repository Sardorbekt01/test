from driver import Driver

class Chempionship:
    def __init__(self):
        self.driver_list: list [Driver] = []

    def crate_driver(self,name):
        driver = Driver(name)
        self.driver_list.append(driver)
        print("Driver qo'shildi")
        return driver
    
    def get_drivers(self):
        return 
     
