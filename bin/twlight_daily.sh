#!/usr/bin/env bash

backup_cmd="${TWLIGHT_HOME}/bin/./twlight_backup.sh"
update_cmd="${TWLIGHT_HOME}/bin/./twlight_update_code.sh"
failure_cmd="${TWLIGHT_HOME}/bin/./twlight_failure.sh"

# Backup database and media files. Leave the rest to version control
${backup_cmd} || ${failure_cmd} ${backup_cmd}

# Apply the latest code from master
${update_cmd} || ${failure_cmd} ${update_cmd}
