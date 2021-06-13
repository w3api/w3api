---
title: LongStream
permalink: Java/LongStream
date: 2021-01-11
key: Java.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LongStream.description }}

## Sintaxis
~~~java
public interface LongStream extends BaseStream<Long,LongStream>
~~~

## Métodos
* [allMatch()](/Java/LongStream/allMatch)
* [anyMatch()](/Java/LongStream/anyMatch)
* [asDoubleStream()](/Java/LongStream/asDoubleStream)
* [average()](/Java/LongStream/average)
* [boxed()](/Java/LongStream/boxed)
* [builder()](/Java/LongStream/builder)
* [collect()](/Java/LongStream/collect)
* [concat()](/Java/LongStream/concat)
* [count()](/Java/LongStream/count)
* [distinct()](/Java/LongStream/distinct)
* [dropWhile()](/Java/LongStream/dropWhile)
* [empty()](/Java/LongStream/empty)
* [filter()](/Java/LongStream/filter)
* [findAny()](/Java/LongStream/findAny)
* [findFirst()](/Java/LongStream/findFirst)
* [flatMap()](/Java/LongStream/flatMap)
* [forEach()](/Java/LongStream/forEach)
* [forEachOrdered()](/Java/LongStream/forEachOrdered)
* [generate()](/Java/LongStream/generate)
* [iterate()](/Java/LongStream/iterate)
* [limit()](/Java/LongStream/limit)
* [map()](/Java/LongStream/map)
* [mapToDouble()](/Java/LongStream/mapToDouble)
* [mapToInt()](/Java/LongStream/mapToInt)
* [mapToObj()](/Java/LongStream/mapToObj)
* [max()](/Java/LongStream/max)
* [min()](/Java/LongStream/min)
* [noneMatch()](/Java/LongStream/noneMatch)
* [of()](/Java/LongStream/of)
* [peek()](/Java/LongStream/peek)
* [range()](/Java/LongStream/range)
* [rangeClosed()](/Java/LongStream/rangeClosed)
* [reduce()](/Java/LongStream/reduce)
* [skip()](/Java/LongStream/skip)
* [sorted()](/Java/LongStream/sorted)
* [sum()](/Java/LongStream/sum)
* [summaryStatistics()](/Java/LongStream/summaryStatistics)
* [takeWhile()](/Java/LongStream/takeWhile)
* [toArray()](/Java/LongStream/toArray)

## Ejemplo
~~~java
{{ site.data.Java.L.LongStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
