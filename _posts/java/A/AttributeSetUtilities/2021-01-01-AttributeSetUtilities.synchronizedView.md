---
title: AttributeSetUtilities.synchronizedView()
permalink: /Java/AttributeSetUtilities/synchronizedView/
date: 2021-01-11
key: Java.A.AttributeSetUtilities
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeSetUtilities.metodos valor="synchronizedView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AttributeSet synchronizedView(AttributeSet attributeSet)
public static DocAttributeSet synchronizedView(DocAttributeSet attributeSet)
public static PrintJobAttributeSet synchronizedView(PrintJobAttributeSet attributeSet)
public static PrintRequestAttributeSet synchronizedView(PrintRequestAttributeSet attributeSet)
public static PrintServiceAttributeSet synchronizedView(PrintServiceAttributeSet attributeSet)
~~~

## Parámetros
* **PrintJobAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_dato parametro="PrintJobAttributeSet attributeSet" %}
* **PrintServiceAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_dato parametro="PrintServiceAttributeSet attributeSet" %}
* **DocAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_dato parametro="DocAttributeSet attributeSet" %}
* **PrintRequestAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_dato parametro="PrintRequestAttributeSet attributeSet" %}
* **AttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributeSet" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AttributeSetUtilities](/Java/AttributeSetUtilities/)

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
