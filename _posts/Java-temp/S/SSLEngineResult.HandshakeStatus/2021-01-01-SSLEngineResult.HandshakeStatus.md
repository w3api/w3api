---
title: SSLEngineResult.HandshakeStatus
permalink: /Java/SSLEngineResult/HandshakeStatus/
date: 2021-01-11
key: Java.S.SSLEngineResult.HandshakeStatus
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'enumerado java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLEngineResult.HandshakeStatus.description }}

## Sintaxis
~~~java
public static enum SSLEngineResult.HandshakeStatus extends Enum<SSLEngineResult.HandshakeStatus>
~~~

## Enumerados
* [FINISHED](/Java/SSLEngineResult/HandshakeStatus/FINISHED)
* [NEED_TASK](/Java/SSLEngineResult/HandshakeStatus/NEED_TASK)
* [NEED_UNWRAP](/Java/SSLEngineResult/HandshakeStatus/NEED_UNWRAP)
* [NEED_UNWRAP_AGAIN](/Java/SSLEngineResult/HandshakeStatus/NEED_UNWRAP_AGAIN)
* [NEED_WRAP](/Java/SSLEngineResult/HandshakeStatus/NEED_WRAP)
* [NOT_HANDSHAKING](/Java/SSLEngineResult/HandshakeStatus/NOT_HANDSHAKING)

## Métodos
* [valueOf()](/Java/SSLEngineResult/HandshakeStatus/valueOf)
* [values()](/Java/SSLEngineResult/HandshakeStatus/values)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLEngineResult.HandshakeStatus.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLEngineResult.HandshakeStatus.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
