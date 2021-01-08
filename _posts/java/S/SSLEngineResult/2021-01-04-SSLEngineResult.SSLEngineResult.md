---
title: SSLEngineResult.SSLEngineResult()
permalink: Java/SSLEngineResult/SSLEngineResult
date: 2021-01-04
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
* **int bytesConsumed**,  {% include w3api/param_description.html metodo=_data parametro="int bytesConsumed" %}
* **SSLEngineResult.Status status**,  {% include w3api/param_description.html metodo=_data parametro="SSLEngineResult.Status status" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long sequenceNumber" %}
* **int bytesProduced**,  {% include w3api/param_description.html metodo=_data parametro="int bytesProduced" %}
* **SSLEngineResult.HandshakeStatus handshakeStatus**,  {% include w3api/param_description.html metodo=_data parametro="SSLEngineResult.HandshakeStatus handshakeStatus" %}

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
{%- for _ldc in site.data.Java.S.SSLEngineResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
