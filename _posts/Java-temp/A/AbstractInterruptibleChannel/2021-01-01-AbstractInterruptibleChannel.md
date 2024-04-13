---
title: AbstractInterruptibleChannel
permalink: /Java/AbstractInterruptibleChannel/
date: 2021-01-11
key: Java.A.AbstractInterruptibleChannel
category: Java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractInterruptibleChannel.description }}

## Sintaxis
~~~java
public abstract class AbstractInterruptibleChannel extends Object implements Channel, InterruptibleChannel
~~~

## Constructores
* [AbstractInterruptibleChannel()](/Java/AbstractInterruptibleChannel/AbstractInterruptibleChannel/)

## Métodos
* [begin()](/Java/AbstractInterruptibleChannel/begin)
* [close()](/Java/AbstractInterruptibleChannel/close)
* [end()](/Java/AbstractInterruptibleChannel/end)
* [implCloseChannel()](/Java/AbstractInterruptibleChannel/implCloseChannel)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractInterruptibleChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractInterruptibleChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
