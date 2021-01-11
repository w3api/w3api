---
title: AsynchronousChannelGroup
permalink: Java/AsynchronousChannelGroup
date: 2021-01-11
key: JavaJava.A.AsynchronousChannelGroup
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AsynchronousChannelGroup.description }}

## Sintaxis
~~~java
public abstract class AsynchronousChannelGroup extends Object
~~~

## Constructores
* [AsynchronousChannelGroup()](/Java/AsynchronousChannelGroup/AsynchronousChannelGroup/)

## Métodos
* [awaitTermination()](/Java/AsynchronousChannelGroup/awaitTermination)
* [isShutdown()](/Java/AsynchronousChannelGroup/isShutdown)
* [isTerminated()](/Java/AsynchronousChannelGroup/isTerminated)
* [provider()](/Java/AsynchronousChannelGroup/provider)
* [shutdown()](/Java/AsynchronousChannelGroup/shutdown)
* [shutdownNow()](/Java/AsynchronousChannelGroup/shutdownNow)
* [withCachedThreadPool()](/Java/AsynchronousChannelGroup/withCachedThreadPool)
* [withFixedThreadPool()](/Java/AsynchronousChannelGroup/withFixedThreadPool)
* [withThreadPool()](/Java/AsynchronousChannelGroup/withThreadPool)

## Ejemplo
~~~java
{{ site.data.Java.A.AsynchronousChannelGroup.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousChannelGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
