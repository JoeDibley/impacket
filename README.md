Impacket - Exchanger.py Fork
=================

It's the temporary PT SWARM's Impacket fork for contributing and sharing our knowledge about Windows.

Features
---------------------------

 * exchanger.py — A tool to connect to Exchange web interface via MS-OXNSPI protocol
 * rpcmap.py — A tool for the remote enumeration of MSRPC UUIDs

Exchanger.py
---------------------------
```
usage: exchanger.py target nspi [-h]
                                {list-tables,dump-tables,guid-known,dnt-lookup}
                                ...

positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  {nspi}                A module name
    nspi                Attack NSPI interface

optional arguments:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG and EXTENDED output ON
  -rpc-hostname RPC_HOSTNAME
                        A name of the server in GUID (preferred) or NetBIOS
                        name format (see description in the beggining of this
                        file)
positional arguments:
  {list-tables,dump-tables,guid-known,dnt-lookup}
                        A submodule name
    list-tables         List Address Books
    dump-tables         Dump Address Books
    guid-known          Retrieve Active Directory objects by GUID / GUIDs
    dnt-lookup          Lookup Distinguished Name Tags

optional arguments:
  -h, --help            show this help message and exit

```
