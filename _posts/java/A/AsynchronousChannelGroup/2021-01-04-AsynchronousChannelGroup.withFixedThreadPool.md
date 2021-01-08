---
title: AsynchronousChannelGroup.withFixedThreadPool()
permalink: Java/AsynchronousChannelGroup/withFixedThreadPool
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelGroup
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelGroup.metodos valor="withFixedThreadPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousChannelGroup withFixedThreadPool(int nThreads, ThreadFactory threadFactory) throws IOException
~~~

## Parámetros
* **int nThreads**,  {% include w3api/param_description.html metodo=_data parametro="int nThreads" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_data parametro="ThreadFactory threadFactory" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AsynchronousChannelGroup](/Java/AsynchronousChannelGroup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousChannelGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
