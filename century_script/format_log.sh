#!/usr/bin/env bash

format_log()
{
    if [ $# -lt 1 ]; then
      echo "Usage: $0 <logFile>"
      return
    fi

    logFile=$1

    cut -f 3 < "$logFile" | jq -r .msg | /usr/bin/grep '^{' | jq -cM . | /usr/bin/grep -v "{}"
}
