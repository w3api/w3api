---
title: AbstractDocument.insertString()
permalink: Java/AbstractDocument/insertString
date: 2021-01-11
key: JavaJava.A.AbstractDocument
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.metodos valor="insertString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertString(int offs, String str, AttributeSet a) throws BadLocationException
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int offs**,  {% include w3api/param_description.html metodo=_dato parametro="int offs" %}
* **AttributeSet a**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet a" %}

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
