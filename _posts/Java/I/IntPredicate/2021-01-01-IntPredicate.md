---
title: IntPredicate
permalink: /Java/IntPredicate/
date: 2021-01-11
key: Java.I.IntPredicate
category: Java
tags: ['java se', 'java.util.function', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IntPredicate.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface IntPredicate
~~~

## Métodos
* [and()](/Java/IntPredicate/and)
* [negate()](/Java/IntPredicate/negate)
* [or()](/Java/IntPredicate/or)
* [test()](/Java/IntPredicate/test)

## Ejemplo
~~~java
{{ site.data.Java.I.IntPredicate.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.IntPredicate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
