---
title: LayoutStyle.getContainerGap()
permalink: /Java/LayoutStyle/getContainerGap/
date: 2021-01-11
key: Java.L.LayoutStyle
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LayoutStyle.metodos valor="getContainerGap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getContainerGap(JComponent component, int position, Container parent)
~~~

## Parámetros
* **JComponent component**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent component" %}
* **int position**,  {% include w3api/param_description.html metodo=_dato parametro="int position" %}
* **Container parent**,  {% include w3api/param_description.html metodo=_dato parametro="Container parent" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
