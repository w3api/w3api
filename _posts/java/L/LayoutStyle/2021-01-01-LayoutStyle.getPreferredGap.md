---
title: LayoutStyle.getPreferredGap()
permalink: Java/LayoutStyle/getPreferredGap
date: 2021-01-11
key: Java.L.LayoutStyle
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LayoutStyle.metodos valor="getPreferredGap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getPreferredGap(JComponent component1, JComponent component2, LayoutStyle.ComponentPlacement type, int position, Container parent)
~~~

## Parámetros
* **JComponent component2**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent component2" %}
* **JComponent component1**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent component1" %}
* **Container parent**,  {% include w3api/param_description.html metodo=_dato parametro="Container parent" %}
* **LayoutStyle.ComponentPlacement type**,  {% include w3api/param_description.html metodo=_dato parametro="LayoutStyle.ComponentPlacement type" %}
* **int position**,  {% include w3api/param_description.html metodo=_dato parametro="int position" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LayoutStyle](/Java/LayoutStyle/)

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
