---
title: TextLayout.hitToPoint()
permalink: /Java/TextLayout/hitToPoint/
date: 2021-01-11
key: Java.T.TextLayout
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="hitToPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void hitToPoint(TextHitInfo hit, Point2D point)
~~~

## Parámetros
* **Point2D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D point" %}
* **TextHitInfo hit**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo hit" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
