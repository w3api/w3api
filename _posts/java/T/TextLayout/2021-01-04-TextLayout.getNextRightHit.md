---
title: TextLayout.getNextRightHit()
permalink: Java/TextLayout/getNextRightHit
date: 2021-01-04
key: JavaJava.T.TextLayout
category: java
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
* **TextLayout.CaretPolicy policy**,  {% include w3api/param_description.html metodo=_data parametro="TextLayout.CaretPolicy policy" %}
* **TextHitInfo hit**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo hit" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
