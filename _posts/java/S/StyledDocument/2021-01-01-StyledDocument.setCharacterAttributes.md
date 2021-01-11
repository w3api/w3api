---
title: StyledDocument.setCharacterAttributes()
permalink: Java/StyledDocument/setCharacterAttributes
date: 2021-01-11
key: JavaJava.S.StyledDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyledDocument.metodos valor="setCharacterAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setCharacterAttributes(int offset, int length, AttributeSet s, boolean replace)
~~~

## Parámetros
* **AttributeSet s**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet s" %}
* **boolean replace**,  {% include w3api/param_description.html metodo=_dato parametro="boolean replace" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Clase Padre
[StyledDocument](/Java/StyledDocument/)

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
