#!/usr/bin/env py
"""
DXKeeper set_contest utility.

Create a DXKeeper script that will set QSOs from an ADIF file to a passed
contest id
"""

import argparse
from typing import List, Dict
import winreg

import adif_io


def collect_arguments() -> tuple[str, str]:
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description="Set DXKeeper contest for QSOs in selected ADIF file"
    )

    parser.add_argument("contestname")
    parser.add_argument("adif_filename")

    args = parser.parse_args()

    return (args.contestname, args.adif_filename)


def import_adif(adif_filename: str) -> List[Dict]:
    """Import QSOS from ADIF file."""
    qsos, _ = adif_io.read_from_file(adif_filename)

    return qsos


def write_script(qsos, contestname):
    """Write DXKeeper Script file."""
    # Get DXKeeper Scripts directory from registry
    dxkeeper_reg = winreg.OpenKeyEx(
        winreg.HKEY_CURRENT_USER,
        "SOFTWARE\\VB and VBA Program Settings\\DXKeeper\\Configuration"
    )
    script_directory = winreg.QueryValueEx(dxkeeper_reg, "ScriptDirectory")[0]
    dxkeeper_reg.Close()

    # Open script file
    script_filename = script_directory + "\\setcontestname.txt"
    with open(script_filename, 'a', encoding="utf-8") as script_file:
        # For each QSO
        for qso in qsos:
            # Set up filter values
            call = qso["CALL"]
            qso_time = adif_io.time_on(qso)
            time = qso_time.strftime('%Y-%m-%d %H:%M:%S')
            # Print Filter and Modify to DXKeeper script
            print("FILTER",
                  f"(CALL='{call}')",
                  f"AND (QSO_Begin = #{time}#)",
                  file=script_file)
            print("Modify CONTEST_ID", contestname, file=script_file)


def main():
    """Set DXKeeper contest for QSOs in selected ADIF file."""
    contestname, adif_filename = collect_arguments()

    # import QSOs from ADIF file
    qsos = import_adif(adif_filename)

    write_script(qsos, contestname)


main()
