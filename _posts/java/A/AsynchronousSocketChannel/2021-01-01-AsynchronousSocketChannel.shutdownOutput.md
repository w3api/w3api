---
title: AsynchronousSocketChannel.shutdownOutput()
permalink: /Java/AsynchronousSocketChannel/shutdownOutput/
date: 2021-01-11
key: Java.A.AsynchronousSocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="shutdownOutput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AsynchronousSocketChannel shutdownOutput() throws IOException
~~~

## Excepciones
[NotYetConnectedException](/Java/NotYetConnectedException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[AsynchronousSocketChannel](/Java/AsynchronousSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
