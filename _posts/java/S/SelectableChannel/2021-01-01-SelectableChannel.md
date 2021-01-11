---
title: SelectableChannel
permalink: Java/SelectableChannel
date: 2021-01-11
key: JavaJava.S.SelectableChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SelectableChannel.description }}

## Sintaxis
~~~java
public abstract class SelectableChannel extends AbstractInterruptibleChannel implements Channel
~~~

## Constructores
* [SelectableChannel()](/Java/SelectableChannel/SelectableChannel/)

## Métodos
* [blockingLock()](/Java/SelectableChannel/blockingLock)
* [configureBlocking()](/Java/SelectableChannel/configureBlocking)
* [isBlocking()](/Java/SelectableChannel/isBlocking)
* [isRegistered()](/Java/SelectableChannel/isRegistered)
* [keyFor()](/Java/SelectableChannel/keyFor)
* [provider()](/Java/SelectableChannel/provider)
* [register()](/Java/SelectableChannel/register)
* [validOps()](/Java/SelectableChannel/validOps)

## Ejemplo
~~~java
{{ site.data.Java.S.SelectableChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SelectableChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
