---
title: PipedInputStream
permalink: Java/PipedInputStream
date: 2021-01-04
key: JavaJava.P.PipedInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PipedInputStream.description }}

## Sintaxis
~~~java
public class PipedInputStream extends InputStream
~~~

## Constructores
* [PipedInputStream()](/Java/PipedInputStream/PipedInputStream/)

## Campos
* [buffer](/Java/PipedInputStream/buffer)
* [in](/Java/PipedInputStream/in)
* [out](/Java/PipedInputStream/out)
* [PIPE_SIZE](/Java/PipedInputStream/PIPE_SIZE)

## Métodos
* [available()](/Java/PipedInputStream/available)
* [close()](/Java/PipedInputStream/close)
* [connect()](/Java/PipedInputStream/connect)
* [read()](/Java/PipedInputStream/read)
* [receive()](/Java/PipedInputStream/receive)

## Ejemplo
~~~java
{{ site.data.Java.P.PipedInputStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PipedInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
