---
title: ChronoField
permalink: Java/ChronoField
date: 2021-01-04
key: JavaJava.C.ChronoField
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'enumerado java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ChronoField.description }}

## Sintaxis
~~~java
public enum ChronoField extends Enum<ChronoField> implements TemporalField
~~~

## Enumerados
* [ALIGNED_DAY_OF_WEEK_IN_MONTH](/Java/ChronoField/ALIGNED_DAY_OF_WEEK_IN_MONTH)
* [ALIGNED_DAY_OF_WEEK_IN_YEAR](/Java/ChronoField/ALIGNED_DAY_OF_WEEK_IN_YEAR)
* [ALIGNED_WEEK_OF_MONTH](/Java/ChronoField/ALIGNED_WEEK_OF_MONTH)
* [ALIGNED_WEEK_OF_YEAR](/Java/ChronoField/ALIGNED_WEEK_OF_YEAR)
* [AMPM_OF_DAY](/Java/ChronoField/AMPM_OF_DAY)
* [CLOCK_HOUR_OF_AMPM](/Java/ChronoField/CLOCK_HOUR_OF_AMPM)
* [CLOCK_HOUR_OF_DAY](/Java/ChronoField/CLOCK_HOUR_OF_DAY)
* [DAY_OF_MONTH](/Java/ChronoField/DAY_OF_MONTH)
* [DAY_OF_WEEK](/Java/ChronoField/DAY_OF_WEEK)
* [DAY_OF_YEAR](/Java/ChronoField/DAY_OF_YEAR)
* [EPOCH_DAY](/Java/ChronoField/EPOCH_DAY)
* [ERA](/Java/ChronoField/ERA)
* [HOUR_OF_AMPM](/Java/ChronoField/HOUR_OF_AMPM)
* [HOUR_OF_DAY](/Java/ChronoField/HOUR_OF_DAY)
* [INSTANT_SECONDS](/Java/ChronoField/INSTANT_SECONDS)
* [MICRO_OF_DAY](/Java/ChronoField/MICRO_OF_DAY)
* [MICRO_OF_SECOND](/Java/ChronoField/MICRO_OF_SECOND)
* [MILLI_OF_DAY](/Java/ChronoField/MILLI_OF_DAY)
* [MILLI_OF_SECOND](/Java/ChronoField/MILLI_OF_SECOND)
* [MINUTE_OF_DAY](/Java/ChronoField/MINUTE_OF_DAY)
* [MINUTE_OF_HOUR](/Java/ChronoField/MINUTE_OF_HOUR)
* [MONTH_OF_YEAR](/Java/ChronoField/MONTH_OF_YEAR)
* [NANO_OF_DAY](/Java/ChronoField/NANO_OF_DAY)
* [NANO_OF_SECOND](/Java/ChronoField/NANO_OF_SECOND)
* [OFFSET_SECONDS](/Java/ChronoField/OFFSET_SECONDS)
* [PROLEPTIC_MONTH](/Java/ChronoField/PROLEPTIC_MONTH)
* [SECOND_OF_DAY](/Java/ChronoField/SECOND_OF_DAY)
* [SECOND_OF_MINUTE](/Java/ChronoField/SECOND_OF_MINUTE)
* [YEAR](/Java/ChronoField/YEAR)
* [YEAR_OF_ERA](/Java/ChronoField/YEAR_OF_ERA)

## Métodos
* [checkValidIntValue()](/Java/ChronoField/checkValidIntValue)
* [checkValidValue()](/Java/ChronoField/checkValidValue)
* [isDateBased()](/Java/ChronoField/isDateBased)
* [isTimeBased()](/Java/ChronoField/isTimeBased)
* [range()](/Java/ChronoField/range)
* [valueOf()](/Java/ChronoField/valueOf)
* [values()](/Java/ChronoField/values)

## Ejemplo
~~~java
{{ site.data.Java.C.ChronoField.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoField.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
