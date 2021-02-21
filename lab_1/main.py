class Safe:
    counter = 0

    def __init__(self, password):
        """
        create new instance of safe
        increases safe counter
        by default state is set to Open (True)


        :type password: object
        """
        self.password = password
        self.opened_state = True
        Safe.counter += 1

    def open(self, password):
        """
        open safe, change state to  Open (True)
        password argument must match password stored in safe's memory

        :type password: object
        """
        if (self.password == password):
            self.opened_state = True
        else:
            raise Exception("cant open safe: incorrect password")

    def close(self):
        """close safe, change state to  Closed (False)"""
        self.opened_state = False

    def set_password(self, new_password):
        """
        set new password for safe
        will only work if this safe is opened

        :type new_password: object
        """
        if (self.opened_state == True):
            self.password = new_password
        else:
            raise Exception("cant change password: safe is not opened")

    @staticmethod
    def beep():
        """this static method is here only for the sake of the assignment"""
        return "beep-boop"


if __name__ == '__main__':

    print(f"Safe.counter           : {Safe.counter}")
    safes = [Safe("123")]
    print(f"Safe.counter           : {Safe.counter}")
    safes = safes + [Safe("1234"),Safe("12345")]
    print(f"Safe.counter           : {Safe.counter}")

    safes[0].close()
    print(f"Safe_0.opened_state    : {safes[0].opened_state}")
    print(f"Safe_2.opened_state    : {safes[2].opened_state}")
    safes[0].open("123")
    print(f"Safe_0.opened_state    : {safes[0].opened_state}")
    safes[0].set_password("qwerty")
    print(f"Safe_0.password        : {safes[0].password}")
    print(f"Safe_2.password        : {safes[2].password}")