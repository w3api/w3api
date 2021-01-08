---
title: DocumentFilter.FilterBypass.replace()
permalink: Java/DocumentFilter/FilterBypass/replace
date: 2021-01-04
key: JavaJava.D.DocumentFilter.FilterBypass
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.FilterBypass.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void replace(int offset, int length, String string, AttributeSet attrs) throws BadLocationException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **AttributeSet attrs**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attrs" %}
* **String string**,  {% include w3api/param_description.html metodo=_data parametro="String string" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.D.DocumentFilter.FilterBypass.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
