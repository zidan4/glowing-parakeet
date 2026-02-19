t = threading.Thread(target=udp_sender,args=(subnet,magic_message))
t.start()

--snip--
try:
  while True:
    --snip--
    #print "ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.¬
    code)
    # now check for the TYPE 3 and CODE
    if icmp_header.code == 3 and icmp_header.type == 3:
      # make sure host is in our target subnet
      if IPAddress(ip_header.src_address) in IPNetwork(subnet):
        # make sure it has our magic message
        if raw_buffer[len(raw_buffer)-len(magic_message):] == 
        magic_message:
          print "Host Up: %s" % ip_header.src_address
