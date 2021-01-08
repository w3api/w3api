---
title: AsynchronousFileChannel.lock()
permalink: Java/AsynchronousFileChannel/lock
date: 2021-01-04
key: JavaJava.A.AsynchronousFileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousFileChannel.metodos valor="lock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Future<FileLock> lock()
public abstract Future<FileLock> lock(long position, long size, boolean shared)
abstract <A> void lock(long position, long size, boolean shared, A attachment, CompletionHandler<FileLock,? super A> handler)
<A> void lock(A attachment, CompletionHandler<FileLock,? super A> handler)
~~~

## Parámetros
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **CompletionHandler&lt;FileLock**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<FileLock" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}
* **long size**,  {% include w3api/param_description.html metodo=_data parametro="long size" %}
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}
* **boolean shared**,  {% include w3api/param_description.html metodo=_data parametro="boolean shared" %}

## Excepciones
[OverlappingFileLockException](/Java/OverlappingFileLockException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [NonReadableChannelException](/Java/NonReadableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
