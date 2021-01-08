---
title: TextLayout.getLogicalHighlightShape()
permalink: Java/TextLayout/getLogicalHighlightShape
date: 2021-01-04
key: JavaJava.T.TextLayout
category: java
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
* **int firstEndpoint**,  {% include w3api/param_description.html metodo=_data parametro="int firstEndpoint" %}
* **Rectangle2D bounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D bounds" %}
* **int secondEndpoint**,  {% include w3api/param_description.html metodo=_data parametro="int secondEndpoint" %}

## Clase Padre
[TextLayout](/Java/TextLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
