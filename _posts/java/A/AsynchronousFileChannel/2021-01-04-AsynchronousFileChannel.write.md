---
title: AsynchronousFileChannel.write()
permalink: Java/AsynchronousFileChannel/write
date: 2021-01-04
key: JavaJava.A.AsynchronousFileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousFileChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Future<Integer> write(ByteBuffer src, long position)
abstract <A> void write(ByteBuffer src, long position, A attachment, CompletionHandler<Integer,? super A> handler)
~~~

## Parámetros
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Integer" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer src" %}
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}

## Excepciones
[NonWritableChannelException](/Java/NonWritableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AsynchronousFileChannel](/Java/AsynchronousFileChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousFileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
