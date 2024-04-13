---
title: AsynchronousChannelProvider.openAsynchronousChannelGroup()
permalink: /Java/AsynchronousChannelProvider/openAsynchronousChannelGroup/
date: 2021-01-11
key: Java.A.AsynchronousChannelProvider
category: Java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelProvider.metodos valor="openAsynchronousChannelGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AsynchronousChannelGroup openAsynchronousChannelGroup(int nThreads, ThreadFactory threadFactory) throws IOException
public abstract AsynchronousChannelGroup openAsynchronousChannelGroup(ExecutorService executor, int initialSize) throws IOException
~~~

## Parámetros
* **int initialSize**,  {% include w3api/param_description.html metodo=_dato parametro="int initialSize" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadFactory threadFactory" %}
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutorService executor" %}
* **int nThreads**,  {% include w3api/param_description.html metodo=_dato parametro="int nThreads" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[AsynchronousChannelProvider](/Java/AsynchronousChannelProvider/)

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
