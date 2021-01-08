---
title: TitledBorder.getBaseline()
permalink: Java/TitledBorder/getBaseline
date: 2021-01-04
key: JavaJava.T.TitledBorder
category: java
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
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TitledBorder](/Java/TitledBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TitledBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
