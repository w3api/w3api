---
title: AsynchronousFileChannel
permalink: Java/AsynchronousFileChannel
date: 2021-01-04
key: JavaJava.A.AsynchronousFileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AsynchronousFileChannel.description }}

## Sintaxis
~~~java
public abstract class AsynchronousFileChannel extends Object implements AsynchronousChannel
~~~

## Constructores
* [AsynchronousFileChannel()](/Java/AsynchronousFileChannel/AsynchronousFileChannel/)

## Métodos
* [force()](/Java/AsynchronousFileChannel/force)
* [lock()](/Java/AsynchronousFileChannel/lock)
* [open()](/Java/AsynchronousFileChannel/open)
* [read()](/Java/AsynchronousFileChannel/read)
* [size()](/Java/AsynchronousFileChannel/size)
* [truncate()](/Java/AsynchronousFileChannel/truncate)
* [tryLock()](/Java/AsynchronousFileChannel/tryLock)
* [write()](/Java/AsynchronousFileChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.A.AsynchronousFileChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousFileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
