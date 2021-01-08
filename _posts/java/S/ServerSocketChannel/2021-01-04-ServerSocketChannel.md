---
title: ServerSocketChannel
permalink: Java/ServerSocketChannel
date: 2021-01-04
key: JavaJava.S.ServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServerSocketChannel.description }}

## Sintaxis
~~~java
public abstract class ServerSocketChannel extends AbstractSelectableChannel implements NetworkChannel
~~~

## Constructores
* [ServerSocketChannel()](/Java/ServerSocketChannel/ServerSocketChannel/)

## Métodos
* [accept()](/Java/ServerSocketChannel/accept)
* [bind()](/Java/ServerSocketChannel/bind)
* [getLocalAddress()](/Java/ServerSocketChannel/getLocalAddress)
* [open()](/Java/ServerSocketChannel/open)
* [setOption()](/Java/ServerSocketChannel/setOption)
* [socket()](/Java/ServerSocketChannel/socket)
* [validOps()](/Java/ServerSocketChannel/validOps)

## Ejemplo
~~~java
{{ site.data.Java.S.ServerSocketChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
