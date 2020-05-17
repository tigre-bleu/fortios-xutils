r"""Very experimental miscellaneous and extra utilities for fortios.
"""
from __future__ import absolute_import
from .api import (  # noqa: F401
    parse_and_save_show_configs,
    query_json_files,
    collect_networks,
    collect_and_save_networks,
    compose_networks,
    compose_and_save_networks,
    make_firewall_policy_table,
    make_firewall_policy_tables,
    make_and_save_firewall_policy_tables,
    load_firewall_policy_table,
    search_firewall_policy_table_by_addr
)


__version__ = "0.2.0"
__all__ = """
parse_and_save_show_configs
query_json_files
collect_networks
collect_and_save_networks
compose_networks
compose_and_save_networks
make_firewall_policy_table
make_firewall_policy_tables
make_and_save_firewall_policy_tables
load_firewall_policy_table
search_firewall_policy_table_by_addr
""".split()

# vim:sw=4:ts=4:et:
