---
title: AsynchronousSocketChannel.open()
permalink: Java/AsynchronousSocketChannel/open
date: 2021-01-04
key: JavaJava.A.AsynchronousSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousSocketChannel open() throws IOException
public static AsynchronousSocketChannel open(AsynchronousChannelGroup group) throws IOException
~~~

## Parámetros
* **AsynchronousChannelGroup group**,  {% include w3api/param_description.html metodo=_data parametro="AsynchronousChannelGroup group" %}

## Excepciones
[ShutdownChannelGroupException](/Java/ShutdownChannelGroupException/), [IOException](/Java/IOException/)

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
