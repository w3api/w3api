---
title: DefaultStyledDocument.setCharacterAttributes()
permalink: Java/DefaultStyledDocument/setCharacterAttributes
date: 2021-01-04
key: JavaJava.D.DefaultStyledDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultStyledDocument.metodos valor="setCharacterAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCharacterAttributes(int offset, int length, AttributeSet s, boolean replace)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **AttributeSet s**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet s" %}
* **boolean replace**,  {% include w3api/param_description.html metodo=_data parametro="boolean replace" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Clase Padre
[DefaultStyledDocument](/Java/DefaultStyledDocument/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultStyledDocument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
