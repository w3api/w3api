---
title: BasicListUI.locationToIndex()
permalink: /Java/BasicListUI/locationToIndex/
date: 2021-01-11
key: Java.B.BasicListUI
category: Java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicListUI.metodos valor="locationToIndex" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int locationToIndex(JList<?> list, Point location)
~~~

## Parámetros
* **Point location**,  {% include w3api/param_description.html metodo=_dato parametro="Point location" %}
* **JList&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="JList<?> list" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicListUI](/Java/BasicListUI/)

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
