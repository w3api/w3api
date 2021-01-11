---
title: JFileChooser.setSelectedFiles()
permalink: Java/JFileChooser/setSelectedFiles
date: 2021-01-11
key: JavaJava.J.JFileChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="setSelectedFiles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="The list of selected files if the chooser is in multiple selection mode.") public void setSelectedFiles(File[] selectedFiles)
~~~

## Parámetros
* **File[] selectedFiles**,  {% include w3api/param_description.html metodo=_dato parametro="File[] selectedFiles" %}

## Clase Padre
[JFileChooser](/Java/JFileChooser/)

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
