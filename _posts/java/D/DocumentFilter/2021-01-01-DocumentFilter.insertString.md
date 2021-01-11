---
title: DocumentFilter.insertString()
permalink: Java/DocumentFilter/insertString
date: 2021-01-11
key: JavaJava.D.DocumentFilter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.metodos valor="insertString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertString(DocumentFilter.FilterBypass fb, int offset, String string, AttributeSet attr) throws BadLocationException
~~~

## Parámetros
* **DocumentFilter.FilterBypass fb**,  {% include w3api/param_description.html metodo=_dato parametro="DocumentFilter.FilterBypass fb" %}
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attr" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **String string**,  {% include w3api/param_description.html metodo=_dato parametro="String string" %}

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
