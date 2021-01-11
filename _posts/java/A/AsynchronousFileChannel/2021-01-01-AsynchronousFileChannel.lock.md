---
title: AsynchronousFileChannel.lock()
permalink: Java/AsynchronousFileChannel/lock
date: 2021-01-11
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
* **boolean shared**,  {% include w3api/param_description.html metodo=_dato parametro="boolean shared" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}
* **CompletionHandler&lt;FileLock**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<FileLock" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super A> handler" %}
* **long size**,  {% include w3api/param_description.html metodo=_dato parametro="long size" %}

## Excepciones
[NonReadableChannelException](/Java/NonReadableChannelException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [OverlappingFileLockException](/Java/OverlappingFileLockException/)

## Clase Padre
[AsynchronousFileChannel](/Java/AsynchronousFileChannel/)

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
