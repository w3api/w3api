---
title: JTabbedPane.JTabbedPane()
permalink: /Java/JTabbedPane/JTabbedPane/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.constructores valor="JTabbedPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JTabbedPane()
public JTabbedPane(int tabPlacement)
public JTabbedPane(int tabPlacement, int tabLayoutPolicy)
~~~

## Parámetros
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}
* **int tabLayoutPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int tabLayoutPolicy" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
