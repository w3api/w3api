---
title: AttributeSetUtilities.synchronizedView()
permalink: Java/AttributeSetUtilities/synchronizedView
date: 2021-01-04
key: JavaJava.A.AttributeSetUtilities
category: java
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
* **PrintRequestAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_data parametro="PrintRequestAttributeSet attributeSet" %}
* **PrintServiceAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_data parametro="PrintServiceAttributeSet attributeSet" %}
* **AttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attributeSet" %}
* **PrintJobAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_data parametro="PrintJobAttributeSet attributeSet" %}
* **DocAttributeSet attributeSet**,  {% include w3api/param_description.html metodo=_data parametro="DocAttributeSet attributeSet" %}

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
{%- for _ldc in site.data.Java.A.AttributeSetUtilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
