---
title: MutableAttributeSet.removeAttributes()
permalink: Java/MutableAttributeSet/removeAttributes
date: 2021-01-04
key: JavaJava.M.MutableAttributeSet
category: java
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
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attributes" %}
* **Enumeration&lt;?&gt; names**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<?> names" %}

## Clase Padre
[MutableAttributeSet](/Java/MutableAttributeSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MutableAttributeSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
