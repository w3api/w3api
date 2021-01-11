---
title: StyleSheet.getRule()
permalink: Java/StyleSheet-javax-swing-text-html/getRule
date: 2021-01-11
key: JavaJava.S.StyleSheet-javax-swing-text-html
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleSheet-javax-swing-text-html.metodos valor="getRule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Style getRule(String selector)
public Style getRule(HTML.Tag t, Element e)
~~~

## Parámetros
* **HTML.Tag t**,  {% include w3api/param_description.html metodo=_dato parametro="HTML.Tag t" %}
* **Element e**,  {% include w3api/param_description.html metodo=_dato parametro="Element e" %}
* **String selector**,  {% include w3api/param_description.html metodo=_dato parametro="String selector" %}

## Clase Padre
[StyleSheet](/Java/StyleSheet-javax-swing-text-html/)

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
