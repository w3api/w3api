---
title: ClientInfoStatus
permalink: /Java/ClientInfoStatus/
date: 2021-01-11
key: Java.C.ClientInfoStatus
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClientInfoStatus.description }}

## Sintaxis
~~~java
public enum ClientInfoStatus extends Enum<ClientInfoStatus>
~~~

## Enumerados
* [REASON_UNKNOWN](/Java/ClientInfoStatus/REASON_UNKNOWN)
* [REASON_UNKNOWN_PROPERTY](/Java/ClientInfoStatus/REASON_UNKNOWN_PROPERTY)
* [REASON_VALUE_INVALID](/Java/ClientInfoStatus/REASON_VALUE_INVALID)
* [REASON_VALUE_TRUNCATED](/Java/ClientInfoStatus/REASON_VALUE_TRUNCATED)

## Métodos
* [valueOf()](/Java/ClientInfoStatus/valueOf)
* [values()](/Java/ClientInfoStatus/values)

## Ejemplo
~~~java
{{ site.data.Java.C.ClientInfoStatus.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClientInfoStatus.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
