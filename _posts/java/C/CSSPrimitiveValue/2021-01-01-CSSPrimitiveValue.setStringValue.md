---
title: CSSPrimitiveValue.setStringValue()
permalink: /Java/CSSPrimitiveValue/setStringValue/
date: 2021-01-11
key: Java.C.CSSPrimitiveValue
category: Java
tags: ['java se', 'org.w3c.dom.css', 'jdk.xml.dom', 'metodo java', 'Java 1.4', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CSSPrimitiveValue.metodos valor="setStringValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setStringValue(short stringType, String stringValue) throws DOMException
~~~

## Parámetros
* **String stringValue**,  {% include w3api/param_description.html metodo=_dato parametro="String stringValue" %}
* **short stringType**,  {% include w3api/param_description.html metodo=_dato parametro="short stringType" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[CSSPrimitiveValue](/Java/CSSPrimitiveValue/)

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
