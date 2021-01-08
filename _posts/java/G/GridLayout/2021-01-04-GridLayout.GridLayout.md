---
title: GridLayout.GridLayout()
permalink: Java/GridLayout/GridLayout
date: 2021-01-04
key: JavaJava.G.GridLayout
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GridLayout.constructores valor="GridLayout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GridLayout()
public GridLayout(int rows, int cols)
public GridLayout(int rows, int cols, int hgap, int vgap)
~~~

## Parámetros
* **int cols**,  {% include w3api/param_description.html metodo=_data parametro="int cols" %}
* **int hgap**,  {% include w3api/param_description.html metodo=_data parametro="int hgap" %}
* **int vgap**,  {% include w3api/param_description.html metodo=_data parametro="int vgap" %}
* **int rows**,  {% include w3api/param_description.html metodo=_data parametro="int rows" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GridLayout](/Java/GridLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GridLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
