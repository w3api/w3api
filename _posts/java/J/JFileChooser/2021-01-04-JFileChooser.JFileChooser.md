---
title: JFileChooser.JFileChooser()
permalink: Java/JFileChooser/JFileChooser
date: 2021-01-04
key: JavaJava.J.JFileChooser
category: java
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
* **FileSystemView fsv**,  {% include w3api/param_description.html metodo=_data parametro="FileSystemView fsv" %}
* **File currentDirectory**,  {% include w3api/param_description.html metodo=_data parametro="File currentDirectory" %}
* **String currentDirectoryPath**,  {% include w3api/param_description.html metodo=_data parametro="String currentDirectoryPath" %}

## Clase Padre
[JFileChooser](/Java/JFileChooser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JFileChooser.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
