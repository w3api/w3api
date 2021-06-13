---
title: AsynchronousFileChannel.open()
permalink: /Java/AsynchronousFileChannel/open/
date: 2021-01-11
key: Java.A.AsynchronousFileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousFileChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AsynchronousFileChannel open(Path file, OpenOption... options) throws IOException
public static AsynchronousFileChannel open(Path file, Set<? extends OpenOption> options, ExecutorService executor, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **Path file**,  {% include w3api/param_description.html metodo=_dato parametro="Path file" %}
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutorService executor" %}
* **OpenOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... options" %}
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends OpenOption> options" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_dato parametro="FileAttribute<?>... attrs" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
