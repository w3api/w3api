---
title: SeekableByteChannel
permalink: Java/SeekableByteChannel
date: 2021-01-11
key: JavaJava.S.SeekableByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SeekableByteChannel.description }}

## Sintaxis
~~~java
public interface SeekableByteChannel extends ByteChannel
~~~

## Métodos
* [position()](/Java/SeekableByteChannel/position)
* [read()](/Java/SeekableByteChannel/read)
* [size()](/Java/SeekableByteChannel/size)
* [truncate()](/Java/SeekableByteChannel/truncate)
* [write()](/Java/SeekableByteChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.S.SeekableByteChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SeekableByteChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
