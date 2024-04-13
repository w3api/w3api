---
title: MutableAttributeSet.removeAttributes()
permalink: /Java/MutableAttributeSet/removeAttributes/
date: 2021-01-11
key: Java.M.MutableAttributeSet
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MutableAttributeSet.metodos valor="removeAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeAttributes(Enumeration<?> names)
void removeAttributes(AttributeSet attributes)
~~~

## Parámetros
* **Enumeration&lt;?&gt; names**,  {% include w3api/param_description.html metodo=_dato parametro="Enumeration<?> names" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Clase Padre
[MutableAttributeSet](/Java/MutableAttributeSet/)

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
