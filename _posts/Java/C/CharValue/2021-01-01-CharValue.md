---
title: CharValue
permalink: /Java/CharValue/
date: 2021-01-11
key: Java.C.CharValue
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CharValue.description }}

## Sintaxis
~~~java
public interface CharValue extends PrimitiveValue, Comparable<CharValue>
~~~

## Métodos
* [equals()](/Java/CharValue/equals/)
* [hashCode()](/Java/CharValue/hashCode/)
* [value()](/Java/CharValue/value/)

## Ejemplo
~~~java
{{ site.data.Java.C.CharValue.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CharValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
