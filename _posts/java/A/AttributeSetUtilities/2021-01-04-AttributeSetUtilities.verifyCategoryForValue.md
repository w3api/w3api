---
title: AttributeSetUtilities.verifyCategoryForValue()
permalink: Java/AttributeSetUtilities/verifyCategoryForValue
date: 2021-01-04
key: JavaJava.A.AttributeSetUtilities
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeSetUtilities.metodos valor="verifyCategoryForValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void verifyCategoryForValue(Class<?> category, Attribute attribute)
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_data parametro="Attribute attribute" %}
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> category" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
