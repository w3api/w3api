---
title: FloatValue
permalink: Java/FloatValue
date: 2021-01-11
key: JavaJava.F.FloatValue
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FloatValue.description }}

## Sintaxis
~~~java
public interface FloatValue extends PrimitiveValue, Comparable<FloatValue>
~~~

## Métodos
* [equals()](/Java/FloatValue/equals)
* [hashCode()](/Java/FloatValue/hashCode)
* [value()](/Java/FloatValue/value)

## Ejemplo
~~~java
{{ site.data.Java.F.FloatValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FloatValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
