---
title: AsynchronousChannelProvider
permalink: Java/AsynchronousChannelProvider
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelProvider
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AsynchronousChannelProvider.description }}

## Sintaxis
~~~java
public abstract class AsynchronousChannelProvider extends Object
~~~

## Constructores
* [AsynchronousChannelProvider()](/Java/AsynchronousChannelProvider/AsynchronousChannelProvider/)

## Métodos
* [openAsynchronousChannelGroup()](/Java/AsynchronousChannelProvider/openAsynchronousChannelGroup)
* [openAsynchronousServerSocketChannel()](/Java/AsynchronousChannelProvider/openAsynchronousServerSocketChannel)
* [openAsynchronousSocketChannel()](/Java/AsynchronousChannelProvider/openAsynchronousSocketChannel)
* [provider()](/Java/AsynchronousChannelProvider/provider)

## Ejemplo
~~~java
{{ site.data.Java.A.AsynchronousChannelProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousChannelProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
