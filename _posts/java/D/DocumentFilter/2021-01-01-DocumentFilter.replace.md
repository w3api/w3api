---
title: DocumentFilter.replace()
permalink: Java/DocumentFilter/replace
date: 2021-01-11
key: JavaJava.D.DocumentFilter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replace(DocumentFilter.FilterBypass fb, int offset, int length, String text, AttributeSet attrs) throws BadLocationException
~~~

## Parámetros
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attrs" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **DocumentFilter.FilterBypass fb**,  {% include w3api/param_description.html metodo=_dato parametro="DocumentFilter.FilterBypass fb" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[DocumentFilter](/Java/DocumentFilter/)

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
