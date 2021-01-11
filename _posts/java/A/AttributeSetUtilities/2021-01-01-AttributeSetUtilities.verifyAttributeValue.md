---
title: AttributeSetUtilities.verifyAttributeValue()
permalink: Java/AttributeSetUtilities/verifyAttributeValue
date: 2021-01-11
key: JavaJava.A.AttributeSetUtilities
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeSetUtilities.metodos valor="verifyAttributeValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Attribute verifyAttributeValue(Object object, Class<?> interfaceName)
~~~

## Parámetros
* **Class&lt;?&gt; interfaceName**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> interfaceName" %}
* **Object object**,  {% include w3api/param_description.html metodo=_dato parametro="Object object" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
