---
title: Spliterator.OfInt
permalink: /Java/Spliterator/OfInt/
date: 2021-01-11
key: Java.S.Spliterator.OfInt
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Spliterator.OfInt.description }}

## Sintaxis
~~~java
public static interface Spliterator.OfInt extends Spliterator.OfPrimitive<Integer,IntConsumer,Spliterator.OfInt>
~~~

## Métodos
* [forEachRemaining()](/Java/Spliterator/OfInt/forEachRemaining)
* [tryAdvance()](/Java/Spliterator/OfInt/tryAdvance)

## Ejemplo
~~~java
{{ site.data.Java.S.Spliterator.OfInt.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Spliterator.OfInt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
