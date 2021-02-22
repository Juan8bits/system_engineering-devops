|#!/usr/bin/env ruby

if ARGV.length < 2
    puts ARGV[0].scan(/^[0-9]{10,10}/).join
end
