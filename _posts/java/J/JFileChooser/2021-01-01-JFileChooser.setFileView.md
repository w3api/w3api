---
title: JFileChooser.setFileView()
permalink: /Java/JFileChooser/setFileView/
date: 2021-01-11
key: Java.J.JFileChooser
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="setFileView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="Sets the File View used to get file type information.") public void setFileView(FileView fileView)
~~~

## Parámetros
* **FileView fileView**,  {% include w3api/param_description.html metodo=_dato parametro="FileView fileView" %}

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
