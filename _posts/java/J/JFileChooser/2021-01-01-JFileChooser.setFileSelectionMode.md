---
title: JFileChooser.setFileSelectionMode()
permalink: Java/JFileChooser/setFileSelectionMode
date: 2021-01-11
key: JavaJava.J.JFileChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="setFileSelectionMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, enumerationValues={"JFileChooser.FILES_ONLY","JFileChooser.DIRECTORIES_ONLY","JFileChooser.FILES_AND_DIRECTORIES"}, description="Sets the types of files that the JFileChooser can choose.") public void setFileSelectionMode(int mode)
~~~

## Parámetros
* **int mode**,  {% include w3api/param_description.html metodo=_dato parametro="int mode" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
