#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

pytest_args=()
for arg in $@; do
	# from the CLI args, filter out some known values and forward the rest to "pytest"
	# note: we don't use "getopts" here b/c of some limitations (e.g. long options),
	#       which means that we can't combine short options (e.g. "./run-tests -Kk pattern")
	case ${arg} in
		*)
			pytest_args+=( ${arg} )
			;;
	esac
done


echo "Validating packaging metadata with an isolated build..."
tmp_build_dir=$(mktemp -d)
cleanup() {
    rm -rf "${tmp_build_dir}"
}
trap cleanup EXIT
uvx --from build pyproject-build --sdist --wheel --outdir "${tmp_build_dir}"
trap - EXIT
cleanup

echo "Running code quality checks with ruff..."
python -m ruff check .
python -m ruff format --check .

if ((${#pytest_args[@]})); then
	python -m pytest "${pytest_args[@]}"
else
	python -m pytest
fi
