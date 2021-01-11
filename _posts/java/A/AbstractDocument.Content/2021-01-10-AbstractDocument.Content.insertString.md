---
title: AbstractDocument.Content.insertString()
permalink: Java/AbstractDocument/Content/insertString
date: 2021-01-10
key: JavaJava.A.AbstractDocument.Content
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.Content.metodos valor="insertString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
UndoableEdit insertString(int where, String str) throws BadLocationException
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int where**,  {% include w3api/param_description.html metodo=_dato parametro="int where" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[AbstractDocument.Content](/Java/AbstractDocument/Content/)

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
