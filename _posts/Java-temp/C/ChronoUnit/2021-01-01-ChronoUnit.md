---
title: ChronoUnit
permalink: /Java/ChronoUnit/
date: 2021-01-11
key: Java.C.ChronoUnit
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'enumerado java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ChronoUnit.description }}

## Sintaxis
~~~java
public enum ChronoUnit extends Enum<ChronoUnit> implements TemporalUnit
~~~

## Enumerados
* [CENTURIES](/Java/ChronoUnit/CENTURIES)
* [DAYS](/Java/ChronoUnit/DAYS)
* [DECADES](/Java/ChronoUnit/DECADES)
* [ERAS](/Java/ChronoUnit/ERAS)
* [FOREVER](/Java/ChronoUnit/FOREVER)
* [HALF_DAYS](/Java/ChronoUnit/HALF_DAYS)
* [HOURS](/Java/ChronoUnit/HOURS)
* [MICROS](/Java/ChronoUnit/MICROS)
* [MILLENNIA](/Java/ChronoUnit/MILLENNIA)
* [MILLIS](/Java/ChronoUnit/MILLIS)
* [MINUTES](/Java/ChronoUnit/MINUTES)
* [MONTHS](/Java/ChronoUnit/MONTHS)
* [NANOS](/Java/ChronoUnit/NANOS)
* [SECONDS](/Java/ChronoUnit/SECONDS)
* [WEEKS](/Java/ChronoUnit/WEEKS)
* [YEARS](/Java/ChronoUnit/YEARS)

## Métodos
* [getDuration()](/Java/ChronoUnit/getDuration)
* [isDateBased()](/Java/ChronoUnit/isDateBased)
* [isDurationEstimated()](/Java/ChronoUnit/isDurationEstimated)
* [isTimeBased()](/Java/ChronoUnit/isTimeBased)
* [valueOf()](/Java/ChronoUnit/valueOf)
* [values()](/Java/ChronoUnit/values)

## Ejemplo
~~~java
{{ site.data.Java.C.ChronoUnit.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ChronoUnit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
