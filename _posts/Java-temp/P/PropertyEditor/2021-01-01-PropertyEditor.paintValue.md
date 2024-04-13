---
title: PropertyEditor.paintValue()
permalink: /Java/PropertyEditor/paintValue/
date: 2021-01-11
key: Java.P.PropertyEditor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyEditor.metodos valor="paintValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void paintValue(Graphics gfx, Rectangle box)
~~~

## Parámetros
* **Rectangle box**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle box" %}
* **Graphics gfx**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics gfx" %}

## Clase Padre
[PropertyEditor](/Java/PropertyEditor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
