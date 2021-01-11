---
title: DocumentFilter.FilterBypass.insertString()
permalink: Java/DocumentFilter/FilterBypass/insertString
date: 2021-01-11
key: JavaJava.D.DocumentFilter.FilterBypass
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.FilterBypass.metodos valor="insertString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void insertString(int offset, String string, AttributeSet attr) throws BadLocationException
~~~

## Parámetros
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attr" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **String string**,  {% include w3api/param_description.html metodo=_dato parametro="String string" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[DocumentFilter.FilterBypass](/Java/DocumentFilter/FilterBypass/)

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
