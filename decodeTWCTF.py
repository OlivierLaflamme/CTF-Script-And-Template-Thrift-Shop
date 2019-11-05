#!/usr/bin/env ruby
# encoding: ascii-8bit

N = 512
ystar = IO.binread('dump_y').split.map(&:to_f)
len = 280
value = IO.binread("values/280.dump").split.map(&:to_i) # vector v
e = []
N.times do |i|
  N.times do |j|
    e << ystar[i * N + j] if i + j >= N / 2
  end
end
result = ''
0.upto(8 * len - 1) do |i|
  sym = [0] * i + value + [0] * (len * 8 - 1 - i)
  # dot product < 0 ? 0 : 1
  result << (sym.zip(e[0, sym.size]).reduce(0.0) { |s, (a, b)| s + a * b } < 0 ? '0' : '1')
end
p result.scan(/.{8}/).map { |v| v.to_i(2)}.pack("C*")
