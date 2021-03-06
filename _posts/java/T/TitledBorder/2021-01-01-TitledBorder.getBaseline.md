---
title: TitledBorder.getBaseline()
permalink: /Java/TitledBorder/getBaseline/
date: 2021-01-11
key: Java.T.TitledBorder
category: Java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TitledBorder.metodos valor="getBaseline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getBaseline(Component c, int width, int height)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TitledBorder](/Java/TitledBorder/)

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
