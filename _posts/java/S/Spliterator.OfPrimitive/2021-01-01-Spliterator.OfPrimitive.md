---
title: Spliterator.OfPrimitive
permalink: Java/Spliterator/OfPrimitive
date: 2021-01-11
key: JavaJava.S.Spliterator.OfPrimitive
category: java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Spliterator.OfPrimitive.description }}

## Sintaxis
~~~java
public static interface Spliterator.OfPrimitive<T,T_CONS,T_SPLITR extends Spliterator.OfPrimitive<T,T_CONS,T_SPLITR>> extends Spliterator<T>
~~~

## Métodos
* [forEachRemaining()](/Java/Spliterator/OfPrimitive/forEachRemaining)
* [tryAdvance()](/Java/Spliterator/OfPrimitive/tryAdvance)

## Ejemplo
~~~java
{{ site.data.Java.S.Spliterator.OfPrimitive.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Spliterator.OfPrimitive.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
