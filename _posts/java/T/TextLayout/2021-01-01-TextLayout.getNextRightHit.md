---
title: TextLayout.getNextRightHit()
permalink: /Java/TextLayout/getNextRightHit/
date: 2021-01-11
key: Java.T.TextLayout
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="getNextRightHit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextHitInfo getNextRightHit(int offset)
public TextHitInfo getNextRightHit(int offset, TextLayout.CaretPolicy policy)
public TextHitInfo getNextRightHit(TextHitInfo hit)
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
