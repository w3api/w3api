---
title: PseudoColumnUsage
permalink: /Java/PseudoColumnUsage/
date: 2021-01-11
key: Java.P.PseudoColumnUsage
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PseudoColumnUsage.description }}

## Sintaxis
~~~java
public enum PseudoColumnUsage extends Enum<PseudoColumnUsage>
~~~

## Enumerados
* [NO_USAGE_RESTRICTIONS](/Java/PseudoColumnUsage/NO_USAGE_RESTRICTIONS)
* [SELECT_LIST_ONLY](/Java/PseudoColumnUsage/SELECT_LIST_ONLY)
* [USAGE_UNKNOWN](/Java/PseudoColumnUsage/USAGE_UNKNOWN)
* [WHERE_CLAUSE_ONLY](/Java/PseudoColumnUsage/WHERE_CLAUSE_ONLY)

## Métodos
* [valueOf()](/Java/PseudoColumnUsage/valueOf)
* [values()](/Java/PseudoColumnUsage/values)

## Ejemplo
~~~java
{{ site.data.Java.P.PseudoColumnUsage.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PseudoColumnUsage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
