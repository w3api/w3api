---
title: LongBuffer
permalink: /Java/LongBuffer/
date: 2021-01-11
key: Java.L.LongBuffer
category: Java
tags: ['java se', 'java.nio', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LongBuffer.description }}

## Sintaxis
~~~java
public abstract class LongBuffer extends Buffer implements Comparable<LongBuffer>
~~~

## Métodos
* [allocate()](/Java/LongBuffer/allocate/)
* [array()](/Java/LongBuffer/array/)
* [arrayOffset()](/Java/LongBuffer/arrayOffset/)
* [asReadOnlyBuffer()](/Java/LongBuffer/asReadOnlyBuffer/)
* [compact()](/Java/LongBuffer/compact/)
* [compareTo()](/Java/LongBuffer/compareTo/)
* [duplicate()](/Java/LongBuffer/duplicate/)
* [equals()](/Java/LongBuffer/equals/)
* [get()](/Java/LongBuffer/get/)
* [hasArray()](/Java/LongBuffer/hasArray/)
* [hashCode()](/Java/LongBuffer/hashCode/)
* [isDirect()](/Java/LongBuffer/isDirect/)
* [order()](/Java/LongBuffer/order/)
* [put()](/Java/LongBuffer/put/)
* [slice()](/Java/LongBuffer/slice/)
* [toString()](/Java/LongBuffer/toString/)
* [wrap()](/Java/LongBuffer/wrap/)

## Ejemplo
~~~java
{{ site.data.Java.L.LongBuffer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
