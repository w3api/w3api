---
title: Spliterator.OfLong
permalink: /Java/Spliterator/OfLong/
date: 2021-01-11
key: Java.S.Spliterator.OfLong
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Spliterator.OfLong.description }}

## Sintaxis
~~~java
public static interface Spliterator.OfLong extends Spliterator.OfPrimitive<Long,LongConsumer,Spliterator.OfLong>
~~~

## Métodos
* [forEachRemaining()](/Java/Spliterator/OfLong/forEachRemaining)
* [tryAdvance()](/Java/Spliterator/OfLong/tryAdvance)

## Ejemplo
~~~java
{{ site.data.Java.S.Spliterator.OfLong.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Spliterator.OfLong.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
