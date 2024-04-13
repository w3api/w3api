---
title: AbstractDocument.AttributeContext.removeAttributes()
permalink: /Java/AbstractDocument/AttributeContext/removeAttributes/
date: 2021-01-11
key: Java.A.AbstractDocument.AttributeContext
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.AttributeContext.metodos valor="removeAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeSet removeAttributes(AttributeSet old, Enumeration<?> names)
AttributeSet removeAttributes(AttributeSet old, AttributeSet attrs)
~~~

## Parámetros
* **AttributeSet old**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet old" %}
* **Enumeration&lt;?&gt; names**,  {% include w3api/param_description.html metodo=_dato parametro="Enumeration<?> names" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attrs" %}

## Clase Padre
[AbstractDocument.AttributeContext](/Java/AbstractDocument/AttributeContext/)

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
