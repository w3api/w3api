---
title: AsynchronousServerSocketChannel
permalink: Java/AsynchronousServerSocketChannel
date: 2021-01-04
key: JavaJava.A.AsynchronousServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AsynchronousServerSocketChannel.description }}

## Sintaxis
~~~java
public abstract class AsynchronousServerSocketChannel extends Object implements AsynchronousChannel, NetworkChannel
~~~

## Constructores
* [AsynchronousServerSocketChannel()](/Java/AsynchronousServerSocketChannel/AsynchronousServerSocketChannel/)

## Métodos
* [accept()](/Java/AsynchronousServerSocketChannel/accept)
* [bind()](/Java/AsynchronousServerSocketChannel/bind)
* [getLocalAddress()](/Java/AsynchronousServerSocketChannel/getLocalAddress)
* [open()](/Java/AsynchronousServerSocketChannel/open)
* [provider()](/Java/AsynchronousServerSocketChannel/provider)
* [setOption()](/Java/AsynchronousServerSocketChannel/setOption)

## Ejemplo
~~~java
{{ site.data.Java.A.AsynchronousServerSocketChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousServerSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
