---
title: TextLayout.getLogicalHighlightShape()
permalink: /Java/TextLayout/getLogicalHighlightShape/
date: 2021-01-11
key: Java.T.TextLayout
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="getLogicalHighlightShape" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Shape getLogicalHighlightShape(int firstEndpoint, int secondEndpoint)
public Shape getLogicalHighlightShape(int firstEndpoint, int secondEndpoint, Rectangle2D bounds)
~~~

## Parámetros
* **Rectangle2D bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D bounds" %}
* **int firstEndpoint**,  {% include w3api/param_description.html metodo=_dato parametro="int firstEndpoint" %}
* **int secondEndpoint**,  {% include w3api/param_description.html metodo=_dato parametro="int secondEndpoint" %}

## Clase Padre
[TextLayout](/Java/TextLayout/)

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
