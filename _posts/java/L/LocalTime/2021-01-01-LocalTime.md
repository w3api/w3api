---
title: LocalTime
permalink: Java/LocalTime
date: 2021-01-11
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LocalTime.description }}

## Sintaxis
~~~java
public final class LocalTime extends Object implements Temporal, TemporalAdjuster, Comparable<LocalTime>, Serializable
~~~

## Campos
* [MAX](/Java/LocalTime/MAX)
* [MIDNIGHT](/Java/LocalTime/MIDNIGHT)
* [MIN](/Java/LocalTime/MIN)
* [NOON](/Java/LocalTime/NOON)

## Métodos
* [adjustInto()](/Java/LocalTime/adjustInto)
* [atDate()](/Java/LocalTime/atDate)
* [atOffset()](/Java/LocalTime/atOffset)
* [compareTo()](/Java/LocalTime/compareTo)
* [equals()](/Java/LocalTime/equals)
* [format()](/Java/LocalTime/format)
* [from()](/Java/LocalTime/from)
* [get()](/Java/LocalTime/get)
* [getHour()](/Java/LocalTime/getHour)
* [getLong()](/Java/LocalTime/getLong)
* [getMinute()](/Java/LocalTime/getMinute)
* [getNano()](/Java/LocalTime/getNano)
* [getSecond()](/Java/LocalTime/getSecond)
* [hashCode()](/Java/LocalTime/hashCode)
* [isAfter()](/Java/LocalTime/isAfter)
* [isBefore()](/Java/LocalTime/isBefore)
* [isSupported()](/Java/LocalTime/isSupported)
* [minus()](/Java/LocalTime/minus)
* [minusHours()](/Java/LocalTime/minusHours)
* [minusMinutes()](/Java/LocalTime/minusMinutes)
* [minusNanos()](/Java/LocalTime/minusNanos)
* [minusSeconds()](/Java/LocalTime/minusSeconds)
* [now()](/Java/LocalTime/now)
* [of()](/Java/LocalTime/of)
* [ofInstant()](/Java/LocalTime/ofInstant)
* [ofNanoOfDay()](/Java/LocalTime/ofNanoOfDay)
* [ofSecondOfDay()](/Java/LocalTime/ofSecondOfDay)
* [parse()](/Java/LocalTime/parse)
* [plus()](/Java/LocalTime/plus)
* [plusHours()](/Java/LocalTime/plusHours)
* [plusMinutes()](/Java/LocalTime/plusMinutes)
* [plusNanos()](/Java/LocalTime/plusNanos)
* [plusSeconds()](/Java/LocalTime/plusSeconds)
* [query()](/Java/LocalTime/query)
* [range()](/Java/LocalTime/range)
* [toEpochSecond()](/Java/LocalTime/toEpochSecond)
* [toNanoOfDay()](/Java/LocalTime/toNanoOfDay)
* [toSecondOfDay()](/Java/LocalTime/toSecondOfDay)
* [toString()](/Java/LocalTime/toString)
* [truncatedTo()](/Java/LocalTime/truncatedTo)
* [until()](/Java/LocalTime/until)
* [with()](/Java/LocalTime/with)
* [withHour()](/Java/LocalTime/withHour)
* [withMinute()](/Java/LocalTime/withMinute)
* [withNano()](/Java/LocalTime/withNano)
* [withSecond()](/Java/LocalTime/withSecond)

## Ejemplo
~~~java
{{ site.data.Java.L.LocalTime.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
