---
title: TextLayout.getNextLeftHit()
permalink: Java/TextLayout/getNextLeftHit
date: 2021-01-11
key: JavaJava.T.TextLayout
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="getNextLeftHit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextHitInfo getNextLeftHit(int offset)
public TextHitInfo getNextLeftHit(int offset, TextLayout.CaretPolicy policy)
public TextHitInfo getNextLeftHit(TextHitInfo hit)
~~~

## Parámetros
* **TextHitInfo hit**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo hit" %}
* **TextLayout.CaretPolicy policy**,  {% include w3api/param_description.html metodo=_dato parametro="TextLayout.CaretPolicy policy" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

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
