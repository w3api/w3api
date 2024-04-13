---
title: BorderFactory.createCompoundBorder()
permalink: /Java/BorderFactory/createCompoundBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createCompoundBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CompoundBorder createCompoundBorder()
public static CompoundBorder createCompoundBorder(Border outsideBorder, Border insideBorder)
~~~

## Parámetros
* **Border insideBorder**,  {% include w3api/param_description.html metodo=_dato parametro="Border insideBorder" %}
* **Border outsideBorder**,  {% include w3api/param_description.html metodo=_dato parametro="Border outsideBorder" %}

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

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
