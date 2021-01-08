---
title: AsynchronousSocketChannel.write()
permalink: Java/AsynchronousSocketChannel/write
date: 2021-01-04
key: JavaJava.A.AsynchronousSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Future<Integer> write(ByteBuffer src)
abstract <A> void write(ByteBuffer[] srcs, int offset, int length, long timeout, TimeUnit unit, A attachment, CompletionHandler<Long,? super A> handler)
abstract <A> void write(ByteBuffer src, long timeout, TimeUnit unit, A attachment, CompletionHandler<Integer,? super A> handler)
<A> void write(ByteBuffer src, A attachment, CompletionHandler<Integer,? super A> handler)
~~~

## Parámetros
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **CompletionHandler&lt;Long**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Long" %}
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] srcs" %}
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Integer" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[WritePendingException](/Java/WritePendingException/), [NotYetConnectedException](/Java/NotYetConnectedException/)

## Clase Padre
[AsynchronousSocketChannel](/Java/AsynchronousSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
