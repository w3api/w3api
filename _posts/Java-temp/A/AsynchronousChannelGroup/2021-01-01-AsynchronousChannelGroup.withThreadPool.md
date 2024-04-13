---
title: AsynchronousChannelGroup.withThreadPool()
permalink: /Java/AsynchronousChannelGroup/withThreadPool/
date: 2021-01-11
key: Java.A.AsynchronousChannelGroup
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelGroup.metodos valor="withThreadPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousChannelGroup withThreadPool(ExecutorService executor) throws IOException
~~~

## Parámetros
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutorService executor" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
