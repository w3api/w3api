---
title: HTMLWriter.HTMLWriter()
permalink: Java/HTMLWriter/HTMLWriter
date: 2021-01-11
key: JavaJava.H.HTMLWriter
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLWriter.constructores valor="HTMLWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HTMLWriter(Writer w, HTMLDocument doc)
public HTMLWriter(Writer w, HTMLDocument doc, int pos, int len)
~~~

## Parámetros
* **Writer w**,  {% include w3api/param_description.html metodo=_dato parametro="Writer w" %}
* **HTMLDocument doc**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLDocument doc" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Clase Padre
[HTMLWriter](/Java/HTMLWriter/)

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
