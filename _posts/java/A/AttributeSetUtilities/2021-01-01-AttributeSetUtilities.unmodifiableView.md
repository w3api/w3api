---
title: AttributeSetUtilities.unmodifiableView()
permalink: Java/AttributeSetUtilities/unmodifiableView
date: 2021-01-11
key: JavaJava.A.AttributeSetUtilities
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeSetUtilities.metodos valor="unmodifiableView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AttributeSet unmodifiableView(AttributeSet attributeSet)
public static DocAttributeSet unmodifiableView(DocAttributeSet attributeSet)
public static PrintJobAttributeSet unmodifiableView(PrintJobAttributeSet attributeSet)
public static PrintRequestAttributeSet unmodifiableView(PrintRequestAttributeSet attributeSet)
public static PrintServiceAttributeSet unmodifiableView(PrintServiceAttributeSet attributeSet)
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
