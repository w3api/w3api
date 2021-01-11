---
title: DocumentFilter.remove()
permalink: Java/DocumentFilter/remove
date: 2021-01-11
key: JavaJava.D.DocumentFilter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentFilter.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(DocumentFilter.FilterBypass fb, int offset, int length) throws BadLocationException
~~~

## Parámetros
* **DocumentFilter.FilterBypass fb**,  {% include w3api/param_description.html metodo=_dato parametro="DocumentFilter.FilterBypass fb" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
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
