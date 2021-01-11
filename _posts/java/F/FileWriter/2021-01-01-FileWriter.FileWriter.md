---
title: FileWriter.FileWriter()
permalink: Java/FileWriter/FileWriter
date: 2021-01-11
key: JavaJava.F.FileWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileWriter.constructores valor="FileWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileWriter(File file) throws IOException
public FileWriter(FileDescriptor fd)
public FileWriter(File file, boolean append) throws IOException
public FileWriter(String fileName) throws IOException
public FileWriter(String fileName, boolean append) throws IOException
~~~

## Parámetros
* **FileDescriptor fd**,  {% include w3api/param_description.html metodo=_dato parametro="FileDescriptor fd" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **boolean append**,  {% include w3api/param_description.html metodo=_dato parametro="boolean append" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileWriter](/Java/FileWriter/)

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
