---
title: AsynchronousFileChannel.open()
permalink: Java/AsynchronousFileChannel/open
date: 2021-01-04
key: JavaJava.A.AsynchronousFileChannel
category: java
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
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_data parametro="FileAttribute<?>... attrs" %}
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends OpenOption> options" %}
* **OpenOption... options**,  {% include w3api/param_description.html metodo=_data parametro="OpenOption... options" %}
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_data parametro="ExecutorService executor" %}
* **Path file**,  {% include w3api/param_description.html metodo=_data parametro="Path file" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
