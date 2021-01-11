---
title: Dimension.setSize()
permalink: Java/Dimension/setSize
date: 2021-01-11
key: JavaJava.D.Dimension
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.Dimension.metodos valor="setSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSize(double width, double height)
public void setSize(int width, int height)
public void setSize(Dimension d)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **double width**,  {% include w3api/param_description.html metodo=_dato parametro="double width" %}
* **Dimension d**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension d" %}
* **double height**,  {% include w3api/param_description.html metodo=_dato parametro="double height" %}

## Clase Padre
[Dimension](/Java/Dimension/)

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
