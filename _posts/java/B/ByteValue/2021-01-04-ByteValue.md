---
title: ByteValue
permalink: Java/ByteValue
date: 2021-01-04
key: JavaJava.B.ByteValue
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.ByteValue.description }}

## Sintaxis
~~~java
public interface ByteValue extends PrimitiveValue, Comparable<ByteValue>
~~~

## Métodos
* [equals()](/Java/ByteValue/equals)
* [hashCode()](/Java/ByteValue/hashCode)
* [value()](/Java/ByteValue/value)

## Ejemplo
~~~java
{{ site.data.Java.B.ByteValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.ByteValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
