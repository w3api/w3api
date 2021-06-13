---
title: AsynchronousServerSocketChannel.open()
permalink: /Java/AsynchronousServerSocketChannel/open/
date: 2021-01-11
key: Java.A.AsynchronousServerSocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousServerSocketChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousServerSocketChannel open() throws IOException
public static AsynchronousServerSocketChannel open(AsynchronousChannelGroup group) throws IOException
~~~

## Parámetros
* **AsynchronousChannelGroup group**,  {% include w3api/param_description.html metodo=_dato parametro="AsynchronousChannelGroup group" %}

## Excepciones
[ShutdownChannelGroupException](/Java/ShutdownChannelGroupException/), [IOException](/Java/IOException/)

## Clase Padre
[AsynchronousServerSocketChannel](/Java/AsynchronousServerSocketChannel/)

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
