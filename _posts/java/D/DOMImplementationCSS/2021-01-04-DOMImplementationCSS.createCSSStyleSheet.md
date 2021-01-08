---
title: DOMImplementationCSS.createCSSStyleSheet()
permalink: Java/DOMImplementationCSS/createCSSStyleSheet
date: 2021-01-04
key: JavaJava.D.DOMImplementationCSS
category: java
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
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **String media**,  {% include w3api/param_description.html metodo=_data parametro="String media" %}

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
{%- for _ldc in site.data.Java.D.DOMImplementationCSS.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
