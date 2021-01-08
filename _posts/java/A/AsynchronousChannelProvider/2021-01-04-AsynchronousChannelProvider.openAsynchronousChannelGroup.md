---
title: AsynchronousChannelProvider.openAsynchronousChannelGroup()
permalink: Java/AsynchronousChannelProvider/openAsynchronousChannelGroup
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelProvider
category: java
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
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_data parametro="ExecutorService executor" %}
* **int nThreads**,  {% include w3api/param_description.html metodo=_data parametro="int nThreads" %}
* **int initialSize**,  {% include w3api/param_description.html metodo=_data parametro="int initialSize" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_data parametro="ThreadFactory threadFactory" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AsynchronousChannelProvider](/Java/AsynchronousChannelProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousChannelProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
