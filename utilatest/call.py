# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import http
import json
import os

import utila

API_PREFIX = 'UTILATEST_API_PREFIX'


def decode(response, expected=None) -> dict:
    """Read binary data from response and convert them to str."""
    assert expected is None or response.status_code == expected
    result = response.data.decode('utf8')
    with contextlib.suppress(json.decoder.JSONDecodeError):
        # json format
        return json.loads(result)
    # html format
    return result


def get(
        client,
        request: str,
        expected=http.HTTPStatus.OK,
        raw: bool = False,
):
    response = client.get(request, follow_redirects=True)
    assert response.status_code == expected, f'{request}:{response.status_code}\n{response}'
    if raw:
        return response
    return decode(response)


def post(
        client,
        page: str,
        data: dict,
        expected=http.HTTPStatus.OK,
):
    response = client.post(page, data=data, follow_redirects=True)
    assert response.status_code == expected, f'{page}:{response.status_code}\n{response}'
    return decode(response, expected=expected)


def upload(client, page: str, file):
    result = apiupload(client, page, 'file', file)
    return result


def apipost(
        client,
        page: str,
        data: dict,
        prefix='',
        expected=http.HTTPStatus.OK,
):
    prefix = prefix if prefix else default()
    request = prefix + page
    return post(client, page=request, data=data, expected=expected)


def apicall(
        client,
        request: str,
        prefix='',
        expected=http.HTTPStatus.OK,
):
    prefix = prefix if prefix else default()
    cmd = prefix + request
    response = client.get(cmd, follow_redirects=True)
    assert response.status_code == expected, f'{request}:{response.status_code}\n{response}'
    return decode(response, expected=expected)


def apidelete(
        client,
        request: str,
        prefix='',
        expected=http.HTTPStatus.OK,
):
    prefix = prefix if prefix else default()
    cmd = prefix + request
    response = client.delete(cmd, follow_redirects=True)
    assert response.status_code == expected, f'{request}:{response.status_code}\n{response}'
    return decode(response, expected=expected)


def apiupload(
        client,
        page: str,
        field: str,
        path: str,
        prefix='',
        expected=http.HTTPStatus.OK,
):
    """Upload file via http post command"""
    prefix = prefix if prefix else default()
    assert field, path
    assert os.path.exists(path), path
    request = prefix + page
    try:
        import werkzeug
        fields = werkzeug.datastructures.MultiDict([(field, open(path, 'rb'))])
    except ImportError as error:
        utila.error('install werkzeug')
        raise error
    response = client.post(request, data=fields, follow_redirects=True)
    assert response.status_code == expected, f'{page}:{response.status_code}\n{response}'
    return decode(response, expected=expected)


def apiput(
        client,
        page: str,
        data: dict,
        prefix='',
        expected=http.HTTPStatus.OK,
):
    prefix = prefix if prefix else default()
    request = prefix + page
    response = client.put(request, data=data, follow_redirects=True)
    assert response.status_code == expected, f'{page}:{response.status_code}\n{response}'
    return decode(response, expected=expected)


def default():
    return os.environ.get(API_PREFIX, '')


def setup(prefix):
    os.environ[API_PREFIX] = prefix
