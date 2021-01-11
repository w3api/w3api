---
title: JFileChooser.showOpenDialog()
permalink: Java/JFileChooser/showOpenDialog
date: 2021-01-11
key: JavaJava.J.JFileChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="showOpenDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int showOpenDialog(Component parent) throws HeadlessException
~~~

## Parámetros
* **Component parent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parent" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

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
