---
title: AsynchronousChannelProvider.openAsynchronousServerSocketChannel()
permalink: Java/AsynchronousChannelProvider/openAsynchronousServerSocketChannel
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelProvider
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelProvider.metodos valor="openAsynchronousServerSocketChannel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AsynchronousServerSocketChannel openAsynchronousServerSocketChannel(AsynchronousChannelGroup group) throws IOException
~~~

## Parámetros
* **AsynchronousChannelGroup group**,  {% include w3api/param_description.html metodo=_data parametro="AsynchronousChannelGroup group" %}

## Excepciones
[ShutdownChannelGroupException](/Java/ShutdownChannelGroupException/), [IllegalChannelGroupException](/Java/IllegalChannelGroupException/), [IOException](/Java/IOException/)

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
