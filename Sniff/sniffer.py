import socket
import struct


def ethernet_frame(data):
    dst_mac, src_mac, ethernet_type = struct.unpack("! 6s 6s H", data[:14])
    return translate_mac(dst_mac), translate_mac(src_mac), ethernet_type, data[14:]


def ip_header(data):
    ipheader = struct.unpack("!BBHHHBBH4s4s",data[:20])
    ip_version = ipheader[0] >> 4
    ttl = ipheader[5]
    proto = ipheader[6]
    ip_src = ipheader[8]
    ip_dst = ipheader[9]
    return ip_version, ttl, proto, socket.inet_ntoa(ip_src), socket.inet_ntoa(ip_dst), data[20:].decode("latin-1")


def translate_mac(bytes):
    return ":".join(map("{:02x}".format, bytes)).upper()


if __name__ == "__main__":
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while 1:
        data, source = s.recvfrom(65535)
        dst_mac, src_mac, tp, ip_pkt = ethernet_frame(data)
        ip_version, ttl, proto, ip_src, ip_dst, pkt_data = ip_header(ip_pkt)
        if proto == 1:
            print("\n#####################################################")
            print("{} ---> {}".format(ip_src, ip_dst))
            print("IPv{}".format(ip_version))
            print("TTL {}".format(ttl))
            print("PROTO {}".format(proto))
            print(pkt_data)