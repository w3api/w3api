---
title: BasicListUI.locationToIndex()
permalink: Java/BasicListUI/locationToIndex
date: 2021-01-04
key: JavaJava.B.BasicListUI
category: java
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
* **JList&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="JList<?> list" %}
* **Point location**,  {% include w3api/param_description.html metodo=_data parametro="Point location" %}

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
{%- for _ldc in site.data.Java.B.BasicListUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
