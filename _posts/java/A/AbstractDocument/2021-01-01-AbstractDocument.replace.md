---
title: AbstractDocument.replace()
permalink: Java/AbstractDocument/replace
date: 2021-01-11
key: JavaJava.A.AbstractDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replace(int offset, int length, String text, AttributeSet attrs) throws BadLocationException
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attrs" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[AbstractDocument](/Java/AbstractDocument/)

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
