---
title: FileSystemView.getFiles()
permalink: Java/FileSystemView/getFiles
date: 2021-01-04
key: JavaJava.F.FileSystemView
category: java
tags: ['java se', 'javax.swing.filechooser', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemView.metodos valor="getFiles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public File[] getFiles(File dir, boolean useFileHiding)
~~~

## Parámetros
* **boolean useFileHiding**,  {% include w3api/param_description.html metodo=_data parametro="boolean useFileHiding" %}
* **File dir**,  {% include w3api/param_description.html metodo=_data parametro="File dir" %}

## Clase Padre
[FileSystemView](/Java/FileSystemView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystemView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
