---
title: FileSystemProvider.getFileAttributeView()
permalink: Java/FileSystemProvider/getFileAttributeView
date: 2021-01-04
key: JavaJava.F.FileSystemProvider
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemProvider.metodos valor="getFileAttributeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <V extends FileAttributeView>V getFileAttributeView(Path path, Class<V> type, LinkOption... options)
~~~

## Parámetros
* **Class&lt;V&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<V> type" %}
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_data parametro="LinkOption... options" %}
* **Path path**,  {% include w3api/param_description.html metodo=_data parametro="Path path" %}

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
