---
title: AsynchronousSocketChannel.read()
permalink: Java/AsynchronousSocketChannel/read
date: 2021-01-04
key: JavaJava.A.AsynchronousSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Future<Integer> read(ByteBuffer dst)
abstract <A> void read(ByteBuffer[] dsts, int offset, int length, long timeout, TimeUnit unit, A attachment, CompletionHandler<Long,? super A> handler)
abstract <A> void read(ByteBuffer dst, long timeout, TimeUnit unit, A attachment, CompletionHandler<Integer,? super A> handler)
<A> void read(ByteBuffer dst, A attachment, CompletionHandler<Integer,? super A> handler)
~~~

## Parámetros
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] dsts" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **CompletionHandler&lt;Long**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Long" %}
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Integer" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer dst" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[ReadPendingException](/Java/ReadPendingException/), [NotYetConnectedException](/Java/NotYetConnectedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
