---
title: FileOutputStream.FileOutputStream()
permalink: Java/FileOutputStream/FileOutputStream
date: 2021-01-04
key: JavaJava.F.FileOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileOutputStream.constructores valor="FileOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileOutputStream(File file) throws FileNotFoundException
public FileOutputStream(FileDescriptor fdObj)
public FileOutputStream(File file, boolean append) throws FileNotFoundException
public FileOutputStream(String name) throws FileNotFoundException
public FileOutputStream(String name, boolean append) throws FileNotFoundException
~~~

## Parámetros
* **FileDescriptor fdObj**,  {% include w3api/param_description.html metodo=_data parametro="FileDescriptor fdObj" %}
* **boolean append**,  {% include w3api/param_description.html metodo=_data parametro="boolean append" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[FileOutputStream](/Java/FileOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
