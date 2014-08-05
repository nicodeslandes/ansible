#!powershell
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# WANT_JSON
# POWERSHELL_COMMON

$ErrorActionPreference = "Stop"
trap
{
	Fail-Json $_.ToString()
};

$src = $params.src
$dest = $params.dest

Set-Attr $result.copy src $src;

$params = Parse-Args $args;

$result = New-Object psobject @{
    copy = New-Object psobject
}

$src = $params.src
$dest = $params.dest

Set-Attr $result.copy src $src;
Set-Attr $result.copy dest $dest;
Set-Attr $result.copy original_basename $params.original_basename;
Set-Attr $result changed $true;

$destParent = [IO.Path]::GetDirectoryName($dest)
if (!(Test-Path -PathType Container $destParent)) {
	mkdir -Force $destParent
}

cp $src $dest

Exit-Json $result;
