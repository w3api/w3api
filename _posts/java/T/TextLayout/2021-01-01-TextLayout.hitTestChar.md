---
title: TextLayout.hitTestChar()
permalink: /Java/TextLayout/hitTestChar/
date: 2021-01-11
key: Java.T.TextLayout
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="hitTestChar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextHitInfo hitTestChar(float x, float y)
public TextHitInfo hitTestChar(float x, float y, Rectangle2D bounds)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **Rectangle2D bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D bounds" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}

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
