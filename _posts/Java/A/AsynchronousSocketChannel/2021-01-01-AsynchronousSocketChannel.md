---
title: AsynchronousSocketChannel
permalink: /Java/AsynchronousSocketChannel/
date: 2021-01-11
key: Java.A.AsynchronousSocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AsynchronousSocketChannel.description }}

## Sintaxis
~~~java
public abstract class AsynchronousSocketChannel extends Object implements AsynchronousByteChannel, NetworkChannel
~~~

## Constructores
* [AsynchronousSocketChannel()](/Java/AsynchronousSocketChannel/AsynchronousSocketChannel/)

## Métodos
* [bind()](/Java/AsynchronousSocketChannel/bind)
* [connect()](/Java/AsynchronousSocketChannel/connect)
* [getLocalAddress()](/Java/AsynchronousSocketChannel/getLocalAddress)
* [getRemoteAddress()](/Java/AsynchronousSocketChannel/getRemoteAddress)
* [open()](/Java/AsynchronousSocketChannel/open)
* [provider()](/Java/AsynchronousSocketChannel/provider)
* [read()](/Java/AsynchronousSocketChannel/read)
* [setOption()](/Java/AsynchronousSocketChannel/setOption)
* [shutdownInput()](/Java/AsynchronousSocketChannel/shutdownInput)
* [shutdownOutput()](/Java/AsynchronousSocketChannel/shutdownOutput)
* [write()](/Java/AsynchronousSocketChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.A.AsynchronousSocketChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
