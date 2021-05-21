#
# sambacc: a samba container configuration tool
# Copyright (C) 2021  John Mulligan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#

import os

from .cli import commands, Fail


def _check_args(parser):
    parser.add_argument(
        "target",
        choices=["winbind"],
        help="Name of the target subsystem to check.",
    )


@commands.command(name="check", arg_func=_check_args)
def check(cli, config):
    """Check that a given subsystem is functioning."""
    if cli.target == "winbind":
        cmd = [
            "wbinfo",
            "--ping",
        ]
        os.execvp(cmd[0], cmd)
    else:
        raise Fail("unknown subsystem: {}".format(cli.target))
