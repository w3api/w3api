---
title: Predicate
permalink: /Java/Predicate-java-util-function/
date: 2021-01-11
key: Java.P.Predicate-java-util-function
category: Java
tags: ['java se', 'java.util.function', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Predicate-java-util-function.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface Predicate<T>
~~~

## Métodos
* [and()](/Java/Predicate-java-util-function/and/)
* [isEqual()](/Java/Predicate-java-util-function/isEqual/)
* [negate()](/Java/Predicate-java-util-function/negate/)
* [or()](/Java/Predicate-java-util-function/or/)
* [test()](/Java/Predicate-java-util-function/test/)

## Ejemplo
~~~java
{{ site.data.Java.P.Predicate-java-util-function.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.Predicate-java-util-function.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
