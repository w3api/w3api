---
title: AbstractBorder.getBaseline()
permalink: Java/AbstractBorder/getBaseline
date: 2021-01-04
key: JavaJava.A.AbstractBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractBorder.metodos valor="getBaseline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getBaseline(Component c, int width, int height)
~~~

## Parámetros
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AbstractBorder](/Java/AbstractBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
