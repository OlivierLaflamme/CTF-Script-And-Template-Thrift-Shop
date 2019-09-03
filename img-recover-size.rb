#!/usr/bin/env ruby
# png_size_recover.rb image
#

require 'crc'

abort "Usage: ./png_size_recover.rb <png_file>" if ARGV.empty?

max = 3000
@png_file = ARGV[0]

data = File.binread(@png_file)

ihdr_head = data[12,4]
org_width = data[16,4]
org_high  = data[20,4]
ihdr_tail = data[24,5]
crc       = data[29,4]

ihdr = ihdr_head + org_width + org_high + ihdr_tail
if CRC.crc32.digest(ihdr) == crc
  abort 'No problem with the picture'
end


def recover_file(data, values)
  values.each do |name, i|
    if name == :width
      data[16,4] = [i].pack('i>')
    else
      data[20,4] = [i].pack('i>')
    end
    puts "[+] recover #{name}: #{i}"
  end

  file = "recover_#{@png_file}"
  File.binwrite(file, data)
  puts "[+] save to: #{file}"
  exit()
end


max.times do |i|
  ihdr = ihdr_head + [i].pack('i>') + org_high + ihdr_tail
  recover_file(data, width: i) if CRC.crc32.digest(ihdr) == crc

  ihdr = ihdr_head + org_width + [i].pack('i>') + ihdr_tail
  recover_file(data, high: i) if CRC.crc32.digest(ihdr) == crc
end

(1..max).each do |wi|
  width = [wi].pack('i>')
  (1..max).each do |hi|
    ihdr = ihdr_head + width + [hi].pack('i>') + ihdr_tail
    recover_file(data, width: wi, high: hi) if CRC.crc32.digest(ihdr) == crc
  end
end

puts "[!] recover fail"
