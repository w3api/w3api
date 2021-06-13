---
title: FileSystemView.getLinkLocation()
permalink: /Java/FileSystemView/getLinkLocation/
date: 2021-01-11
key: Java.F.FileSystemView
category: Java
tags: ['java se', 'javax.swing.filechooser', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemView.metodos valor="getLinkLocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public File getLinkLocation(File file) throws FileNotFoundException
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/), [NullPointerException](/Java/NullPointerException/)

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
