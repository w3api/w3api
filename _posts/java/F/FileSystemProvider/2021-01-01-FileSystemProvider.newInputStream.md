---
title: FileSystemProvider.newInputStream()
permalink: /Java/FileSystemProvider/newInputStream/
date: 2021-01-11
key: Java.F.FileSystemProvider
category: Java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="newInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream newInputStream(Path path, OpenOption... options) throws IOException
~~~

## Parámetros
* **OpenOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... options" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[FileSystemProvider](/Java/FileSystemProvider/)

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
