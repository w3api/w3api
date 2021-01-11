---
title: SSLEngineResult.SSLEngineResult()
permalink: Java/SSLEngineResult/SSLEngineResult
date: 2021-01-11
key: JavaJava.S.SSLEngineResult
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngineResult.constructores valor="SSLEngineResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SSLEngineResult(SSLEngineResult.Status status, SSLEngineResult.HandshakeStatus handshakeStatus, int bytesConsumed, int bytesProduced)
public SSLEngineResult(SSLEngineResult.Status status, SSLEngineResult.HandshakeStatus handshakeStatus, int bytesConsumed, int bytesProduced, long sequenceNumber)
~~~

## Parámetros
* **SSLEngineResult.HandshakeStatus handshakeStatus**,  {% include w3api/param_description.html metodo=_dato parametro="SSLEngineResult.HandshakeStatus handshakeStatus" %}
* **SSLEngineResult.Status status**,  {% include w3api/param_description.html metodo=_dato parametro="SSLEngineResult.Status status" %}
* **int bytesProduced**,  {% include w3api/param_description.html metodo=_dato parametro="int bytesProduced" %}
* **int bytesConsumed**,  {% include w3api/param_description.html metodo=_dato parametro="int bytesConsumed" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLEngineResult](/Java/SSLEngineResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
