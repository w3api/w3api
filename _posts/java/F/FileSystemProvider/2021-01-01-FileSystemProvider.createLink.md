---
title: FileSystemProvider.createLink()
permalink: Java/FileSystemProvider/createLink
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="createLink" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void createLink(Path link, Path existing) throws IOException
~~~

## Parámetros
* **Path existing**,  {% include w3api/param_description.html metodo=_dato parametro="Path existing" %}
* **Path link**,  {% include w3api/param_description.html metodo=_dato parametro="Path link" %}

## Excepciones
[IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
