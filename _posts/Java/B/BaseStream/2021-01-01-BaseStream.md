---
title: BaseStream
permalink: /Java/BaseStream/
date: 2021-01-11
key: Java.B.BaseStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BaseStream.description }}

## Sintaxis
~~~java
public interface BaseStream<T,S extends BaseStream<T,S>> extends AutoCloseable
~~~

## Métodos
* [close()](/Java/BaseStream/close/)
* [isParallel()](/Java/BaseStream/isParallel/)
* [iterator()](/Java/BaseStream/iterator/)
* [onClose()](/Java/BaseStream/onClose/)
* [parallel()](/Java/BaseStream/parallel/)
* [sequential()](/Java/BaseStream/sequential/)
* [spliterator()](/Java/BaseStream/spliterator/)
* [unordered()](/Java/BaseStream/unordered/)

## Ejemplo
~~~java
{{ site.data.Java.B.BaseStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BaseStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
