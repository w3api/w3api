---
title: HijrahEra
permalink: Java/HijrahEra
date: 2021-01-04
key: JavaJava.H.HijrahEra
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'enumerado java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HijrahEra.description }}

## Sintaxis
~~~java
public enum HijrahEra extends Enum<HijrahEra> implements Era
~~~

## Enumerados
* [AH](/Java/HijrahEra/AH)

## Métodos
* [getDisplayName()](/Java/HijrahEra/getDisplayName)
* [getValue()](/Java/HijrahEra/getValue)
* [of()](/Java/HijrahEra/of)
* [range()](/Java/HijrahEra/range)
* [valueOf()](/Java/HijrahEra/valueOf)
* [values()](/Java/HijrahEra/values)

## Ejemplo
~~~java
{{ site.data.Java.H.HijrahEra.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HijrahEra.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
