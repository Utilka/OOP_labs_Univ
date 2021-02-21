class Safe
  attr_accessor :counter, :opened, :password

  @@counter = 0

  # create new instance of safe
  # increases safe counter
  # by default state is set to Open (True)
  # @param [Object] password
  def initialize(password)
    @password = password
    @opened = true
    @@counter += 1
  end

  # open safe, change state to Open (True)
  # password argument must match password stored in safe's memory
  # @param [Object] password
  def open(password)
    if @password == password
      @opened = true
    else
      raise StandardError.new("cant open safe: incorrect password")
    end
  end

  # close safe, change state to  Closed (False)
  def close()
    @opened = true
  end

  # set new password for safe
  # will only work if this safe is opened
  # @param [Object] new_password
  def set_password(new_password)
    if @opened
      @password = new_password
    else
      raise StandardError.new("cant change password : safe is not opened")

    end
  end

  # this static method is here only for the sake of the assignment
  def self.beep()
    "" "" ""
    return "beep-boop"
  end

  def self.counter
    @@counter
  end
end

if __FILE__ == $0
  puts("Safe.counter           : #{Safe.counter}")
  safes = [Safe.new("123")]
  puts("Safe.counter           : #{Safe.counter}")
  safes = safes + [Safe.new("1234"), Safe.new("12345")]
  puts("Safe.counter           : #{Safe.counter}")

  safes[0].close()
  puts("Safe_0.opened_state    : #{safes[0].opened}")
  puts("Safe_2.opened_state    : #{safes[2].opened}")
  safes[0].open("123")
  puts("Safe_0.opened_state    : #{safes[0].opened}")
  safes[0].set_password("qwerty")
  puts("Safe_0.password        : #{safes[0].password}")
  puts("Safe_2.password        : #{safes[2].password}")

end