FROM python:3.11.0a7-slim

ARG _USER="lilchz"
ARG _UID="1001"
ARG _GID="100"
ARG _SHELL="/bin/bash"

ARG BUILD_DATE

RUN useradd -m -s "${_SHELL}" -N -u "${_UID}" "${_USER}"

ENV USER ${_USER}
ENV UID ${_UID}
ENV GID ${_GID}
ENV HOME /home/${_USER}
ENV PATH "${HOME}/.local/bin/:${PATH}"
ENV PIP_NO_CACHE_DIR "true"

RUN mkdir /app && chown ${UID}:${GID} /app

USER ${_USER}

COPY --chown=${UID}:${GID} ./requirements* /app/
WORKDIR /app

RUN pip install -r requirements.lock -r requirements-test.txt

CMD bash
