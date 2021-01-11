---
title: FileSystemView.createFileObject()
permalink: Java/FileSystemView/createFileObject
date: 2021-01-11
key: JavaJava.F.FileSystemView
category: java
tags: ['java se', 'javax.swing.filechooser', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemView.metodos valor="createFileObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public File createFileObject(File dir, String filename)
public File createFileObject(String path)
~~~

## Parámetros
* **String path**,  {% include w3api/param_description.html metodo=_dato parametro="String path" %}
* **String filename**,  {% include w3api/param_description.html metodo=_dato parametro="String filename" %}
* **File dir**,  {% include w3api/param_description.html metodo=_dato parametro="File dir" %}

## Clase Padre
[FileSystemView](/Java/FileSystemView/)

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
