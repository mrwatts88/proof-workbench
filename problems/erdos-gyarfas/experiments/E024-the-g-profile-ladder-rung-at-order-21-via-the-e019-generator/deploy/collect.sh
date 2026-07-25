#!/bin/bash
# O012 step 5 (retrieve) — pull every production volume down to a staging tree.
#
#   collect.sh <n_services> <staging_dir>
#
# Each production service writes to its own volume at /e024.  Downloads land in
# <staging_dir>/part-<k>/ and are merged and verified afterwards by
# merge_verify.py, which is where the integrity checking lives.
set -euo pipefail

N=${1:?usage: collect.sh <n_services> <staging_dir>}
STAGE=${2:?usage: collect.sh <n_services> <staging_dir>}
CTX=/private/tmp/claude-501/-Users-mattwatts-code-rh/34080fcf-635d-458d-88bf-8a372e5a8195/scratchpad/e024-cloud
export RAILWAY_CALLER=skill:use-railway@1.3.6
export RAILWAY_AGENT_SESSION=rh-e024-migration-1
cd "$CTX"

mkdir -p "$STAGE"
for k in $(seq 0 $((N - 1))); do
  echo "=== downloading part-$k-volume:/e024 -> $STAGE/part-$k"
  railway volume files --volume "part-$k-volume" download /e024 "$STAGE/part-$k" \
      --overwrite --concurrency 32 --json | tail -2
done

echo
echo "downloaded into $STAGE:"
du -sh "$STAGE"/part-* 2>/dev/null || true
