---
title: SimpleAttributeSet.removeAttributes()
permalink: Java/SimpleAttributeSet/removeAttributes
date: 2021-01-04
key: JavaJava.S.SimpleAttributeSet
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleAttributeSet.metodos valor="removeAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removeAttributes(Enumeration<?> names)
public void removeAttributes(AttributeSet attributes)
~~~

## Parámetros
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attributes" %}
* **Enumeration&lt;?&gt; names**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<?> names" %}

## Clase Padre
[SimpleAttributeSet](/Java/SimpleAttributeSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleAttributeSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
