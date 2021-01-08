---
title: CharBuffer
permalink: Java/CharBuffer
date: 2021-01-04
key: JavaJava.C.CharBuffer
category: java
tags: ['java se', 'java.nio', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CharBuffer.description }}

## Sintaxis
~~~java
public abstract class CharBuffer extends Buffer implements Comparable<CharBuffer>, Appendable, CharSequence, Readable
~~~

## Métodos
* [allocate()](/Java/CharBuffer/allocate)
* [append()](/Java/CharBuffer/append)
* [array()](/Java/CharBuffer/array)
* [arrayOffset()](/Java/CharBuffer/arrayOffset)
* [asReadOnlyBuffer()](/Java/CharBuffer/asReadOnlyBuffer)
* [charAt()](/Java/CharBuffer/charAt)
* [compact()](/Java/CharBuffer/compact)
* [compareTo()](/Java/CharBuffer/compareTo)
* [duplicate()](/Java/CharBuffer/duplicate)
* [equals()](/Java/CharBuffer/equals)
* [get()](/Java/CharBuffer/get)
* [hasArray()](/Java/CharBuffer/hasArray)
* [hashCode()](/Java/CharBuffer/hashCode)
* [isDirect()](/Java/CharBuffer/isDirect)
* [length()](/Java/CharBuffer/length)
* [order()](/Java/CharBuffer/order)
* [put()](/Java/CharBuffer/put)
* [read()](/Java/CharBuffer/read)
* [slice()](/Java/CharBuffer/slice)
* [subSequence()](/Java/CharBuffer/subSequence)
* [toString()](/Java/CharBuffer/toString)
* [wrap()](/Java/CharBuffer/wrap)

## Ejemplo
~~~java
{{ site.data.Java.C.CharBuffer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
