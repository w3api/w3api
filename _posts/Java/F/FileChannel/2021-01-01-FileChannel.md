---
title: FileChannel
permalink: /Java/FileChannel/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FileChannel.description }}

## Sintaxis
~~~java
public abstract class FileChannel extends AbstractInterruptibleChannel implements SeekableByteChannel, GatheringByteChannel, ScatteringByteChannel
~~~

## Constructores
* [FileChannel()](/Java/FileChannel/FileChannel/)

## Métodos
* [force()](/Java/FileChannel/force)
* [lock()](/Java/FileChannel/lock)
* [map()](/Java/FileChannel/map)
* [open()](/Java/FileChannel/open)
* [position()](/Java/FileChannel/position)
* [read()](/Java/FileChannel/read)
* [size()](/Java/FileChannel/size)
* [transferFrom()](/Java/FileChannel/transferFrom)
* [transferTo()](/Java/FileChannel/transferTo)
* [truncate()](/Java/FileChannel/truncate)
* [tryLock()](/Java/FileChannel/tryLock)
* [write()](/Java/FileChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.F.FileChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
