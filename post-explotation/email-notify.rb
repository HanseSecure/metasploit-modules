# Content: Metasploit Modul to send email notification if a session is opened
# Author: Florian Hansemann | @HanseSecure | https://hansesecure.de
# Date: 05/2018


require 'msf/core'

class MetasploitModule < Msf::Post

def initialize
        super(
        'Name' => 'Email Notification for opened session',
        'Version' => '1.0',
        'Description' => 'This module will notify you with an email if a session is opened',
        'Author' => 'Florian Hansemann <info@hanseSecure.de>',
        'License' => MSF_LICENSE,
        'Platform' => 'multi')

end

def run

begin

system("python $Path2File/msf-email.py")

end
end
end
