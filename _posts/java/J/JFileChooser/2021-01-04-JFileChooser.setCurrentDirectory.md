---
title: JFileChooser.setCurrentDirectory()
permalink: Java/JFileChooser/setCurrentDirectory
date: 2021-01-04
key: JavaJava.J.JFileChooser
category: java
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
* **File dir**,  {% include w3api/param_description.html metodo=_data parametro="File dir" %}

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
