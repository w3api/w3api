---
title: DOMImplementationCSS.createCSSStyleSheet()
permalink: /Java/DOMImplementationCSS/createCSSStyleSheet/
date: 2021-01-11
key: Java.D.DOMImplementationCSS
category: Java
tags: ['java se', 'org.w3c.dom.css', 'jdk.xml.dom', 'metodo java', 'Java 1.4', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMImplementationCSS.metodos valor="createCSSStyleSheet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CSSStyleSheet createCSSStyleSheet(String title, String media) throws DOMException
~~~

## Parámetros
* **String media**,  {% include w3api/param_description.html metodo=_dato parametro="String media" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[DOMImplementationCSS](/Java/DOMImplementationCSS/)

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
