---
title: Spliterator
permalink: /Java/Spliterator/
date: 2021-01-11
key: Java.S.Spliterator
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Spliterator.description }}

## Sintaxis
~~~java
public interface Spliterator<T>
~~~

## Campos
* [CONCURRENT](/Java/Spliterator/CONCURRENT)
* [DISTINCT](/Java/Spliterator/DISTINCT)
* [IMMUTABLE](/Java/Spliterator/IMMUTABLE)
* [NONNULL](/Java/Spliterator/NONNULL)
* [ORDERED](/Java/Spliterator/ORDERED)
* [SIZED](/Java/Spliterator/SIZED)
* [SORTED](/Java/Spliterator/SORTED)
* [SUBSIZED](/Java/Spliterator/SUBSIZED)

## Métodos
* [characteristics()](/Java/Spliterator/characteristics)
* [estimateSize()](/Java/Spliterator/estimateSize)
* [forEachRemaining()](/Java/Spliterator/forEachRemaining)
* [getComparator()](/Java/Spliterator/getComparator)
* [getExactSizeIfKnown()](/Java/Spliterator/getExactSizeIfKnown)
* [hasCharacteristics()](/Java/Spliterator/hasCharacteristics)
* [tryAdvance()](/Java/Spliterator/tryAdvance)
* [trySplit()](/Java/Spliterator/trySplit)

## Ejemplo
~~~java
{{ site.data.Java.S.Spliterator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Spliterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
