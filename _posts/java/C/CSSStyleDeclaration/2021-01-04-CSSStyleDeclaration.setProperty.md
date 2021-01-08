---
title: CSSStyleDeclaration.setProperty()
permalink: Java/CSSStyleDeclaration/setProperty
date: 2021-01-04
key: JavaJava.C.CSSStyleDeclaration
category: java
tags: ['java se', 'org.w3c.dom.css', 'jdk.xml.dom', 'metodo java', 'Java 1.4', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CSSStyleDeclaration.metodos valor="setProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setProperty(String propertyName, String value, String priority) throws DOMException
~~~

## Parámetros
* **String priority**,  {% include w3api/param_description.html metodo=_data parametro="String priority" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[CSSStyleDeclaration](/Java/CSSStyleDeclaration/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CSSStyleDeclaration.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
