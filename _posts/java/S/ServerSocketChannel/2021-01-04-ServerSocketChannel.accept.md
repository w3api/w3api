---
title: ServerSocketChannel.accept()
permalink: Java/ServerSocketChannel/accept
date: 2021-01-04
key: JavaJava.S.ServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocketChannel.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SocketChannel accept() throws IOException
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NotYetBoundException](/Java/NotYetBoundException/)

## Clase Padre
[ServerSocketChannel](/Java/ServerSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
