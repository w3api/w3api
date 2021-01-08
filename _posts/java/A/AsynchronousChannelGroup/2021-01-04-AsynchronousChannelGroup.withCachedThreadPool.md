---
title: AsynchronousChannelGroup.withCachedThreadPool()
permalink: Java/AsynchronousChannelGroup/withCachedThreadPool
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelGroup
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelGroup.metodos valor="withCachedThreadPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousChannelGroup withCachedThreadPool(ExecutorService executor, int initialSize) throws IOException
~~~

## Parámetros
* **int initialSize**,  {% include w3api/param_description.html metodo=_data parametro="int initialSize" %}
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_data parametro="ExecutorService executor" %}

## Excepciones
[IOException](/Java/IOException/)

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
