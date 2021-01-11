---
title: FileSystemProvider.setAttribute()
permalink: Java/FileSystemProvider/setAttribute
date: 2021-01-11
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setAttribute(Path path, String attribute, Object value, LinkOption... options) throws IOException
~~~

## Parámetros
* **String attribute**,  {% include w3api/param_description.html metodo=_dato parametro="String attribute" %}
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="LinkOption... options" %}
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
