---
title: StyleContext.removeAttributes()
permalink: Java/StyleContext/removeAttributes
date: 2021-01-04
key: JavaJava.S.StyleContext
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleContext.metodos valor="removeAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributeSet removeAttributes(AttributeSet old, Enumeration<?> names)
public AttributeSet removeAttributes(AttributeSet old, AttributeSet attrs)
~~~

## Parámetros
* **AttributeSet old**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet old" %}
* **Enumeration&lt;?&gt; names**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<?> names" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attrs" %}

## Clase Padre
[StyleContext](/Java/StyleContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StyleContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
