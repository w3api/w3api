---
title: JFileChooser.JFileChooser()
permalink: /Java/JFileChooser/JFileChooser/
date: 2021-01-11
key: Java.J.JFileChooser
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.constructores valor="JFileChooser" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JFileChooser()
public JFileChooser(File currentDirectory)
public JFileChooser(File currentDirectory, FileSystemView fsv)
public JFileChooser(String currentDirectoryPath)
public JFileChooser(String currentDirectoryPath, FileSystemView fsv)
public JFileChooser(FileSystemView fsv)
~~~

## Parámetros
* **String currentDirectoryPath**,  {% include w3api/param_description.html metodo=_dato parametro="String currentDirectoryPath" %}
* **File currentDirectory**,  {% include w3api/param_description.html metodo=_dato parametro="File currentDirectory" %}
* **FileSystemView fsv**,  {% include w3api/param_description.html metodo=_dato parametro="FileSystemView fsv" %}

## Clase Padre
[JFileChooser](/Java/JFileChooser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
