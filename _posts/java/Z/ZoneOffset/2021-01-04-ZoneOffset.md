---
title: ZoneOffset
permalink: Java/ZoneOffset
date: 2021-01-04
key: JavaJava.Z.ZoneOffset
category: java
tags: ['java se', 'java.time', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.Z.ZoneOffset.description }}

## Sintaxis
~~~java
public final class ZoneOffset extends ZoneId implements TemporalAccessor, TemporalAdjuster, Comparable<ZoneOffset>, Serializable
~~~

## Campos
* [MAX](/Java/ZoneOffset/MAX)
* [MIN](/Java/ZoneOffset/MIN)
* [UTC](/Java/ZoneOffset/UTC)

## Métodos
* [adjustInto()](/Java/ZoneOffset/adjustInto)
* [compareTo()](/Java/ZoneOffset/compareTo)
* [equals()](/Java/ZoneOffset/equals)
* [from()](/Java/ZoneOffset/from)
* [get()](/Java/ZoneOffset/get)
* [getId()](/Java/ZoneOffset/getId)
* [getLong()](/Java/ZoneOffset/getLong)
* [getRules()](/Java/ZoneOffset/getRules)
* [getTotalSeconds()](/Java/ZoneOffset/getTotalSeconds)
* [hashCode()](/Java/ZoneOffset/hashCode)
* [isSupported()](/Java/ZoneOffset/isSupported)
* [of()](/Java/ZoneOffset/of)
* [ofHours()](/Java/ZoneOffset/ofHours)
* [ofHoursMinutes()](/Java/ZoneOffset/ofHoursMinutes)
* [ofHoursMinutesSeconds()](/Java/ZoneOffset/ofHoursMinutesSeconds)
* [ofTotalSeconds()](/Java/ZoneOffset/ofTotalSeconds)
* [query()](/Java/ZoneOffset/query)
* [range()](/Java/ZoneOffset/range)
* [toString()](/Java/ZoneOffset/toString)

## Ejemplo
~~~java
{{ site.data.Java.Z.ZoneOffset.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Z.ZoneOffset.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
