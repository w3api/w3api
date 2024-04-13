---
title: SSLEngineResult.Status
permalink: /Java/SSLEngineResult/Status/
date: 2021-01-11
key: Java.S.SSLEngineResult.Status
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'enumerado java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLEngineResult.Status.description }}

## Sintaxis
~~~java
public static enum SSLEngineResult.Status extends Enum<SSLEngineResult.Status>
~~~

## Enumerados
* [BUFFER_OVERFLOW](/Java/SSLEngineResult/Status/BUFFER_OVERFLOW)
* [BUFFER_UNDERFLOW](/Java/SSLEngineResult/Status/BUFFER_UNDERFLOW)
* [CLOSED](/Java/SSLEngineResult/Status/CLOSED)
* [OK](/Java/SSLEngineResult/Status/OK)

## Métodos
* [valueOf()](/Java/SSLEngineResult/Status/valueOf)
* [values()](/Java/SSLEngineResult/Status/values)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLEngineResult.Status.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLEngineResult.Status.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
