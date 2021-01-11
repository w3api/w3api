---
title: ChronoZonedDateTime
permalink: Java/ChronoZonedDateTime
date: 2021-01-11
key: JavaJava.C.ChronoZonedDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ChronoZonedDateTime.description }}

## Sintaxis
~~~java
public interface ChronoZonedDateTime<D extends ChronoLocalDate> extends Temporal, Comparable<ChronoZonedDateTime<?>>
~~~

## Métodos
* [compareTo()](/Java/ChronoZonedDateTime/compareTo)
* [equals()](/Java/ChronoZonedDateTime/equals)
* [format()](/Java/ChronoZonedDateTime/format)
* [from()](/Java/ChronoZonedDateTime/from)
* [getChronology()](/Java/ChronoZonedDateTime/getChronology)
* [getOffset()](/Java/ChronoZonedDateTime/getOffset)
* [getZone()](/Java/ChronoZonedDateTime/getZone)
* [hashCode()](/Java/ChronoZonedDateTime/hashCode)
* [isAfter()](/Java/ChronoZonedDateTime/isAfter)
* [isBefore()](/Java/ChronoZonedDateTime/isBefore)
* [isEqual()](/Java/ChronoZonedDateTime/isEqual)
* [isSupported()](/Java/ChronoZonedDateTime/isSupported)
* [minus()](/Java/ChronoZonedDateTime/minus)
* [plus()](/Java/ChronoZonedDateTime/plus)
* [query()](/Java/ChronoZonedDateTime/query)
* [timeLineOrder()](/Java/ChronoZonedDateTime/timeLineOrder)
* [toEpochSecond()](/Java/ChronoZonedDateTime/toEpochSecond)
* [toInstant()](/Java/ChronoZonedDateTime/toInstant)
* [toLocalDate()](/Java/ChronoZonedDateTime/toLocalDate)
* [toLocalDateTime()](/Java/ChronoZonedDateTime/toLocalDateTime)
* [toLocalTime()](/Java/ChronoZonedDateTime/toLocalTime)
* [toString()](/Java/ChronoZonedDateTime/toString)
* [with()](/Java/ChronoZonedDateTime/with)
* [withEarlierOffsetAtOverlap()](/Java/ChronoZonedDateTime/withEarlierOffsetAtOverlap)
* [withLaterOffsetAtOverlap()](/Java/ChronoZonedDateTime/withLaterOffsetAtOverlap)
* [withZoneSameInstant()](/Java/ChronoZonedDateTime/withZoneSameInstant)
* [withZoneSameLocal()](/Java/ChronoZonedDateTime/withZoneSameLocal)

## Ejemplo
~~~java
{{ site.data.Java.C.ChronoZonedDateTime.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoZonedDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
