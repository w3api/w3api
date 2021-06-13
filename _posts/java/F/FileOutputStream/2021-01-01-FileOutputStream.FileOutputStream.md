---
title: FileOutputStream.FileOutputStream()
permalink: /Java/FileOutputStream/FileOutputStream/
date: 2021-01-11
key: Java.F.FileOutputStream
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **FileDescriptor fdObj**,  {% include w3api/param_description.html metodo=_dato parametro="FileDescriptor fdObj" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **boolean append**,  {% include w3api/param_description.html metodo=_dato parametro="boolean append" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/)

## Clase Padre
[FileOutputStream](/Java/FileOutputStream/)

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
