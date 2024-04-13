---
title: BasicSpinnerUI.getBaseline()
permalink: /Java/BasicSpinnerUI/getBaseline/
date: 2021-01-11
key: Java.B.BasicSpinnerUI
category: Java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicSpinnerUI.metodos valor="getBaseline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getBaseline(JComponent c, int width, int height)
~~~

## Parámetros
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicSpinnerUI](/Java/BasicSpinnerUI/)

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
