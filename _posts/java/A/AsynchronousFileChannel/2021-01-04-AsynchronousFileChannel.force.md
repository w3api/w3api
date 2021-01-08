---
title: AsynchronousFileChannel.force()
permalink: Java/AsynchronousFileChannel/force
date: 2021-01-04
key: JavaJava.A.AsynchronousFileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousFileChannel.metodos valor="force" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void force(boolean metaData) throws IOException
~~~

## Parámetros
* **boolean metaData**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaData" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
