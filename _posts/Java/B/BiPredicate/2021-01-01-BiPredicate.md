---
title: BiPredicate
permalink: /Java/BiPredicate/
date: 2021-01-11
key: Java.B.BiPredicate
category: Java
tags: ['java se', 'java.util.function', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BiPredicate.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface BiPredicate<T,U>
~~~

## Métodos
* [and()](/Java/BiPredicate/and/)
* [negate()](/Java/BiPredicate/negate/)
* [or()](/Java/BiPredicate/or/)
* [test()](/Java/BiPredicate/test/)

## Ejemplo
~~~java
{{ site.data.Java.B.BiPredicate.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BiPredicate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
