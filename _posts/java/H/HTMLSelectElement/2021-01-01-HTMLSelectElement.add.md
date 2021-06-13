---
title: HTMLSelectElement.add()
permalink: /Java/HTMLSelectElement/add/
date: 2021-01-11
key: Java.H.HTMLSelectElement
category: Java
tags: ['java se', 'org.w3c.dom.html', 'jdk.xml.dom', 'metodo java', 'Java 1.4', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLSelectElement.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(HTMLElement element, HTMLElement before) throws DOMException
~~~

## Parámetros
* **HTMLElement element**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLElement element" %}
* **HTMLElement before**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLElement before" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[HTMLSelectElement](/Java/HTMLSelectElement/)

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
