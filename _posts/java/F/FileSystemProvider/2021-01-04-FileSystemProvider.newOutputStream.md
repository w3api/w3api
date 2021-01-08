---
title: FileSystemProvider.newOutputStream()
permalink: Java/FileSystemProvider/newOutputStream
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OutputStream newOutputStream(Path path, OpenOption... options) throws IOException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}
* **OpenOption... options**,  {% include w3api/param_description.html metodo=_data parametro="OpenOption... options" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FileSystemProvider](/Java/FileSystemProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystemProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
