---
title: FileChannel.open()
permalink: /Java/FileChannel/open/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static FileChannel open(Path path, OpenOption... options) throws IOException
public static FileChannel open(Path path, Set<? extends OpenOption> options, FileAttribute<?>... attrs) throws IOException
~~~

## Parámetros
* **OpenOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... options" %}
* **FileAttribute&lt;?&gt;... attrs**,  {% include w3api/param_description.html metodo=_dato parametro="FileAttribute<?>... attrs" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}
* **Set&lt;? extends OpenOption&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends OpenOption> options" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

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
