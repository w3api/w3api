---
title: AbstractDocument.replace()
permalink: Java/AbstractDocument/replace
date: 2021-01-04
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attrs" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.A.AbstractDocument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
