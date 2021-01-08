---
title: DocumentFilter.replace()
permalink: Java/DocumentFilter/replace
date: 2021-01-04
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attrs" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **DocumentFilter.FilterBypass fb**,  {% include w3api/param_description.html metodo=_data parametro="DocumentFilter.FilterBypass fb" %}

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
{%- for _ldc in site.data.Java.D.DocumentFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
