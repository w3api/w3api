---
title: AsynchronousSocketChannel.read()
permalink: /Java/AsynchronousSocketChannel/read/
date: 2021-01-11
key: Java.A.AsynchronousSocketChannel
category: Java
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
* **CompletionHandler&lt;Long**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<Long" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<Integer" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super A> handler" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] dsts" %}

## Excepciones
[NotYetConnectedException](/Java/NotYetConnectedException/), [ReadPendingException](/Java/ReadPendingException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
