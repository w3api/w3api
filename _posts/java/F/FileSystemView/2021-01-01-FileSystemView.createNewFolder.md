---
title: FileSystemView.createNewFolder()
permalink: Java/FileSystemView/createNewFolder
date: 2021-01-11
key: JavaJava.F.FileSystemView
category: java
tags: ['java se', 'javax.swing.filechooser', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemView.metodos valor="createNewFolder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract File createNewFolder(File containingDir) throws IOException
~~~

## Parámetros
* **File containingDir**,  {% include w3api/param_description.html metodo=_dato parametro="File containingDir" %}

## Excepciones
[IOException](/Java/IOException/)

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
