---
title: FileSystemProvider.checkAccess()
permalink: /Java/FileSystemProvider/checkAccess/
date: 2021-01-11
key: Java.F.FileSystemProvider
category: Java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="checkAccess" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void checkAccess(Path path, AccessMode... modes) throws IOException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}
* **AccessMode... modes**,  {% include w3api/param_description.html metodo=_dato parametro="AccessMode... modes" %}

## Excepciones
[IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [AccessDeniedException](/Java/AccessDeniedException/), [NoSuchFileException](/Java/NoSuchFileException/)

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
