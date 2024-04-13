---
title: JFileChooser.setCurrentDirectory()
permalink: /Java/JFileChooser/setCurrentDirectory/
date: 2021-01-11
key: Java.J.JFileChooser
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="setCurrentDirectory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The directory that the JFileChooser is showing files of.") public void setCurrentDirectory(File dir)
~~~

## Parámetros
* **File dir**,  {% include w3api/param_description.html metodo=_dato parametro="File dir" %}

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
