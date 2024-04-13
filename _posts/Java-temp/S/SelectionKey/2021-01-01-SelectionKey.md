---
title: SelectionKey
permalink: /Java/SelectionKey/
date: 2021-01-11
key: Java.S.SelectionKey
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SelectionKey.description }}

## Sintaxis
~~~java
public abstract class SelectionKey extends Object
~~~

## Constructores
* [SelectionKey()](/Java/SelectionKey/SelectionKey/)

## Campos
* [OP_ACCEPT](/Java/SelectionKey/OP_ACCEPT)
* [OP_CONNECT](/Java/SelectionKey/OP_CONNECT)
* [OP_READ](/Java/SelectionKey/OP_READ)
* [OP_WRITE](/Java/SelectionKey/OP_WRITE)

## Métodos
* [attach()](/Java/SelectionKey/attach)
* [attachment()](/Java/SelectionKey/attachment)
* [cancel()](/Java/SelectionKey/cancel)
* [channel()](/Java/SelectionKey/channel)
* [interestOps()](/Java/SelectionKey/interestOps)
* [isAcceptable()](/Java/SelectionKey/isAcceptable)
* [isConnectable()](/Java/SelectionKey/isConnectable)
* [isReadable()](/Java/SelectionKey/isReadable)
* [isValid()](/Java/SelectionKey/isValid)
* [isWritable()](/Java/SelectionKey/isWritable)
* [readyOps()](/Java/SelectionKey/readyOps)
* [selector()](/Java/SelectionKey/selector)

## Ejemplo
~~~java
{{ site.data.Java.S.SelectionKey.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SelectionKey.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
