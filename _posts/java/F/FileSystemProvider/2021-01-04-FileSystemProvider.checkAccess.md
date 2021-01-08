---
title: FileSystemProvider.checkAccess()
permalink: Java/FileSystemProvider/checkAccess
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
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
* **AccessMode... modes**,  {% include w3api/param_description.html metodo=_data parametro="AccessMode... modes" %}
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NoSuchFileException](/Java/NoSuchFileException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [AccessDeniedException](/Java/AccessDeniedException/), [IOException](/Java/IOException/)

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
