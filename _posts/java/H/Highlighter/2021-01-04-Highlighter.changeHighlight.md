---
title: Highlighter.changeHighlight()
permalink: Java/Highlighter/changeHighlight
date: 2021-01-04
key: JavaJava.H.Highlighter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Highlighter.metodos valor="changeHighlight" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void changeHighlight(Object tag, int p0, int p1) throws BadLocationException
~~~

## Parámetros
* **int p1**,  {% include w3api/param_description.html metodo=_data parametro="int p1" %}
* **Object tag**,  {% include w3api/param_description.html metodo=_data parametro="Object tag" %}
* **int p0**,  {% include w3api/param_description.html metodo=_data parametro="int p0" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[Highlighter](/Java/Highlighter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.Highlighter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
